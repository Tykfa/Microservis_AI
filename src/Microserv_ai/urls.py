from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Witaj w Microserv_ai!</h1><p>API dostępne pod /api/</p>")


urlpatterns = [
    path("", home, name="home"),  # Strona główna
    path("api/", include("chat.urls")),  # Twoje API
    path("admin/", admin.site.urls),  # Panel admina
]
