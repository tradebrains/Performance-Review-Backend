from django.db import models

class PerformanceReview(models.Model):
    employee_id = models.CharField(max_length=20, null=False, blank=False)
    job_title = models.CharField(max_length=50 , null=True, blank=True)
    supervisor = models.CharField(max_length=30 , null=True, blank=True)
    department = models.CharField(max_length=20 , null=True, blank=True)
    jobDuties = models.TextField(null=True, blank=True)
    performanceSummary = models.TextField(null=True, blank=True)
    planning_comments = models.TextField(null=True, blank=True)
    planning_employee_rating = models.IntegerField(null=True, blank=True)
    planning_manager_rating = models.IntegerField(null=True, blank=True)
    productivity_comments = models.TextField(null=True, blank=True)
    productivity_employee_rating = models.IntegerField(null=True, blank=True)
    productivity_manager_rating = models.IntegerField(null=True, blank=True)
    quality_comments = models.TextField(null=True, blank=True)
    quality_employee_rating = models.IntegerField(null=True, blank=True)
    quality_manager_rating = models.IntegerField(null=True, blank=True)
    knowledge_comments = models.TextField(null=True, blank=True)
    knowledge_employee_rating = models.IntegerField(null=True, blank=True)
    knowledge_manager_rating = models.IntegerField(null=True, blank=True)
    innovation_comments = models.TextField(null=True, blank=True)
    innovation_employee_rating = models.IntegerField(null=True, blank=True)
    innovation_manager_rating = models.IntegerField(null=True, blank=True)
    peerComm_comments = models.TextField(null=True, blank=True)
    peerComm_employee_rating = models.IntegerField(null=True, blank=True)
    peerComm_manager_rating = models.IntegerField(null=True, blank=True)
    teamRel_comments = models.TextField(null=True, blank=True)
    teamRel_employee_rating = models.IntegerField(null=True, blank=True)
    teamRel_manager_rating = models.IntegerField(null=True, blank=True)
    writing_comments = models.TextField(null=True, blank=True)
    writing_employee_rating = models.IntegerField(null=True, blank=True)
    writing_manager_rating = models.IntegerField(null=True, blank=True)
    oralComm_comments = models.TextField(null=True, blank=True)
    oralComm_employee_rating = models.IntegerField(null=True, blank=True)
    oralComm_manager_rating = models.IntegerField(null=True, blank=True)
    selfImprovement_comments = models.TextField(null=True, blank=True)
    selfImprovement_employee_rating = models.IntegerField(null=True, blank=True)
    selfImprovement_manager_rating = models.IntegerField(null=True, blank=True)
    otherCriteria = models.TextField(null=True, blank=True)
    futureGoals = models.TextField(null=True, blank=True)
    overallSummary = models.TextField(null=True, blank=True)
    employeeComments = models.TextField(null=True, blank=True)
    managerComments = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

class AnnouncementReview(models.Model):
    notification_title = models.CharField(max_length=255, null=False, blank=False)
    notification_description = models.TextField(null=False, blank=False)
    notification_date = models.DateField(blank=False, null=False)

class UserList(models.Model):
    email = models.EmailField(max_length=254, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    designation = models.CharField(max_length=50, null=False, blank=False)
    user_role = models.CharField(max_length=20, null=False, blank=False)
    reporting_manager = models.EmailField(max_length=254, null=False, blank=False)

class ManagerList(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    manager_id = models.CharField(max_length=20, null=True, blank=True)

class StatusCheck(models.Model):
    employee_id = models.CharField(max_length=20, null=False, blank=False)
    status = models.CharField(max_length=20, null=False, blank=False)

      