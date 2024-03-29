from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('me', views.Me.as_view()),
    path('google-login', views.GoogleLogin.as_view()),
    path('alumni-users', views.AlumniUsers.as_view()),
    path('academic-history', views.AcademicHistory.as_view()),
    path('companies', views.Company.as_view()),
    path('employment-history', views.EmploymentHistory.as_view()),
    path('posts', views.Posts.as_view()),
    path('courses', views.Courses.as_view()),
    path('course-schedule', views.CourseSchedule.as_view()),
    path('course-schedule-student-subscriptions', views.CourseScheduleStudentSubscriptions.as_view(), name='course-schedule-student-subscriptions'),
    path('examination-periods', views.ExaminationPeriods.as_view()),
    path('examination-entries', views.ExaminationEntries.as_view()),
    path('raf-service-webhook', views.RafServiceWebhook.as_view()),
    path('raf-service-rabbit', views.RafServiceMessageBroker.as_view()),
]