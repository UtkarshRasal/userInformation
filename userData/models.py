from django.db import models
from accounts.models import User

class UserProjects(models.Model):
	owner 		 = models.ForeignKey(User, null=True, on_delete = models.CASCADE)
	start_date 	 = models.DateField()
	end_date	 = models.DateField()
	title		 = models.CharField(max_length=200, blank=False)
	description  = models.TextField()
	link		 = models.CharField(max_length=200, blank=False)

	class Meta:
		ordering = ['id']
		verbose_name_plural = 'Projects'

	def __all__(self):
		return self.owner

class UserEducation(models.Model):
	owner  		 = models.ForeignKey(User, null=True, on_delete = models.CASCADE)
	start_date 	 = models.DateField()
	end_date	 = models.DateField()
	course  	 = models.CharField(max_length=255)
	branch		 = models.CharField(max_length=255)

	class Meta:
		verbose_name_plural = 'Education'

	def __all__(self):
		return self.owner

class UserExperience(models.Model):
	owner 		 = models.ForeignKey(User, null=True, on_delete = models.CASCADE)
	start_date 	 = models.DateField()
	end_date	 = models.DateField()
	designation  = models.CharField(max_length=100)
	description  = models.TextField()

	class Meta:
		verbose_name_plural = 'Experience'

	def __all__(self):
		return self.owner
