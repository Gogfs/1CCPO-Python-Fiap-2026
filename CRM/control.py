from pathlib import Path
import json, csv

DATA_DIR = Path(__file__).resolve().parent/"data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR/"leads.json"
print(DATA_DIR)

# READ
def read_leads():
    if not DB_PATH.exists():
        return []

    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return "Bla bla bla ble ble ble oh blu blu blu blu"

print(read_leads())

# CREATE
def create_lead(lead_dict):
    leads = read_leads()
    leads.append(lead_dict)
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")

# LER OS LEADS DE ACORDO COM A BUSCA
def read_search_leads(query):
    leads = read_leads() # lista de dicionários / lista de leads / array of dicts
    results = []

    for i, lead in enumerate(leads):
        txt_lead = f"{lead["name"]} {lead["email"]} {lead["company"]}".lower()

        if query.lower() in txt_lead:
            results.append((i, lead))

    return results

# EXPORTAR LEADS COMO CSV
def export_csv():
    path_csv = DATA_DIR / "leads.csv"

    leads = read_leads()

    try:
        with path_csv.open("w", newline="", encoding="utf-8") as file_csv:
            writer = csv.DictWriter(file_csv, leads[0].keys())
            writer.writeheader()
            for row in leads:
                writer.writerow(row)
        return path_csv
    except PermissionError:
        return None