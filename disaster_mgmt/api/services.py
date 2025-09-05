# import requests

# SUPABASE_URL = "https://awpsjsjzfubzzzcexddv.supabase.co"
# API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF3cHNqc2p6ZnVienp6Y2V4ZGR2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTcwOTA3MTgsImV4cCI6MjA3MjY2NjcxOH0.bNEz7G8DHuS3ReSPQysOtQ7H86HsaLlMUxUkuP_GBoE"  # your key

# HEADERS = {
#     "apikey": API_KEY,
#     "Authorization": f"Bearer {API_KEY}",
#     "Content-Type": "application/json"
# }

# import requests

# SUPABASE_URL = "https://awpsjsjzfubzzzcexddv.supabase.co"
# API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF3cHNqc2p6ZnVienp6Y2V4ZGR2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTcwOTA3MTgsImV4cCI6MjA3MjY2NjcxOH0.bNEz7G8DHuS3ReSPQysOtQ7H86HsaLlMUxUkuP_GBoE"  # your key

# HEADERS = {
#     "apikey": API_KEY,
#     "Authorization": f"Bearer {API_KEY}",
#     "Content-Type": "application/json"
# }

# def fetch_table(table_name):
#     response = requests.get(f"{SUPABASE_URL}/rest/v1/{table_name}", headers=HEADERS)
#     return response.json()

# def insert_row(table_name, row_data):
#     response = requests.post(f"{SUPABASE_URL}/rest/v1/{table_name}", headers=HEADERS, json=row_data)
#     return response.json()

# def update_row(table_name, row_id, row_data):
#     response = requests.patch(f"{SUPABASE_URL}/rest/v1/{table_name}?id=eq.{row_id}", headers=HEADERS, json=row_data)
#     return response.json()

# def delete_row(table_name, row_id):
#     response = requests.delete(f"{SUPABASE_URL}/rest/v1/{table_name}?id=eq.{row_id}", headers=HEADERS)
#     return response.status_code
import requests

SUPABASE_URL = "https://awpsjsjzfubzzzcexddv.supabase.co"  # your Supabase project URL
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF3cHNqc2p6ZnVienp6Y2V4ZGR2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTcwOTA3MTgsImV4cCI6MjA3MjY2NjcxOH0.bNEz7G8DHuS3ReSPQysOtQ7H86HsaLlMUxUkuP_GBoE"  # Replace with your service_role key

HEADERS = {
    "apikey": API_KEY,
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def fetch_table(table_name):
    response = requests.get(f"{SUPABASE_URL}/rest/v1/{table_name}", headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text, "status_code": response.status_code}

def insert_row(table_name, row_data):
    response = requests.post(f"{SUPABASE_URL}/rest/v1/{table_name}", headers=HEADERS, json=row_data)
    if response.status_code in (200, 201):
        return response.json()
    else:
        return {"error": response.text, "status_code": response.status_code}
