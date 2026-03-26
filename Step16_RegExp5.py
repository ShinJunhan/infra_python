# Step16_RegExp5.py

import re

if __name__ == "__main__":
    input_id = input("아이디 입력(영문자로 시작하고, 5~10글자 이내, 특수문자 허용안함):")

    # 위 조건에 맞으면 "가입되었습니다", 맞지 않으면 "사용할 수 없는 아이디 입니다" 출력

    pattern = r"^[a-zA-Z][a-zA-Z0-9_]{4,9}$" # +는 1번 이상 반복, *는 0번 이상 반복

    if re.search(pattern, input_id):
        print("가입 되었습니다!")
    else:
        print("사용할 수 없는 아이디입니다.")
