
from . import models
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = ('id',
                  'firstName',
                  'lastName',
                  'phone',
                  'email',
                  'employerId')


class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EMPLOYER
        fields = ('id',
                  'name',
                  'phone',
                  'email')