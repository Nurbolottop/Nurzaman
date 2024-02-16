from django.shortcuts import render,redirect
from apps.base import models
from django.http import HttpResponse
from apps.secondary.models import Slide,Projects,Pride,Euro,Choise,Advantages,Environment,Street,AdvantagesTwo
from apps.contacts.models import Contact
from django.core.mail import send_mail
from apps.telegram_bot.views import get_text
# Create your views here.
def index(request):
    #BASE
    settings = models.Settings.objects.latest("id")
    about = models.About.objects.latest('id')
    gallery = models.Gallery.objects.latest('id')

    #SECONDARY
    slide = Slide.objects.latest('id')
    pride = Pride.objects.latest('id')
    projects = Projects.objects.all()
    euro = Euro.objects.latest("id")
    choise = Choise.objects.latest("id")
    advantages = Advantages.objects.latest("id")
    advantagestwo = AdvantagesTwo.objects.latest("id")

    environment = Environment.objects.all()
    street = Street.objects.latest("id")
    

    #CONTACTS
    contactinfo = models.ContactInfo.objects.latest('id')
    if request.method == "POST":
        if "call1" in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            number = request.POST.get('number')
            consent = request.POST.get('consent') == 'on'  # Проверка, что чекбокс был отмечен
            if consent:
                contact = Contact.objects.create(name=name, email=email, number=number)
                send_mail(
                    f'{name}',
                    f'Здравствуйте {name}, Спасибо за обратную связь, Мы скоро свами свяжемся. Ваша почта: {email}',
                    "noreply@somehost.local",
                    [email])
            if consent:
                get_text(f"""
                ✅Оставлена заявка на обратный звонок
                         
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                         
Имя пользователя: {name}
emai: {email}
Номер телефона: {number}""")
                return redirect('index')
        if "call2" in request.POST:
            name = request.POST.get('name2')
            email = request.POST.get('email2')
            number = request.POST.get('number2')
            consent = request.POST.get('consent2') == 'on'  # Проверка, что чекбокс был отмечен
            if consent:
                contact = Contact.objects.create(name=name, email=email, number=number)
                send_mail(
                    f'{name}',
                    f'Здравствуйте {name}, Спасибо за обратную связь, Мы скоро свами свяжемся. Ваша почта: {email}',
                    "noreply@somehost.local",
                    [email])
            if consent:
                get_text(f"""
                ✅Оставлена заявка на обратный звонок
                         
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                         
Имя пользователя: {name}
emai: {email}
Номер телефона: {number}""")
                return redirect('index')
            
    return render(request,'base/index.html', locals())

################################################################################################################################################################################
