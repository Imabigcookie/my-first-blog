from django.shortcuts import render

def post_list(request):
    render(request, 'blog/post_list.html', {})
