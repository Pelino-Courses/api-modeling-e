from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from .models import category,event_managment,speaker_management,participant_management,schedule_management,event_payment
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, views as auth_views
from django.db.models import Count, Sum, Avg, F, ExpressionWrapper, DurationField
from django.template import loader
from django.contrib import messages
from django.utils import timezone
from .forms import RegisterSpeakerForm, RegisterconferenceForm, LoginForm, SignupForm,EventPaymentForm,ScheduleForm
from Event_app.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import speaker_managementSerializer
# Create your views here.

#api
@api_view(['GET'])
def indexs(request):
    return Response({"success": "setup was successful!"})

@api_view(['GET'])
def list_of_all_speaker_api(request):
       myevent = speaker_management.objects.all().values()
       seriarizer = speaker_managementSerializer(myevent, many= True)
       return Response(seriarizer.data)

@api_view(['GET','POST'])
def add_speaker_api(request):
       myevent = request.data
       seriarizer = speaker_managementSerializer(data = myevent)
       if seriarizer.is_valid():
           seriarizer.save()
           return Response({"success": "speaker added successful!"}, status=201)
       else:
           return Response(seriarizer.errors, status=400)






def index(request):
    event = event_managment.objects.filter(is_free=True) 
    return render(request, 'Event_app/index.html', {'event1':event})
def contact(request):
    return render(request, 'Event_app/contact.html')
def signup(request):
    if request.method =="POST":
       name = request.POST.get("name")
       email= request.POST.get("email")
       phone = request.POST.get("phone")
       pass1 = request.POST.get("pass1")
       pass2 = request.POST.get("pass2")
       user1 = participant_management.objects.filter(password=pass1).values()
       if user1.exists():
            messages.info(request,"your password is weak")
            return redirect(signup)
       if pass1 != pass2:
            messages.info(request,"confirm your password correct") 
            return redirect(signup) 
       else:
           new_participant = participant_management(name=name,email_address=email,phone_number=phone,password=pass1)
           new_participant.save()
           messages.info(request,"sign_up done")
           return redirect(signup) 

    return render(request,'Event_app/signup.html')


def login(request):
    if request.method == "POST":
       name = request.POST.get("name")
       pass1 = request.POST.get("pass1")
       user1 = participant_management.objects.filter(name=name,password=pass1).values()
       if user1.exists():
           part = participant_management.objects.all().values()
           template = loader.get_template('Event_app/d.html')
           context = {
            'mymember': user1,
                     }
           return HttpResponse(template.render(context, request))
            #return render(request,'Event_app/signup.html')
       else:
           messages.info(request,"your name and password did not match")
           return redirect(login)
    return render(request,'Event_app/login.html')
#a list of all events.
def list_of_all_event(request):
       myevent = event_managment.objects.all().values()
       template = loader.get_template('Event_app/list_of_all_event.html')
       context = {
           'mymembers': myevent,
           }
       return HttpResponse(template.render(context, request))

#details of a specific event by its title.

def details_of_event(request, id):
    myevent = event_managment.objects.get(id=id)
    template = loader.get_template('Event_app/ditail_of_event.html')
    context = {
          'mymember': myevent,
           }
    return HttpResponse(template.render(context, request))

#the upcoming events based on the current date.
def upcoming_events(request):
       myevent = event_managment.objects.filter(start_date__gte=timezone.now()).values() 
       template = loader.get_template('Event_app/upcoming_Event.html')
       context = {
           'mymembers': myevent,
           }
       return HttpResponse(template.render(context, request))
#list of all speakers.
def list_of_all_speaker(request):
       myevent = speaker_management.objects.all().values()
       template = loader.get_template('Event_app/list_of_all_speaker.html')
       context = {
           'mymembers': myevent,
           }
       return HttpResponse(template.render(context, request))

# details of a specific speaker by their name.
def details_of_speaker(request, id):
    myevent = speaker_management.objects.get(id=id)
    template = loader.get_template('Event_app/ditail_of_speaker.html')
    context = {
          'mymember': myevent,
           }
    return HttpResponse(template.render(context, request))

#a list of all participants.
def list_of_all_partcipants(request):
       myevent = participant_management.objects.all().values()
       template = loader.get_template('Event_app/list _of _all_participants.html')
       context = {
           'mymembers': myevent,
           }
       return HttpResponse(template.render(context, request))

#details of a specific participant by their email address.
def details_of_participant(request, id):
    myevent = participant_management.objects.get(id=id)
    template = loader.get_template('Event_app/ditail_of_speaker.html')
    context = {
          'mymember': myevent,
           }
    return HttpResponse(template.render(context, request))

# a list of all schedules.
def list_of_all_schedules(request):
    schedules = schedule_management.objects.select_related('event_managment', 'speaker_management')
    return render(request, 'Event_app/list_of_all_schedules.html', {'schedules': schedules})

#schedules of a specific event.
def details_of_schedule(request, id):
    myevent = schedule_management.objects.get(id=id)
    template = loader.get_template('Event_app/detail_of_schedule.html')
    context = {
          'mymember': myevent,
           }
    return HttpResponse(template.render(context, request))
