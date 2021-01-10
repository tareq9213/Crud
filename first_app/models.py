from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return str(self.pk) + " " + self.first_name + " " + self.last_name
