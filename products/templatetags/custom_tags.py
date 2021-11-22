from django import template
from products.models import Product

register = template.Library()

def image(product, product_id):
    product = Product.objects.get(id=product_id)
    image = product.album.images.get(name="front")#You can optionally use the default parameter 
    image_url = image.image.url
    print(image_url)
    return image_url
    #return image.image.url# Return the image from the

register.filter('image', image)    