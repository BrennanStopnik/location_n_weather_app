from django.db import models


class Location(models.Model):
    location_query = models.CharField(max_length=200)


    def __str__(self):
        return self.question_text


class Answer(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)


    def __str__(self):
        return self.choice_text