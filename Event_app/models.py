from django.db import models
from django.conf import settings

class category(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name
class event_managment(models.Model):
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=10)
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name='events')
    is_free = models.BooleanField()
    
    def __str__(self):
        return self.title

class speaker_management(models.Model):
    name = models.CharField(max_length = 15) 
    biography = models.TextField() 
    optional_photo = models.ImageField(upload_to='speaker_photo', blank=True , null=True)
    email_address = models.EmailField() 
    phone_number = models.CharField(max_length = 25)  
    linkedin = models.URLField(blank= True)  
    twitter = models.URLField(blank= True)  

    def __str__(self):
       return self.name

class participant_management(models.Model):
    name = models.CharField(max_length= 15)
    email_address = models.EmailField() 
    phone_number = models.CharField(max_length = 25)
    events_attending = models.ManyToManyField(event_managment , blank = True, related_name='participants')
    password = models.CharField(max_length=15, default='0000')
     
    def __str__(self):
        return self.name

class schedule_management(models.Model):
    event_managment = models.ForeignKey(event_managment ,on_delete = models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    topic = models.CharField(max_length = 50)
    speaker_management =models.ForeignKey(speaker_management, on_delete =models.CASCADE, related_name='schedules')

    def __str__(self):
        return self.topic

class event_payment(models.Model):
    payment_status_choices = (('Paid','paid'),
    ('Pending','pending'),
    ('Failed', 'failed'))
    payment_method_choices = (('MoMo', 'Mobile Money'), ('PayPal', 'PayPal'), ('Airtel Money', 'Airtel Money'), ('MasterCard', 'MasterCard'), ('Visa', 'Visa Card'), ('Wire transfer', 'Wire transfer'), ('Western Union', 'Western Union'),)
    participant_management = models.ForeignKey(participant_management , on_delete=models.CASCADE, related_name='payments')
    event_managment = models.ForeignKey(event_managment , on_delete=models.CASCADE)
    amount_paid=models.DecimalField(max_digits=10,decimal_places=3)
    payment_method=models.CharField(max_length=20, choices=payment_method_choices)
    payment_date=models.DateTimeField(auto_now_add=True)
    transaction_id=models.CharField(max_length=10)
    payment_status=models.CharField(max_length=20,choices=payment_status_choices)
    def __str__(self):
        return f"{self.participant_management.name} - {self.event_managment.title} - Payment ID: {self.id}"

    












