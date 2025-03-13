from django.db import models
from ckeditor.fields import RichTextField
import json

class Category(models.Model):
    name = models.CharField("Yangi janr", max_length=255, unique=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Janr"
        verbose_name_plural = "Janrlar"
        ordering = ['name']

class Book(models.Model):
    title = models.CharField("Kitob nomi", max_length=255)
    author = models.CharField("Muallif", max_length=255)
    category = models.ForeignKey(Category, verbose_name="Janri", on_delete=models.CASCADE)
    description = RichTextField("Tavsif")
    image = models.ImageField("Muqova", upload_to='books/covers/')
    isbn = models.CharField("ISBN", max_length=20, blank=True)
    publisher = models.CharField("Nashriyot", max_length=255, blank=True)
    year = models.PositiveIntegerField("Nashr yili", null=True, blank=True)
    views = models.IntegerField("Ko'rishlar", default=1, editable=False)
    created_at = models.DateTimeField("Qo'shilgan sana", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['author']),
            models.Index(fields=['-created_at']),
        ]

class News(models.Model):
    title = models.CharField("Sarlavha", max_length=255)
    content = RichTextField("Matn")
    image = models.ImageField("Rasm", upload_to='news/')
    views = models.IntegerField("Ko'rishlar", default=1, editable=False)
    created_at = models.DateTimeField("Qo'shilgan sana", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
        ordering = ['-created_at']

class Announcement(models.Model):
    title = models.CharField("E'lon sarlavhasi", max_length=255)
    content = RichTextField("E'lon matni")
    views = models.IntegerField("Ko'rishlar", default=1, editable=False)
    created_at = models.DateTimeField("Qo'shilgan sana", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "E'lon"
        verbose_name_plural = "E'lonlar"
        ordering = ['-created_at']

class Statistics(models.Model):
    total_books = models.CharField("Kutubxona fondi", max_length=100)
    new_books = models.CharField("Yangi kelgan adabiyotlar", max_length=100) 
    total_readers = models.CharField("Kitobxonlar soni", max_length=100)
    new_readers = models.CharField("Yangi kitobxonlar", max_length=100)
    
    def __str__(self):
        return "Statistik ma'lumotlar"

    class Meta:
        verbose_name = "Statistika"
        verbose_name_plural = "Statistika"

class Staff(models.Model):
    full_name = models.CharField("F.I.O", max_length=255)
    position = models.CharField("Lavozim", max_length=255)
    phone = models.CharField("Telefon", max_length=100)
    email = models.EmailField("Email", max_length=255)
    reception_days = models.CharField("Qabul kunlari", max_length=255)
    bio = RichTextField("Ma'lumot")
    image = models.ImageField("Rasm", upload_to='staff/')
    order = models.IntegerField("Tartib raqami", default=0)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Xodim"
        verbose_name_plural = "Xodimlar"
        ordering = ['order']

class StudyHall(models.Model):
    title = models.CharField("Nomi", max_length=255)
    image = models.ImageField("Rasm", upload_to='study_halls/')
    description = models.TextField("Izoh", blank=True)
    order = models.IntegerField("Tartib raqami", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "O'quv zali rasmi"
        verbose_name_plural = "O'quv zallari rasmlari"
        ordering = ['order']

class Management(models.Model):
    full_name = models.CharField("F.I.O", max_length=255)
    position = models.CharField("Lavozim", max_length=255)
    phone = models.CharField("Telefon", max_length=100)
    email = models.EmailField("Email", max_length=255, null=True, blank=True)
    bio = RichTextField("Ma'lumot", blank=True, null=True)
    image = models.ImageField("Rasm", upload_to='management/', null=True, blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Rahbar"
        verbose_name_plural = "Rahbarlar"
        ordering = ['full_name']

class About(models.Model):
    name = models.CharField("Kutubxona nomi", max_length=255)
    history = RichTextField("Kutubxona tarixi")
    history_image = models.ImageField("Tarix uchun rasm", upload_to='about/', blank=True)
    mission = RichTextField("Kutubxona vazifasi")
    structure_image = models.ImageField("Tuzilma rasmi", upload_to='about/', null=True, blank=True)
    management = models.ManyToManyField(Management, verbose_name="Rahbarlar")
    study_halls = RichTextField("O'quv zallar haqida")
    work_order = RichTextField("Ish tartibi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kutubxona haqida"
        verbose_name_plural = "Kutubxona haqida"

class Service(models.Model):
    title = models.CharField("Xizmat nomi", max_length=255)
    description = RichTextField("Xizmat haqida")
    icon = models.FileField("Ikonka", upload_to='services/', blank=True)
    order = models.IntegerField("Tartib raqami", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Xizmat turi"
        verbose_name_plural = "Xizmat turlari"
        ordering = ['order']

class Contact(models.Model):
    address = RichTextField("Manzil")
    phone = models.CharField("Telefon raqami", max_length=100)
    email = models.EmailField("Email", max_length=255)
    location_map = models.TextField("Xaritadagi manzil (iframe)")
    work_hours = models.CharField("Ish vaqti", max_length=100)
    social_links = models.TextField(
        "Ijtimoiy tarmoqlar", 
        help_text="JSON formatda kiriting. Masalan: {'telegram': 'https://t.me/example'}"
    )

    def get_social_links(self):
        try:
            return json.loads(self.social_links or '{}')  # None bo'lgan holatni ham tekshirish
        except json.JSONDecodeError:
            return {}

    def __str__(self):
        return "Bog'lanish ma'lumotlari"

    class Meta:
        verbose_name = "Bog'lanish"
        verbose_name_plural = "Bog'lanish ma'lumotlari"

class Slider(models.Model):
    image = models.ImageField("Rasm", upload_to='sliders/')
    order = models.IntegerField("Tartib raqami", default=0)
    
    def __str__(self):
        return f"Slayder {self.id}"

    class Meta:
        verbose_name = "Slayder"
        verbose_name_plural = "Slayderlar"
        ordering = ['order']

class Vacancy(models.Model):
    title = models.CharField("Lavozim nomi", max_length=255)
    education = models.CharField("Ta'lim", max_length=255)
    salary = models.CharField("Ish haqi", max_length=255)
    workload = models.CharField("Stavka", max_length=100)
    requirements = RichTextField("Talablar", blank=True)
    description = RichTextField("Qo'shimcha ma'lumot", blank=True)
    is_active = models.BooleanField("Faol", default=True)
    created_at = models.DateTimeField("Yaratilgan sana", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Bo'sh ish o'rni"
        verbose_name_plural = "Bo'sh ish o'rinlari"
        ordering = ['-created_at']

class Structure(models.Model):
    structure_image = models.ImageField("Tuzilma rasmi", upload_to='structure/')
    updated_at = models.DateTimeField("Yangilangan sana", auto_now=True)

    class Meta:
        verbose_name = "Tuzilma"
        verbose_name_plural = "Tuzilma"

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = Structure.objects.get(pk=self.pk)
            if old_instance.structure_image and self.structure_image != old_instance.structure_image:
                old_instance.structure_image.delete(save=False)
        
        if not self.pk and Structure.objects.exists():
            Structure.objects.all().delete()
            
        super().save(*args, **kwargs)

class Search(models.Model):
    query = models.CharField("So'rov", max_length=255)
    results = models.ManyToManyField(
        Book,
        verbose_name="Topilgan kitoblar",
        related_name="searches"
    )
    created_at = models.DateTimeField("Qidirilgan vaqt", auto_now_add=True)

    def __str__(self):
        return f"{self.query} ({self.results.count()} ta natija)"

    class Meta:
        verbose_name = "Qidiruv"
        verbose_name_plural = "Qidiruvlar"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['query']),
            models.Index(fields=['-created_at']),
        ]