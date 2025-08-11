from django.urls import path
from .views import TeacherRegistrationView, TeacherLoginView
urlpatterns=[
    path('register/', TeacherRegistrationView.as_view(), name='teacher_registration'),
    path('login/', TeacherLoginView.as_view(), name='teacher_login'),
]

