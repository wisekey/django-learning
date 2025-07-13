from django import template
from women.models import Category, TagPost

register = template.Library()


@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, "cat_selected": cat_selected}


@register.inclusion_tag('women/list_tags.html')
def show_all_tags(cat_selected=0):
    tags = TagPost.objects.all()
    return {'tags': tags}