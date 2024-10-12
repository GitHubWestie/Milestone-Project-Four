import uuid
from django.db import models
from users.models import CustomUser

# Create your models here.
from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='course-logo')
    instructor = models.CharField(max_length=100)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.title
    

class Lesson(models.Model):
    course_id = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    # Specifies how lesson videos should be ordered
    class Meta:
        ordering = ['order']


    def __str__(self):
        return self.title
    

class Enrollment(models.Model):
    user = models.ForeignKey(CustomUser, related_name="enrollments",
                             on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name="enrollments",
                               on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.title}"