import re
import Base_Setting, Public_Func
SqlData_FuncO = Public_Func.SqlData_FuncO

if __name__ == '__main__':


    check_arg = "撒旦法!!!！！！%￥#￥#%#"
    res = re.compile("[^\\u4e00-\\u9fa5^a-z^A-Z^0-9]")
    check_arg = res.sub("", check_arg)
    print(check_arg)



    # try:
    #     uuid4_str = request.COOKIES.get("username_id")
    #     user_name = str(request.session.get(uuid4_str))
    #     request.session.flush()
    #     response.delete_cookie('username_id')
    # except BaseException as e:
    #     print("-" * 50, e)
