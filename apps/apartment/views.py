from django.shortcuts import render,redirect
from django.core.mail import send_mail
from apps.contacts.models import Contact,Messages,View
from apps.base.models import Settings,ContactInfo
from apps.apartment import models
from apps.telegram_bot.views import get_text
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from apps.apartment.forms import ApartmentSearchForm

# Create your views here.
def catalog(request):
#base
    settings = Settings.objects.latest("id")
    apartments = models.Apartment.objects.all()
#Пагинация



# фильтрация квартир по категории
    categories = models.Category.objects.all()
    category_id = request.GET.get('category')

    if category_id:
        apartments = apartments.filter(category__id=category_id)

# фильтрация квартир по комнатам
    rooms = models.Rooms.objects.all()
    room_id = request.GET.get("room")

    if room_id:
        apartments = apartments.filter(room__id=room_id)  

    features = models.Osob.objects.all()
    feature_id = request.GET.get('Ben')  # Получаем ID выбранной особенности из запроса

    if feature_id and feature_id != "0":
        apartments = apartments.filter(apartmentosob__title_id=feature_id)

# фильтрация квартир по Цене, Площади, Этажам
    search_form = ApartmentSearchForm(request.GET or None)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if search_form.is_valid():
            apartments = apartments.filter(
                price__gte=search_form.cleaned_data.get('min_price', 0),
                price__lte=search_form.cleaned_data.get('max_price', 1000000000),
                razmer__gte=search_form.cleaned_data.get('min_size', 0),
                razmer__lte=search_form.cleaned_data.get('max_size', 1000),
                floor__title__gte=search_form.cleaned_data.get('min_floor', 0),
                floor__title__lte=search_form.cleaned_data.get('max_floor', 11),
           
            )
            apartment_count = apartments.count()
            
            page = request.GET.get('page', 1)
            paginator = Paginator(apartments, 4)  # 4 квартиры на страницу

            try:
                apartments = paginator.page(page)
            except PageNotAnInteger:
                apartments = paginator.page(1)
            except EmptyPage:
                apartments = paginator.page(paginator.num_pages)

            # Формируем данные для каждой квартиры
            apartments_data = list(apartments.object_list.values(
                'id', 
                'category__title', 
                'info',
                'room__title', 
                'status__title', 
                'razmer', 
                'price',
                'layote',  
                'floor__title'
            ))

            for apt in apartments_data:
                apt['layote_url'] = apt['layote'] and getattr(models.Apartment.objects.get(pk=apt['id']).layote, 'url', '')
            print(f"Page: {page}, Showing apartments: {len(apartments_data)}")
            # Возвращаем данные в JSON-формате
            return JsonResponse({
                'results': apartments_data,
                'apartment_count': paginator.count,
                'has_next': apartments.has_next(),
                'has_previous': apartments.has_previous(),
                'next_page_number': apartments.next_page_number() if apartments.has_next() else None,
                'previous_page_number': apartments.previous_page_number() if apartments.has_previous() else None,
            }, safe=False)
        else:
            return JsonResponse({'error': search_form.errors}, status=400)

#подсчет количество квартир    
    apartment_count = apartments.count()

# Контактная информация и отправка POST запросов
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
                ✅Оставлена заявка на обратный звонок🤗
                         
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                         
Имя пользователя: {name}
emai: {email}
Номер телефона: {number}""")
                return redirect('index')

    return render(request, 'catalog.html', locals())

def planing(request,id):
    #base
    settings = Settings.objects.latest("id")

    #apartment
    apartment = models.Apartment.objects.get(id=id)
    apartment_slide = models.Apartment.objects.all().order_by('?')[:5]

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
                contact = Messages.objects.create(name=name, email=email, phone=phone,message=message)
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
    return render(request, 'planing.html', locals())

