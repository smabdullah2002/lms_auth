from django.urls import path
from .views import TeacherActivationView, TeacherRegistrationView, TeacherLoginView
urlpatterns=[
    path('register/', TeacherRegistrationView.as_view(), name='teacher_registration'),
    path('login/', TeacherLoginView.as_view(), name='teacher_login'),
    path('activate/', TeacherActivationView.as_view(), name='teacher_activate'),

]

#http://127.0.0.1:8000/teacher/login/
#http://127.0.0.1:8000/teacher/register/
#http://127.0.0.1:8000/teacher/activate/
