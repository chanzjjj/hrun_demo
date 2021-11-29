
def get_account(num):
    '''生成多组测试数据'''
    accounts = []
    for i in range(1, num+1):
        accounts.append(
            {"user": "test%s" %i, "psw": "123456"}
        )
    return accounts

if __name__ == '__main__':
    print(get_account(10))
