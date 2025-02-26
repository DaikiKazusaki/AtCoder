s1, s2 = input().split()

if s1 == "sick" and s2 == "sick":
    print('1')
elif s1 == "sick" and s2 == "fine":
    print('2')
elif s1 == "fine" and s2 == "sick":
    print('3')
else:
    print('4')