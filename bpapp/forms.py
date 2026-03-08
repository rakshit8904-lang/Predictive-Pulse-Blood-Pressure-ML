from django import forms

class BPForm(forms.Form):

    gender = forms.IntegerField(label="Gender (0 = Female, 1 = Male)")
    age = forms.IntegerField()

    history = forms.IntegerField(label="History of Hypertension")

    patient = forms.IntegerField(label="Patient Type")

    medication = forms.IntegerField(label="Taking Medication")

    severity = forms.IntegerField()

    breath = forms.IntegerField(label="Breath Shortness")

    visual = forms.IntegerField(label="Visual Changes")

    nose = forms.IntegerField(label="Nose Bleeding")

    diagnosed = forms.IntegerField(label="Years Since Diagnosed")

    systolic = forms.IntegerField()

    diastolic = forms.IntegerField()

    diet = forms.IntegerField(label="Controlled Diet")