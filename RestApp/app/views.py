from django.shortcuts import render, redirect
from django.views import View


class IndexMain(View):
    def get(self, request):
        return render(request, 'index.html')
