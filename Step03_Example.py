# Step03_Example.py

"""
    회원 한 명의 정보는 번호, 이름, 주소로 이뤄져 있다.
    그리고 그러한 회원이 여러명 있다.
    여러명의 회원 목록을 하나의 묶음(하나의 data)로 관리하고 싶다면...
"""

# 회원 1명의 정보 > dict 
# 회원 여러명의 정보 > 여러 개의 dict를 순서대로 관리 > list

# 3명의 회원 정보를 각각 dict에 담은 후, list에 담는 코드를 작성
mem1 = {"num":1, "name":"Kim", "addr":"Seoul"}
mem2 = {"num":2, "name":"Shin", "addr":"Daejeon"}
mem3 = {"num":3, "name":"Lee", "addr":"Busan"}

members = [mem1,mem2,mem3] #dict 3개를 list에 담기

a = members
b = members[0]
c = members[0]["num"]
d = members[0]["name"]
e = members[0]["addr"]

print("종료됩니다.")