from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import PostModel

# Create your views here.
def signupfunc(request):
    # user2 = User.objects.all()
    if request.method == 'POST':
        user_name = request.POST['username']
        user_email = request.POST['email']
        user_password = request.POST['password']

        if User.objects.filter(username = user_name, email=user_email, password=user_password).exists():
            # 複数条件を利用したいからfilterを利用
            User.objects.filter(email=user_email, password=user_password)
            return render(request, 'signup.html', {'error': 'このユーザーは登録されています'})

        User.objects.create_user(user_name, user_email, user_password)
        user = authenticate(request, username=user_name, password=user_password)
        login(request, user)
        return render(request, 'signup.html', {'error': 'ログイン成功'}) #ログインが成功した時の画面移動先
    return render(request, 'signup.html', {'error': 'こないはず'}) #これがないとエラーが出る。Djangoの仕様かもしれない

def loginfunc(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        user_password = request.POST['password']
        # 権限確認らしい
        user = authenticate(request, username=user_name, password=user_password)
        if user is not None:
            login(request, user)
            return redirect('signup')
        else:
            return redirect('login')# ログイン成功後の遷移先
    return render(request,'login.html')

def index_post(request):
    posts = PostModel.objects.all()
    params = {'posts': PostModel.objects.all()}
    return render(request, 'list.html', params)

