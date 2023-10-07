from django.shortcuts import render
from django.http import HttpResponse

posts = [
  
   { ' author': 'Nazmul',
    ' title': 'think of coding',
    ' content': 'first content'
    },
    
   { ' author': 'Alam',
    ' title': 'think of Learning',
    ' content': 'second content'
    } 
]

def home (request):
  context = {
    'posts': posts
  }
  return render(request,'blog/home.html', context) 
def about (request):
  return render(request,'blog/about.html')
