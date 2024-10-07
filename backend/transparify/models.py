from django.db import models

class Citizen(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=200)
    joined_at = models.DateTimeField(auto_now_add=True)

    # Temporary field to trigger migration
    temporary_field = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class GovernmentProject(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    budget = models.DecimalField(max_digits=15, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=100, choices=[('ongoing', 'Ongoing'), ('completed', 'Completed'), ('planned', 'Planned')])

    def __str__(self):
        return self.title

class Policy(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    enacted_date = models.DateField()
    status = models.CharField(max_length=100, choices=[('active', 'Active'), ('inactive', 'Inactive')])

    def __str__(self):
        return self.title

class Feedback(models.Model):
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    project = models.ForeignKey(GovernmentProject, on_delete=models.CASCADE, null=True, blank=True)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, null=True, blank=True)
    feedback_text = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.citizen} on {self.project or self.policy}"

class PublicSpending(models.Model):
    project = models.ForeignKey(GovernmentProject, on_delete=models.CASCADE)
    amount_spent = models.DecimalField(max_digits=15, decimal_places=2)
    date_spent = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.project.title} - {self.amount_spent}"
