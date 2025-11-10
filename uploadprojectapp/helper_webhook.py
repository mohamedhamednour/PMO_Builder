import requests
from io import BytesIO
from decouple import config
from subscribeapp.models import Subscription , Stage



def start_project(payload):
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
def prepare_files( file_urls):
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
def upload_files(resume_url, files_to_upload):
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



def update_subscription( user , payload):
                 count_stages = 0
                 stageName = payload
                 stages_cost = Stage.objects.filter(id__in=stageName)
                 for stage in stages_cost:
                     count_stages += stage.cost
                 count_stages += Stage.objects.filter(id__in=stageName).count()
                 subscription = Subscription.objects.filter(user=user , is_active=True).first()
                 subscription.used_projects += 1
                 subscription.used_credits += count_stages
                 subscription.save()