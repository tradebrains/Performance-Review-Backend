from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from .views import *

router=routers.DefaultRouter()
router.register('performance-reviews', PerformanceReviewViewset)
router.register('announcementReview/notification', AnnouncementReviewViewset)
router.register('user-list', UserListViewset)
router.register('manager-list', ManagerListViewset)
router.register('status-check', StatusCheckViewset)

urlpatterns = [
    path('', include(router.urls)),
]