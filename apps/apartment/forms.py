from django import forms
from .models import Apartment, Floor, Category, Rooms, Status


class ApartmentSearchForm(forms.Form):
    min_price = forms.IntegerField(label='Минимальная цена', required=False)
    max_price = forms.IntegerField(label='Максимальная цена', required=False)
    min_size = forms.FloatField(label='Минимальный размер', required=False)
    max_size = forms.FloatField(label='Максимальный размер', required=False)
    floor = forms.ModelChoiceField(queryset=Floor.objects.all(), required=False, label='Этаж')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, label='Категория')
    rooms = forms.ModelChoiceField(queryset=Rooms.objects.all(), required=False, label='Количество комнат')
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=False, label='Статус')
    
    # Здесь вы можете добавить любые дополнительные поля, которые вам нужны для фильтрации
