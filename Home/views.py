from django.views.generic import TemplateView
from .models import TextAnimate
from About.models import AuthorPeronal
# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        text_animate = TextAnimate.objects.all()   
        context["text_animate"] = text_animate
        context["text_animatelen"] = len(text_animate)
        return context







