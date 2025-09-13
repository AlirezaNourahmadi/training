from django.urls import path

from students.views import student_list, student_courses, add_grade, list_grades

urlpatterns = [
    path("list/", student_list, name="student-list"),
    path("<int:student_id>/courses/", student_courses, name="student-courses"),
    path("grades/add/", add_grade, name="add-grade"),
    path("grades/", list_grades, name="grades"),
]
