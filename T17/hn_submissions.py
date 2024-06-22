from operator import itemgetter
import requests

# llamada a api
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# procesar informacion de cada envio
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    # una nueva llamada a la api separada para cada envio
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"ID: {submission_id}\tStatus code: {r.status_code}")
    response_dict = r.json()

    # se crea un diccionario para cada articulo
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants',0),
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
for submission_dict in submission_dicts:
    print(f"\nTitulo: {submission_dict['title']}")
    print(f"Link Discusion: {submission_dict['hn_link']}")
    print(f"Comentarios: {submission_dict['comments']}")