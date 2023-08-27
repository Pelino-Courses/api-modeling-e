from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from Event_app.models import event_managment, category

# Create your views here.

@login_required
# def index(request):
#     event = event_managment.objects.filter(Created_by=request.user)
#     return render(request, 'dashboard/index.html', {'event':event,})
def index(request):
    event = event_managment.objects.all().values()
    categories = category.objects.all()
    template = loader.get_template('Event_app/index.html')
    context = {
    'categories': categories,'event': event,
    }
    return HttpResponse(template.render(context, request))