import pyautogui				# pyautogui 패키지 불러오기
import time						# time 패키지 불러오기
import clipboard				# 클립보드 패키지 불러오기

# 예제 파일 불러오기
time.sleep(1)
pyautogui.hotkey("win", "r")				# 윈도우의 실행 메뉴 단축키 입력
time.sleep(0.5)
pyautogui.write("c:/score.xlsx")		# 경로를 포함한 파일 이름 지정
pyautogui.press("enter")
pyautogui.sleep(5)

# 총점과 평균 제목 입력하기
pyautogui.hotkey("ctrl", "home")							# [A1] 셀로 위치 변경
pyautogui.press("right", presses = 4, interval = 0.1)		# 현재 위치에서 오른쪽으로 4칸 이동
clipboard.copy("총점\t평균") 								# 입력할 내용을 클립보드에 복사
time.sleep(1)
pyautogui.hotkey("ctrl", "v")								# 제목 복사
time.sleep(1)

# 총점 및 평균 계산하기
time.sleep(1)
pyautogui.press("down") 				# [E1] 셀에서 [E2] 셀로 이동

for i in range(10):
    pyautogui.write(f"=sum(B{2+i}:D{2+i})", interval=0.1)		# 총점 계산식 입력
    pyautogui.press("right")
    pyautogui.write(f"=average(B{2+i}:D{2+i})", interval=0.1)	# 평균 계산식 입력
    pyautogui.press(["enter", "left"]) 

# 셀 정렬하기  
pyautogui.hotkey("ctrl", "g")				# 엑셀의 이동 메뉴 실행
pyautogui.typewrite("a1", interval=0.1)		# [A1] 셀에 입력
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.hotkey("ctrl", "a")				# 범위 지정 단축키 입력
time.sleep(0.5)
pyautogui.hotkey("alt", "h")				# [홈] 탭 실행
pyautogui.typewrite("c")					# 가운데 맞춤 실행(엑셀 2016 버전)
pyautogui.typewrite("2")

# 엑셀 2013, 2019 이후 버전에서는 가운데 맞춤 단축키가 a, c이므로
# pyautogui.typewrite("a"), pyautogui.typewrite("c") 코드를 사용하기 바랍니다.

# 표 만들기
time.sleep(0.5)
pyautogui.hotkey("ctrl", "t")				# 표 만들기 메뉴 실행
pyautogui.press("enter")					# 표 만들기 확인

# 총점 순으로 정렬하기
pyautogui.hotkey("ctrl", "g")				# 엑셀의 이동 메뉴 실행
pyautogui.typewrite("e1", interval=0.1)		# [E1] 셀에 입력
pyautogui.press("enter")					# 확인 입력
pyautogui.hotkey("alt", "a")				# 정렬 단축키 실행
pyautogui.press("s")						# 내림차순 단축키 입력
pyautogui.press("d")

# 저장 및 닫기
time.sleep(1)
pyautogui.hotkey("alt", "f2")				# 파일 저장 메뉴 불러오기
pyautogui.typewrite("score_result.xlsx", interval=0.1)		# 현재 위치에 "score_result.xlsx"로 저장
pyautogui.press("enter")
pyautogui.hotkey("alt", "f4")				# 엑셀 종료