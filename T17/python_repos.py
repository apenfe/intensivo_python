import requests

url = 'https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

response_dict = r.json()

print(f"Repositorios totales: {response_dict['total_count']}")
print(f"Resultados completos: {not response_dict['incomplete_results']}")

# explora la informacion sobre los repositorios.
repo_dicts = response_dict['items']
print(f"Repositorios devueltos: {len(repo_dicts)}")

# examinar repositorios
print("\nInformacion seleccionada de repositorios:\n")

for repo_dict in repo_dicts:
    print(f"\t* Nombre: {repo_dict['name']}")
    print(f"\t* Propietario: {repo_dict['owner']['login']}")
    print(f"\t* Estrellas: {repo_dict['stargazers_count']}")
    print(f"\t* Repositorio: {repo_dict['html_url']}")
    print(f"\t* Creado: {repo_dict['created_at']}")
    print(f"\t* Actualizado: {repo_dict['updated_at']}")
    print(f"\t* Descripcion: {repo_dict['description']}\n")
