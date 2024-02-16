from django.contrib import admin

from apps.secondary import models

# Register your models here.

################################################################################################################################################################################

class SlideFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title',)
    search_fields = ('title',)

################################################################################################################################################################################

class ProjectsFilterAdmin(admin.ModelAdmin):
    list_filter = ('image', )
    list_display = ('image',)
    search_fields = ('image',)
################################################################################################################################################################################

class PrideFilterAdmin(admin.ModelAdmin):
    list_filter = ('first','second','third','four','five','six', )
    list_display = ('first','second','third','four','five','six',)
    search_fields = ('first','second','third','four','five','six',)

################################################################################################################################################################################

class EuroImageInline(admin.TabularInline):
    model = models.EuroImage
    extra = 1

class EuroFilterAdmin(admin.ModelAdmin):
    list_filter = ('descriptions',)
    list_display = ('descriptions',)
    search_fields = ('descriptions',)
    inlines = [EuroImageInline]

################################################################################################################################################################################

class ChoiseImageInline(admin.TabularInline):
    model = models.ChoiseTitle
    extra = 1

class ChoiseFilterAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('title',)
    search_fields = ('title',)
    inlines = [ChoiseImageInline]

################################################################################################################################################################################

class AdvantagesImageInline(admin.TabularInline):
    model = models.AdvantagesTitle
    extra = 1

class AdvantagesFilterAdmin(admin.ModelAdmin):
    list_filter = ('descriptions',)
    list_display = ('descriptions',)
    search_fields = ('descriptions',)
    inlines = [AdvantagesImageInline]

################################################################################################################################################################################

class AdvantagesTwoImageInline(admin.TabularInline):
    model = models.AdvantagesTwoTitle
    extra = 1

class AdvantagesTwoFilterAdmin(admin.ModelAdmin):
    list_filter = ('descriptions',)
    list_display = ('descriptions',)
    search_fields = ('descriptions',)
    inlines = [AdvantagesTwoImageInline]

################################################################################################################################################################################

class EnvironmentInline(admin.TabularInline):
    model = models.EnviromentTitle
    extra = 1

class EnvironmentFilterAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('title',)
    search_fields = ('title',)
    inlines = [EnvironmentInline]

################################################################################################################################################################################

class StreetFilterAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('title',)
    search_fields = ('title',)

################################################################################################################################################################################

admin.site.register(models.Slide, SlideFilterAdmin)
admin.site.register(models.Projects, ProjectsFilterAdmin)
admin.site.register(models.Pride, PrideFilterAdmin)
admin.site.register(models.Euro, EuroFilterAdmin)
admin.site.register(models.Choise, ChoiseFilterAdmin)
admin.site.register(models.Advantages, AdvantagesFilterAdmin)
admin.site.register(models.Environment, EnvironmentFilterAdmin)
admin.site.register(models.Street, StreetFilterAdmin)
admin.site.register(models.AdvantagesTwo, AdvantagesTwoFilterAdmin)



################################################################################################################################################################################
