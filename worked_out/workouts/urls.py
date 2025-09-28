from django.urls import path
from workouts import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('all-workouts/', views.all_workouts_view, name='all workouts'),
    path('new-client/', views.new_client_view, name='new client'),
    path('client-update/<int:id>', views.client_update_view, name='client update'),
    path('delete-client/<int:id>', views.delete_client_view, name='delete client'),
    path('workouts/<int:id>/', views.workout_list_by_client_view, name='workout list by client'),
    path('new-workout/<int:id>', views.new_workout_view, name='new workout'),
    path('workout-update/<int:id>', views.workout_update_view, name='workout update'),
    path('delete-workout/<int:id>', views.delete_workout_view, name='delete workout'),
]