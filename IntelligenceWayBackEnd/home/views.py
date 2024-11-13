from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Create your views here.

class IndexView(View):
    template_name = "index.html"
    
    def get(self, request):
        return render(request, self.template_name)
    
class AboutUsView(TemplateView):
    template_name = 'about_us.html'