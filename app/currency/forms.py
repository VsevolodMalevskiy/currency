from django import forms
from currency.models import Rate, Source, ContactUs


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'buy',
            'sell',
            'source',
            'currency'
        )


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = (
            'source_url',
            'name',
            'phone'
        )


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'name',
            'email',
            'subject',
            'message'
        )
