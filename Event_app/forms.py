from django import forms
from .models import speaker_management, event_managment,event_payment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import event_managment, schedule_management
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your username', 'class': 'w-full py-4 px-6 rounded-xl'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password', 'class': 'w-full py-4 px-6 rounded-xl'}))
    
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your username', 'class': 'w-full py-4 px-6 rounded-xl'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Your email address', 'class': 'w-full py-4 px-6 rounded-xl'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password', 'class': 'w-full py-4 px-6 rounded-xl'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password', 'class': 'w-full py-4 px-6 rounded-xl'}))


class RegisterSpeakerForm(forms.ModelForm):
    class Meta:
        model = speaker_management
        fields = ('name', 'biography', 'optional_photo', 'email_address', 'phone_number', 'linkedin', 'twitter',)
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'biography': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'optional_photo': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'email_address': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'phone_number': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'linkedin': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'twitter': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
class RegisterconferenceForm(forms.ModelForm):
    class Meta:
        model = event_managment
        fields = ('title', 'description', 'start_date', 'end_date', 'location', 'category', 'is_free',)
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'start_date': forms.DateInput(attrs={
                'class': INPUT_CLASSES
            }),
            'end_date': forms.DateInput(attrs={
                'class': INPUT_CLASSES
            }),
            'location': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'is_free': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
class EventPaymentForm(forms.ModelForm):
    class Meta:
        model = event_payment
        fields = '__all__'              
class ScheduleForm(forms.ModelForm):
   class Meta:
       model = schedule_management
       fields = ['event_managment', 'start_time', 'end_time', 'topic', 'speaker_management']
     