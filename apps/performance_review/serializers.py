
from rest_framework import serializers
from .models import *

class PerformanceReviewSerializer(serializers.ModelSerializer):
    employee_id = serializers.SerializerMethodField()
    sections = serializers.SerializerMethodField()

    class Meta:
        model = PerformanceReview
        fields = [
            'id','employee_id','name', 'job_title', 'supervisor', 'department',
            'jobDuties', 'performanceSummary',
            'planning_comments', 'planning_employee_rating', 'planning_manager_rating',
            'productivity_comments', 'productivity_employee_rating', 'productivity_manager_rating',
            'quality_comments', 'quality_employee_rating', 'quality_manager_rating',
            'knowledge_comments', 'knowledge_employee_rating', 'knowledge_manager_rating',
            'innovation_comments', 'innovation_employee_rating', 'innovation_manager_rating',
            'peerComm_comments', 'peerComm_employee_rating', 'peerComm_manager_rating',
            'teamRel_comments', 'teamRel_employee_rating', 'teamRel_manager_rating',
            'writing_comments', 'writing_employee_rating', 'writing_manager_rating',
            'oralComm_comments', 'oralComm_employee_rating', 'oralComm_manager_rating',
            'selfImprovement_comments', 'selfImprovement_employee_rating', 'selfImprovement_manager_rating',
            'otherCriteria', 'futureGoals', 'overallSummary',
            'employeeComments', 'managerComments', 'date',
            'sections' 
        ]

        # You could optionally exclude the raw fields from output
        extra_kwargs = {
            'planning_comments': {'write_only': True},
            'planning_employee_rating': {'write_only': True},
            'planning_manager_rating': {'write_only': True},
            'productivity_comments': {'write_only': True},
            'productivity_employee_rating': {'write_only': True},
            'productivity_manager_rating': {'write_only': True},
            'quality_comments': {'write_only': True},
            'quality_employee_rating': {'write_only': True},
            'quality_manager_rating': {'write_only': True},
            'knowledge_comments': {'write_only': True},
            'knowledge_employee_rating': {'write_only': True},
            'knowledge_manager_rating': {'write_only': True},
            'innovation_comments': {'write_only': True},
            'innovation_employee_rating': {'write_only': True},
            'innovation_manager_rating': {'write_only': True},
            'peerComm_comments': {'write_only': True},
            'peerComm_employee_rating': {'write_only': True},
            'peerComm_manager_rating': {'write_only': True},
            'teamRel_comments': {'write_only': True},
            'teamRel_employee_rating': {'write_only': True},
            'teamRel_manager_rating': {'write_only': True},
            'writing_comments': {'write_only': True},
            'writing_employee_rating': {'write_only': True},
            'writing_manager_rating': {'write_only': True},
            'oralComm_comments': {'write_only': True},
            'oralComm_employee_rating': {'write_only': True},
            'oralComm_manager_rating': {'write_only': True},
            'selfImprovement_comments': {'write_only': True},
            'selfImprovement_employee_rating': {'write_only': True},
            'selfImprovement_manager_rating': {'write_only': True},
        }

    def get_employee_id(self, obj):
        return obj.employee_id_id if obj.employee_id_id else None

    def get_sections(self, obj):
        return {
            "planning": {
                "employeeRating": obj.planning_employee_rating,
                "managerRating": obj.planning_manager_rating,
                "employeeComment": obj.planning_comments,
            },
            "productivity": {
                "employeeRating": obj.productivity_employee_rating,
                "managerRating": obj.productivity_manager_rating,
                "employeeComment": obj.productivity_comments,
            },
            "quality": {
                "employeeRating": obj.quality_employee_rating,
                "managerRating": obj.quality_manager_rating,
                "employeeComment": obj.quality_comments,
            },
            "knowledge": {
                "employeeRating": obj.knowledge_employee_rating,
                "managerRating": obj.knowledge_manager_rating,
                "employeeComment": obj.knowledge_comments,
            },
            "innovation": {
                "employeeRating": obj.innovation_employee_rating,
                "managerRating": obj.innovation_manager_rating,
                "employeeComment": obj.innovation_comments,
            },
            "peerComm": {
                "employeeRating": obj.peerComm_employee_rating,
                "managerRating": obj.peerComm_manager_rating,
                "employeeComment": obj.peerComm_comments,
            },
            "teamRel": {
                "employeeRating": obj.teamRel_employee_rating,
                "managerRating": obj.teamRel_manager_rating,
                "employeeComment": obj.teamRel_comments,
            },
            "writing": {
                "employeeRating": obj.writing_employee_rating,
                "managerRating": obj.writing_manager_rating,
                "employeeComment": obj.writing_comments,
            },
            "oralComm": {
                "employeeRating": obj.oralComm_employee_rating,
                "managerRating": obj.oralComm_manager_rating,
                "employeeComment": obj.oralComm_comments,
            },
            "selfImprovement": {
                "employeeRating": obj.selfImprovement_employee_rating,
                "managerRating": obj.selfImprovement_manager_rating,
                "employeeComment": obj.selfImprovement_comments,
            }
        }
    
class AnnouncementReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementReview
        fields = ['id', 'notification_title', 'notification_description', 'notification_date']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Meta.depth = self.context.get('depth', 0)