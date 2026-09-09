from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit

class SignUpForm(UserCreationForm):
   class Meta:
      model = User
      fields = [
         "username",
         "first_name",
         "last_name",
         "email",
         "password1",
         "password2",
      ]
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

      self.helper = FormHelper()

      self.helper.layout = Layout(
         "username",
         Row(
            Column("first_name", css_class="col-md-6"),
            Column("last_name", css_class="col-md-6"),
         ),

         "email",

         Row(
            Column("password1", css_class="col-md-6"),
            Column("password2", css_class="col-md-6"),
         ),
         Submit("submit", "Sign Up"),
      )