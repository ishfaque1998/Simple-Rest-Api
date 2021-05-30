from django.shortcuts import render
from rest_framework import viewsets
from .serializers import  StudentSerizlizer
from .models import Student

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('firstname')
    serializer_class = StudentSerizlizer
