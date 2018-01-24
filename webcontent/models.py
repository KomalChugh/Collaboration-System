from django.db import models

# Create your models here.

class Feedback(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	user = models.ForeignKey(User, related_name='user')
	provided_at = models.DateTimeField(auto_now_add=True)

class Faq(models.Model):
	category = models.CharField(max_length=100)
	question = models.CharField(max_length=100)
	answer = models.CharField(max_length=100)
