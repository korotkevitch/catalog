from django import forms
from django.core.mail import send_mail as django_send_mail
from django.forms import ModelForm
from .models import Contact, FeedbackPhone


class UserForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'  # вместо перечисления всех полей: fields = ['name', 'phone', 'message']

    def send_mail(self):
        return django_send_mail('Сообщение с сайта iko-studio.com',
                    str('Имя: ') + self.cleaned_data['name'] + '\n' + str('Телефон: ') + self.cleaned_data['phone'] + '\n' + str('Сообщение: ') + self.cleaned_data['message'],
                    'no-reply@iko-studio.com',
                    ['info@iko-studio.com'])


class UserForm2(ModelForm):
    class Meta:
        model = FeedbackPhone
        fields = ['date_time', 'phone']

    def send_mail(self):
        return django_send_mail('Просьба позвонить',
                    str('Телефон: ') + self.cleaned_data['phone'],
                    'no-reply@iko-studio.com',
                    ['info@iko-studio.com'])


