from rest_framework import serializers

from courses.models import Teacher, Course, Difficulty, Category, CourseReview
from users.models import CustomUser


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'first_name', 'last_name', 'bio', 'profile_picture')


class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficulty
        fields = ('id', 'level')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'profile_picture', 'date_joined')


class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    difficulty = DifficultySerializer(read_only=True)
    teacher = TeacherSerializer(read_only=True)

    category_id = serializers.IntegerField(write_only=True)
    difficulty_id = serializers.IntegerField(write_only=True)
    teacher_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'duration', 'number_of_students', 'last_update', 'target', 'course_picture', 'to_whom',
                  'introduction_video', 'category', 'difficulty', 'teacher', 'category_id', 'difficulty_id',
                  'teacher_id')


class CourseReviewSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    course_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CourseReview
        fields = ('id', 'stars_given', 'comment', 'course', 'user', 'course_id', 'user_id')


