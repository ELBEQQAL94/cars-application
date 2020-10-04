from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import CarSerializer
from .models import Car

# class SimpleApI(APIView):
#     permission_classes = (IsAuthenticated,)
#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)

# Create Employee Api
class CarCreateApi(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

# Get Employees Api
class CarApi(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

# Update Employee Api 
class CarUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

# Delete Employee Api
class CarDeleteApi(generics.DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer