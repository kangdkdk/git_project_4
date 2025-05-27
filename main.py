from add import add
from subtract import subtract
from multiply import multiply
from divide import divide


def calculator():
    a = float(input("첫 번째 숫자 넣어주세요~~: "))
    b = float(input("두 번째 숫자 넣어주세요~~: "))
    op = input("연산자 (+, -, *, /): ")
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    if op in operations:
        try:
            result = operations[op](a, b)
            print("결과는 이거에요~~:", result)
        except Exception as e:
            print("오류는 이거에요~~:", e)
    else:
        print("올바르지 않은 연산자입니다.")


if __name__ == "__main__":
    calculator()