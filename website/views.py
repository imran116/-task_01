from django.views.generic import TemplateView

from website.models import slider_01, Services_01, Portfolio


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = slider_01.objects.all()
        context['services'] = Services_01.objects.all()
        context['portfolios'] = Portfolio.objects.all()
        return context
