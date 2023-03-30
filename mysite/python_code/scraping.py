from bs4 import BeautifulSoup
import requests

def run_scraping(query):
    query = query.replace(" ", "+")
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, "html.parser")
    search_results = soup.find_all("div", class_="g")
    list_of_site = {}
    for result in search_results:
        try:
            title = result.find("h3").get_text()
            link = result.find("a")["href"]
            print(f"{title}\n{link}\n")
            list_of_site[title] = link
        except:
            print("No")


    search_results_2 = soup.find(id="result-stats")
    if search_results_2:
        content = search_results_2.text
        result_content = "Content in google:" + content.split(" ")[1] + f'or - {content.split(" ")[3][1:]}/per second'
    else:
        result_content = "No result found"

    return query, result_content, list_of_site

