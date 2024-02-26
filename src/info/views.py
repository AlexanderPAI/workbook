from django.shortcuts import render

from articles.models import Tag


def AboutView(request):
    tags = Tag.objects.all().order_by('name')
    context = {
        'tags': tags
    }
    return render(
        request,
        'info/about.html',
        context,
    )
