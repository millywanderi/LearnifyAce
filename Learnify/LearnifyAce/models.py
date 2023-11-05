from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    startDate = models.DateField()
    image = models.ImageField(upload_to="image")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    endDate = models.DateField()

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    

    def __str__(self):
        return self.name

def generateStudentId():
    prefix = "STU-"
    uuid_id = uuid.uuid4()
    uuid4_short = uuid_id.hex[:6]
    student_id = f'{prefix}{uuid4_short}'
    return student_id

class RegisteredCourse(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    studentId = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Registered Course"
        verbose_name_plural = "Registered Courses"

    def __str__(self):
        return f'{self.student.username} {self.date}'
    
class Lessons(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"

    def __str__(self):
        return f'{self.course.name} {self.title}'
