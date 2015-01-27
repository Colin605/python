__author__ = 'Colin'
# coding:utf8

'''
知识点：
    1，列表的extend和append方法的区别
        extend 接受一个list 参数，而且是把list中的每个元素加入到原来的list中去
        append接受任何类型的参数，并且是把接受到的参数简单的添加到原来的list后面而已， 接受到的是一个整体
    2，lambda 的使用
        lambda的实际意义是代替一个函数，也叫匿名函数，也就是可以省去函数名，但是其返回也是函数类型这样有利有弊吧，
        大多情况可以用别的方法实现。但是lambda也有其存在的意义。
            2.1，简化代码
            2.2，对于只调用一次函数这样情况，毕竟有时候大项目中命名也是比较伤脑筋的吧
    3，python函数的定义和返回值
        利用def定义函数，return返回值，函数的返回值可以有很多个，利用 list或者 tuple 可以实现

    Failure case：

    def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

    f1, f2, f3 = count()

    这里f1,f2,f3的返回值不是期望的1,4,9
    原因在于 这里函数 count里面只是把 f 函数简单的添加到了 fs 列表中去，f 代表的是函数本身，而不是函数的返回值

'''


def counter():
    fs = ['begin']
    for i in range(1, 4):
        def f():
            return i * i
        # print(f)  # 测试用，为了证明添加到列表中的是 f 函数本身而不是函数值
        fs.append(f)
    fs.append('end')
    return fs

# 此处添加了 begin/end 用作测试
f1, f2, f3, f4, f5 = counter()
print("case 1 result:")
print("f1 = %s; f2 = %s; f3 = %s; f4 = %s; f5 = %s;" %(f1, f2, f3, f4, f5))
# print(f1)
# print(f2)


'''
如果想让输出的结果为 1 4 9 可以像下面这样实现
'''


def counter2():
    fs = []
    for i in range(1, 4):
        r = i * i
        fs.append(r)
    return fs

f1, f2, f3 = counter2()
print("case 2 result:")
print("f1 = %s; f2 = %s; f3 = %s" %(f1, f2, f3))


'''
case 3
利用lambda实现 f 函数
'''


def counter3():
    fs = []
    for i in range(1, 4):
        '''
        这里刚开始对python3里面的lambda用法理解有点问题，
        lambda的实际意义是代替一个函数，也叫匿名函数，也就是可以省去函数名，但是其返回也是函数类型这样有利有弊吧，
        大多情况可以用别的方法实现。但是lambda也有其存在的意义。
        1，简化代码
        2，对于只调用一次函数这样情况，毕竟有时候大项目中命名也是比较上脑筋的吧
        '''
        f = lambda: i * i
        print("函数f的类型是:%s" % type(f))
        # print(type(f))
        r = f()
        fs.append(r)
    return fs

f1, f2, f3 = counter3()
print("case 3 result:")
print("f1 = %s; f2 = %s; f3 = %s" % (f1, f2, f3))

'''
case 4
或者在添加到fs列表之前，调用一下f函数得到其值就可以
'''


def counter4():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        r = f()
        fs.append(f)
    return fs

f1, f2, f3 = counter2()
print("case 4 result:")
print("f1 = %s; f2 = %s; f3 = %s" % (f1, f2, f3))

'''
the result show:

case 1 result:
f1 = begin; f2 = <function counter.<locals>.f at 0x000000000280CC80>; f3 = <function counter.<locals>.f at 0x000000000280CD08>; f4 = <function counter.<locals>.f at 0x000000000280CD90>; f5 = end;
case 2 result:
f1 = 1; f2 = 4; f3 = 9
函数f的类型是:<class 'function'>
函数f的类型是:<class 'function'>
函数f的类型是:<class 'function'>
case 3 result:
f1 = 1; f2 = 4; f3 = 9
case 4 result:
f1 = 1; f2 = 4; f3 = 9
'''
