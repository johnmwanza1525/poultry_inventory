from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Entry, EntryType, Response


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ('title', 'entry_type', 'image', 'excerpt', 'content',)
        widgets = {
            'content': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        types = EntryType.objects.all()
        friendly_names = [(t.id, t.get_friendly_name()) for t in types]

        self.fields['entry_type'].choices = friendly_names


class ResponseForm(forms.ModelForm):

    class Meta:
        model = Response
        fields = ('body',)
