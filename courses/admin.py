from django.contrib import admin

# Register your models here.
from .models import Category, Difficulty, Course, Teacher, CourseReview

admin.site.register(Category)
admin.site.register(Difficulty)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(CourseReview)