class C:
    def __init__(self):
        self.__x = None

    # 해당 클래스의 getter
    @property
    def x(self):
        """I'm the 'x' property."""
        print("getter of x called")
        return self.__x

    # 해당 클래스의 setter
    @x.setter
    def x(self, value):
        print("setter of x called")
        self.__x = value


c = C()
c.x = 'foo'  # setter는 이렇게 호출한다.
foo = c.x    # getter는 이렇게 호출한다.

