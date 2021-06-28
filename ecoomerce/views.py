from django.shortcuts import render
from .mpdels import Product
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from. models import product,comment
# Create your views here.
def available_product(request):
  data={}
  poll_list = Product.objects.filter(status=True)
  data['available'] = poll_list
  return render(request, "available_product.html", context=data)

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

class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'order_summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")

def about_view(request):
    data = {}
    data["about_us"] = "e-commerce" 
    return render(request, "about.html", context=data)
 