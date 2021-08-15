from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.views.generic.base import TemplateView

# class HomeView(LoginRequiredMixin, TemplateView):
#     """Home page view"""

#     template_name = "index.html"
#     login_url = "/auth/login/"
#     redirect_field_name = "home"


# class PageLoaderView(LoginRequiredMixin, TemplateView):
#     """Page loader view"""

#     login_url = "/auth/login/"

#     def dispatch(self, request, template, *args, **kwargs):
#         try:
#             self.template_name = f"pages/{template}.html"
#             get_template(self.template_name)
#             return super().dispatch(request, *args, **kwargs)
#         except TemplateDoesNotExist as template_no_exist:
#             raise Http404 from template_no_exist
