from django.shortcuts import render
from django.db import models
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import F
from .models import (
    Announcement, Book, Category, Search,
    News, About, Contact, Staff, 
    StudyHall, Service, Slider, Vacancy, Structure
)

class BaseContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['contact'] = Contact.objects.first()
        return context

class HomeView(BaseContextMixin, ListView):
    template_name = 'index.html'
    model = News
    context_object_name = 'latest_news'

    def get_queryset(self):
        return News.objects.select_related().all()[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_books'] = Book.objects.select_related('category').all()[:6]
        context['sliders'] = Slider.objects.all().order_by('order')
        context['announcements'] = Announcement.objects.all()[:3]
        return context

class NewsListView(BaseContextMixin, ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news_list'
    paginate_by = 9
    ordering = ['-created_at']

class NewsDetailView(BaseContextMixin, DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'

    def get_object(self):
        obj = super().get_object()
        News.objects.filter(id=obj.id).update(views=F('views') + 1)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # So'nggi yangiliklar
        context['latest_news'] = News.objects.exclude(
            id=self.object.id
        ).order_by('-created_at')[:3]
        return context

class AnnouncementListView(BaseContextMixin, ListView):
    model = Announcement
    template_name = 'announcements.html'
    context_object_name = 'announcements'
    paginate_by = 9
    ordering = ['-created_at']

class AnnouncementDetailView(BaseContextMixin, DetailView):
    model = Announcement
    template_name = 'announcement_detail.html'
    context_object_name = 'announcement'

    def get_object(self):
        obj = super().get_object()
        Announcement.objects.filter(id=obj.id).update(views=F('views') + 1)
        return obj

class BookListView(BaseContextMixin, ListView):
    model = Book
    template_name = 'library_category.html'
    context_object_name = 'books'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = Book.objects.select_related('category')
        category_id = self.request.GET.get('category')
        search = self.request.GET.get('search')

        if category_id:
            queryset = queryset.filter(category_id=category_id)
        
        if search:
            # Barcha maydonlar bo'yicha qidirish
            search_results = queryset.filter(
                models.Q(title__icontains=search) |
                models.Q(author__icontains=search) |
                models.Q(description__icontains=search) |
                models.Q(isbn__icontains=search) |
                models.Q(publisher__icontains=search) |
                models.Q(year__icontains=search)
            )
            
            # Qidiruv natijasini saqlash
            if search_results.exists():
                search_entry = Search.objects.create(query=search)
                search_entry.results.set(search_results)
                
            return search_results
            
        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.prefetch_related('book_set').all()
        context['selected_category'] = self.request.GET.get('category')
        context['total_books'] = Book.objects.count()
        
        category_id = self.request.GET.get('category')
        if category_id:
            try:
                context['current_category'] = context['categories'].get(id=category_id)
            except Category.DoesNotExist:
                pass
        return context

class BookDetailView(BaseContextMixin, DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

    def get_object(self):
        obj = super().get_object()
        obj.views = F('views') + 1
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['similar_books'] = Book.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:4]
        return context

class StaffListView(BaseContextMixin, ListView):
    model = Staff
    template_name = 'department.html'
    context_object_name = 'staff_list'
    ordering = ['order']

class StudyHallListView(BaseContextMixin, ListView):
    model = StudyHall
    template_name = 'study_halls.html'  # Fayl nomi to'g'ri yozilganiga ishonch hosil qilish
    context_object_name = 'halls'
    ordering = ['order']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        return context

class ServiceListView(BaseContextMixin, ListView):
    model = Service
    template_name = 'services.html'
    context_object_name = 'services'
    ordering = ['order']

class LibraryHistoryView(BaseContextMixin, TemplateView):
    template_name = 'lib_history.html'

class StatisticsView(BaseContextMixin, TemplateView):
    template_name = 'statistics.html'

class TermsOfUseView(BaseContextMixin, TemplateView):
    template_name = 'terms_of_use.html'

class VacancyListView(BaseContextMixin, ListView):
    model = Vacancy
    template_name = 'vacancies.html'
    context_object_name = 'vacancies'
    
    def get_queryset(self):
        return Vacancy.objects.filter(is_active=True)

class WorkOrderView(BaseContextMixin, TemplateView):
    template_name = 'work_order.html'

class ContactView(BaseContextMixin, TemplateView):
    template_name = 'contacts.html'

class StructureView(BaseContextMixin, TemplateView):
    template_name = 'structure.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['structure'] = Structure.objects.first()
        return context
