from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView

from articles.models import Article


class ProductListView(ListView):

    model = Article
    paginate_by = 10  # if need pagination

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
