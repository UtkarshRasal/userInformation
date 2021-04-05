from django.shortcuts import render
from rest_framework import generics, status, permissions
from .serializers import UserProjectSerializer, UserExperienceSerializer, UserEducationSerializer
from .models import UserProjects, UserEducation, UserExperience
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .permissions import IsOwner

class ProjectsRegisterView(APIView):
    model_class = UserProjects
    serializer_class = UserProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        owner = request.data
        serializer=self.serializer_class(data={**owner, **{"owner":request.user.pk}})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        _data = serializer.data

        return Response(_data, status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        instance = self.model_class.objects.filter(owner=request.user.pk)

        serializer = self.serializer_class(instance, many=True)
        _data = serializer.data
        return Response(_data)


# class ProjectsView(RetrieveUpdateDestroyAPIView):

#     serializer_class = UserProjectSerializer
#     permissions=[permissions.IsAuthenticated, IsOwner]
#     queryset = UserProjects.objects.all()
#     lookup_field = "owner"

#     def get_queryset(self):
#         return self.queryset.filter(owner=self.request.user)

#     def get(self, request, owner, *args, **)


class EducationView(generics.GenericAPIView):
	pass

class ExperienceView(generics.GenericAPIView):
	pass

class UserListing(APIView):
	pass
