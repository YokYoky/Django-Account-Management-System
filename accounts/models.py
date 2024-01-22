from django.db import models

# Create your models here.
class Account(models.Model):
    class Sex(models.TextChoices):
        MALE = 'M', 'MALE'
        FEMALE = 'F', 'FEMALE'

    account_number = models.PositiveBigIntegerField()
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=Sex.choices)
    residence = models.CharField(max_length=50)

    def __str__(self):
        return f'Account: {self.first_name} {self.last_name}'