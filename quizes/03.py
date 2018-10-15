# -*- coding:utf-8 -*-


'''
list.copy()

리스트의 shallow copy를 수행한다.
원본 리스트와 id값이 다르고 값은 복사 당시의 값과 동일하다.

새 리스트의 값이 달라졌다고 기존 리스트의 값이 변하지 않는다.

그런데 '=' 오퍼레이터를 통해 복사했다면 id값까지 동일해진다.(deep copy)
이럴 땐 새 리스트의 값을 변경하면 기존 리스트의 값을 같이 변경하게 된다.
'''

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list.copy()
new_list2 = old_list

print(id(old_list))
print(id(new_list))
print(id(new_list2))

print(old_list)
print(new_list)
print(new_list2)

new_list.append(['b','c','d'])
print("------- new_list.append--------")
print(old_list)
print(new_list)
print(new_list2)

new_list2.append(['e','f','10'])
print("------- new_list2.append-------")
print(old_list)
print(new_list)
print(new_list2)

