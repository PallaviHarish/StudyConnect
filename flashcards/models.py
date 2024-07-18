from django.db import models

class Flashcard(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    topic = models.CharField(max_length=100)

    def __str__(self):
        return self.question

class QuizOption(models.Model):
    question = models.ForeignKey(Flashcard, related_name='options', on_delete=models.CASCADE)
    option_text = models.CharField(max_length=255)

    def __str__(self):
        return self.option_text
