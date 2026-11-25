"""
URL configuration for exam_pilot_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from accounts.views import TrainerSignupView

from rest_framework.authtoken.views import ObtainAuthToken

from accounts.views import TrainerRetrieveUpdateView

from assessment_management.views import AssessmentListCreateView
from assessment_management.views import AssessmentRetrieveUpdateDeleteView

from question_management.views import QuestionCreateView
from question_management.views import QuestionRetrieveUpdateDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),

    #trainer signup
    path("trainer/signup/",TrainerSignupView.as_view()),

    #token
    path("token/",ObtainAuthToken.as_view()),

    #trainer profile
    path("trainer/profile/",TrainerRetrieveUpdateView.as_view()),

    #assessment
    path("trainer/assessment/",AssessmentListCreateView.as_view()),
    path("trainer/assessment/<int:pk>/",AssessmentRetrieveUpdateDeleteView.as_view()),

    #question
    path("assessment/<int:pk>/question/",QuestionCreateView.as_view()),
    path("question/<int:pk>/",QuestionRetrieveUpdateDeleteView.as_view()),
]
