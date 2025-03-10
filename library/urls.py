from django.urls import path
from .views import (
    HomeView, NewsListView, NewsDetailView,
    AnnouncementListView, AnnouncementDetailView,
    BookListView, BookDetailView,
    StaffListView, StudyHallListView, ServiceListView,
    LibraryHistoryView, StatisticsView, TermsOfUseView,
    VacancyListView, WorkOrderView, ContactView, StructureView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news/', NewsListView.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('announcements/', AnnouncementListView.as_view(), name='announcements'),
    path('announcements/<int:pk>/', AnnouncementDetailView.as_view(), name='announcement_detail'),
    path('library/', BookListView.as_view(), name='library'),
    path('library/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('library-history/', LibraryHistoryView.as_view(), name='library_history'),
    path('department/', StaffListView.as_view(), name='department'),
    path('study-halls/', StudyHallListView.as_view(), name='study_halls'),
    path('services/', ServiceListView.as_view(), name='services'),
    path('statistics/', StatisticsView.as_view(), name='statistics'),
    path('terms-of-use/', TermsOfUseView.as_view(), name='terms_of_use'),
    path('work-order/', WorkOrderView.as_view(), name='work_order'),
    path('vacancies/', VacancyListView.as_view(), name='vacancies'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('structure/', StructureView.as_view(), name='structure'),
]