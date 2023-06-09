# Pointer
一个在python中的指针类

本模块有一个Pointer的指针基类，当他被与其他类继承时将创造一个指针类

例：
```python
from Pointer import Pointer


class A:
    
    def __init__(self, a):
        self.a = a


class B(Pointer, A):
    pass

```
这时，B类就是A类的指针类，同时，除了赋值操作外，其他功能和使用A类没有任何区别

而赋值操作需要对类的变量__value__进行赋值

即：
```python
b = B()
b.__value__ = A()
```
想获取被指向的对象也要通过__value__获取

即：
```python
a = b.__value__
```

但是如果直接输出是可以调用被指向的类的__str__方法的

即：
```python
class String(Pointer, str):
    pass


a = String('b')
print(a)  # 输出: b
```
包括其他调用魔法方法的情况。

同时，普通方法也是可以直接调用的

即：
```python
a = String('a b')
print(a.split(' '))  # 输出: ['a', 'b']
```

本模块自带了str, int, bool的指针类
