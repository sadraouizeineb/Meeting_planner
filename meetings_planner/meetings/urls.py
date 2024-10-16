# meetings/urls.py

from django.urls import path
from .views import detail,meetings_list_view, room_detail,add_meeting,delete_meeting,update_meeting

urlpatterns = [
    path('', meetings_list_view, name='meetings_list_view'),  # List of meetings and rooms

    path('detail/<int:id>/', detail, name='detail'),  # Meeting detail
    path('room/<int:id>/', room_detail, name='room_detail'),  # Room detail 
    path('new', add_meeting, name='add_meeting'),  # Room detail 
    path('delete/<int:id>/', delete_meeting, name='delete_meeting'),  # Add this line
    path('update/<int:id>/', update_meeting, name='update_meeting'),  # Mise à jour d'une réunion

]

