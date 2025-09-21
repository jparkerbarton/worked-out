from django.db import models
from accounts.models import User
import datetime

# Create your models here.
class Client(models.Model):
    trainer = models.ForeignKey(User, on_delete=models.PROTECT)
    first_name = models.CharField("First Name", max_length=64, default='')
    last_name = models.CharField("Last Name", max_length=64, default='')
    birth_date = models.DateField(null=True, blank=True)
    weight_lbs = models.IntegerField("Weight in pounds", null=True, blank=True)
    height_in = models.IntegerField("Height in inches", null=True, blank=True)
    waist_in = models.IntegerField("Waist in inches", null=True, blank=True)
    resting_heart_rate_bpm = models.IntegerField("Resting Heart Rate BPM", null=True, blank=True)
    blood_pressure_mmhg = models.IntegerField("Blood Pressure mmHg", null=True, blank=True)
    meds = models.TextField("Medications", null=True, blank=True)
    doctor_release = models.BooleanField("Has a doctor's release?", default=False)
    medical_history_risks = models.TextField("Medical History and Risk Factors", null=True, blank=True)
    ambulatory = models.BooleanField("Can stand to work out?", default=True)
    goals_incentives = models.TextField("Goals and Incentives", null=True, blank=True)

class Workout(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True, default=datetime.date.today)
    warmups = models.TextField("Warmups", null=True, blank=True)
    large_muscle_group_exercises = models.TextField("Large Muscle Group Exercises", null=True, blank=True)
    small_muscle_group_exercises = models.TextField("Small Muscle Group Exercises", null=True, blank=True)
    cooldowns = models.TextField("Cooldowns and Stretches", null=True, blank=True)
    other_notes = models.TextField("Accommodations and Other Notes", null=True, blank=True)