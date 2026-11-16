
from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "roll",
        "age",
        "course",
        "email",
        "phone",
    )

    search_fields = ("name", "roll", "email")
    list_filter = ("course",)
    ordering = ("roll",)
  
