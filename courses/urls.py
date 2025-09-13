from django.urls import path
from .views import course_student

urlpatterns = [
    path("<int:course_id>/students/", course_student, name="course-students")
]
