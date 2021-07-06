from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Blogpost


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
    

class BlogDetails(DetailView):
    model = Blogpost
    template_name = "blog-post.html"

    def get_post(self):
        slug =  self.kwargs.get('slug')
        post = Blogpost.objects.get(slug=slug)
        post.read += 1
        post.save(update_fields = ['read'])
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_post()
        return context




