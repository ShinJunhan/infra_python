# Step16_RegExp4.py

import re

if __name__ == "__main__":
    # 임의의 문자열을 입력 받는다.
    user_id = input("아이디를 입력(영문자 대소문자, 숫자만 가능):")

    '''
        입력한 문자열을 검증해서 조건에 맞으면 "가입되었습니다", 
        조건에 맞지 않으면 "사용할 수 없는 아이디 입니다"
        출력하는 프로그래밍을 해보세요.
    '''
    pattern = r"^[a-zA-Z0-9]+$" # +는 1번 이상 반복, *는 0번 이상 반복

    if re.search(pattern, user_id):
        print("가입 되었습니다!")
    else:
        print("사용할 수 없는 아이디입니다.")