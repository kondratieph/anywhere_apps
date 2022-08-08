from django import template
from news.models import Category
from django.db.models import Count, F
from django.core.cache import cache

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    # return Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    return Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
    # return Category.objects.all()