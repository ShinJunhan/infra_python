# step08_Input.py

# 콘솔창으로부터 문자열 입력 받기

input_msg = input("메세지 입력:")

print(f"입력한 메세지: {input_msg}")

input_name: str=input("이름 입력:")
input_addr: str=input("주소 입력:")

print(f"이름:{input_name}, 주소:{input_addr}")

# 문자열로 입력 받은 후
input_age: str=input("나이 입력:")
#숫자로 변경해서 1을 더한 값을 얻어 낸다.
age: int = int(input_age) + 1

print(f"당신은 내년에 {age} 살 입니다.")