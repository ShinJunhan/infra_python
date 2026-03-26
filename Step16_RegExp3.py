# Step16_RegExp3.py


import re

# list 안에 어떤 서버의 로그가 들어 있다고 가정
logs = [
    "[INFO] Server started successfully.",
    "[WARN] Memory usage is high.",
    "[ERROR] Database connection failed.",
    "[DEBUG] x = 10"
]

# logs 에서 ERROR or WARN 로그만 찾아서 출력

# [WARN] 또는 [ERROR] 로 문자열이 시작하는지 검증할 정규 표현식 만들기

# 첫글자가 W or A or R or N 인지를 검증하는 정규 표현식
pattern1 = r"^[WARN]"
# [WARN]으로 시작하는지 검증하는 정규 표현식
pattern2 = r"^\[WARN\]"
# [ERROR]으로 시작하는지 검증하는 정규 표현식
pattern3 = r"^\[ERROR\]"
# WARN or ERROR으로 시작하는지 검증하는 정규 표현식
pattern4 = r"^(WARN|ERROR)"

# [WARN] or [ERROR] 으로 시작하는지 검증하는 정규 표현식
pattern = r"^\[(WARN|ERROR)\]"

for tmp in logs:
    # 정규 표현식에 매칭되는 문자열이 있으면
    if re.search(pattern, tmp):
        print(tmp)

'''
제미나이 도움
# 1. Define the pattern: matches [ERROR] or [WARN]
# Note: \[ and \] are used because brackets are special characters in Regex
pattern = r"\[(ERROR|WARN)\]"

# 2. Use a list comprehension to filter and print
for log in logs:
    if re.search(pattern, log):
        print(log)
'''
