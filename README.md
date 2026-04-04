
[`تنبية !!`]
`يجب استخدام نسخة بايثون Python 3.14.3 وتحديدها من الاعدادات  Python Interpreter في PyCharm او اي محرر آخر`

### الإصدارات المستخدمة في Python & Django  
```bash
Python 3.14.3 # python version
django 6.0.2 # django version
```

###  . إنشاء بيئة افتراضية وتفعيلها
```bash
     py -3.14 -m venv venv | python -m venv venv
     
     # Activate in Windows:
      venv\Scripts\activate 
     # Activate in Others :
      source venv/bin/activate  
   
```

### . تحديث pip  

```bash 
python.exe -m pip install --upgrade pip
```


### . تثبيت المكتبات المطلوبة 

```bash 
pip install -r requirements.txt
```


[//]: # (### . تثبيت الإطار  )

[//]: # ()
[//]: # (```bash )

[//]: # (pip install django==6.0.2)


###   مثال على اضافة الهويات في المشروع من ملف
config > settings.py

```

SITE_ROLES = [

    {
        'code': 'identity_code', # student
        'name': 'identity_name', # student
        'app_name': 'identity_app_name', # students
        'is_identity': True,      # هل له بروفايل وهوية مستقلة؟
        'requires_approval': False, # هل يحتاج تفعيل من الإدارة؟
        'view_in_register': True,  # هل يظهر في خيارات التسجيل؟
    },
    { .... }
]
```
### بناء قاعدة البيانات  
```bash
python manage.py makemigrations 
python manage.py migrate 
```

### . إنشاء حساب مدير النظام
```bash
python manage.py createsuperuser
```
### Install Frontend Dependencies
```bash

Run the following commands after cloning the project.

```bash
# Install cross-env (needed for Windows compatibility)
npm install -D cross-env

# Move to the Tailwind theme directory
cd theme

# Install UI components
npm install daisyui
npm install

# Install Tailwind CSS 4 and PostCSS tooling
npm install tailwindcss @tailwindcss/postcss postcss postcss-cli autoprefixer postcss-simple-vars postcss-nested

# Return to project root
cd ..
```

After installing dependencies, start the Tailwind watcher:

```bash
python manage.py tailwind start
```


### . 🌍 نظام تعدد اللغات (Internationalization)

الاستخراج: جمع النصوص الجديدة من القوالب:

```Bash
python manage.py makemessages -l ar
````
التفعيل: تحويل الترجمات إلى صيغة ثنائية سريعة:

```Bash
python manage.py compilemessages
```
### . 📂 تنظيم الملفات الساكنة (Static Files) 

إنشاء المجلدات التنظيمية:

```Bash
mkdir static
mkdir static/css
mkdir static/js
mkdir static/img 
```

تجميع الملفات للنشر (Production):

```Bash
python manage.py collectstatic
```

### . تشغيل المشروع

أفتح Terminal جديد ونفذ الامر التالي  لتشغيل المراقبة (Start/Dev) بهدف تطبيق تنسيقات tailwind على الواجهات 
```bash
#python manage.py tailwind install
python manage.py tailwind dev | python manage.py tailwind start # لتشغيل المراقبة الحية أثناء التطوير

```
أفتح Terminal أخر ونفذ الامر التالي لتشغيل السرفر 
```bash
python manage.py runserver
```

### Generated Apps 
اذا اردت البدء بانشاء تطبيقات Apps  مثل accounts او core داخل مجلد المشروع استخدم الامر التالي
```bash
python manage.py startapp  your_app_name
```


###  

```bash
pip install playwright playwright-stealth
playwright install chromium
```

