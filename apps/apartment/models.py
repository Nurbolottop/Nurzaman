from django.db import models
from django_resized.forms import ResizedImageField 
from django.core.exceptions import ValidationError
from django.conf import settings
from django.core.files import File
from django.db import models
import tempfile
from PIL import Image
from fpdf import FPDF
import os

# Create your models here.
class Category(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название категории",
        blank= True, null = True

    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Категория квартир"
        verbose_name_plural = "Категория квартир"

################################################################################################################################################################################

class Rooms(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Сколько Комнат"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Добавить Комнаты"
        verbose_name_plural = "Добавить Комнаты"

################################################################################################################################################################################

class Status(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Статус квартиры"
    )
    it = models.IntegerField(
        verbose_name = "Id"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Добавить Статус"
        verbose_name_plural = "Добавить Статус"
        
################################################################################################################################################################################

class Block(models.Model):
    number = models.IntegerField(
        default = 0,
        verbose_name = "Название блока"
    )
    date = models.DateTimeField(
        blank=True,null = True,
        verbose_name = "Дата сдачи"
    )
    it = models.IntegerField(
        verbose_name = "Нумерация",
        blank=True,null=True
    )

    def apartments_count(self):
        # Подсчитываем количество квартир через связанные объекты Floor и Apartment
        return Apartment.objects.filter(floor__block=self).count()
    def __str__(self):
        return f"Блок: {self.number}" 
    
    class Meta:
        verbose_name = "Добавить Блок"
        verbose_name_plural = "Добавить Блоки"

################################################################################################################################################################################

class Floor(models.Model):
    block = models.ForeignKey(
        'Block',
        on_delete=models.CASCADE,
        verbose_name="Выбрать блок"
    )
    title = models.IntegerField(
        default=0,
        verbose_name="этаж"
    )

    def __str__(self):
        return f"{self.block} - {self.title} этаж"

    class Meta:
        verbose_name = "Добавить Этаж"
        verbose_name_plural = "Добавить Этажи"
class Osob(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название особенности"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Добавить Особенность"
        verbose_name_plural = "Добавить Особенности"


class Apartment(models.Model):
    category = models.ForeignKey(
        Category,
        related_name = "category_room",
        on_delete = models.CASCADE,
        verbose_name = "Выбрерите категорию"
    )
    floor = models.ForeignKey(
        Floor,
        related_name='floor_form',
        on_delete = models.CASCADE,
        verbose_name = "Сколько этаж",
    )
    room = models.ForeignKey(
        Rooms,
        on_delete = models.CASCADE,
        verbose_name = "Выбрерите сколько комнат"
    )
    status = models.ForeignKey(
        Status,
        related_name = "choise_room",
        on_delete = models.CASCADE,
        verbose_name = "Выбрерите статус"
    )

    razmer = models.FloatField(
        verbose_name = "Введите размер"
    )
    info = models.CharField(
        max_length = 255,
        verbose_name ="Дополнительная информация",
        blank = True,null=True

    )
    layote = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='layote/',
        verbose_name="Фотография планировки",
        blank = True,null=True

    )
    plan = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='plan/',
        verbose_name="Фотография на плане этажа",
        blank = True,null=True

    )
    object = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='object/',
        verbose_name="Фотография на объекте",
        blank = True,null=True
    )
    price = models.IntegerField(
        verbose_name = "Цена"
    )
    exploitation = models.CharField(
        max_length = 255,
        verbose_name = "Ввод в эксплуатацию"
    )
    layout_text = models.CharField(
        max_length = 255,
        verbose_name = "Тип планировок "
    )
    pdf = models.FileField(
        upload_to='pdfs/',
        blank=True, null=True
    )

    def __str__(self):
        return self.info

    class Meta:
        verbose_name = "Добавить Квартиру"
        verbose_name_plural = "Добавить Квартиру"

################################################################################################################################################################################
    def clean(self):
        # Проверяем, сколько уже есть квартир для данного этажа
        floor_count = Apartment.objects.filter(floor=self.floor).count()

        # Если уже выбрано 4 квартиры для этого этажа, выходим с ошибкой
        if floor_count >= 4:
            raise ValidationError("Нельзя добавить более 4 квартир для данного этажа.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    def convert_images_to_pdf(self):
        pdf = FPDF()
        added_images = False

        for field in [self.layote, self.plan, self.object]:
            if field:
                img_path = os.path.join(settings.MEDIA_ROOT, field.name)
                if os.path.exists(img_path):
                    try:
                        img = Image.open(img_path)
                        # Если изображение в формате WEBP, конвертируем его
                        if img.format == 'WEBP':
                            # Конвертируем в RGB, если изображение имеет альфа-канал
                            if img.mode == 'RGBA':
                                img = img.convert('RGB')
                            # Сохраняем изображение во временный файл
                            with tempfile.NamedTemporaryFile(suffix='.jpeg', delete=False) as tmp_img:
                                img.save(tmp_img, format='JPEG')
                                tmp_img_path = tmp_img.name
                            # Добавляем страницу и изображение в PDF
                            pdf.add_page()
                            pdf.image(tmp_img_path, x=10, y=8, w=190)
                            added_images = True
                            # Удаляем временный файл изображения
                            os.unlink(tmp_img_path)
                    except IOError as e:
                        print(f"Ошибка при открытии изображения {img_path}: {e}")

        # Сохраняем PDF только если были добавлены изображения
        if added_images:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_pdf:
                pdf.output(temp_pdf.name)
                temp_pdf.seek(0)
                self.pdf.save(f"{self.id}_apartment.pdf", File(temp_pdf), save=False)
                os.unlink(temp_pdf.name)

    def save(self, *args, **kwargs):
        # Вызываем функцию конвертации перед сохранением экземпляра
        self.convert_images_to_pdf()
        # Сохраняем экземпляр модели
        super().save(*args, **kwargs)

################################################################################################################################################################################


class ApartmentOsob(models.Model):
    settings = models.ForeignKey(Apartment, related_name='apartmentosob', on_delete=models.CASCADE)
    title = models.ForeignKey(Category,related_name = "osob",on_delete = models.CASCADE)
    
    class Meta:
        unique_together = ('settings', 'title')
        verbose_name = "Добавить Особенности"
        verbose_name_plural = "Добавить Особенности"

################################################################################################################################################################################
