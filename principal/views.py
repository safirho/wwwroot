#from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def home(request):
    return HttpResponse("""
        <h1>¡Hola desde Azure + Django!</h1>
        <p>Power BI embebido (ejemplo):</p>
        <iframe width='800' height='600'
                src='https://app.powerbi.com/reportEmbed?reportId=3705c713-72ec-428f-878a-0ec8ed9efdf7&autoAuth=true&ctid=2ce69147-2638-4f36-8769-4eb269cb1526'
                frameborder='0' allowFullScreen='true'>
        </iframe>
        <p>Estás autenticado.</p>
        <p><a href='/logout/'>Cerrar sesión</a></p>
    """)
