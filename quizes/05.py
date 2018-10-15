'''

get(key[, default]):
키값이 딕셔너리에 있으면 리턴한다. 만일 없으면 None을 리턴한다.
다시말해 KeyError를 raise하지 않는다.

하지만 직접 키 값을 참조할 때 값이 없다면 KeyError가 raise된다.
'''

obj = {'key': 123}

print(obj['key'])
print(obj.get('key'))


print(obj.get('keys'))
print(obj['keys'])
