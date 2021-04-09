from rest_framework import serializers
from .models import UserProjects, UserEducation, UserExperience

class UserProjectSerializer(serializers.ModelSerializer):
	link = serializers.CharField(max_length=200, required=False)

	class Meta:
		model = UserProjects
		fields = '__all__'

class UserEducationSerializer(serializers.ModelSerializer):

	class Meta:
		model   = UserEducation
		fields  = '__all__'

class UserExperienceSerializer(serializers.ModelSerializer):
	
	class Meta:
		model   = UserExperience
		fields  = '__all__'