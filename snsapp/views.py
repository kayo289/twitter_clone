from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from .models import PostModel, ProfileModel,FollowModel,GoodModel
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

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
            return render(request, 'signup.html')

        user = User.objects.create_user(user_name, user_email, user_password)
        ProfileModel.objects.create(user=user)
        user = authenticate(request, username=user_name, password=user_password)
        login(request, user)
        return redirect('index_post')#ログインが成功した時の画面移動先
    return render(request, 'signup.html') #これがないとエラーが出る。Djangoの仕様かもしれない

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
            return redirect('index_post')# ログイン成功後の遷移先
    return render(request,'login.html')
def logoutfunc(request):
    logout(request)
    return redirect('login')
@login_required
def index_post(request):
    items = FollowModel.objects.filter(user=request.user)
    follow_users = []
    for item in items:
        follow_users.append(User.objects.get(id=item.follow_id)) 
    local_posts = PostModel.objects.filter(Q(user__in=follow_users) | Q(user=request.user))
    params = {
        'global_posts': PostModel.objects.all().order_by("-id"),
        'local_posts' : local_posts.order_by("-id"),
        'current_user': request.user,
        'profile': ProfileModel.objects.get(user=request.user)
    }
    return render(request, 'list.html', params)

class create_posts(CreateView):
    template_name='create.html'
    model = PostModel
    fields = {'content','images','like_num'}
    success_url = reverse_lazy('index_post')
    def form_valid(self, form):
        print("はいった")
        form.instance.user = self.request.user
        return super(create_posts, self).form_valid(form)
    

#mypage
def mypage(request,pk):
   
    user=User.objects.get(id=pk)
    params={
        'user' : User.objects.get(id=pk),
        'profile':ProfileModel.objects.get(user=user),
        'current_user': request.user,
        'post':PostModel.objects.all().filter(user=user),
        'follow':FollowModel.objects.all().filter(user=user,follow_id=pk)
    }
    return render(request,'mypage.html', params)


def followfunc(request,pk):
    user=User.objects.get(id=pk)
    FollowModel.objects.create(user=user,follow_id=pk)
    return redirect('mypage',pk=pk)
    #return render(request,'follow.html', params)
    
def follow_delete(request,pk):
    user=User.objects.get(id=pk)
    FollowModel.objects.filter(follow_id=pk).delete()
    return redirect('mypage',pk=pk)
    #return render(request,'follow.html', params)

def goodfunc(request,pk):
    post=PostModel.objects.get(id=pk)
    post2=GoodModel.objects.all().filter(post=post,user=request.user)
    print(request)
    if post2  :
        post.like_num-=1 
        post.save()
        GoodModel.objects.filter(user=request.user,post=post,count=1).delete()
        return redirect(request.META['HTTP_REFERER'],pk=post.user.id)
    else :
        post.like_num=post.like_num+1
        post.save()
        GoodModel.objects.create(user=request.user,post=post,count=1)
        return redirect(request.META['HTTP_REFERER'],pk=post.user.id)

#<a href="{% url 'good' post.pk %}" type="button" class="btn btn-primary">いいね: {{post.like_num}}</a>

def search(request):
    """ 検索機能の処理 """
    keyword = request.GET.get('keyword')
    print(keyword)
    posts = PostModel.objects.filter(Q(content__icontains=keyword))
    print(request.user)
    print(posts)
    params = {
        'current_user': request.user,
        'posts' : posts, 
        'keyword': keyword,
    }
    return render(request, 'result.html', params)