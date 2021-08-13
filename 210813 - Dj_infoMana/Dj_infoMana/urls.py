"""Dj_infoMana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from urls_viewShow import dj_infomanaVs,dj_loginAndlogoutVs,dj_dataToolsVs

urlpatterns = [
    path(r'', dj_loginAndlogoutVs.infoMa_login),
    path(r"logout/", dj_loginAndlogoutVs.infoMa_logout),
    # ————————————————————————————————————————————————————————————
    path(r"activity_show",dj_infomanaVs.activity_show),
    path(r"activity_details", dj_infomanaVs.activity_details),
    path(r"activity_add", dj_infomanaVs.activity_add),
    path(r"activity_modify", dj_infomanaVs.activity_modify),
    path(r"activity_delete", dj_infomanaVs.activity_delete),
    # ————————————————————————————————————————————————————————————
    path(r"exportExcel",dj_dataToolsVs.Info_exportExcel)

]
