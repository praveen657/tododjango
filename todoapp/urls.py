from django.urls import path,include
from . views import HomePageView,TaskCreateView,TaskDeleteView

urlpatterns = [
    
    path('',HomePageView.as_view(), name = 'home'),
    path('new/',TaskCreateView.as_view(), name = 'newtask'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(),name='task_delete'), 
    ]