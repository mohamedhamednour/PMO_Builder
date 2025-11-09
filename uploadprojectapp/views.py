from rest_framework import viewsets 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ProjectSerializer
from .models import Project
from .webhook_handelr import WebHookHandler
from .data_validation import InitProjectData

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def inital_webhook_project(request):
    print(request.data)
    payload = {
        "projectName": request.data.get('projectName'),
        "projectId": request.data.get('projectId'),
        "files": request.data.get('files', [])
    }
    try:
        handler = WebHookHandler()
        result = handler.init_project(payload)
        return Response(result, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=400)


    