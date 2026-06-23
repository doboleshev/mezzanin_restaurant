# Mezzanin Restaurant

Веб-сайт ресторана **«Мезонин»** — Django-приложение для онлайн-бронирования столиков с меню, личным кабинетом и административной панелью.

**Репозиторий:** [github.com/doboleshev/mezzanin_restaurant](https://github.com/doboleshev/mezzanin_restaurant)

## Возможности

- Главная страница с описанием ресторана и призывом к бронированию
- Страница **«О нас»** с историей и командой
- **Меню** с категориями блюд, ценами и фотографиями
- **Онлайн-бронирование** столиков (требуется регистрация)
- **Личный кабинет** и список бронирований пользователя
- **Регистрация и авторизация**
- **Админ-панель** Django для управления данными

## Стек технологий

| Категория | Технологии |
|-----------|------------|
| Backend | Python, Django 6.0 |
| Frontend | HTML5, CSS3, JavaScript, Bootstrap 5 |
| База данных | SQLite3 |
| Шаблоны | Django Template Language |
| Иконки | Bootstrap Icons |

## Быстрый старт

### 1. Клонирование репозитория

```bash
git clone https://github.com/doboleshev/mezzanin_restaurant.git
cd mezzanin_restaurant/restaurant_booking
```

### 2. Виртуальное окружение

```bash
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. База данных

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Запуск сервера

```bash
python manage.py runserver
```

Если порт `8000` занят другим проектом:

```bash
python manage.py runserver 8001
```

## Страницы сайта

| URL | Описание |
|-----|----------|
| `/` | Главная |
| `/about/` | О ресторане |
| `/menu/` | Меню |
| `/bookings/create/` | Бронирование столика |
| `/bookings/` | Мои бронирования |
| `/register/` | Регистрация |
| `/login/` | Вход |
| `/profile/` | Профиль пользователя |
| `/admin/` | Админ-панель |

## Структура проекта

```
mezzanin_restaurant/
└── restaurant_booking/
    ├── accounts/              # Регистрация, профиль
    ├── bookings/              # Бронирования столиков
    ├── contacts/              # Обратная связь
    ├── pages/                 # Главная, «О нас», меню
    ├── restaurant_booking/    # Настройки Django
    ├── templates/             # HTML-шаблоны
    ├── manage.py
    └── requirements.txt
```

## Основные модели

- **User** — пользователи (Django Auth)
- **Table** — столики ресторана
- **Booking** — бронирования
- **ContactMessage** — сообщения обратной связи

## Разработка

Меню блюд хранится в `restaurant_booking/pages/menu_data.py`.  
Для изменения категорий, описаний, цен и изображений достаточно отредактировать этот файл.

## Автор

**Денис** — [GitHub @doboleshev](https://github.com/doboleshev)

## Лицензия

Проект создан в образовательных целях.
