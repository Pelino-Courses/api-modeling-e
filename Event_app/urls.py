from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from Event_app import views
from .forms import LoginForm
from Event_app.views import index, contact
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Event_app'

urlpatterns = [
      path('',index, name="index"),
      path('contact/', contact, name="contact"),
      path('signup/', views.signup, name='signup'),
      path('login/', auth_views.LoginView.as_view(template_name='Event_app/login.html', authentication_form=LoginForm), name='login'),
      path('newspeaker/', views.newspeaker, name="newspeaker"),
      path('newEvent/', views.newEvent, name="newEvent"),
      path('logout/', views.custom_logout, name="logout"),
      path('list_of_all_event/',views.list_of_all_event, name="list_of_all_event"),
      path('list_of_all_event/details_of_event/<int:id>',views.details_of_event, name='details_of_event'),
      path('list_of_all_speaker/',views.list_of_all_speaker, name="list_of_all_speaker"),
      path('list_of_all_speaker/details_of_speaker/<int:id>',views.details_of_speaker, name='details_of_speaker'),
      path('list_of_all_participants/',views.list_of_all_partcipants),
      path('list_of_all_participants/details_of_participant/<int:id>',views.details_of_participant, name='details_of_participant'),
      path('upcoming_event/',views.upcoming_events, name="upcoming_event"),
      path('list_of_all_schedules/',views.list_of_all_schedules, name="list_of_all_schedules"),
      path('list_of_all_schedules/details_of_schedule/<int:id>',views.details_of_schedule),
       path('add_schedule/', views.add_schedule_view, name='add_schedule'),
      path('list_of_all_payments/',views.list_of_all_payments),
      path('list_of_all_payments/details_of_payment/<int:id>',views.details_of_payment),
      path('paid_event', views.paid_event, name='paid_event'),
      path('participant_per_event', views.participant_per_event, name='participant_per_event'),
      path('event_attending/', views.event_attending, name='event_attending'),
      path('count_schudule/', views.count_schudule, name='count_schudule'),
      path('total_amount/<int:event_id>/', views.total_amount, name="otal_amount"),
      path('avg_price/', views.avg_price, name='avg_price'),
      path('partic_attend_spec_event/<int:event_id>/', views.partic_attend_spec_event, name='participants_attending_a_specific event'),
      path('list_speaker_on_specific_event/<int:event_id>/', views.list_speaker_on_specific_event, name='list_speaker_on_specific_event'),
      path('event_on_specific_date/<str:start_date>/<str:end_date>/', views.event_on_specific_date, name = "event_on_specific_date"),
      path('attend_all_events/', views.attend_all_events, name='attend_all_events'),
      path('no_assigned_speakers/', views.no_assigned_speakers, name = "no_assigned_speakers" ),
      path('event_highest_amount_paid/',views.event_highest_amount_paid, name="event_highest_amount_paid"),
      path('particp_paid_most/', views.particp_paid_most, name='particp_paid_most'),
      path('speakers_schedule_most_events/', views.speakers_schedule_most_events, name="speakers_schedule_most_event"),
      path('long_duration/', views.long_duration, name="long_duration"),
      path('partcipant_attent_most_event_in_month/<int:month>/', views.partcipant_attent_most_event_in_month, name="partcipant_attent_most_event_in_month"),
      path('overlaping_events/', views.overlaping_events, name='overlaping_events'),
      path('participants_payments/', views.participants_payments, name='participants_payments'),
      path('speaker_without_events/', views.speaker_without_events, name="speaker_without_events"),
      path('total_amount_payment/', views.total_amount_payment, name="total_amount_payment"),
      path('multi_locations/', views.multi_locations, name="multi_locations"),
      path('speaker_on_differnt_topics/', views.speaker_on_differnt_topics, name="speaker_on_differnt_topics"),
      path('longest_gap/', views.longest_gap, name='longest_gap'),
      path('participants_location/<int:location_id>', views.participants_location, name="participants_location"),
      path('highest_average_ratings/', views.highest_average_ratings, name='highest_average_ratings'),
      path('made_all_payment/', views.made_all_payment, name='made_all_payment'),
      path('payment/', views.payment_form_view, name='payment-form'),
      #api urs
      path('index/',views.indexs),
      path('list_of_all_speaker_api/',views.list_of_all_speaker_api),
      path('add_speaker_api/',views.add_speaker_api),

]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)