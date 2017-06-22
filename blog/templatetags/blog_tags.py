from ..models import Post, Category
from django import template
register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    #return Post.objects.all().order_by('-created_time')[:num]
    return Post.objects.all()[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()