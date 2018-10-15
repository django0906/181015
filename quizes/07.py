'''
위치인자:
일반적인 파라미터와 동일하다.
*args로 가변인자 전달이 가능하다.

키워드인자:
딕셔너리 형태의 파라미터 전달이 가능하다.
key에 따른 value값을 파라미터로 전달할 수 있다.
단, 순서는 오른쪽부터 전달된다.
'''


def add2(a, b):
    return a+b

def adddd(*args):
    a = 0
    for num in args:
        a += num
    print(a)


def printttt(**kwargs):
    for key, value in kwargs.items():
        print(f'this is key: {key} and value: {value}')


if __name__ == '__main__':
    add2(1, 9)
    adddd(1, 2)
    adddd(1, 2, 3)
    adddd(1, 2, 3, 4)
    printttt(mine='a', yours='b')
    printttt(key='kkeeyy', value='vvvalluuueeeee')
    printttt(a='a', b='b', c='c', d='d')
