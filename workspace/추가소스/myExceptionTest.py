#%% my exception
class NickNameError(Exception):
    pass

def checkNickName(name):
    if name == "바보":
        raise NickNameError
        
nickname = input("닉네임 : ")

try :
    checkNickName(nickname)
    print("닉네임 생성 성공!")
except NickNameError :
    print("비속어는 사용할 수 없습니다.")

#%% my exception task

# =============================================================================
# 외부에서 채팅 문자열을 받아와서 in으로 비속어 검사를 한다.
# 비속어는 바보, 멍청이, 똥개이다.
# 사용자 예외처리로 선언하여 만든다. 비속어가 없다면
# 채팅 메세지를 출력한다.
# =============================================================================

class BadWordError(Exception):
    pass

chat = ""

def checkChatting(temp) :
    badWords = ["바보", "멍청", "똥개"]
    for i in badWords:
        if i in temp :
            global chat
            chat = temp.replace(i, "**")
            raise BadWordError()
cnt = 0
while True:
    chat = input("채팅[나가기:q] : ")
    if chat.lower() == 'q':
        break

    try:
        checkChatting(chat)
        print(chat)
    except BadWordError:
        cnt += 1
        print("%d회 비속어를 사용하셨습니다." %cnt)
        print(chat)


















