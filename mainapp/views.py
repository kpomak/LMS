import os
import json
from datetime import datetime
from django.conf import settings
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        with open(os.path.join(settings.BASE_DIR, "news.json")) as f:
            context["news"] = json.load(f)

        context["news_title"] = "Горящий заголовок"
        context["news_preview"] = "Захватывающее описание"
        context["range"] = range(5)
        context["datetime_obj"] = datetime.now()
        return context


class NewsWithPaginatorView(NewsPageView):
    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context["page_num"] = page
        return context


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
