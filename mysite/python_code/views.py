from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from . import scraping
from .calculator import calculator_res

@csrf_exempt
def run_scraping(request):
    result = None
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')
        result = scraping.run_scraping(input_text)

    return render(request, 'demos/run_scraping.html', {'result': result})

@csrf_exempt
def run_calculator(request):
    if request.method == 'POST':
        num_one = float(request.POST.get('num_one'))
        num_two = float(request.POST.get('num_two'))
        operation = request.POST.get('operation')
        result = calculator_res (num_one, num_two, operation)
        context = {
            'result': result
        }
        return render(request, 'demos/run_calculator.html', context)
    else:
        return render(request, 'demos/run_calculator.html')

class Demos_view(View):
    def get(self, request):
        return render(request, "demos/list.html")