from email.mime.text import MIMEText
import smtplib
from . import receive_info
from receive_info import *
# 目标邮箱
mail_to_list = [RECEIVE_ADDR]
# 发件方
me = SEND_ADDR
mail_host = MAIL_HOSR
# 账号
mail_user = MAIL_USER
mail_pass = MAIL_PASSWORD


def send_mail(sub, content):
    try:
        # 内容
        msg = MIMEText(content)
        msg['Subject'] = sub  # 邮件标题
        msg['From'] = me  # 从哪发
        msg['To'] = ';'.join(mail_to_list)
        # 连接邮件服务器
        s = smtplib.SMTP_SSL(mail_host, 465)
        s.connect(mail_host)
        s.login(mail_user, mail_pass)

        # 邮件服务器调试信息
        # s.set_debuglevel(1)

        s.sendmail(me, mail_to_list, msg.as_string())
        s.close()
        print('邮件发送成功')
    except Exception as e:
        print(e)
        # error('Send Email Error', e)
        print('发送失败')


if __name__ == "__main__":
    a = set()
    a.add('a')
    send_mail('Hello', str(a))
