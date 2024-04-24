# Basic Django CRUD App By Kunal
This is a basic Django application that demonstrates the creation, retrieval(read), update and deletion of records in a database.

## Run the app
Terminal
```
python manage.py runserver
```

## Basic Django setup
1. Install django if you haven't already
Terminal
```
django-admin startproject <project_name>
```
2. Navigate to your project directory
Terminal
```
cd <project_name>
```
3. Create a new app in your project
Terminal
```
python manage.py startapp <app_name>
```
4. Add the created app into installed apps of your main project settings file
<project_name>/settings.py
```
INSTALLED_APPS = [
    ...
    '<app_name>',
]
```
5. Now, create a model inside `<app_name>`/models.py with fields that you want to store information about.
6. After creating models, run migrations:
Terminal
```
python manage.py makemigrations
```
7. Then apply those migrations:
Terminal
```
python manage.py migrate
```
8. You can now use this data model in views, templates or any other part of your Django application.
Note: In order for Django to recognize your custom model, it needs to be imported somewhere. To access it from another app, import the model To access it from another app you need to include.
9. Define URL of your view in urls.py file of your app (you should import it from `django.urls`):
<app_name>/urls.py
```
from django.urls import path
from . import views

urlpatterns = [
    path('<url>', views.<page_name>, name='<page_name>'),
    <!-- e.g., path('', views.index, name='index'), -->
]
```
10. Include App URL in urls.py of your project:
<project_name>/urls.py
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('<app_name>.urls')),
]
```
11. To run the project:
Terminal
```
python manage.py runserver
```