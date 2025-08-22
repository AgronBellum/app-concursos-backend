import requests
import json

# ================================
# Classificação por área (igual antes)
# ================================
def classificar_area(texto):
    texto = texto.lower()
    if "tribunal" in texto or "tce" in texto or "tj" in texto:
        return "Tribunais"
    if "prefeitura" in texto or "administrativo" in texto or "auxiliar" in texto:
        return "Administrativa"
    if "banco" in texto or "bb" in texto or "caixa" in texto:
        return "Bancária"
    if "receita" in texto or "fiscal" in texto or "auditor" in texto:
        return "Fiscal"
    if "polícia" in texto or "delegado" in texto or "agente" in texto:
        return "Policial"
    if "exército" in texto or "marinha" in texto or "aeronáutica" in texto:
        return "Militar"
    if "professor" in texto or "educação" in texto or "universidade" in texto:
        return "Educacional"
    if "promotor" in texto or "procurador" in texto or "juiz" in texto:
        return "Jurídica"
    return "Outros"

# ================================
# Usando API WordPress do Estratégia
# ================================
url = "https://www.estrategiaconcursos.com.br/wp-json/wp/v2/posts?categories=327&per_page=20"

response = requests.get(url)
posts = response.json()

concursos = []
for post in posts:
    titulo = post["title"]["rendered"]
    link = post["link"]
    detalhes = post["excerpt"]["rendered"]

    concursos.append({
        "titulo": titulo,
        "link": link,
        "detalhes": detalhes,
        "area": classificar_area(titulo + " " + detalhes)
    })

# ================================
# Salvar em JSON
# ================================
with open("concursos.json", "w", encoding="utf-8") as f:
    json.dump(concursos, f, indent=2, ensure_ascii=False)

print("✅ Concursos salvos em concursos.json via API")