#addd
def add_schedule_view(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')  # Redirect to the schedule list view after successful form submission
    else:
        form = ScheduleForm()

    return render(request, 'Event_app/add_schedule.html', {'form': form})

# a list of all payments.
def list_of_all_payments(request):
       myevent = event_payment.objects.all().values()
       template = loader.get_template('Event_app/list_of_all_payments.html')
       context = {
           'mymembers': myevent,
           }
       return HttpResponse(template.render(context, request))
# payments made by a specific participant.
def details_of_payment(request, id):
    myevent = event_payment.objects.get(id=id)
    template = loader.get_template('Event_app/ditail_of_payment.html')
    context = {
          'mymember': myevent,
           }
    return HttpResponse(template.render(context, request))

####################################
#guturuka hano gusubira hasi izi query zose nta ma templates page zifite. na URLS zazo ntabwo zirimo. ndumva ariyo task ubu dufite gukoraho. gusa murabona ko nashyizemo default page ya index.html.
 #the total amount paid for a specific event.
    amount_paid = event_managment
    
    return render(request, 'Event_app/contact.html', {'count1':count })
def paid_event(request):
    # - a list of paid events.
    paid = event_managment.objects.filter(event_payment__payment_status='paid').distinct()
    return render(request, 'Event_app/index.html', {'paid':paid})
    
     # the count of participants for each event.
def participant_per_event(request):
     event_part_counts = event_managment.annotate(part_counts=Count('participants_managments'))
     return render(request, 'Event_app/index.html', {'events1':event_part_counts})
     #the count of events attended by each participant.
def event_attending(request):
    events_attending = participant_management.objects.annotate(event_count=Count('event_attending')) 
    return render(request, 'Event_app/index.html', {'paid':events_attending} )   

def  count_schudule(request):
     #the count of schedules for each event.
    shedule_event = event_managment.objects.annotate(schedule_count=Count('schedule_managment'))
    return render(request, 'Event_app/index.html', {'schedule_event':shedule_event}) 
     #the total amount paid for a specific event.
def total_amount(request, event_id):
    event = event_managment.objects.get(id=event_id)
    total_amount = event_managment.event_payment_set.filter(payment_status='payment_status').aggregate(total_amount_paid=Sum('amount_paid'))['total_amount'] 
    return render(request, 'Event_app/index.html', {'total_amount_paid':total_amount}) 

def avg_price(request):
    avg_price = event_managment.objects.filter(event_payment__payment_status='paid').aggregate(avg_price=Avg('payment__amount_paid'))['average_price']  
    return render(request, 'Event_app/index.html', {'avg_amount':total_amount}) 
    #the list of participants attending a specific event.
def partic_attend_spec_event(request, event_id):
    spec_event =  get_object_or_404(event_managment, id=event_id)
    partic = spec_event.partic.all()
    return render(request, 'Event_app/index.html', {'spec_event':spec_event, 'partic':partic})
    #The list of speakers for a specific event.
def list_speaker_on_specific_event(request, event_id):
    speaker_event = get_object_or_404(event_managment, id=event_id)
    speakers = speaker_event.speakers.all()
    return render(request, 'Event_app/index.html', {'event':speaker_event, 'speaker':speakers})
 
    #the events scheduled for a specific date range.
def event_on_specific_date(request, start_date, end_date):
    event = event_managment.objects.filter(start_date__range=(start_date, end_date))
    return render(request, 'Event_app/index.html', {'Events':event})

    #participants who have attended all events.
def attend_all_events(request):
    participant = participant_management.objects.annotate(event_count=models.Count('title')).filter(event_count=event_managment.objects.count())
    return render(request, 'Event_app/index.html', {'partic':participant})

    #events that have no assigned speakers.
def  no_assigned_speakers(request):
    event_part = event_managment.objects.filter(event_managment__isnull=True)
    return render(request, 'Event_app/index.html', {'no_event':event_part})

     #events with the highest amount paid.
def event_highest_amount_paid(request):
    event2 = event_managment.objects.order_by('-event_payment__amount_paid')[:1]
    return render(request, 'Event_app/index.html', {'event_high':event2})

     #participants who have paid the most.
     
def particp_paid_most(request):
    paid_most = participant_management.objects.annotate(total_amount_paid=Sum('event_payment__amount_paid')).order_by('-total_amount_paid')
    return render(request, 'Event_app/index.html', {'amount_paid':paid_most})

    #speakers who have the most scheduled events.
def speakers_schedule_most_events(request):
    speakers = speaker_management.objects.annotate(schedule_num=Count('event_managment__schedule')).order_by('-schedule_num')
    return render(request, 'Event_app/index.html', {'num_speaker':speakers})

    #events with the longest duration.
def long_duration(request):
    durational_events = event_managment.objects.annotate(durat=ExpressionWrapper(F('end_date') - F('start_date'), output_date = DurationField())).order_by('-durat')
    return render(request, 'Event_app/index.html', {'duration':durational_events })

    #participants who have attended the most events in a specific month.
def  partcipant_attent_most_event_in_month(request, month):
    month_particpant = participant_management.objects.filter(events__start_date__month=month).annotate(events_attended=Count('events')).order_by('-events_attended')
    return render(request, 'Event_app/index.html', {'participants':month_particpant})

    #events with overlapping schedules.
def overlaping_events(request):
    overlap_events = event_managment.objects.filter(schedule__isnull=False).distinct() 
    Overlap_events = []
    for i in Overlap_events:
         overlap_schedules = schedule_management.objects.filter(event=i).order_by('start_time')
         for x in range(len(overlap_schedules) - 1): 
             if overlap_schedules[x]. end_time > overlap_schedules[x + 1].start_time:
                 overlap_events.append(i)
                 break
    return render(request, 'Event_app/index.html', {'overlap_events':overlap_events})


    #participants who have made a payment in the last 7 days.
def participants_payments(request):
    _7_days_ago = timezone.now() - timezone.timedelta(days=7)
    partci = participant_management.objects.filter(payment__payment_date__gte=_7_days_ago).distinct()
    return render(request, 'Event_app/index.html', {'_7_days_ago':_7_days_ago})


    #participants who have attended consecutive events.
def consecutive_events(request):
    participants = participants_payments.objects.all()
    consec_part = []
    
    for i in participants:
        events = event_managment.objects.filter(participants=i).order_by('start_date')
        for x in range(len(events) - 1):
            if events[x].end_date == events[x + 1].start_date:
                consec_part.append(i)
                break
    return render(request, 'Event_app/index.html', {'consec_part':consec_part})
  
  
    # speakers who have not been assigned to any events.
def speaker_without_events(request):
     speaker = speaker_management.objects.filter(events__isnull=True) 
     return render(request, 'Event_app/index.html', {'speaker_without_event':speaker}) 
 
    # events with the highest total payment amount.
    
def total_amount_payment(request):
    events = event_managment.objects.annotate(total_payments=Sum('payment__amount_paid')).order_by('-total_payment')[:5] 
    return render(request, 'Event_app/index.html', {'events':events})


    # participants who have attended events in multiple locations.

def multi_locations(request):
    participants = participant_management.objects.annotate(locations = Count('events__locations', distinct=True)).filter(locations__gt=1)
    return render(request, 'Event_app/index.html', {'participants':participants})
      
    # speakers who have presented on different topics.
def speaker_on_differnt_topics(request):
    speaker = speaker_management.objects.annotate(num_topic=Count('events__topic', distinct=True)).filter(num_topic__gt=1)
    return render(request, 'Event_app/index.html', {'speake':speaker})


    #events with the longest gap between start and end dates.
    
def longest_gap(request):
    events = event_managment.objects.annotate(duration=F('end_date') - F('start_date')).order_by('-duration')
    return render(request, 'Event_app/index.html', {'events':events})

    # participants who have attended events organized by a specific location.
def participants_location(request, locat_id):
    events =  participant_management.objects.filter(events__location=locat_id) 
    return render(request, 'Event_app/index.html', {'locations':events})

   #speakers who have the highest average rating.
def highest_average_ratings(request):
     speaker = speaker_management.objects.annotate(averag_rate=Avg('events__rating')).order_by('-averag_rate')[:5]
     return render(request, 'Event_app/index.html', {'speaker':speaker})
 
    #participants who have made payments for all events.
def made_all_payment(request):
    partci = participant_management.objects.annotate(event_count=Count('events')).filter(event_count=event_managment.objects.count(), payment__isnull=False).distinct()
    return render(request, 'Event_app/index.html', {'speaker_part':partci})
@login_required
def newspeaker(request):
    if request.method == 'POST':
        form = RegisterSpeakerForm(request.POST, request.FILES)
        
        if form.is_valid():
            speaker = form.save(commit=False)
            speaker.Created_by = request.user
            speaker.save()
            
            return redirect('Event_app:details_of_speaker', id = speaker.id)
    else:
        form =  RegisterSpeakerForm()
    
    return render(request, 'Event_app/form.html', {'form':form, 'title': 'New Speaker'})
@login_required
def newEvent(request):
    if request.method == 'POST':
        form1 = RegisterconferenceForm(request.POST, request.FILES)
        
        if form1.is_valid():
            event = form1.save(commit=False)
            event.Created_by = request.user
            event.save()
            
            return redirect('Event_app:list_of_all_event')
    else:
        form1 =  RegisterconferenceForm()
    
    return render(request, 'Event_app/newevent.html', {'form1':form1, 'title': 'New Conference'})

def signup(request):
    if request.method =='POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:   
        form = SignupForm()
    return render(request, 'Event_app/signup.html', {'form':form})
#event payment 
def payment_form_view(request):
    if request.method == 'POST':
        form = EventPaymentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"payment successfully")
           # return redirect(payment_form_view)
            # Add any additional logic for successful form submission
    else:
        form = EventPaymentForm()

    return render(request, 'Event_app/payment_form_template.html', {'form': form})
def custom_logout(request):
    return auth_views.LogoutView.as_view(next_page='/login/')(request)