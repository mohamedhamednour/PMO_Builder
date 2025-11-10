from rest_framework import viewsets 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ProjectSerializer
from .models import Project
from .webhook_handelr import WebHookHandler
from subscribeapp.models import Subscription
from .helper_webhook import  update_subscription
from .data_validation import GenrateDomainData
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
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def genrate_domain(request):
    print(request.data)
    subscription = Subscription.objects.filter(user=request.user , is_active=True).first()
    if subscription.used_projects >= int(subscription.plan.project_limit) or subscription.used_credits >= subscription.plan.credits_per_month:
        return Response({'error': 'You have reached the maximum number of projects.'}, status=400)

    try:
        handler = WebHookHandler()
        result = handler.genrate_domain(GenrateDomainData(projectName=request.data.get('projectName'),
                                stageName=[1,2,3,4,5], projectId=request.data.get('projectId')).dict())
        if result.get('message') == 'Workflow was started':
            update_subscription(request.user ,  request.data.get('stageName', []))
            return Response(result, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=400)


    