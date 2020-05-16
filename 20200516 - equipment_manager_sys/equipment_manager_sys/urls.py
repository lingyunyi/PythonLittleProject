"""equipment_manager_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from func_controller import storehouse_managerBP
from func_controller import equipment_managerBP
from func_controller import API_equipment_managerBP
from func_controller import redirect_viewsBP
from func_controller import db_backupsBP
from func_controller import API_db_backupsBP
from func_controller import API_PublicBP
from func_controller import Excel_managerBP


urlpatterns = [
    # ___________________________________________________________________________________________________

    #path('admin/', admin.site.urls),
    path("", redirect_viewsBP.index),
    path("public_api/logout/",redirect_viewsBP.index),
    # 首先是仓库管理页面
    path("storehouse_manager/", storehouse_managerBP.storehouse_manager_show),
    # 仓库设备管理页面
    path("equipment_manager/", equipment_managerBP.equipment_manager_show),
# 仓库设备管理页面
    path("equipment_manager/equipment_manager_details/", equipment_managerBP.equipment_manager_details),
    # 新增一条设备信息
    path("equipment_manager/add_one_equipment/", equipment_managerBP.equipment_manager_show_insert),
    path("API/storehouse_manager/equipment_delete/",API_equipment_managerBP.API_equipment_manager_delete),
    #___________________________________________________________________________________________________
    path("DB_backups/", db_backupsBP.db_backups_show),


    # excel管理系统
    path("excel_manager/", Excel_managerBP.excel_manager_show),
    path("excel_manager/output_excel/", Excel_managerBP.API_excel_manager_output_excel),
    path("excel_manager/input_excel/", Excel_managerBP.API_excel_manager_excel_input_sql),

    # excel管理系统




    # ___________________________________________________________________________________________________
    # API接口
    path("API/storehouse_manager/equipment_manager_insert/", API_equipment_managerBP.API_equipment_manager_insert),
    path("API/storehouse_manager/equipment_manager_show/", API_equipment_managerBP.API_equipment_manager_show),
    path("API/storehouse_manager/equipment_manager_details/", API_equipment_managerBP.API_equipment_manager_details),

    # 保存数据库文件的API API_db_backups_save
    path("API/DB_backups/db_backups_save/", API_db_backupsBP.API_db_backups_save),

    # 公共API
    path("download_files/", API_PublicBP.download_files),
    path("download_files_all/", API_PublicBP.download_files_all),
]
