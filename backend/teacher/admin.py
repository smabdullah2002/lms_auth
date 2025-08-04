from django.contrib import admin
from .models import TeacherModel

# Register your models here.
@admin.register(TeacherModel)
class TeacherAdmin(admin.ModelAdmin):
    list_display=(
        "phone_number",
        "full_name",
        "gender",
        "status",
        "created_at",
    )
