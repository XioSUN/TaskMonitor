import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from xmlrpc.client import SERVER_ERROR

# 需要配置的邮件参数
SMTP_SERVER = "smtp.qq.com"  # 替换为你的 SMTP 服务器
SMTP_PORT_SSL = 465  # TLS 端口号
SMTP_PORT_TLS = 587  # TLS 端口号
SENDER_EMAIL = "xio.work@foxmail.com"
SENDER_PASSWORD = "kinoumudkcdedcfj"
RECIPIENT_EMAIL = "xio.work@foxmail.com"
EMAIL_SUBJECT = "Test Email with Attachment"
EMAIL_BODY = "This is a test email with an attachment."
ATTACHMENT_PATH = "./task_tracker.log"
ATTACHMENT_NAME = "task_tracker.log"

def test_smtp_connection():
    # 测试 SSL 连接
    try:
        print(f"尝试连接 SMTP 服务器 (SSL: {SMTP_PORT_SSL})...")
        server_ssl = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT_SSL)
        print("SSL 连接成功！")
        server_ssl.quit()
    except Exception as e:
        print(f"SSL 连接失败: {e}")

    # 测试 TLS 连接
    try:
        print(f"\n尝试连接 SMTP 服务器 (TLS: {SMTP_PORT_TLS})...")
        server_tls = smtplib.SMTP(SMTP_SERVER, SMTP_PORT_TLS)
        server_tls.starttls()  # 开启 TLS
        print("TLS 连接成功！")
        server_tls.quit()
    except Exception as e:
        print(f"TLS 连接失败: {e}")

def test_smtp_login():
    # 测试 SMTP 登录
    try:
        print(f"\n尝试使用 SMTP 登录...")
        server_ssl = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT_SSL)
        server_ssl.login(SENDER_EMAIL, SENDER_PASSWORD)
        print("SMTP 登录成功！")
        server_ssl.quit()
    except smtplib.SMTPAuthenticationError:
        print("SMTP 登录失败：请检查邮箱账号和授权码是否正确！")
    except Exception as e:
        print(f"SMTP 登录失败: {e}")

def send_email_with_attachment(smtp_server=SMTP_SERVER, port=SMTP_PORT_TLS, sender_email=SENDER_EMAIL,
                               sender_password=SENDER_PASSWORD, recipient_email=RECIPIENT_EMAIL,
                               subject=EMAIL_SUBJECT, body=EMAIL_BODY,
                               attachment_path=ATTACHMENT_PATH, attachment_name=ATTACHMENT_NAME):
    try:
        # 创建邮件对象
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # 添加邮件正文
        message.attach(MIMEText(body, 'plain'))

        if not os.path.exists(attachment_path):
            print(f"attachment not exist: {attachment_path}")
            return

        with open(attachment_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
        encoders.encode_base64(part)

        part.add_header(
            'Content-Disposition',
            f'attachment; filename="{attachment_name}"'
        )
        message.attach(part)

        # 连接到 SMTP 服务器并发送邮件
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # 启用 TLS 加密
            # server.set_debuglevel(1)    # 开始服务器的debug日志，用于问题定位
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
            server.quit()   # QQ的SMTP服务器在成功发送邮件后返回了非标准的响应，可以通过手动调用quit来规避

        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")


if __name__ == "__main__":
    # 测试 SMTP 连接和登录
    print("测试 QQ SMTP 服务可用性：")
    test_smtp_connection()
    test_smtp_login()

    # 完整测试：发送带有附件的邮件
    send_email_with_attachment(
        SMTP_SERVER, SMTP_PORT_TLS, SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL,
        EMAIL_SUBJECT, EMAIL_BODY, ATTACHMENT_PATH, ATTACHMENT_NAME
    )
