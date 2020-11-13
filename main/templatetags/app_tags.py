from django import template
from main.models import Menu

register = template.Library()


@register.simple_tag
def get_menus():
    return Menu.objects.all()