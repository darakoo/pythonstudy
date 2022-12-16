# 모듈로 분리 하는 이유 : 공통된 기능을 공유하기위해, 작업의 분배를 위해

# [실행예]
# 김**
# 951012-1######
# 010-###*-5678

def secure_name(name):
    return name[0] + '**'

def secure_no(no):
    return no[0:8] + '******'

def secure_phone(phone):
    # return phone.replace(phone[4:8], '###*')
    return phone[0:4] + '****' + phone[8:]
    
