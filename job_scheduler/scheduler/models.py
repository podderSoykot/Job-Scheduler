from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    profit = models.IntegerField()

    def __str__(self):
        return self.title

