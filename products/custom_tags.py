from django import template
from .models import Product

register = template.Library()

def image(product, product_id):
    product = Product.objects.get(id=product_id)
    image = product.album.images.get(name="front")#You can optionally use the default parameter 
    return image

register.filter('image', image)    