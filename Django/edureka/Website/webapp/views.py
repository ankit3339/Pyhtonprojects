from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import employee
from .serializers import employeeSerializer
from rest_framework import status
# Create your views here.

class employeeList(APIView):

    def get(self, request):
        employees1 = employee.objects.all()
        serializer = employeeSerializer(employees1, many=True)
        return Response(serializer.data)

    def post(self):
        pass


