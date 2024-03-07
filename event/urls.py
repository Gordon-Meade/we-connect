from django.urls import path
from .views import EventListView, EventDetailView, MyEventView

urlpatterns = [
    path('event_list/', EventListView.as_view(), name='event-list'),
    path('event_detail/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('my_event/', MyEventView.as_view(), name='my-event'),
]


