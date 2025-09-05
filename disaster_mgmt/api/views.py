from django.shortcuts import render
from django.http import JsonResponse
from .services import fetch_table, insert_row

# -------------------------
# API Endpoints
# -------------------------
def list_resources(request):
    return JsonResponse(fetch_table("resources"), safe=False)

def list_requests(request):
    return JsonResponse(fetch_table("requests"), safe=False)

def list_assessments(request):
    return JsonResponse(fetch_table("assessments"), safe=False)

def list_assignments(request):
    return JsonResponse(fetch_table("assignments"), safe=False)

def add_resource(request):
    new_resource = {"type": "Water Truck", "location": "City A"}
    return JsonResponse(insert_row("resources", new_resource), safe=False)

# -------------------------
# Dummy Frontend Pages
# -------------------------
def home(request):
    return render(request, 'api/home.html')

def resources_page(request):
    resources = fetch_table("resources")
    return render(request, 'api/resources.html', {'resources': resources})

def requests_page(request):
    requests_data = fetch_table("requests")
    return render(request, 'api/requests.html', {'requests': requests_data})

def assessments_page(request):
    assessments = fetch_table("assessments")
    return render(request, 'api/assessments.html', {'assessments': assessments})

def assignments_page(request):
    assignments = fetch_table("assignments")
    return render(request, 'api/assignments.html', {'assignments': assignments})
