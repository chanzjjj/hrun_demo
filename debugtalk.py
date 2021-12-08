import time
import hashlib


def hook_up():
    print("---------------------setup------------------------")

def hook_up2():
    print("---------------------setup 2------------------------")

def hook_teardown():
    print("---------------------teardown----------------------")

def sign_body(body, apikey="12345678"):
    '''请求body，sign签名'''
    # 列表生成式，生成key=value格式
    a = ["".join(i) for i in body.items() if i[1] and i[0] != "sign"]
    # 参数名ASCII码从小到大排序
    strA = "".join(sorted(a))

    # 在strA后面拼接apikey得到strSignTemp字符串
    strSignTemp = strA+apikey

    # 将strSignTemp字符串转换为小写字符串后进行MD5运算
    def jiamimd5(src):
        m = hashlib.md5()
        m.update(src.encode('UTF-8'))
        return m.hexdigest()
    sign = jiamimd5(strSignTemp.lower())

    return sign

def setup_request(request):
    '''请求预处理，sign签名'''
    body = request.get("json")
    sign = sign_body(body, apikey="12345678")
    request["json"]["sign"] = sign

def get_account(num):
    '''生成多组测试数据'''
    accounts = []
    for i in range(1, num+1):
        accounts.append(
            {"user": "test%s" %i, "psw": "123456"}
        )
    return accounts


def register_user():
    '''随机生成注册账号'''
    username = "test" + str(int(time.time()))
    # print(username)
    return username

if __name__ == '__main__':
    # print(get_account(10))
    # register_user()
    body = {
        "username": "test",
        "password": "123456"
    }
    print(sign_body(body))
