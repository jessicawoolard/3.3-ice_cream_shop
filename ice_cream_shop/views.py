from django.shortcuts import render

from django.views.generic import TemplateView
from .models import IceCream


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        daily_creams = IceCream.objects.filter(available='daily')
        weekly_creams = IceCream.objects.filter(available='weekly')
        seasonal_creams = IceCream.objects.filter(available='seasonal')
        featured_creams = IceCream.objects.filter(featured=True)

        context = {
            'daily_flavors': daily_creams,
            'weekly_flavors': weekly_creams,
            'seasonal_flavors': seasonal_creams,
            'featured_flavors': featured_creams,
        }

        return context

