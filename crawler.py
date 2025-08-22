import requests
import json

URL = "https://apiconcursos.vercel.app/"  # API pública do Vinimartinsc

try:
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()

        # salva no JSON
        with open("concursos.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print("✅ Dados atualizados com sucesso!")
    else:
        print(f"❌ Erro {response.status_code} ao acessar API: {response.text}")
except Exception as e:
    print("❌ Erro:", e)
