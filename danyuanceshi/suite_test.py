import unittest
from danyuanceshi.test_mathfunc import TestMathFunc
import HTMLTestRunner

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

if __name__ == '__main__':
   ''' suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))

    fp = open("result.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test result', description=u'result:',verbosity=2)
    runner.run(suite)
    fp.close()

    #------------------------发送邮件--------------------
    file_name = "result.html"
    sender = "251266295@qq.com"
    receivers = ["565873048@qq.com", "251266295@qq.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("张三", 'utf-8')
    message['To'] = Header("测试经理", 'utf-8')
    subject = '算数的测试报告'
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('这是算数的测试报告，附件是具体报告！', 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open(file_name, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="result.html"'
    message.attach(att1)

    # # 构造附件2，传送当前目录下的 runoob.txt 文件
    # att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
    # att2["Content-Type"] = 'application/octet-stream'
    # att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
    # message.attach(att2)

    try:
        smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
        smtpObj.login("251266295@qq.com", "etitfpsfisttbhfe")  # 仅smtp服务器需要验证时
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")

    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

'''


   suite = unittest.TestSuite()

   tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide"),TestMathFunc("test_multi")]
   suite.addTests(tests)

   # runner = unittest.TextTestRunner(verbosity=2)
   # runner.run(suite)

   with open('UnittestTextReport.txt', 'a') as f:
       runner = unittest.TextTestRunner(stream=f, verbosity=2)
       runner.run(suite)

