# List type 에 대해서 알아보기

nums = [10,20,30,40,50]
names = ["kim", "shin", "Lee", "park", "choi"]

# list에 들어 있는 데이터를 앞에서부터 순서대로 참조하면서 어떤 동작을 할 일들이 많다
for item in nums :
    print(item)

for item in names:
    print("이름을 순서대로 출력중...")
    print(item)

r1 = range(5)
r2 = range(10)

print(r1) # [0,1,2,3,4]
print(r2) # [0,1,2,3,4,5,6,7,8,9]

for item in range(5) :
    print(item)


result2 = range(len(names))

for i in range(len(names)) :
    print("list의 index와 함께 출력")
    print(i, names[i])


print("Quit")
