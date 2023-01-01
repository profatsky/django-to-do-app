from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField, Form


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].help_text = None


class PositionForm(Form):
    position = CharField()
