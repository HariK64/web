# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic

from blog.models import Post, Comment


def home(request):

    template_name = "blog/home.html"
    posts=Post.objects.all()
    for i in posts:
        i.content=i.content[0:1000]+"...."
    context = {'object_list': posts}

    return render(request, template_name, context)



def post_detail(request,pk):
    post=Post.objects.get(id=int(pk))
    comment=Comment.objects.filter(post=post)
    template = 'blog/post.html'
    context={"post":post,"comments":comment}
    return render(request, template, context)

def add_post(request):
    if request.method=="POST":
        title=request.POST['title']
        content=request.POST['content']
        img=request.FILES['img']
        is_piblished=request.POST['is_piblished']
        user=User.objects.get(username=request.user.username)
        new_post=Post(title=title,content=content,img=img,is_piblished=is_piblished,user=user)
        new_post.save()
        return redirect('post',new_post.id)

    else:
        template_name = 'blog/addpost.html'
        context={}
        return render(request, template_name, context)


def edit_post(request,pk):
    post=Post.objects.get(id=int(pk))
    if request.user.username !=post.user.username:
        raise PermissionDenied
    if request.method =="GET":
        template_name='blog/post_edit.html'
        context={"post":post}
        return render(request,template_name,context)
    else:
        post.title=request.POST['title']
        post.content=request.POST['content']
        if 'img' in request.FILES:
            post.img=request.FILES['img']
        if 'is_piblished'in request.POST:
            post.is_piblished=request.POST['is_piblished']
        post.save()
        return redirect('post',post.id)

def delete_post(request,id):
    if Post.objects.get(id=id) is not None:
        post=Post.objects.get(id=id)
        if post.user.username== request.user.username:
            post.delete()
            return  redirect('home')
        raise PermissionDenied

#class DeletePostView(generic.DeleteView):
    model = Post
    success_url = '/'


