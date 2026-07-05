from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    ROLE_CHOICES = (
        ('STUDENT', 'Student'),
        ('ALUMNI', 'Alumni'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='STUDENT')
    class_year = models.IntegerField(null=True, blank=True)
    department = models.CharField(max_length=100, blank=True)
    industry = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(
    upload_to="profiles/",
    blank=True,
    null=True
)
    skills = models.ManyToManyField(Skill, blank=True)
    company = models.CharField(max_length=100, blank=True)
    designation = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    post_image = models.ImageField(
    upload_to="posts/",
    blank=True,
    null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.author.user.username} at {self.created_at}"

class Job(models.Model):
    TYPE_CHOICES = (
        ('FULL_TIME', 'Full-time'),
        ('PART_TIME', 'Part-time'),
        ('CONTRACT', 'Contract'),
        ('REMOTE', 'Remote'),
    )
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    company_logo_url = models.URLField(max_length=500, blank=True)
    location = models.CharField(max_length=100)
    salary_range = models.CharField(max_length=100, blank=True)
    industry = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='FULL_TIME')
    experience_level = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    requirements = models.TextField(blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    hiring_manager = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='job_postings')

    def __str__(self):
        return f"{self.title} at {self.company}"

class Event(models.Model):
    CATEGORY_CHOICES = (
        ('SUMMIT', 'Summit'),
        ('WEBINAR', 'Webinar'),
        ('NETWORKING', 'Networking'),
        ('REUNION', 'Reunion'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='NETWORKING')
    capacity = models.IntegerField(default=100)
    attendees = models.ManyToManyField(Profile, related_name='attending_events', blank=True)
    image_url = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"From {self.sender} to {self.receiver} at {self.timestamp}"
