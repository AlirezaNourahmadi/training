from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.cache import cache
from .models import Course
from .serializers import CourseSerializer

# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def course_student(request, course_id):
    cache_key = f"course_{course_id}_students"
    data = cache.get(cache_key)
    
    if not data:
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=404)
        
        serializer = CourseSerializer(course)
        data = serializer.data
        cache.set(cache_key, data, timeout=60)
    return Response(data)