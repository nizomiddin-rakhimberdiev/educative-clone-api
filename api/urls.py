from rest_framework.routers import DefaultRouter

from api.views import CourseViewSet, CourseReviewViewSet, UserViewSet

app_name = 'api'

router = DefaultRouter()
router.register('course', CourseViewSet, basename='course'),
router.register('review', CourseReviewViewSet, basename='review'),
router.register('users', UserViewSet, basename='user'),

urlpatterns = router.urls
