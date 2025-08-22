import requests
from bs4 import BeautifulSoup
import json

# ================================
# Classificação por área
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
# Scraper de exemplo (site Estratégia)
# ================================
url = "https://www.estrategiaconcursos.com.br/blog/concursos-sul/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

concursos = []
for item in soup.select(".card-concurso"):
    titulo = item.select_one(".card-title").get_text(strip=True) if item.select_one(".card-title") else "Sem título"
    link = item.find("a")["href"] if item.find("a") else ""
    detalhes = item.get_text(" ", strip=True)

    concursos.append({
        "titulo": titulo,
        "link": link,
        "area": classificar_area(titulo + " " + detalhes),
        "detalhes": detalhes
    })

# ================================
# Salvar em JSON
# ================================
with open("concursos.json", "w", encoding="utf-8") as f:
    json.dump(concursos, f, indent=2, ensure_ascii=False)

print("✅ Concursos salvos em concursos.json")
