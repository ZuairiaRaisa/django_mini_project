from django import forms
from .models import ContactMessage, Order

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity']