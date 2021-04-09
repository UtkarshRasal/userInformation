from django.shortcuts import render
from .serializers import UserProjectSerializer, UserExperienceSerializer, UserEducationSerializer
from .models import UserProjects, UserEducation, UserExperience
from .permissions import IsOwner
from .mixin import ProjectsFilterMixin, EducationFilterMixin, PaginationHandlerMixin
from rest_framework import generics, status, permissions, pagination, filters
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter


class ProjectsRegisterView(APIView, PaginationHandlerMixin, ProjectsFilterMixin):
    model_class          = UserProjects
    serializer_class     = UserProjectSerializer
    permission_classes   = [permissions.IsAuthenticated]
    pagination_class     = PageNumberPagination

    def post(self, request):
        owner = request.data
        serializer=self.serializer_class(data={**owner, **{"owner":request.user.pk}})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        _data = serializer.data

        return Response(_data, status.HTTP_201_CREATED)


    def get(self, request, format=None, *args, **kwargs):
        instance = self.model_class.objects.filter(owner=request.user.pk)
        queryset_list = self.filter_queryset(instance)
        

        page = self.paginate_queryset(queryset_list)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = self.serializer_class(instance, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # if queryset_list is not None: 
        #     return Response(queryset_list.values())
        # data = queryset_list.values() if queryset_list is not None else serializer.data

class EducationView(APIView, PaginationHandlerMixin, EducationFilterMixin):
    model_class          = UserEducation
    serializer_class     = UserEducationSerializer
    permission_classes   = [permissions.IsAuthenticated]
    pagination_class     = PageNumberPagination

    def post(self, request):
        owner = request.data

        serializer = self.serializer_class(data={**owner, **{"owner":request.user.pk}})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
    
    def get(self, request, format=None, *args, **kwargs):
        instance = self.model_class.objects.filter(owner=request.user)

        queryset_list = self.filter_queryset(instance)

        page = self.paginate_queryset(queryset_list)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(instance, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)


class ExperienceView(generics.GenericAPIView):
	pass
