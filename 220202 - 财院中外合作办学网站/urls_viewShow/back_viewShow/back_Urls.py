from django.urls import path
from urls_viewShow.back_viewShow.v_public import login_vS
from urls_viewShow.back_viewShow.v_public import adminHtml_vS
from urls_viewShow.back_viewShow.v_public import adminAPI_vS
from urls_viewShow.back_viewShow.v_student import studentHtml_vS
from urls_viewShow.back_viewShow.v_student import studentAPI_vS
from urls_viewShow.back_viewShow.v_teacher import teacherHtml_vS
from urls_viewShow.back_viewShow.v_teacher import teacherAPI_vS


urlpatterns = [
    #后台管理登入界面
    path(r"index/",login_vS.login_vS),
    #用户退出清空页面
    path(r"all/logut/",login_vS.logout_anyone),
    path(r"all/teAstWallDelete/API/", adminAPI_vS.teAstWallDelete_API),
    path(r"all/teAstWallAdd/API/", adminAPI_vS.all_teAstWallAdd_API),

    #管理员管理后续视图---前面已经有/back了
    path("ad/infomation/", adminHtml_vS.bc_ad_infomation),
    path("ad/notice/", adminHtml_vS.bc_ad_notice),
    path("ad/news/", adminHtml_vS.bc_ad_news),
    path("ad/download/", adminHtml_vS.bc_ad_download),
    path("ad/law/", adminHtml_vS.bc_ad_law),
    path("ad/teAstWall/",adminHtml_vS.bc_ad_teAstWall),
    path("ad/teAstWallShow/API/", adminAPI_vS.teAstWallShow_API),
    path("ad/contentAdd/", adminHtml_vS.bc_ad_contentAdd),
    path("ad/contentAdd/API/", adminAPI_vS.contentAdd_API),
    path("ad/contentShow/API/", adminAPI_vS.contentShow_API),
    path("ad/contentDelete/API/", adminAPI_vS.contentDelete_API),
    path("ad/infomationModify/API/", adminAPI_vS.infomationModify_API),


    #学生管理后续视图
    path("st/infomation/", studentHtml_vS.bc_st_infomation),
    path("st/infomationModify/API/", studentAPI_vS.infomationModify_API),
    path("st/teAstWall/", studentHtml_vS.bc_st_teAstWall),
    path("st/teAstWallShow/API/", studentAPI_vS.teAstWallShow_API),
    path("st/contentAdd/", studentHtml_vS.bc_st_contentAdd),


    #教师管理后续视图
    path("te/infomation/", teacherHtml_vS.bc_te_infomation),
    path("te/infomationModify/API/", teacherAPI_vS.infomationModify_API),
    path("te/teAstWall/", teacherHtml_vS.bc_te_teAstWall),
    path("te/teAstWallShow/API/", teacherAPI_vS.teAstWallShow_API),
    path("te/contentAdd/", teacherHtml_vS.bc_te_contentAdd),


]
