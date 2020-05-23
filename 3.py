'''
(1)简述什么是FBV和CBV？
FBV和CBV本质是一样的
基于函数的视图叫做FBV，基于类的视图叫做CBV
在python中使用CBV的优点：
1.提高了代码的复用性，可以使用面向对象的技术，比如Mixin（多继承）
2.可以用不同的函数针对不同的HTTP方法处理，而不是通过很多if判断，提高代码可读性

(2)Django本身提供了runserver，为什么不能用来部署？
1.runserver方法是调试 Django 时经常用到的运行方式，它使用Django自带的
WSGI Server 运行，主要在测试和开发中使用，并且 runserver 开启的方式也是单进程 。
2.uWSGI是一个Web服务器，它实现了WSGI协议、uwsgi、http 等协议。注意uwsgi是一种通信协议，而uWSGI是实现uwsgi协议和WSGI协议的 Web 服务器。uWSGI具有超快的性能、低内存占用和多app管理等优点，并且搭配着Nginx就是一个生产环境了，能够将用户访问请求与应用 app 隔离开，实现真正的部署 。相比来讲，支持的并发量更高，方便管理多进程，发挥多核的优势，提升性能。

(3)基于django使用ajax发送post请求时，都可以使用哪种方法携带csrf token？
1.后端将csrftoken传到前端，发送post请求时携带这个值发送
2.获取form中隐藏标签的csrftoken值，加入到请求数据中传给后端                                           
3.cookie中存在csrftoken,将csrftoken值放到请求头中

(4)django中csrf的实现机制
第一步：django第一次响应来自某个客户端的请求时,后端随机产生一个token值，把这个token保存在SESSION状态中;同时,后端把这个token放到cookie中交给前端页面；
第二步：下次前端需要发起请求（比如发帖）的时候把这个token值加入到请求数据或者头信息中,一起传给后端；Cookies:{csrftoken:xxxxx}
第三步：后端校验前端请求带过来的token和SESSION里的token是否一致。

(5)django的Model中的ForeignKey字段中的on_delete参数有什么作用？
删除关联表中的数据时,当前表与其关联的field的操作
django2.0之后，表与表之间关联的时候,必须要写on_delete参数,否则会报异常


'''