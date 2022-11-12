
from django import forms
from .models import Emp

class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Enter your email",max_length=100,required=True)
    name=forms.CharField(label="Enter your name",max_length=100)
    feedback = forms.CharField(label="Your Feedback",widget=forms.Textarea)

# Adding CLass From Stackoverflow ...
    def __init__(self, *args, **kwargs):
      super(FeedbackForm,self).__init__(*args,**kwargs)
      for visible in self.visible_fields():
         visible.field.widget.attrs['class'] = 'form-control'



