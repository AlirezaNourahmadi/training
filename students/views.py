from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.cache import cache
from .models import Student, Grade
from .serializers import StudentSerializer, GradeSerializer
from .permissions import IsTeacher
from courses.serializers import CourseSerializer

# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_list(request):

    student_data = cache.get('student_list')

    if not student_data:

        students = Student.objects.all()

        serializer = StudentSerializer(students, many=True)

        student_data = serializer.data

        cache.set('student_list', student_data, timeout=60)

    return Response(student_data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_courses(request, student_id):
    cache_key = f"student_{student_id}_courses"
    data = cache.get(cache_key)

    if not data:
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=404)

        courses = student.courses.all()
        serializer = CourseSerializer(courses, many=True)
        data = serializer.data
        cache.set(cache_key, data, timeout=60)
    return Response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsTeacher])
def add_grade(request):
    serializer = GradeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(teacher=request.user)
        
        return Response(serializer.data, status=201)
    
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_grades(request):
    if request.user.role == "student":
        grades = Grade.objects.filter(student__user=request.user)
    else:
        grades = Grade.objects.all()
    serializer = GradeSerializer(grades, many=True)
    return Response(serializer.data)
