from django.db import models

# Create your models here.

class Quiz(models.Model):
    name = models.CharField(max_length= 255)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='inactive')

    def __str__(self) -> str:
        return self.name

class Question (models.Model):
    quiz = models.ForeignKey(Quiz , on_delete=models.CASCADE)
    text = models.CharField(max_length= 255)

class Choice (models.Model):
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)


