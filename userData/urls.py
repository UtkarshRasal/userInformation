from django.urls import path
from .views import (ProjectsRegisterView,
					EducationView, ExperienceView,
				)			

urlpatterns = [
	path('projects/', ProjectsRegisterView.as_view(), name = 'projects'),
	path('education/', EducationView.as_view(), name = 'education'),
	path('experience/', ExperienceView.as_view(), name = 'experience'),
]