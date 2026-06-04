# import os
# import django
# from django.contrib.auth.hashers import make_password
#
# from training_entities.models import TrainingEntityProfile
#
# from members.models import MemberProfile
#
# # تهيئة بيئة دجانغو
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
# django.setup()
#
# from django.contrib.auth import get_user_model
# from core.models import City
#
# User = get_user_model()
#
#
# def create_training_accounts():
#     # قائمة جهات التدريب المراد إنشاؤها
#     entities = [
#         {
#             "email": "ali@gmail.com",
#             "username": "ali90",
#             "password": "Test@123",
#
#         },
#         {
#             "email": "salim@gmail.com",
#             "username": "salim",
#             "password": "Test@123",
#
#         },
#         {
#             "email": "qasim@gmail.com",
#             "username": "qasim",
#             "password": "Test@123",
#
#         },  {
#             "email": "Ammer@gmail.com",
#             "username": "ammer",
#             "password": "Test@123",
#
#         },
#         {
#             "email": "amera@gmail.com",
#             "username": "amera",
#             "password": "Test@123",
#
#         },
#         {
#             "email": "turki@gmail.com",
#             "username": "turki",
#             "password": "Test@123",
#
#         }
#     ]
#
#     print("🚀 Starting account creation...")
#
#     for data in entities:
#         # 1. إنشاء حساب المستخدم
#         user, created = User.objects.get_or_create(
#             email=data['email'],
#             defaults={
#                 'username': data['username'],
#                 'password': make_password(data['password']),  # تشفير كلمة المرور
#                 'is_active': True,
#             }
#         )
#
#         if not created:
#             print(f"⚠️ User {data['username']} already exists.")
#         else:
#             print(f"👤 User {data['username']} created successfully.")
#
#         # 2. جلب المدينة لربطها بالبروفايل
#         city_obj = City.objects.filter(name__icontains=data['city']).first()
#
#         # 3. إنشاء البروفايل المرتبط بالحساب
#         profile, p_created = MemberProfile.objects.update_or_create(
#             user=user,
#             defaults={
#                 'first_name': data['name'],
#                 'last_name': data['reg_num'],
#                 'birth_date': city_obj,
#                 'entity_type': 'PRIVATE',  # أو النوع المناسب حسب EntityType.choices
#                 'is_available': True
#             }
#         )
#
#         if p_created:
#             print(f"🏢 Profile for {data['name']} linked successfully.")
#
#     print("✅ Operation completed!")
#
#
# if __name__ == '__main__':
#     create_training_accounts()