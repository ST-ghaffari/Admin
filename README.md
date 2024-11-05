# Admin
customizing admin interface in django
Using A Package
There is this package available which we can use django-admin-interface to change the color of admin.
![image](https://github.com/user-attachments/assets/e636fb72-affd-4cd3-8e58-f7318495b2e3)

1. pip install django-admin-interface
2. INSTALLED_APPS = [
                     #...
                     'admin_interface',
                     'colorfield',
                     #...
                    'django.contrib.admin',
                      #...
                    ]
3. python manage.py migrate
4. python manage.py collectstatic
