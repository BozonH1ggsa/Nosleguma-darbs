from django.db import models


class Deposit(models.Model):

    deposit = models.IntegerField()
    term = models.IntegerField()
    rate = models.FloatField(max_length=5)
    interest = models.IntegerField()
