from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from main.views import send_mail
from .models import BlogModel


def blog(request):  
    blog_list = list(BlogModel.objects.all())

    paginator = Paginator(blog_list, 6)
    pageNumber = request.GET.get('page')
    page_obj = paginator.get_page(pageNumber)

    context = {
        'blog' : page_obj,
        'page_obj' : page_obj,
        'form' : send_mail(request),
    }

    return render(request, 'blog.html', context)

def detail_view(request, id):
    post = BlogModel.objects.get(id=id)

    data = {
        'post' : post,
        'form' : send_mail(request),
    }
    

    return render(request, 'detail.html', data)


