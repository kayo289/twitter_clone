from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import PostModel, ProfileModel

from .models import Blog
from django.contrib import messages
from django.db.models import Q


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
    params = {
        'posts': PostModel.objects.all(),
        'current_user': request.user,
        'profile': ProfileModel.objects.get(user=request.user)
    }
    return render(request, 'list.html', params)


def index(request):
    blog = Blog.objects.order_by('-id')
    """ 検索機能の処理 """
    keyword = request.GET.get('keyword')
    if keyword:
        """ テキスト用のQオブジェクトを追加 """
        blog = blog.filter(
                 Q(title__icontains=keyword) | Q(text__icontains=keyword)
               )
        messages.success(request, '「{}」の検索結果'.format(keyword))
    return render(request, 'blog/index.html', {'blog': blog })
def detail(requst, blog_id):
    blog_text = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
