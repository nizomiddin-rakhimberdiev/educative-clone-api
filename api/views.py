from rest_framework import viewsets
from api.serializers import CourseSerializer, CourseReviewSerializer, UserSerializer
from courses.models import Course, CourseReview
from users.models import CustomUser


class CourseViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer
    queryset = Course.objects.all().order_by('last_update')
    lookup_field = 'id'


class CourseReviewViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = CourseReviewSerializer
    queryset = CourseReview.objects.all().order_by('created_at')
    lookup_field = 'id'


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    lookup_field = 'id'


