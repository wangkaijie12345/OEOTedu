from django.shortcuts import render, redirect
from .models import Company, Post
from django.http import HttpResponse


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'training/index.html', {'posts': posts})


def company(request):
    company = Company.objects.all()
    return render(request, 'training/company.html', {'company': company})


# 删除——艾鹏
def post_delete(request, id):
    user = request.user
    if user.profile.job == 'staff':
        post = Post.objects.get(id=id)
        post.delete()
        return redirect('/')
    else:
        return HttpResponse('当前登录用户没有权限，请切换用户或者联系管理员.')
