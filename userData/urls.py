from django.urls import path
from .views import (ProjectsRegisterView,
					EducationView, ExperienceView, UserListing,
				)			

urlpatterns = [
	path('projects/', ProjectsRegisterView.as_view(), name = 'projects'),
	# path('viewprojects/<owner>/', ProjectsView.as_view(), name = 'viewProjects'),
	path('education/', EducationView.as_view(), name = 'education'),
	path('experience/', ExperienceView.as_view(), name = 'experience'),
	path("users/", UserListing.as_view()),
]