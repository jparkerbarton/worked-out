from django import forms
from workouts.models import Client, Workout

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('trainer',)
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'birth_date': 'Birth Date',
            'weight_lbs': 'Weight in pounds',
            'height_in': 'Height in inches',
            'waist_in': 'Waist in inches',
            'resting_heart_rate_bpm': 'Resting Heart Rate BPM',
            'blood_pressure_mmhg': 'Blood Pressure mmHg',
            'meds': 'Medications',
            'doctor_release': 'Has a doctor\'s release?',
            'medical_history_risks': 'Medical History and Risk Factors',
            'ambulatory': 'Can stand to work out?',
            'goals_incentives': 'Goals and Incentives',
        }
        # count on the default widgets for most
        YEARS = range(1930, 2025)
        widgets = {
            'birth_date': forms.SelectDateWidget(attrs={'class': 'form-control'}, years=YEARS),
        }

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        exclude = ('client',)
        labels = {
            'date': 'Date',
            'duration_min': 'Duration in mins.',
            'warmups': 'Warmups',
            'large_muscle_group_exercises': 'Large Muscle Group Exercises',
            'small_muscle_group_exercises': 'Small Muscle Group Exercises',
            'cooldowns': 'Cooldowns and Stretches',
            'other_notes': 'Accommodations and Other Notes',
        }
        # again counting on default widgets
        widgets = {
            'date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
        }