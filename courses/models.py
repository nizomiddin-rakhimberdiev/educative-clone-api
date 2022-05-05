from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from users.models import CustomUser

# Create your models here.


class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    profile_picture = models.ImageField()
    bio = models.TextField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Difficulty(models.Model):
    level = models.CharField(max_length=50)

    def __str__(self):
        return self.level


class Course(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    duration = models.CharField(max_length=50)
    number_of_students = models.IntegerField(default=0,
                                             validators=[MinValueValidator(0)]
                                             )
    last_update = models.DateTimeField(default=timezone.now)
    target = models.CharField(max_length=200)
    course_picture = models.ImageField()
    to_whom = models.CharField(max_length=100)
    introduction_video = models.URLField(default='https://www.youtube.com/')

    class Meta:
        ordering = ['last_update']

    def __str__(self):
        return self.name


class CourseReview(models.Model):
    comment = models.TextField()
    stars_given = models.IntegerField(default=0,
                                      validators=[MinValueValidator(0), MaxValueValidator(5)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Rated {self.stars_given} stars by {self.user.username}"

