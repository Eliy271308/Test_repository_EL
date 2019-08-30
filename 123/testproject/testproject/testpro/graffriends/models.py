from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    MAN = "M"
    WOMEN = "W"
    SEX_CHOICES = (
        (MAN, "Man"),
        (WOMEN, "Woman")

    )

    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    birthday = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name + " " + self.last_name

