from django.shortcuts import render
from django.views import View


class CorrectionView(View):
    template_name = 'public/correction.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
