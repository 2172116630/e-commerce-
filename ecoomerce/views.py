from django.shortcuts import render
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from. models import product,comment

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

