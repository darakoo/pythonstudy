# 함수로 구현하기
# def input_expr():
#     return input('수식을 입력하세요 >> ')

# def calculate(expr):
#     return eval(expr)

# expr = input_expr()
# result = calculate(expr) 
# print(f"수식 결과는 {format(result, ',')}입니다.")

# 클래스로 구현하기
class Calculator:
    def input_expr(self):
        expr = input('수식을 입력하세요 >> ')
        self.expr = expr
    def calculate(self):
        return eval(self.expr)

calc = Calculator()
calc.input_expr()
print(f"수식 결과는 {format(calc.calculate(), ',')}입니다.")
