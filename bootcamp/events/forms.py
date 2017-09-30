from django import forms

from bootcamp.events.models import Events


class EventsForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=255)

    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        max_length=4000)

    Dateevent = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    nummaxplayers = forms.NumericField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Events
        fields = ['title', 'content', 'dateevent', 'status']
