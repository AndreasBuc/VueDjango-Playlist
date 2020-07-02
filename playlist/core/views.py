from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexTemplateView(LoginRequiredMixin, TemplateView):
    def get_template_names(self):
        template_name = "index-dev.html"
        return template_name
