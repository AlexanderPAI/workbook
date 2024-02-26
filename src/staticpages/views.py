from django.views.generic.base import TemplateView


class AboutProjectView(TemplateView):
    template_name = 'staticpages/about.html'
