from django.urls import path
from urls_viewShow.back_viewShow.v_public import login_vS


urlpatterns = [
    #后台管理登入界面
    path(r"index/",login_vS.login_vS),
    #用户退出清空页面
    path(r"all/logut",login_vS.logout_anyone),

#     #管理员管理后续视图
#     path("/ad/ad_index", ),
#
#     #教师管理后续视图
#     path("/te/te_index", ),
#
#     #学生管理后续视图
#     path("/st/st_index", ),
]
