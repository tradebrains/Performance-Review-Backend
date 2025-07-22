from django.shortcuts import render

from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from apps.authentication.models import User
from django.db.models import Q


# Create your views here.
class PerformanceReviewViewset(viewsets.ModelViewSet):
    queryset = PerformanceReview.objects.none()
    serializer_class = PerformanceReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if not user or not user.is_authenticated:
            return PerformanceReview.objects.none()

        # 1. Superuser sees all
        if user.is_superuser:
            return PerformanceReview.objects.all()

        # 2. Check if user is a manager (by matching employee_id with manager_id in ManagerList)
        manager_entry = ManagerList.objects.filter(manager_id=user.employee_id).first()

        if manager_entry:
            # Get all employees who report to this manager (i.e. whose reporting_manager = this manager_entry)
            employee_ids = User.objects.filter(
                reporting_manager=manager_entry
            ).values_list("employee_id", flat=True)

            # Include own review + subordinates' reviews
            return PerformanceReview.objects.filter(
                Q(employee_id__in=employee_ids) | Q(employee_id=user.employee_id)
            )

        # 3. Regular employee - return only their own review
        return PerformanceReview.objects.filter(employee_id=user.employee_id)
        
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
    
class UserListViewset(viewsets.ModelViewSet):
    queryset = UserList.objects.all()
    serializer_class = UserListSerializer

    def get(self, request):
        serializer = UserListSerializer()
        serializer.is_valid()
        return Response(serializer.data)
        
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "User list Created successfully."}, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()  
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "User list Updated successfully."}, status=status.HTTP_200_OK)
    
class ManagerListViewset(viewsets.ModelViewSet):
    queryset = ManagerList.objects.all()
    serializer_class = ManagerListSerializer

    def get(self, request):
        serializer = ManagerListSerializer()
        serializer.is_valid()
        return Response(serializer.data) 
    
class StatusCheckViewset(viewsets.ModelViewSet):
    queryset = StatusCheck.objects.none()
    serializer_class = StatusCheckSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return StatusCheck.objects.filter(employee_id=user.employee_id)
        
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "Status check Created successfully."}, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()  
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "Status check Updated successfully."}, status=status.HTTP_200_OK)