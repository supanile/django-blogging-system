from django.http import HttpResponse
from django.shortcuts import render
from category.models import Category
from .models import Blogs
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.


def index(request):
    categories = Category.objects.all()
    blogs = Blogs.objects.all()
    latest = Blogs.objects.all().order_by('-pk')[:4]

    # Popular articles
    popular = Blogs.objects.all().order_by('-views')[:3]
    
    # Suggestions articles
    suggestion = Blogs.objects.all().order_by('views')[:3]

    # Pagination
    paginator = Paginator(blogs, 2)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        blogPerPage = paginator.page(page)
    except (EmptyPage, InvalidPage):
        blogPerPage = paginator.page(paginator.num_pages)

    return render(request, 'frontend/index.html', {
        'categories': categories,
        'blogs': blogPerPage,
        'latest': latest,
        'popular': popular,
        'suggestion': suggestion
    })


def blogDetail(request, id):
    categories = Category.objects.all()

    # Popular articles
    popular = Blogs.objects.all().order_by('-views')[:3]
    
    # Suggestions articles
    suggestion = Blogs.objects.all().order_by('views')[:3]
    
    singleBlog = Blogs.objects.get(id=id)
    singleBlog.views = singleBlog.views + 1
    singleBlog.save()
    return render(request, 'frontend/blogDetail.html', {"blog": singleBlog, 'categories': categories, 'popular': popular, 'suggestion': suggestion})