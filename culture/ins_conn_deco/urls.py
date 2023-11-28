
from django.urls import path, include
from.views import *

urlpatterns = [
    path('inscription/', inscription, name='inscription' ),
	path('connexion/', connexion, name='connexion' ),
	path('deconnexion/', deconnexion, name='deconnexion' ),
	path('home/', home, name='home' ),
   
]
