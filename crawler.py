import requests
from bs4 import BeautifulSoup
import json

# ================================
# Função para classificar área
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
# Scraper do site Estratégia
# ================================
url = "https://www.estrategiaconcursos.com.br/blog/concursos-sul/"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")

concursos = []
for item in soup.select("article"):
    titulo_elem = item.select_one("h3")
    link_elem = item.select_one("a")
    detalhes_elem = item.select_one("p")

    if not titulo_elem:
        continue

    titulo = titulo_elem.get_text(strip=True)
    link = link_elem["href"] if link_elem else ""
    detalhes = detalhes_elem.get_text(strip=True) if detalhes_elem else ""

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

print(f"✅ Salvo {len(concursos)} concursos em concursos.json")
