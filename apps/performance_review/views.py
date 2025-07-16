from django.shortcuts import render

from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class PerformanceReviewViewset(viewsets.ModelViewSet):
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer

    def get(self, request):
        serializer = PerformanceReviewSerializer()
        serializer.is_valid()
        return Response(serializer.data)
        
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "Performance review form Created successfully."}, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
        {"message": "Performance review form updated successfully."},status=status.HTTP_200_OK)
    
class AnnouncementReviewViewset(viewsets.ModelViewSet):
    queryset = AnnouncementReview.objects.all()
    serializer_class = AnnouncementReviewSerializer

    def get(self, request):
        serializer = AnnouncementReviewSerializer()
        serializer.is_valid()
        return Response(serializer.data)
        
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "Announcement notification Created successfully."}, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()  
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "Announcement notification Updated successfully."}, status=status.HTTP_200_OK)