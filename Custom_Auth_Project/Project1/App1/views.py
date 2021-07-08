from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import EmployeeModel
from .serializers import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .authentication import CustomAuthentication

# Create your views here.
class EmployeeCRUD(ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]