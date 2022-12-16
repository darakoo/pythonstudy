##### 기본예제 1 : 클래스 작성과 이용

class Computer:

    def set_spec(self, cpu, ram, vga, ssd):
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self):
        print(f'CPU = {self.cpu}')
        print(f'RAM = {self.cpu}')
        print(f'VGA = {self.cpu}')
        print(f'SSD = {self.cpu}')

desktop = Computer()
desktop.set_spec('i7', '16GB', 'GTX1060', '512GB')
desktop.hardware_info()
print('=================')
notebook = Computer()
notebook.set_spec('i5', '8GB', 'MX300', '256GB')
notebook.hardware_info()
