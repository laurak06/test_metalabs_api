# test_metalabs_api
# Django REST Auth + JWT + Login Logs

Проект — это REST API на **Django REST Framework**, реализующий:
- регистрацию пользователей с подтверждением по email,  
- авторизацию через **JWT-токены**,  
- восстановление пароля,  
- профиль пользователя,  
- логирование входов (IP + User-Agent) при каждом успешном логине.  

---

## Стек технологий

- **Python 3.11+**
- **Django 5+**
- **Django REST Framework**
- **djangorestframework-simplejwt**
- **django-filter**
- **python-decouple**
- **PostgreSQL**

---

## Установка и запуск проекта

###  Клонирование репозитория

```bash
git clone https://github.com/laurak06/testProjectMetalabs.git
cd testProjectMetalabs
```

###  Виртуальное окружение

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
```

###  Зависимости

```bash
pip install -r requirements.txt
```

###  .env настройки

Создай файл **.env**:

```env
SECRET_KEY= 

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

EMAIL_HOST_USER= 
EMAIL_HOST_PASSWORD=

HOST_FOR_SEND_MAIL=

```

>  Для тестов можно использовать:
> ```env
> EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
> ```

---

###  Миграции и суперпользователь

```bash
python manage.py migrate
python manage.py createsuperuser
```

###  Запуск сервера

```bash
python manage.py runserver
```

---

##  API endpoints

| Метод | URL | Описание |
|-------|------|-----------|
| POST | `/api/v1/users/register/` | Регистрация |
| GET | `/api/v1/users/activate/?code=...` | Активация аккаунта |
| POST | `/api/v1/users/forgot-password/` | Восстановление пароля |
| POST | `/api/v1/users/restore-password/` | Новый пароль |
| POST | `/api/v1/auth/token/` | JWT логин |
| POST | `/api/v1/auth/token/refresh/` | Обновление токена |
| GET / PATCH | `/api/v1/users/me/` | Профиль |
| GET | `/api/v1/logs/login/` | Логи входов |

---

##  Примеры запросов

###  Регистрация
```
POST /api/v1/users/register/
{
  "email": "test@example.com",
  "password": "12345678",
  "password_confirm": "12345678"
}
```

###  JWT Логин
```
POST /api/v1/auth/token/
{
  "email": "test@example.com",
  "password": "12345678"
}
```
**Ответ:**
```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

###  Логи входов
```
GET /api/v1/logs/login/
Authorization: Bearer <access_token>
```

---

##  Логирование входов

Каждый успешный логин сохраняет данные:
| Поле | Тип | Описание |
|------|-----|-----------|
| user | ForeignKey | Пользователь |
| ip_address | IP | IP адрес |
| user_agent | Text | Устройство |
| timestamp | DateTime | Время |

---

##  Автор

**Лаура Кагирова**  
Backend Developer • Django & REST API  
