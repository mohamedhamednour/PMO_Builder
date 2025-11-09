import requests
from io import BytesIO
from decouple import config
class WebHookHandler:

    def init_project(self, payload):
        """Main entry point"""
        resume_url = self.start_project(payload)
        if not resume_url:
            return {"error": "Cannot get resume URL"}

        files_to_upload = self.prepare_files(payload.get('files', []))
        if not files_to_upload:
            return {"error": "No files to upload"}

        return self.upload_files(resume_url, files_to_upload)

    # -----------------------------
    # Step 1: Start project
    # -----------------------------
    def start_project(self, payload):
        try:
            response = requests.post(
                url=config('WEBHOOKPMOINIT'),
                headers={"Content-Type": "application/json"},
                json={
                    "projectName": payload['projectName'],
                    "projectId": payload['projectId']
                },
                timeout=30
            )
            response.raise_for_status()
        except requests.RequestException as e:
            print("Error contacting webhook/start:", e)
            return None

        try:
            data = response.json()
        except ValueError:
            print("Response is not JSON:", response.text)
            return None

        return data.get('resumeUrl')

    # -----------------------------
    # Step 2: Prepare files
    # -----------------------------
    def prepare_files(self, file_urls):
        files_to_upload = []
        for url in file_urls:
            try:
                r = requests.get(url, timeout=30)
                r.raise_for_status()
            except requests.RequestException as e:
                print(f"Error downloading file {url}: {e}")
                continue

            file_name = url.split('/')[-1]
            file_content = BytesIO(r.content)
            files_to_upload.append(('files', (file_name, file_content, 'application/pdf')))

        return files_to_upload

    # -----------------------------
    # Step 3: Upload files
    # -----------------------------
    def upload_files(self, resume_url, files_to_upload):
        try:
            response = requests.post(
                url=resume_url,
                files=files_to_upload,
                verify=False,  # مؤقت
                timeout=60
            )
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error uploading files: {e}")
            return {"error": str(e)}

        try:
            return response.json()
        except ValueError:
            return {"response_text": response.text}
