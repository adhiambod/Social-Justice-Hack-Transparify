from django.contrib import admin
from .models import Citizen, GovernmentProject, Policy, Feedback, PublicSpending
from backend.transparify.users.UserCitizen import UserCitizen, UserFeedback  # Corrected import path

admin.site.register(UserCitizen)
admin.site.register(GovernmentProject)
admin.site.register(Policy)
admin.site.register(Feedback)
admin.site.register(PublicSpending)
admin.site.register(UserFeedback)
