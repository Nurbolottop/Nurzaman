from django.db import models
from ckeditor.fields import RichTextField
from django_resized.forms import ResizedImageField 

# Create your models here.
class Slide(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='slide/',
        verbose_name="Фотография",
        blank = True, null = True
    )

    title = models.CharField(
        max_length =  255,
        verbose_name="Название"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Слайд"
        verbose_name_plural = "Слайды"

################################################################################################################################################################################

class Projects(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='projects/',
        verbose_name="Фотография",
        blank = True, null = True
    )


    class Meta:
        verbose_name="Партнер"
        verbose_name_plural = "НАШИ ПРОЕКТЫ"

################################################################################################################################################################################

class Pride(models.Model):
    first = RichTextField(
        verbose_name="Первый Информационный текст",
        blank=True,null=True
    )
    second = RichTextField(
        verbose_name="Второй Информационный текст",
        blank=True,null=True
    )
    third = RichTextField(
        verbose_name="Третий Информационный текст",
        blank=True,null=True
    )
    four = RichTextField(
        verbose_name="Четвертый Информационный текст",
        blank=True,null=True
    )
    five = RichTextField(
        verbose_name="Пятый Информационный текст",
        blank=True,null=True
    )
    six = RichTextField(
        verbose_name="Шестой Информационный текст",
        blank=True,null=True
    )
    def __str__(self):
        return f"{self.first}  - {self.second}  -  {self.third}  -  {self.four}  -  {self.five}  -  {self.six}"
    
    class Meta:
        verbose_name="Нам есть чем гордиться"
        verbose_name_plural = "Нам есть чем гордиться"

################################################################################################################################################################################

class Euro(models.Model):
    descriptions  = RichTextField(
        verbose_name="Информационный текст",
        blank=True,null=True
    )

    def __str__(self):
        return f"{self.descriptions}"
    
    class Meta:
        verbose_name="Что такое Европейский квартал"
        verbose_name_plural = "Что такое Европейский квартал"

class EuroImage(models.Model):
    settings = models.ForeignKey(Euro, related_name='euro_image', on_delete=models.CASCADE)
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='euro/',
        verbose_name="Фотография",
        blank = True, null = True
    )

    class Meta:
        unique_together = ('settings', 'image')

################################################################################################################################################################################

class Choise(models.Model):
    title  = RichTextField(
        verbose_name="Информационный текст",
        blank=True,null=True
    )
    chert = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='Choise_chert/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    def __str__(self):
        return self.title
    
    class Meta:
            verbose_name = "Сделай свой выбор"
            verbose_name_plural = "Сделай свой выбор"
            
class ChoiseTitle(models.Model):
    settings = models.ForeignKey(Choise, related_name='choise_image', on_delete=models.CASCADE)
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    razmer = models.CharField(
        max_length = 255,
        verbose_name = "Площадь"
    )

    class Meta:
        unique_together = ('settings', 'title', 'razmer')

################################################################################################################################################################################

class  Advantages(models.Model):
    descriptions  = RichTextField(
        verbose_name="Информационный текст",
        blank=True,null=True
    )
    def __str__(self):
        return self.descriptions
    
    class Meta:
            verbose_name = "Преимущества номер один"
            verbose_name_plural = "Преимущества номер один"

class AdvantagesTitle(models.Model):
    settings = models.ForeignKey(Advantages, related_name='adventagess', on_delete=models.CASCADE)
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    info  = RichTextField(
        verbose_name="Информационный текст",
        blank=True,null=True
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='Advantages/',
        verbose_name="Фотография",
        blank = True, null = True
    )

    class Meta:
        unique_together = ('settings', 'title', 'info','image')

################################################################################################################################################################################

class  AdvantagesTwo(models.Model):
    descriptions  = RichTextField(
        verbose_name="Информационный текст",
        blank=True,null=True
    )
    def __str__(self):
        return self.descriptions
    
    class Meta:
            verbose_name = "Преимущества номер два"
            verbose_name_plural = "Преимущества номер два"

class AdvantagesTwoTitle(models.Model):
    settings = models.ForeignKey(AdvantagesTwo, related_name='adventagess', on_delete=models.CASCADE)
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    info  = RichTextField(
        verbose_name="Информационный текст",
        blank=True,null=True
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='AdvantagesTwo/',
        verbose_name="Фотография",
        blank = True, null = True
    )

    class Meta:
        unique_together = ('settings', 'title', 'info','image')

################################################################################################################################################################################

class Environment(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='Advantages/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    title =  RichTextField(
        verbose_name="Информационный текст",
        blank=True,null=True
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
            verbose_name = "Окружение Европейского квартала"
            verbose_name_plural = "Окружение Европейского квартала"

class EnviromentTitle(models.Model):
    settings = models.ForeignKey(Environment, related_name='environment_test', on_delete=models.CASCADE)
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    subtitle = models.CharField(
        max_length = 255,
        verbose_name = "Описание"
    )


################################################################################################################################################################################


class Street(models.Model):
    title = RichTextField(
        verbose_name="Заголовок",
        blank=True,null=True
    )
    subtitle = RichTextField(
        verbose_name="Подзаголовок",
        blank=True,null=True
    )

    
    def __str__(self):
        return self.title
    
    class Meta:
            verbose_name = "Улица"
            verbose_name_plural = "Улица"