from django.views.generic import ListView
from django.views import View  
from .models import Event

class EventListView(ListView):
    model = Event
    template_name = 'event/event_list.html'  
    context_object_name = 'events'

class MyEventView(View):
    def get(self, request, *args, **kwargs):
        # Your view logic here
        return render(request, 'event/my_event_template.html', context={})
