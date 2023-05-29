from django.db import models

# Create your models here.


class Course(models.Model):
    image = models.ImageField(upload_to="courses/")
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    image = models.ImageField(upload_to="teachers/")
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    course = models.ForeignKey(
        Course, related_name="teachers", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.name


class Request(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=255)
    student_surname = models.CharField(max_length=255)
    student_phone_number = models.CharField(max_length=255)

    def __str__(self):
        return self.student_name
