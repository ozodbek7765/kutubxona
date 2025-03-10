from django.contrib import admin
from .models import (
    Category, Book, News, Staff, Slider, Announcement, Structure,
    StudyHall, Service, Vacancy, Contact, About, Management
)
admin.site.site_header = "Arnasoy tuman AKM"
admin.site.site_title = "Arnasoy AKM admin"
admin.site.index_title = "Arnasoy AKM ma'muriyati"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    
    def has_module_permission(self, request):
        return False
    
admin.site.register(Management)

@admin.register(Book) 
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'views']
    list_filter = ['category', 'created_at']
    search_fields = ['title', 'author']
    readonly_fields = ['views']
    
    def get_form(self, request, obj=None, **kwargs):
        Category._meta.managed = True
        return super().get_form(request, obj, **kwargs)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'views', 'created_at']
    search_fields = ['title']
    readonly_fields = ['views']

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'position', 'order']
    list_editable = ['order']

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'views']
    search_fields = ['title', 'content']
    list_filter = ['created_at']
    readonly_fields = ['views']

@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not Structure.objects.exists()

@admin.register(StudyHall)
class StudyHallAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not Contact.objects.exists()

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not About.objects.exists()