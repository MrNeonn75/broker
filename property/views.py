from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from main.views import send_mail
from profile_app.models import LikeModel, SaveModel
from .models import ProductModel, CategoryModel, AreaModel, CommentModel, CommentReplyModel
from .forms import FilterForm, SearchForm, CommentForm, CommentReplyForm

def property(request):
    categories = list(CategoryModel.objects.all().values())
    posts = ProductModel.objects.order_by('date').all()

    filter_form = FilterForm()
    search_form = SearchForm()

    search_category_input = request.GET.get('search_category')
    search_area_input = request.GET.get('search_area')
    search_rooms_input = request.GET.get('search_rooms')
    search_min_price_input = request.GET.get('search_min_price')
    search_max_price_input = request.GET.get('search_max_price')

    search_bar_input = request.GET.get('search')

    filter_data_list = [
        search_category_input,
        search_area_input,
        search_rooms_input,
        search_min_price_input,
        search_max_price_input
    ]

    filter_data_object = {}
    price_filter_object = {}

    try:
        for g in filter_data_list:
            if(g != None or g != ""):
                
                if(g == search_category_input):
                    if(g != 'Kateqoriya'):
                        search_category_input_id = CategoryModel.objects.get(category = g)
                        filter_data_object['product_category'] = search_category_input_id
                elif(g == search_area_input):
                    if(g != 'Ərazi'):
                        search_area_input_id = AreaModel.objects.get(area = g)
                        filter_data_object['area'] = search_area_input_id
                elif(g == search_rooms_input and g != ''):
                    filter_data_object['rooms'] = g
                elif(g == search_min_price_input and g != ''): 
                    price_filter_object['min_price'] = g
                elif(g == search_max_price_input and g != ''): 
                    price_filter_object['max_price'] = g 
                else: pass
            else: print('Test')
        print(f'filter_data_object -> {filter_data_object}')

        posts = ProductModel.objects.filter(**filter_data_object)
                
        if(price_filter_object):
            min_price = price_filter_object['min_price']
            max_price = price_filter_object['max_price']

            filtered_price_data = []

            for c in posts.values():
                if(c['product_price'] > float(min_price) and c['product_price'] < float(max_price)):
                    filtered_price_data.append(c)

            posts = filtered_price_data

    except: pass

    posts_list = list(posts)

    if(search_bar_input != None):
        all_posts_titles = []

        for z in list(ProductModel.objects.all().values()):
            all_posts_titles.append(z['product_name'])
        
        result = []
        for test in all_posts_titles:
            if(search_bar_input.casefold() == test.casefold()):
                result.append(ProductModel.objects.get(product_name = test))
            else:
                for w in search_bar_input.casefold().split():
                    for r in test.casefold().split():
                        try:
                            if(r.index(w)):
                                result.append(ProductModel.objects.get(product_name = test))
                            else: result.append(ProductModel.objects.get(product_name = test))
                        except: pass
        

        posts_list = list(result)

    paginator = Paginator(posts_list, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    data = {
        'posts' : page_obj,
        'page_obj' : page_obj,
        'categories' : categories,
        'form' : send_mail(request),
        'search_form' : search_form,
        'filter_form' : filter_form,
    }

    return render(request, 'listing.html', data)

def property_detail_view(request, id):
    post = ProductModel.objects.get(id=id)
    comments = CommentModel.objects.filter(post=post)
    comment_replies = CommentReplyModel.objects.filter(post=post)
    
    comment = CommentForm()
    answer_to_comment = CommentReplyForm()

    comment_input = request.GET.get('comment')
    

    if(comment_input != None):
        comment_model_variable = CommentModel.objects.create(
            user = request.user,
            post = ProductModel.objects.get(id=id),
            comment = comment_input
        )
        if(comment_model_variable):
            return redirect('property-detail-view', id=id)
        
    try:
        if(SaveModel.objects.get(user=request.user, post=post)): post_is_saved = True
    except: post_is_saved = False

    try:
        if(LikeModel.objects.get(user=request.user, post=post)): post_is_liked = True
    except: post_is_liked = False

    data = {
        'post'    : post,
        'comment' : comment,
        'coms'    : comments,
        'com_ans' : comment_replies,
        'reply'   : answer_to_comment,
        'is_saved': post_is_saved,
        'is_liked': post_is_liked,
        'form'    : send_mail(request),
    }

    return render(request, 'product.html', data)

def like_post(request, id):
    post_object = ProductModel.objects.get(id=id)

    try:
        current_post = LikeModel.objects.get(
            user = request.user,
            post = post_object
        )
    except Exception as ex:
        LikeModel.objects.create(
            user = request.user,
            post = post_object
        )
    
    return redirect('property-detail-view', id=id)

def save_post(request, id):
    post_object = ProductModel.objects.get(id=id)

    try:
        current_post = SaveModel.objects.get(
            user = request.user,
            post = post_object
        )
    except Exception as ex:
        SaveModel.objects.create(
            user = request.user,
            post = post_object
        )
    
    
    return redirect('property-detail-view', id=id)

def remove_comment(request, id, com_id):
    CommentModel.objects.get(id=com_id).delete()
    return redirect('property-detail-view', id=id)
