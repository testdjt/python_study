# 发送邮件的模块
import smtplib
# 定义邮件内容
from email.mime.text import MIMEText
# 定义邮件标题
from email.header import Header
import random


def send_mail(mail, randoms):
    # 发送邮箱的服务器
    smtpsever = 'smtp.qq.com'
    # 邮箱的账号授权码
    user = '70469793@qq.com'
    password = ''
    # 用来发送的邮箱
    sender = '70469793@qq.com'
    # 用来接收的邮箱，需要用户输入
    receive = mail
    # 发送的主题和内容
    subject = '您的验证码'
    content = randoms
    # html正文
    msg = MIMEText(content, "html", "utf-8")
    msg["Subject"] = Header(subject, 'utf-8')
    # SSL端口是465
    smtp = smtplib.SMTP_SSL(smtpsever, 465)
    # 向服务器标识用户身份
    smtp.helo(smtpsever)
    # 服务器返回结果确认
    smtp.ehlo(smtpsever)
    # 登录邮箱的账号和密码
    smtp.login(user, password)
    # 发送邮件
    smtp.sendmail(sender, receive, msg.as_string())
    smtp.quit()


def mail_login():
    flag = 0
    while flag == 0:
        try:
            mail = input("请输入您的邮箱\n")
            print("验证码尝试发送您邮箱，请等待。。。")
            randoms = str(random.randint(1, 99999))
            send_mail(mail, randoms)
            mailyanzheng = str(input("输入您收到的验证码"))
            while True:
                if mailyanzheng == randoms:
                    print('验证码输入正确,登录成功')
                    flag = 1
                    break
                else:
                    n = input("输入错误，请重新输入")
                    if n == randoms:
                        print("登录成功")
                        flag = 1
                        break
        except:
            print("您的邮箱输入错误，请输入正确的邮箱")
            pass


mail_login()

