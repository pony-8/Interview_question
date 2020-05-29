'''

11 面向切面编程AOP和装饰器

这个AOP一听起来有点懵,同学面阿里的时候就被问懵了…

装饰器是一个很著名的设计模式，经常被用于有切面需求的场景，较为经典的有插入日志、性能测试、事务处理等。装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量函数中与函数功能本身无关的雷同代码并继续重用。概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。

这个问题比较大,推荐: http://stackoverflow.com/questions/739654/how-can-i-make-a-chain-of-function-decorators-in-python

中文: http://taizilongxu.gitbooks.io/stackoverflow-about-python/content/3/README.html

12 鸭子类型

“当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。”

我们并不关心对象是什么类型，到底是不是鸭子，只关心行为。

比如在python中，有很多file-like的东西，比如StringIO,GzipFile,socket。它们有很多相同的方法，我们把它们当作文件使用。

又比如list.extend()方法中,我们并不关心它的参数是不是list,只要它是可迭代的,所以它的参数可以是list/tuple/dict/字符串/生成器等.

鸭子类型在动态语言中经常使用，非常灵活，使得python不想java那样专门去弄一大堆的设计模式。

13 Python中重载

引自知乎:http://www.zhihu.com/question/20053359

函数重载主要是为了解决两个问题。

可变参数类型。
可变参数个数。
另外，一个基本的设计原则是，仅仅当两个函数除了参数类型和参数个数不同以外，其功能是完全相同的，此时才使用函数重载，如果两个函数的功能其实不同，那么不应当使用重载，而应当使用一个名字不同的函数。

好吧，那么对于情况 1 ，函数功能相同，但是参数类型不同，python 如何处理？答案是根本不需要处理，因为 python 可以接受任何类型的参数，如果函数的功能相同，那么不同的参数类型在 python 中很可能是相同的代码，没有必要做成两个不同函数。

那么对于情况 2 ，函数功能相同，但参数个数不同，python 如何处理？大家知道，答案就是缺省参数。对那些缺少的参数设定为缺省参数即可解决问题。因为你假设函数功能相同，那么那些缺少的参数终归是需要用的。

好了，鉴于情况 1 跟 情况 2 都有了解决方案，python 自然就不需要函数重载了。

14 新式类和旧式类

这个面试官问了,我说了老半天,不知道他问的真正意图是什么.

stackoverflow

这篇文章很好的介绍了新式类的特性: http://www.cnblogs.com/btchenguang/archive/2012/09/17/2689146.html

新式类很早在2.2就出现了,所以旧式类完全是兼容的问题,Python3里的类全部都是新式类.这里有一个MRO问题可以了解下(新式类是广度优先,旧式类是深度优先),<Python核心编程>里讲的也很多.

一个旧式类的深度优先的例子

class A():

    def foo1(self):

        print "A"

class B(A):

    def foo2(self):

        pass

class C(A):

    def foo1(self):

        print "C"

class D(B, C):

    pass

 

d = D()

d.foo1()

 

# A

按照经典类的查找顺序从左到右深度优先的规则，在访问d.foo1()的时候,D这个类是没有的..那么往上查找,先找到B,里面没有,深度优先,访问A,找到了foo1(),所以这时候调用的是A的foo1()，从而导致C重写的foo1()被绕过

15 __new__和__init__的区别

这个__new__确实很少见到,先做了解吧.

__new__是一个静态方法,而__init__是一个实例方法.
__new__方法会返回一个创建的实例,而__init__什么都不返回.
只有在__new__返回一个cls的实例时后面的__init__才能被调用.
当创建一个新实例时调用__new__,初始化一个实例时用__init__.
stackoverflow

ps: __metaclass__是创建类时起作用.所以我们可以分别使用__metaclass__,__new__和__init__来分别在类创建,实例创建和实例初始化的时候做一些小手脚.

16 单例模式

​ 单例模式是一种常用的软件设计模式。在它的核心结构中只包含一个被称为单例类的特殊类。通过单例模式可以保证系统中一个类只有一个实例而且该实例易于外界访问，从而方便对实例个数的控制并节约系统资源。如果希望在系统中某个类的对象只能存在一个，单例模式是最好的解决方案。

__new__()在__init__()之前被调用，用于生成实例对象。利用这个方法和类的属性的特点可以实现设计模式的单例模式。单例模式是指创建唯一对象，单例模式设计的类只能实例
这个绝对常考啊.绝对要记住1~2个方法,当时面试官是让手写的.

1 使用__new__方法

class Singleton(object):

    def __new__(cls, *args, **kw):

        if not hasattr(cls, '_instance'):

            orig = super(Singleton, cls)

            cls._instance = orig.__new__(cls, *args, **kw)

        return cls._instance

 

class MyClass(Singleton):

    a = 1

2 共享属性

创建实例时把所有实例的__dict__指向同一个字典,这样它们具有相同的属性和方法.

 

class Borg(object):

    _state = {}

    def __new__(cls, *args, **kw):

        ob = super(Borg, cls).__new__(cls, *args, **kw)

        ob.__dict__ = cls._state

        return ob

 

class MyClass2(Borg):

    a = 1

3 装饰器版本

def singleton(cls):

    instances = {}

    def getinstance(*args, **kw):

        if cls not in instances:

            instances[cls] = cls(*args, **kw)

        return instances[cls]

    return getinstance

 

@singleton

class MyClass:

  ...

4 import方法

作为python的模块是天然的单例模式

# mysingleton.py

class My_Singleton(object):

    def foo(self):

        pass

 

my_singleton = My_Singleton()

 

# to use

from mysingleton import my_singleton

 

my_singleton.foo()

'''