# [문제]
# 복합 대입 연산자
# 다음은 저금통에 용돈을 넣고 빼는 과정을 보여 주는 프로그램입니다.
# [실행예]
# 저금통에 용돈 10000원을 넣었습니다.
# 지금 저금통에는 10000원이 있습니다.
# 저금통에서 스낵 구입비 2000원을 뺐습니다.
# 지금 저금통에는 8000원이 있습니다.


piggy_bank = 0

money = 10000
piggy_bank += money
print('저금통에 용돈 {}원을 넣었습니다.'.format(money))
print('지금 저금통에는 {}원이 있습니다.'.format(piggy_bank))

snack = 2000
piggy_bank -= snack
print('저금통에서 스낵 구입비 {}원을 뺐습니다.'.format(snack))
print('지금 저금통에는 {}원이 있습니다.'.format(piggy_bank))
