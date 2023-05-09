class Describer:

    def __init__(self, name=None, *, value=None, get_fun=None, set_fun=None):
        print(self)
        if not hasattr(self, 'name'):
            if name is None:
                raise ValueError('name is None')
            self.name = name
        if not hasattr(self, 'value'):
            self.value = value
        if not hasattr(self, 'get_fun'):
            self.get_fun = get_fun
        if not hasattr(self, 'set_fun'):
            self.set_fun = set_fun

    def __get__(self, instance, owner):
        n = instance.__data__.get(self.name, self.value)
        if self.get_fun is not None:
            n = self.get_fun(instance)
        return n

    def __set__(self, instance, value):
        if self.set_fun is not None:
            value = self.set_fun(value)
        instance.__data__[self.name] = value

    def __init_subclass__(cls, get_fun=None, set_fun=None):
        base = tuple(set(cls.__bases__) - {Describer})
        if len(base) != 1:
            raise ValueError('只能再继承一个类')
        base = base[0]
        cls_ = type(base.__name__, (), {'get_fun': get_fun, 'set_fun': set_fun, 'value': None, 'name': base.__name__})
        cls_.__get__ = Describer.__get__
        cls_.__set__ = Describer.__set__
        print(cls_.__dict__)
        return cls_


def __get_fun(*args, **kwargs):
    return 1


class A(Describer, int, get_fun=__get_fun):
    pass


class B:
    a = A()


def main():
    a = B()
    print(a.a)


if __name__ == '__main__':
    main()
