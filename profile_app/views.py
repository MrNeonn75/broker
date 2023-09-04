from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from main.views import send_mail
from .models import LikeModel, SaveModel

def liked(request):
    try:
        liked_posts = list(LikeModel.objects.filter(user=request.user))
    except: liked_posts = []

    paginator = Paginator(liked_posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'posts' : page_obj,
        'page_obj' : page_obj,
        'form'     : send_mail(request),
    }

    return render(request, 'profile.html', data)

def saved(request):
    try:
        saved_posts = list(SaveModel.objects.filter(user=request.user))
    except: saved_posts = []

    paginator = Paginator(saved_posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'posts' : page_obj,
        'page_obj' : page_obj,
        'form'     : send_mail(request),
    }

    return render(request, 'profile.html', data)

def delete_saved_post(request, id):
    if(SaveModel.objects.filter(id=id).delete()):
        return redirect('saved')
    else: return render(request, '404.html')
    
def delete_liked_post(request, id):
    if(LikeModel.objects.filter(id=id).delete()):
        return redirect('liked')
    else: return render(request, '404.html')

def delete_saved_post_detail(request, id):
    if(SaveModel.objects.filter(id=id).delete()):
        return redirect('property-detail-view', id=id)
    else: return redirect('property-detail-view', id=id)
    
def delete_liked_post_detail(request, id):
    if(LikeModel.objects.filter(id=id).delete()):
        return redirect('property-detail-view', id=id)
    else: return redirect('property-detail-view', id=id)