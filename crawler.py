import requests
from bs4 import BeautifulSoup
import json

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
# API oficial do Estratégia (Concursos Sul = categoria 4853)
# ================================
url = "https://www.estrategiaconcursos.com.br/wp-json/wp/v2/posts?categories=4853&per_page=10"

response = requests.get(url)

# 🔹 Debug: se não vier JSON, mostrar o erro
if response.status_code != 200:
    print("❌ Erro na requisição:", response.status_code)
    print(response.text[:500])  # mostra só o início da resposta
    exit(1)

try:
    data = response.json()
except Exception as e:
    print("❌ Erro ao converter para JSON:", str(e))
    print("Resposta recebida:", response.text[:500])
    exit(1)

concursos = []
for item in data:
    titulo = item.get("title", {}).get("rendered", "Sem título")
    link = item.get("link", "")
    resumo_html = item.get("excerpt", {}).get("rendered", "")
    resumo = BeautifulSoup(resumo_html, "html.parser").get_text(" ", strip=True)

    concursos.append({
        "titulo": titulo,
        "link": link,
        "detalhes": resumo,
        "area": classificar_area(titulo + " " + resumo)
    })

with open("concursos.json", "w", encoding="utf-8") as f:
    json.dump(concursos, f, indent=2, ensure_ascii=False)

print("✅ Concursos salvos em concursos.json")
