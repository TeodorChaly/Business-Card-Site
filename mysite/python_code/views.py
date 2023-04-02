from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.generic import ListView

from . import scraping
from .ask_ai import ask_question
from .calculator import calculator_res


@csrf_exempt
def run_scraping(request):
    query, result_conent, list_of_site = None, None, None
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')
        query, result_conent, list_of_site = scraping.run_scraping(input_text)

    return render(request, 'demos/run_scraping.html',
                  {"query": query, "result_conent": result_conent, "list_of_site": list_of_site})


@csrf_exempt
def run_calculator(request):
    if request.method == 'POST':
        num_one = float(request.POST.get('num_one'))
        num_two = float(request.POST.get('num_two'))
        operation = request.POST.get('operation')
        result = calculator_res(num_one, num_two, operation)
        context = {
            'result': result
        }
        return render(request, 'demos/run_calculator.html', context)
    else:
        return render(request, 'demos/run_calculator.html')

@csrf_exempt
def run_ai_bot(request):
    result= None
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')
        result = ask_question(input_text)

    return render(request, 'demos/run_askAI.html',
                  {"result":result})



class Demos_view(View):
    def get(self, request):
        return render(request, "demos/list.html")
