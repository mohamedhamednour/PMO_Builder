import requests
from uploadprojectapp.models import FilesProject

class WebHookHandler:
    def init_project(self, payload):
        print(payload, 'Payload Received')

        response = requests.post(
            url='https://primary-production-70e2.up.railway.app/webhook/start',
            headers={"Content-Type": "application/json"},
            json={
                "projectName": payload['projectName'],
                "projectId": payload['projectId']
            },
        )
        print(response, 'Response Object')

        try:
            data = response.json()  
        except ValueError:
            print("Response is not JSON:", response.text)
            return {"error": "Invalid response from webhook"}

        print(data, 'Response JSON')

        resume_url = data.get('resumeUrl')
        print(resume_url, 'Resume URL')

        if not resume_url:
            return {"error": "Resume URL not found in response"}
        from uuid import UUID
        ids_files = [UUID(id) for id in payload.get('idsFiles', [])]
        files_qs = FilesProject.objects.filter(
            id__in=ids_files,
            project_id=payload['projectId']
        ).values_list('file', flat=True)  # flatten عشان يطلع بس المسار

        print(files_qs, 'Files Queryset')
        files_to_upload = []

        file_paths = [
        'http://127.0.0.1:8002/media/project_files/mohamedhamednoor.pdf', ]
     
        from io import BytesIO
        for url in file_paths:
            response = requests.get(url)
            print(response, 'Response Object')

            file_name = url.split('/')[-1]
            file_content = BytesIO(response.content)
            files_to_upload.append(
                ('files', (file_name, file_content, 'application/pdf'))
            )
        
        if files_to_upload:
            upload_response = requests.post(
                url=resume_url,
                files=files_to_upload,
                verify=False)
            
     
    # )
        print(upload_response, 'New Response')
        


        return upload_response.json()




    def genrate_pmo(self, payload ) : ...



    payloadx={
        "projectId": "0c87d76e-5d99-4a88-a272-653660190dd5",
        "projectName": "My Project Title",
        "idsFiles": [
            "38d89bf6-fb9c-4acb-a095-e18210c130ce"
        ]
    }
{
        "projectId": "0c87d76e-5d99-4a88-a272-653660190dd5",
        "projectName": "My dc Title",
        "files": [
            "http://127.0.0.1:8002/media/project_files/m.hamed.nour_.pdf"
        ]
    }



















import requests
from uploadprojectapp.models import FilesProject

class WebHookHandler:
    def init_project(self, payload):

        response = requests.post(
            url='https://primary-production-70e2.up.railway.app/webhook/start',
            headers={"Content-Type": "application/json"},
            json={
                "projectName": payload['projectName'],
                "projectId": payload['projectId']
            },
        )

        try:
            data = response.json()  
        except ValueError:
            print("Response is not JSON:", response.text)
            return {"error": "Invalid response from webhook"}


        resume_url = data.get('resumeUrl')

        if not resume_url:
            return {"error": "Resume URL not found in response"}
        
        files_to_upload = []
        file_paths = payload.get('files', [])
     
        from io import BytesIO
        for url in file_paths:
            response = requests.get(url)
            print(response, 'Response Object')

            file_name = url.split('/')[-1]
            file_content = BytesIO(response.content)
            files_to_upload.append(
                ('files', (file_name, file_content, 'application/pdf'))
            )
        
        if files_to_upload:
            upload_response = requests.post(
                url=resume_url,
                files=files_to_upload,
                verify=False)

        return upload_response.json()




    def genrate_pmo(self, payload ) : ...



        