# Arnasoy tuman AKM kutubxonasi

Arnasoy tuman kutubxonasining rasmiy veb-sayti

## O'rnatish

1. Loyihani clone qilish:
```bash
git clone https://github.com/username/kutubxona.git
cd kutubxona
```

2. Virtual muhit yaratish va faollashtirish:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Kerakli kutubxonalarni o'rnatish:
```bash
pip install -r requirements.txt
```

4. Migratsilarni amalga oshirish:
```bash
python manage.py migrate
```

5. Admin foydalanuvchini yaratish:
```bash
python manage.py createsuperuser
```

6. Serverni ishga tushirish:
```bash
python manage.py runserver
```

## Texnologiyalar
- Django 5.1.6
- Python 3.13
- SQLite