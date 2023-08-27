# Generated by Django 4.2.2 on 2023-07-03 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event_app', '0003_participant_management_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='event_managment',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='event_managment',
            name='location',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='event_managment',
            name='title',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='event_payment',
            name='payment_method',
            field=models.CharField(choices=[('MoMo', 'Mobile Money'), ('PayPal', 'PayPal'), ('Airtel Money', 'Airtel Money'), ('MasterCard', 'MasterCard'), ('Visa', 'Visa Card'), ('Wire transfer', 'Wire transfer'), ('Western Union', 'Western Union')], max_length=20),
        ),
        migrations.AlterField(
            model_name='event_payment',
            name='payment_status',
            field=models.CharField(choices=[('Paid', 'paid'), ('Pending', 'pending'), ('Failed', 'failed')], max_length=20),
        ),
        migrations.AlterField(
            model_name='event_payment',
            name='transaction_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='participant_management',
            name='name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='participant_management',
            name='password',
            field=models.CharField(default='0000', max_length=15),
        ),
        migrations.AlterField(
            model_name='schedule_management',
            name='topic',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='speaker_management',
            name='name',
            field=models.CharField(max_length=15),
        ),
    ]