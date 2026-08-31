from django.db import models
from django.contrib.auth.models import User

class LearnerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_skill_level = models.CharField(max_length=50) # e.g., Beginner, Intermediate
    primary_interest = models.CharField(max_length=100) # e.g., Web Development, Data Science
    learning_goal = models.TextField() # Natural language goal

class CourseCompleted(models.Model):
    learner = models.ForeignKey(LearnerProfile, on_delete=models.CASCADE)
    course_id = models.IntegerField()
    completion_date = models.DateField(auto_now_add=True)

class LearningPath(models.Model):
    learner = models.ForeignKey(LearnerProfile, on_delete=models.CASCADE)
    course_id = models.IntegerField()
    milestone_order = models.IntegerField() # 1, 2, 3...
    ai_explanation = models.TextField() # Why this course is recommended