from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message
import json
from django.contrib.auth import get_user_model

def user_login(request):
    User = get_user_model()

    # إنشاء superuser
    if not User.objects.filter(username="abdou").exists():
        User.objects.create_superuser("abdou", "abdou@gmail.com", "123")
        print("✅ Superuser created!")

    # إنشاء مستخدم عادي
    if not User.objects.filter(username="yahya").exists():
        User.objects.create_user("yahya", "yahya@gmail.com", "123")
        print("✅ Normal user created!")

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة')
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'accounts/home.html')

@login_required
def get_messages(request):
    messages = Message.objects.select_related('sender').all()
    data = [
        {
            'sender': msg.sender.username,
            'content': msg.content,
            'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }
        for msg in messages
    ]
    return JsonResponse(data, safe=False)

@csrf_exempt
@login_required
def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        msg = Message.objects.create(
            sender=request.user,
            content=data['content']
        )
        return JsonResponse({'status': 'success', 'message': msg.content})
    return JsonResponse({'status': 'error'})