from django import forms
from .models import Course, Lessons

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

class LessonsForm(forms.ModelForm):
    class Meta:
        model = Lessons
        fields = "__all__"
