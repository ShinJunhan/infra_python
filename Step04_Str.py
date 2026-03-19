# str type 에 대해서 알아보기 (중요!)

# 양쪽에 공백이 포함될 가능성이 있는 문자열이 있다고 가정하자
# 만일 공백을 제거하고 싶다면?
text = "   Cloud Infra   "
result1 = text.strip() # 문자열 양쪽 공백 제거시, strip() 함수 사용
print(text)
print(result1)


# IP주소의 숫자 하나하나를 분리해서 list에 담기
myIp = "192.168.0.2"
result2 = myIp.split(".") # split(".") 함수 사용
print(result2)


# 다시 합치기 >> join
result3 = ".".join(result2) # 다시 합치기
print(result3)

# 특정 문자열 찾아서 대체하기
result4 = "hello mimi".replace("mi", "ma")
print(result4)

result5 = "python".upper()
result6 = "PYTHON".lower()

print(result5)
print(result6)


print("제거 되었습니다")