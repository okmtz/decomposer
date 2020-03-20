num = input('please input num:')

# 空の配列を作成
lst = []

num = int(num)

while num>0:
    lst.append(num%10)
    # 切り上げて除算
    num //= 10


lst.reverse()

print(lst)