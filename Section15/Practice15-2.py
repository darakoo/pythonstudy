# [문제]
# 사용자로부터 'HH:mm:ss' 형식의 시간을 입력받아서 이를 Watch 클래스의 hour, minute, second 인스턴스 변수에 저장하세요.

class Watch:

    def set_time(self, now):
        hms = now.split(':')
        self.hour = int(hms[0])
        self.minute = int(hms[1])
        self.second = int(hms[2])

    def add_hour(self, hour):
        if hour <= 0:
            return
        self.hour += hour
        self.hour %= 24

    def add_minute(self, minute):
        if minute <= 0:
            return
        self.minute += minute
        self.add_hour(self.minute // 60)
        self.minute %= 60

    def add_second(self, second):
        if second <= 0:
            return
        self.second += second
        self.add_minute(self.second // 60)
        self.second %= 60

    def see(self):
        print('계산된 시간은 {}시 {}분 {}초입니다.'.format(self.hour, self.minute, self.second))


watch = Watch()
watch.set_time(input('현재 시간을 입력하세요.(예시:15:30:29) >>> '))
watch.add_hour(int(input('더할 시간을 입력하세요 >>> ')))
watch.add_minute(int(input('더할 분을 입력하세요 >>> ')))
watch.add_second(int(input('더할 초를 입력하세요 >>> ')))
watch.see()
