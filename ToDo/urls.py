from django.urls import path
from .views import TaskListView,TaskUpdateView,TaskDeleteView,TaskToggleStatusView





urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    path('toggle-status/<int:pk>/', TaskToggleStatusView.as_view(), name='task-toggle-status'),
]

