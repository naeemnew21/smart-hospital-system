# Generated by Django 3.2.9 on 2022-03-15 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ys_appointment', '0001_initial'),
        ('ys_laboratory', '0002_auto_20220315_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labmodel',
            name='appoint',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ys_appointment.requsetappointment'),
        ),
    ]