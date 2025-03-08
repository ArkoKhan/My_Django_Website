from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ResumeHead(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100, blank=True)
    dob = models.DateField()
    image = models.ImageField(upload_to='profile_pics', blank=True)
    summary = models.TextField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class ResumeEducation(models.Model):
    resume = models.ForeignKey(ResumeHead, on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return self.degree

class ResumeExperience(models.Model):
    resume = models.ForeignKey(ResumeHead, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return self.title

class ResumeSkill(models.Model):
    SKILL_LEVEL = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Expert', 'Expert')
    )
    resume = models.ForeignKey(ResumeHead, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)
    level = models.CharField(max_length=100, choices=SKILL_LEVEL, default='Beginner')

    def __str__(self):
        return self.skill