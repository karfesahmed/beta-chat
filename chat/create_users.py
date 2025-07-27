# chat/create_users.py

from django.contrib.auth import get_user_model

User = get_user_model()

# إنشاء superuser
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("abdou", "abdou@gmail.com", "123")
    print("✅ Superuser created!")

# إنشاء مستخدم عادي
if not User.objects.filter(username="normaluser").exists():
    User.objects.create_user("yahya", "yahya@gmail.com", "123")
    print("✅ Normal user created!")
