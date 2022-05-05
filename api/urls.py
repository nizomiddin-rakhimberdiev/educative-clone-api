from rest_framework.routers import DefaultRouter

from api.views import CourseViewSet, CourseReviewViewSet, UserViewSet

app_name = 'api'

router = DefaultRouter()
router.register('courses', CourseViewSet, basename='course'),
router.register('reviews', CourseReviewViewSet, basename='review'),
router.register('users', UserViewSet, basename='user'),

urlpatterns = router.urls
