import requests
from uploadprojectapp.helper_webhook import start_project, upload_files, prepare_files
class WebHookHandler:

    def init_project(self, payload):
        """Main entry point"""
        resume_url = start_project(payload)
        if not resume_url:
            return {"error": "Cannot get resume URL"}

        files_to_upload = prepare_files(payload.get('files', []))
        if not files_to_upload:
            return {"error": "No files to upload"}

        return upload_files(resume_url, files_to_upload)


    def genrate_domain(self, payload):
        
        try:
            response = requests.post(
                url='https://primary-production-70e2.up.railway.app/webhook/domains',
                headers={"Content-Type": "application/json"},

                json=payload)
            
        except requests.RequestException as e:
            return None
        return response.json()
