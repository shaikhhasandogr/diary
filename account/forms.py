from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['doc_no', 'received_date', 'received_from', 'doc_type', 'language', 'to', 'remark']

        widgets = {
            'received_date': forms.DateInput(attrs={'type': 'date'}),
            'doc_type': forms.Select(choices=Document.TYPE_CHOICES),
            'language': forms.SelectMultiple(choices=Document.LANGUAGE_CHOICES),
            'to': forms.SelectMultiple(),  # For multiple users
            'remark': forms.Textarea(attrs={'rows': 3}),
        }

