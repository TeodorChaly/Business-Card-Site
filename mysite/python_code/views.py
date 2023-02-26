from django.shortcuts import render
from . import scraping

def run_scraping(request):
    if request.method == 'POST':
        scrap_res = scraping.run_scraping()
        print(scrap_res)
        return render(request, 'scraper/run_scraping.html', {'message': scrap_res})
    else:
        return render(request, 'scraper/run_scraping.html')
