from django.views.generic import TemplateView
from .models import AuthorPeronal,Boxes,Skills,Expreance,Education, CvUpload

# Create your views here.

class AboutView(TemplateView):
    template_name = "about.html"
  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        boxes = Boxes.objects.all()
        skills = Skills.objects.all()
        expreance = Expreance.objects.all()
        education = Education.objects.all()

        context["boxes"] = boxes
        context["skills"] = skills
        context["expreance"] = expreance
        context["education"] = education


        return context
      
        
      