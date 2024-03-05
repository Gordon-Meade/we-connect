from django.views.generic import ListView
<<<<<<< HEAD
from django.views import View  
=======
>>>>>>> cabc0fa (Create Event App)
from .models import Event

class EventListView(ListView):
    model = Event
<<<<<<< HEAD
    template_name = 'event/event_list.html'  
    context_object_name = 'events'

class MyEventView(View):
    def get(self, request, *args, **kwargs):
        # Your view logic here
        return render(request, 'event/my_event_template.html', context={})
=======
    template_name = 'event/event_list.html'  # Create this template in the 'event' app
    context_object_name = 'events'
>>>>>>> cabc0fa (Create Event App)
