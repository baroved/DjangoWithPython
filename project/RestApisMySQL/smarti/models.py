from django.db import models


class EMPLOYER(models.Model):
    name = models.CharField(max_length=20, blank=False, default='non')
    phone = models.CharField(max_length=11, blank=False, default='non')
    email = models.EmailField()


class Contact(models.Model):
    firstName = models.CharField(max_length=10, blank=False, default='non')
    lastName = models.CharField(max_length=10, blank=False, default='non')
    phone = models.CharField(max_length=11, blank=False, default='non')
    email = models.EmailField()
    employerId = models.ForeignKey(EMPLOYER, on_delete=models.CASCADE)
