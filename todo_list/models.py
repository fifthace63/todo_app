from django.db import models

# Create your models here.


class List(models.Model):
    item = models.CharField(max_length=200)
    completed_item = models.BooleanField(default=False)

    def __str__(self):
        return self.item + str(self.completed_item)