from django.urls import path
from .views import TeacherRegistrationView, TeacherLoginView
urlpatterns=[
    path('register/', TeacherRegistrationView.as_view(), name='teacher_registration'),
    path('login/', TeacherLoginView.as_view(), name='teacher_login'),
]

#http://127.0.0.1:8000/teacher/login/