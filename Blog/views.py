from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect,render
from django.contrib import messages
from .models import Blogpost
from .forms import CommentForm

# Create your views here.

class BlogView(ListView):
    template_name = "blog.html"
    paginate_by = 6
    queryset = Blogpost.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            slug = Blogpost.objects.values('slug')[0]['slug']
            context['slug'] = slug
            return context
        except Exception:
            context['slug'] = ''
            return context
    


def BlogDetails(request,slug):
    try:
        post = Blogpost.objects.get(slug=slug)
        comments = post.comments.filter(approve=True)
        
        if request.method == 'POST':      
            comment_form = CommentForm(request.POST)    
            if comment_form.is_valid():       
                new_comment = comment_form.save(commit=False)          
                new_comment.post = post            
                new_comment.save()
                # redirect to a new URL:           
                messages.success(request, 'Your comment submitted. Please wait for approve.')

                return HttpResponseRedirect(request.path_info)
        else:       
            comment_form = CommentForm()
    
    
        context = {'post': post,'comments': comments}

        return render(request, 'blog-post.html', context)
    except Exception:
        return render(request,'404.html')



# class BlogDetails(DetailView):
#     model = Blogpost
#     template_name = "blog-post.html"
#     form_class = CommentForm

#     def get_post(self):
#         slug =  self.kwargs.get('slug')
#         post = Blogpost.objects.get(slug=slug)
#         post.read += 1
#         post.save(update_fields = ['read'])
#         return post
    
   
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['post'] = self.get_post()
#         context['comment_form'] = CommentForm()
 
#         return context
    

#     def post(self, request, *args, **kwargs):

#         slug =  self.kwargs.get('slug')
#         post = Blogpost.objects.get(slug=slug)
        
#         comment_form = CommentForm(request.POST)  

#         if comment_form.is_valid():       
#             new_comment = comment_form.save(commit=False)          
#             new_comment.post = post            
#             new_comment.save()
#             # redirect to a new URL:           
#             messages.success(request, 'Your comment submitted.')
#             return HttpResponseRedirect(request.path_info)




