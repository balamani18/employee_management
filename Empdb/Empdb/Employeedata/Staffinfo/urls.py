from django.urls import path
from.views import *
urlpatterns = [
    path('', loademp, name="le"),
    path('ls/',loadsal),
    path('ue/',upemp),
    path('us/',upsal),
    path('de/', delemp),
    path('se/',seremp),

    path('ge/',getemp),
    path('gs/',getsal),
    path('upe/',updateemp),
    path('ups/',updatesal),
    path('demp/',deleteemp),
    path('semp/',searchemp),

]
