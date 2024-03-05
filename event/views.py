from django.views.generic import ListView
from .models import Event

class EventListView(ListView):
    model = Event
    template_name = 'event/event_list.html'  # Create this template in the 'event' app
    context_object_name = 'events'