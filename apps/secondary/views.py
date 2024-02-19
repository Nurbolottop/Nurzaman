from django.shortcuts import render
from apps.contacts.models import Contact
from apps.base.models import Settings,ContactInfo
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from apps.telegram_bot.views import get_text
from django.http import JsonResponse
from apps.apartment.models import Block,Floor,Apartment
from django.shortcuts import get_object_or_404
from apps.contacts.models import Contact,Messages,View
from django.db.models import Count
# Create your views here.

def get_floors_and_apartments(request):
    # Получаем номер блока из параметров запроса
    block_number = request.GET.get('block_number')
    
    # Если номер блока не предоставлен, возвращаем пустой ответ
    if not block_number:
        return JsonResponse({"error": "Block number not provided"}, status=400)
    
    # Получаем объект блока или возвращаем 404 ошибку, если такого блока нет
    block = get_object_or_404(Block, number=block_number)
    
    # Фильтруем этажи и квартиры по блоку
    floors = Floor.objects.filter(block=block).order_by('title')
    apartments = Apartment.objects.filter(floor__block=block).select_related('floor')

    floor_data = [
        {
            "block": floor.block.number,
            "floor_id": floor.id,
            "floor_title": floor.title
        }
        for floor in floors
    ]
    
    apartment_data = [
        {
            "apartment_id": apartment.id,
            "block": apartment.floor.block.number,
            "floor": apartment.floor.title,
            "room": apartment.room.title,
            "status": apartment.status.it
        } 
        for apartment in apartments
    ]

    return JsonResponse({
        "floors": floor_data,
        "apartments": apartment_data
    })

# Основная функция для рендеринга страницы и обработки формы обратной связи

def genPlaning(request):
    # Собираете данные как раньше
    settings = Settings.objects.latest("id")
    floors = Floor.objects.all().order_by('block', 'title')

    block_data_1 = Block.objects.get(number=1)  # Здесь предполагается, что 'number' это уникальный идентификатор блока
    block_data_2 = Block.objects.get(number=2)  # Здесь предполагается, что 'number' это уникальный идентификатор блока
    block_data_3 = Block.objects.get(number=3)  # Здесь предполагается, что 'number' это уникальный идентификатор блока
    block_data_4 = Block.objects.get(number=4)
    block_data_5 = Block.objects.get(number=5)
    block_data_6 = Block.objects.get(number=6)
    block_data_7 = Block.objects.get(number=7)
    block_data_8 = Block.objects.get(number=8)
    block_data_9 = Block.objects.get(number=9)
    block_data_10 = Block.objects.get(number=10)
    block_data_11 = Block.objects.get(number=11)
    block_data_12 = Block.objects.get(number=12)
    

    blocks = Block.objects.annotate(
        apartments_count=Count('floor__floor_form')  # Используем related_name 'floor_form' в модели Apartment
    ).order_by('number') 

    #contacts
    #contacts
    contactinfo = ContactInfo.objects.latest('id')
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
                ✅Пользователь оставил заявку на  обратный звонок
                         
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
                ✅Пользователь оставил заявку на  обратный звонок
                         
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                         
Имя пользователя: {name}
emai: {email}
Номер телефона: {number}""")
                return redirect('index')
            
        if "quations" in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            consent = request.POST.get('consent') == 'on'  # Проверка, что чекбокс был отмечен
            if consent:
                contact = Messages.objects.create(name=name, email=email, phone=phone,message=message)
                send_mail(
                    f'{name}',
                    f'Здравствуйте {name}, Спасибо за обратную связь, Мы скоро свами свяжемся. Ваша почта: {email}. Ваш вопрос: {message}' ,
                    "noreply@somehost.local",
                    [email])
            if consent:
                get_text(f"""
                ✅Пользователь задал вопрос
                         
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                         
Имя пользователя: {name}
emai: {email}
Номер телефона: {phone}

Вопрос: <b>{message}</b>""")
                return redirect('index')
            
        if "views" in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            consent = request.POST.get('consent') == 'on'  # Проверка, что чекбокс был отмечен
            if consent:
                contact = View.objects.create(name=name, email=email, phone=phone,message=message)
                send_mail(
                    f'{name}',
                    f'Здравствуйте {name}, Спасибо за обратную связь, Мы скоро свами свяжемся. Ваша почта: {email}. Ваш вопрос: {message}' ,
                    "noreply@somehost.local",
                    [email])
            if consent:
                get_text(f"""
                ✅Пользователь оставил заявку на просмотр
                         
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                         
Имя пользователя: {name}
emai: {email}
Номер телефона: {phone}

Коментарий: <b>{message}</b>""")
                return redirect('index')

    return render(request,'genPlaning.html', locals())

def genplaning_detail(request, apartment_id):
    blocks = Block.objects.all()
    apartment = get_object_or_404(Apartment, id=apartment_id)
    # Собираете данные как раньше
    settings = Settings.objects.latest("id")
    floors = Floor.objects.all().order_by('block', 'title')

    block_data_1 = Block.objects.get(number=1)  # Здесь предполагается, что 'number' это уникальный идентификатор блока
    block_data_2 = Block.objects.get(number=2)  # Здесь предполагается, что 'number' это уникальный идентификатор блока
    block_data_3 = Block.objects.get(number=3)  # Здесь предполагается, что 'number' это уникальный идентификатор блока
    block_data_4 = Block.objects.get(number=4)
    block_data_5 = Block.objects.get(number=5)
    block_data_6 = Block.objects.get(number=6)
    block_data_7 = Block.objects.get(number=7)
    block_data_8 = Block.objects.get(number=8)
    block_data_9 = Block.objects.get(number=9)
    block_data_10 = Block.objects.get(number=10)
    block_data_11 = Block.objects.get(number=11)
    block_data_12 = Block.objects.get(number=12)
    

    #contacts
    contactinfo = ContactInfo.objects.latest('id')
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
                ✅Пользователь оставил заявку на  обратный звонок
                         
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
                ✅Пользователь оставил заявку на  обратный звонок
                         
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                         
Имя пользователя: {name}
emai: {email}
Номер телефона: {number}""")
                return redirect('index')
            
        if "quations" in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            consent = request.POST.get('consent') == 'on'  # Проверка, что чекбокс был отмечен
            if consent:
                contact = Messages.objects.create(name=name, email=email, phone=phone,message=message)
                send_mail(
                    f'{name}',
                    f'Здравствуйте {name}, Спасибо за обратную связь, Мы скоро свами свяжемся. Ваша почта: {email}. Ваш вопрос: {message}' ,
                    "noreply@somehost.local",
                    [email])
            if consent:
                get_text(f"""
                ✅Пользователь задал вопрос
                         
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                         
Имя пользователя: {name}
emai: {email}
Номер телефона: {phone}

Вопрос: <b>{message}</b>""")
                return redirect('index')
            
        if "views" in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            consent = request.POST.get('consent') == 'on'  # Проверка, что чекбокс был отмечен
            if consent:
                contact = View.objects.create(name=name, email=email, phone=phone,message=message)
                send_mail(
                    f'{name}',
                    f'Здравствуйте {name}, Спасибо за обратную связь, Мы скоро свами свяжемся. Ваша почта: {email}. Ваш вопрос: {message}' ,
                    "noreply@somehost.local",
                    [email])
            if consent:
                get_text(f"""
                ✅Пользователь оставил заявку на просмотр
                         
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                         
Имя пользователя: {name}
emai: {email}
Номер телефона: {phone}

Коментарий: <b>{message}</b>""")
                return redirect('index')
    return render(request, 'genPlaning_detail.html', locals())

