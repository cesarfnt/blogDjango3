from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

def hello_blog(request):
    
    lista = [
            'Django', 'Python', 'Git', 'HTML', 
            'Banco de dados', 'Linux', 'nginx', 'Uwsgi'
            'Systemctl',
            ]
    list_posts = Post.objects.filter(deleted=False)


    data = {
            'name': 'Django3', 
            'lista_tecnologias': lista,
            'posts': list_posts,
            }
    return render(request, 'index.html', data)
