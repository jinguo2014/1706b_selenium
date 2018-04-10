import unittest
from baidu.baidu_yun import BaiduYun
import  HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [BaiduYun("test_register"),BaiduYun("test_login") , BaiduYun("test_link")]
    suite.addTests(tests)

    fp = open("result_baidu.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test result', description=u'result:', verbosity=2)
    runner.run(suite)
    fp.close()

    # # ------------------------发送邮件--------------------
    # file_name = "result_baidu.html"
    # sender = "251266295@qq.com"
    # receivers = ["565873048@qq.com", "251266295@qq.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    #
    # # 创建一个带附件的实例
    # message = MIMEMultipart()
    # message['From'] = Header("张三", 'utf-8')
    # message['To'] = Header("测试经理", 'utf-8')
    # subject = '算数的测试报告'
    # message['Subject'] = Header(subject, 'utf-8')
    #
    # # 邮件正文内容
    # message.attach(MIMEText('这是算数的测试报告，附件是具体报告！', 'plain', 'utf-8'))
    #
    # # 构造附件1，传送当前目录下的 test.txt 文件
    # att1 = MIMEText(open(file_name, 'rb').read(), 'base64', 'utf-8')
    # att1["Content-Type"] = 'application/octet-stream'
    # # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    # att1["Content-Disposition"] = 'attachment; filename="result.html"'
    # message.attach(att1)
    #
    # # # 构造附件2，传送当前目录下的 runoob.txt 文件
    # # att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
    # # att2["Content-Type"] = 'application/octet-stream'
    # # att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
    # # message.attach(att2)
    #
    # try:
    #     smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
    #     smtpObj.login("251266295@qq.com", "etitfpsfisttbhfe")  # 仅smtp服务器需要验证时
    #     smtpObj.sendmail(sender, receivers, message.as_string())
    #     print("邮件发送成功")
    #
    # except smtplib.SMTPException:
    #     print("Error: 无法发送邮件")




        # 这里的verbosity是一个选项, 表示测试结果的信息复杂度，有三个值
    # 0(静默模式): 你只能获得总的测试用例数和总的结果
    # 比如
    # 总共100个
    # 失败20
    # 成功80
    # 1(默认模式): 非常类似静默模式
    # 只是在每个成功的用例前面有个“.”  每个失败的用例前面有个 “F”
    # 2(详细模式): 测试结果会显示每个测试用例的所有相关的信息
    # 并且
    # 你在命令行里加入不同的参数可以起到一样的效果
    # 加入 - -quiet
    # 参数
    # 等效于
    # verbosity = 0
    # 加入 - -verbose参数等效于
    # verbosity = 2
    # 什么都不加就是
    # verbosity = 1