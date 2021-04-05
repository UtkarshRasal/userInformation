from django.contrib import admin
from .models import User
from userData.models import UserProjects, UserEducation, UserExperience

admin.site.register(User)
admin.site.register(UserProjects)
admin.site.register(UserEducation)
admin.site.register(UserExperience)
