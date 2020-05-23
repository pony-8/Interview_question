'''
(1)输出9*9乘法口诀
for i in range(1, 10):
   for j in range(1, i+1):
      print "%d*%d=%d" % (i, j, i*j)

(2)如何实现用户的登陆认证
1.cookie session
2.token 登陆成功后生成加密字符串
3.JWT：json wed token缩写 它将用户信息加密到token中,服务器不保存任何用户信息
服务器通过使用保存的密钥来验证token的正确性

(3)django中如何根据数据库表生成model中的类？
1.在settings中设置要连接的数据库
2.生成model模型文件
  python manage.py inspectdb
3.模型文件导入到models中
  python manage.py inspectdb > app/models.py

(4)django的Form和ModeForm的作用？
Form作用：
 1.在前端生成HTML代码
 2.对数据作有效性校验
 3.返回校验信息并展示
ModeForm：根据模型类生成From组件,并且可以操作数据库

(5)F和Q的作用?
F:对数据本身的不同字段进行操作 如:比较和更新
Q：用于构造复杂的查询条件 如：& |操作




'''