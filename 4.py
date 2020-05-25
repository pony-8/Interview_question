'''

(1)values和values_list的区别
values : queryset类型的列表中是字典
values_list : queryset类型的列表中是元组

(2)filter和exclude的区别？
两者取到的值都是QuerySet对象,filter选择满足条件的,exclude:排除满足条件的

(3)select_related和prefetch_related的区别？
前提：有外键存在时，可以很好的减少数据库请求的次数,提高性能
select_related通过多表join关联查询,一次性获得所有数据,只执行一次SQL查询
prefetch_related分别查询每个表,然后根据它们之间的关系进行处理,执行两次查询

(4)说说 nginx 和 uWISG 服务器之间如何配合工作的？
首先浏览器发起 http 请求到 nginx 服务器，Nginx 根据接收到请求包，进行 url 分析,判断访问的资源类型.
如果是静态资源，直接读取静态资源返回给浏览器.
如果请求的是动态资源就转交给 uwsgi服务器，uwsgi 服务器根据自身的 uwsgi 和 WSGI 协议，找到对应的 Django 框架，
Django 框架下的应用进行逻辑处理后，将返回值发送到 uwsgi 服务器，然后 uwsgi 服务器再返回给 nginx，最后 nginx将
返回值返回给浏览器进行渲染显示给用户。

(5)说出git常用命令并说出该命令的作用
a)作用：对源代码进行分布式,版本控制，方便跟踪源代码的修改过程，备份源代码,在团队开发中经常使用
b)常用命令：
  git init 初始化本地git仓库
  git add . 将当前工作区的所有文件添加到暂存区
  git commit -m “”将当前暂存区文件添加到本地仓库进行版本管理
  git push 将本地仓库内容添加到远程仓库中
  git pull 将远程仓库代码拉取到本地
  git clone 拷贝远程仓库内容到本地

'''