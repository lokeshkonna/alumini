
from django.contrib import admin
from .models import Skill, Profile, Post, Job, Event, Message

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "department", "company")
    list_filter = ("role",)
    search_fields = ("user__username", "department", "company")

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "created_at")

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "employment_type", "location")

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "location")

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("sender", "receiver", "timestamp", "is_read")