import requests
from datetime import datetime
import os
import json
import html

URL = "https://papfy.com/testca/raw"
DATA_DIR = "data"

def main():
    print(f"➡️ Свалям JSON от {URL}")
    r = requests.get(URL)
    if r.status_code != 200:
        raise Exception(f"Грешка при сваляне: {r.status_code}")

    os.makedirs(DATA_DIR, exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Запиши архивен файл
    dated_file = os.path.join(DATA_DIR, f"data_{now}.json")
    with open(dated_file, "w", encoding="utf-8") as f:
        f.write(r.text)

    # Обнови latest.json
    with open("latest.json", "w", encoding="utf-8") as f:
        f.write(r.text)

    print("✅ Записани файлове:", dated_file, "и latest.json")

    data = json.load(open("latest.json", encoding="utf-8"))

    html_content = f"""
    <html>
    <head><title>Crypto Data</title></head>
    <body>
    <h1>Crypto Data Snapshot</h1>
    <pre>{html.escape(json.dumps(data, indent=2, ensure_ascii=False))}</pre>
    </body>
    </html>
    """
    
    with open("latest.html", "w", encoding="utf-8") as f:
        f.write(html_content)

if __name__ == "__main__":
    main()
