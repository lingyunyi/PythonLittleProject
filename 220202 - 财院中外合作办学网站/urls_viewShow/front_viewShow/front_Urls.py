from django.urls import path
from urls_viewShow.front_viewShow.v_public import showHtml_vS
from urls_viewShow.front_viewShow.v_public import frontShowAPI_vS


urlpatterns = [
    # 学院前端展示页面（首页）
    path(r"", showHtml_vS.fr_index),
    # 学院展示
    path(r"front/fr/show/", showHtml_vS.fr_sc_show),
    # 学院动态
    path(r"front/fr/dynamic/", showHtml_vS.fr_sc_dynamic),
    # 合作院校
    path(r"front/fr/partners/", showHtml_vS.fr_sc_partners),
    # 留学生招生
    path(r"front/fr/overseas/", showHtml_vS.fr_sc_overseas),
    # 教师留言
    path(r"front/fr/teacher/", showHtml_vS.fr_sc_teacher),
    # 学生留言
    path(r"front/fr/student/", showHtml_vS.fr_sc_student),
    # 后台登入
    path(r"front/fr/login/", showHtml_vS.fr_sc_login),






    # API————————————————————————————————————————
    # 通知公告-等等-渲染API
    path(r"front/fr/dynamic/contentShow/API/", frontShowAPI_vS.Fr_contentShow_API),
    # 学生留言内容渲染API
    path(r"front/fr/student/teWallShow/API/", frontShowAPI_vS.Fr_stWallShow_API),
    # 教室留言内容渲染API
    path(r"front/fr/teacher/teWallShow/API/", frontShowAPI_vS.Fr_teWallShow_API),



]
