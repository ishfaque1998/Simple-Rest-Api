from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Student

class StudentSerizlizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ( 'firstname','lastname')