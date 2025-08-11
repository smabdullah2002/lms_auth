from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teacher/', include('teacher.urls'), name='teacher'),
]

#http://127.0.0.1:8000/teacher/login/
#http://127.0.0.1:8000/teacher/register/
