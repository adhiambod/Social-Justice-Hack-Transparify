from django.db import models  # Import models from Django

class UserFeedback(models.Model):
    user_name = models.CharField(max_length=255)
    feedback_text = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name}'s Feedback"

class UserCitizen(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
