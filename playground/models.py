from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=255)

class Role(models.Model) :
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    teammember = models.ForeignKey(Team, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)