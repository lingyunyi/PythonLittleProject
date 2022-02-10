import re
import Base_Setting, Public_Func

SqlData_FuncO = Public_Func.SqlData_FuncO


def count_firEnd(number, init=36):
    if number: number = int(number)
    if number == 1:
        fir, end = str(0), str(init)
    else:
        number -= 1
        count = init * number
        fir, end = str(count), str(count + init)
    return fir, end


if __name__ == '__main__':
    for i in range(1, 30):
        fir, end = count_firEnd(i)
        a = "{}".format(fir + ',' + end)

        print(a)

    # try:
    #     uuid4_str = request.COOKIES.get("username_id")
    #     user_name = str(request.session.get(uuid4_str))
    #     request.session.flush()
    #     response.delete_cookie('username_id')
    # except BaseException as e:
    #     print("-" * 50, e)
