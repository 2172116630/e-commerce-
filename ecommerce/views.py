from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from .models import Product, Comment
from .forms import CommentForm

# read pep8 documentation on how to write python code

# Create your views here.
def available_product(request):
  data={}
  poll_list = Product.objects.filter(status=True)
  data['available'] = poll_list
  return render(request, "available_product.html", context=data)

    #unavailable_poduct 
def unavailable_product(request):
  data={}
  poll_list = Product.objects.filter(status=False)
  data['unavailable'] = poll_list
  return render(request, "unavailable_product.html", context=data)

def product_detail(request, product_id):
  data={}
  product_list = Product.objects.get(id = product_id)
  comment_list = product_list.comment_set.all()
  data['product'] = product_list
  data['comment'] = comment_list
  return render(request, "product_detail.html", context=data)
def product_comment(request, slug):
  template_name = 'product_comment.html'
  post = get_object_or_404(product_detail, slug=slug)
  comments = post.comments.filter(active=True)
  new_comment = None
# Comment posted
  if request.method == 'POST':
      comment_form = CommentForm(data=request.POST)
      if comment_form.is_valid():
# Create Comment object but don&#39;t save to database yet
          new_comment = comment_form.save(commit=False)
# Assign the current post to the comment
          new_comment.product = product
# Save the comment to the database
          new_comment.save()
  else:
       comment_form = CommentForm()
  return render(request, template_name, {'product': product,
'comments': comments,
'new_comment':new_comment,
'comment_form': comment_form})

