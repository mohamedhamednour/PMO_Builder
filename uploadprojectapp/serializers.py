from rest_framework import serializers
from .models import Project, FilesProject

class FilesProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilesProject
        fields = ['id', 'file', 'created_at']

class ProjectSerializer(serializers.ModelSerializer):
    files = FilesProjectSerializer(many=True,  source='filesproject_set')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Project
        fields = ['id', 'user', 'title', 'description', 'created_at', 'files']
        read_only_fields = ['id', 'created_at', 'files']

    def create(self, validated_data):
        files = validated_data.pop('files')
        project = Project.objects.create(**validated_data)
        for file in files:
            FilesProject.objects.create(project=project, file=file)
        return project
    
    def update(self, instance, validated_data):
        files = validated_data.pop('files')
        project = super().update(instance, validated_data)
        for file in files:
            FilesProject.objects.create(project=project, file=file)
        return project