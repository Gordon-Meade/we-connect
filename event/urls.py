from django.urls import path
from .views import MyEventView

urlpatterns = [
    # Other URL patterns
    path('my_event/', MyEventView.as_view(), name='my_event'),
]
