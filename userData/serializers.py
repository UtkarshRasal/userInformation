from rest_framework import serializers
from .models import UserProjects, UserEducation, UserExperience

class UserProjectSerializer(serializers.ModelSerializer):
    link = serializers.CharField(max_length=200, required=False)
    # owner = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model   = UserProjects
        fields  = ['owner', 'start_date', 'end_date', 'title', 'description', 'link']
		

class UserEducationSerializer(serializers.ModelSerializer):

	class Meta:
		model   = UserEducation
		fields  = '__all__'

class UserExperienceSerializer(serializers.ModelSerializer):
	
	class Meta:
		model   = UserExperience
		fields  = '__all__'