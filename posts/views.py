from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

from telegraph import Telegraph


def index(request):
    # return HttpResponse('Hello World')

    posts = Posts.objects.all()[:10]

    context = {
        'title': 'Welcome To Weblog',
        'posts': posts
    }

    return render(request, 'posts/index.html', context)


def details(request, id):
    post = Posts.objects.get(id=id)

    context = {
        'title': 'Posts',
        'post': post
    }
    return render(request, 'posts/details.html', context)



# telegraph = Telegraph()
# telegraph.create_account(short_name='Alyx69')

# response = telegraph.create_page(
#     f'{Posts.title}',
#     html_content=f'<p>{Posts.body} \n response["url"]</p>'
# )
# print(response['url'])