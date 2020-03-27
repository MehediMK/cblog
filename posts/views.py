from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render,get_object_or_404

from django.db.models import Count,Q

from . models import Post
from marketing.models import Signup


def search(request):
    post_list = Post.objects.all()
    query = request.GET.get('query')
    if query:
        post_list= post_list.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
        context = {
            'query_post':post_list
        }
    return render(request,'search.html',context)

def get_category():
    queryset= Post.objects.values('categorys__title').annotate(Count('categorys__title'))
    return queryset
# Create your views here.
def index(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]

    if request.method == 'POST':
        email = request.POST['email']
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'object_list': featured,
        'latest_post':latest
    }
    return render(request,'index.html',context)

def blog(request):
    category_count = get_category()
    print(category_count)
    # post_list = Post.objects.all()
    post_list= Post.objects.order_by('-timestamp') #this is for new update status or post or latest update post order_by
    latest_post = Post.objects.order_by('-timestamp')[0:3] #for right side latest post

    paginator = Paginator(post_list,2)
    page_var = 'page'
    page = request.GET.get(page_var)
    try:
        paginator_query = paginator.page(page)
    except PageNotAnInteger:
        paginator_query = paginator.page(1)
    except EmptyPage:
        paginator_query = paginator.page(paginator.num_pages)

    context= {
        'cat_count':category_count,
        'post_list':paginator_query,   # :post_list,
        'post_latest':latest_post, 
        'page_var':page_var
    }
    return render(request,'blog.html',context)

def post(request,id):
    post_detail = get_object_or_404(Post, pk=id)
    latest_post = Post.objects.order_by('-timestamp')[0:3]
    category_count = get_category()
    context = {
        'cat_count':category_count,
        'post_latest':latest_post,
        'posts': post_detail,
    }
    return render(request,'post.html',context)



# this is optional
# def detail(request,post_id):
#     post_detail = get_object_or_404(Post, pk=post_id)
#     latest_post = Post.objects.order_by('-timestamp')[0:3]
#     context = {
#         'post_latest':latest_post,
#         'posts':post_detail,
#     }
#     return render(request,'post.html',context)

