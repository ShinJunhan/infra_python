# List type 에 대해서 알아보기

"""
1. 순서가 있다
2. 여러 type의 데이터를 저장할 수 있다
3. 값 변경 가능
"""

# 보통 list type은 같은 데이터 타입으로 사용함
nums = [10,20,30]
names = ["junhan", "chihiro", "ethan"]

# 여러가지 데이터 타입을 섞어서 담을 수도 있지만, 이렇게 보통 사용하지 않음
datas = [10, "xxx", True]

# append() builtin 함수를 이용해서 list에 데이터 추가
nums.append(40) #데이터 덧붙이기 함수 >> nums = [10,20,30,40]
print(nums)

#len() builtin 함수를 이용해서 list의 길이를 얻어낼 수 있다
nums_len = len(nums)
print(nums_len)

# 인덱스에 의한 참조
name0 = names[0]

# 인덱스를 이용하여 삭제
del names[0]

# 값에 의한 삭제
names.remove("ethan")
print(names)

# 맨마지막 index 를 삭제하면서 값을 가져오기
nums.pop()
result = nums.pop()
print(nums)



print("Quit")