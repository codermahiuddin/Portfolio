from django.views.generic.list import ListView

from .models import Portfolio, MultipleImageUpload


class MyPortfolioView(ListView):
    template_name = "portfolio.html"
    queryset = Portfolio.objects.all().order_by('-pk')
    # queryset = Portfolio.objects.all()
    paginate_by = 6
    SliderImage = Portfolio.objects.values('pk')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        image_list = []

        for i in self.SliderImage:
            images = MultipleImageUpload.objects.filter(portfolio=i['pk'])
            image_list.append(images)

        context['portfolio'] = self.queryset
        context['allimages'] = image_list

        return context
