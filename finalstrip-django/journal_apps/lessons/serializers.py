from rest_framework import serializers

from journal_apps.lessons.models import Lesson
from journal_apps.social.models import ConnectFencers
from journal_apps.profiles.models import Profile


class LessonSerializer(serializers.ModelSerializer):
    coach_list = serializers.SerializerMethodField(read_only=True)

    def get_coach_list(self, obj):
        # get user from context
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        
        coach_query = ConnectFencers.objects.filter(student=user, s_accepts=True, c_accepts=True)
        coach_list = coach_query.values_list("coach", flat=True)
        
        # https://stackoverflow.com/questions/39096763/how-to-filter-result-with-another-model-values-django-restframework
        # coach_profiles = Profile.objects.filter(user__in=coach_list)
        # serializer = SomeSerializer(coach_profiles, many=True)
        return coach_list

    class Meta:
        model = Lesson
        exclude = ('pkid','id')