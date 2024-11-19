import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send_email_with_attachment(smtp_server, port, sender_email, sender_password, recipient_email, subject, body,
                               attachment_name, attachment_content):
    try:
        # 创建邮件对象
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # 添加邮件正文
        message.attach(MIMEText(body, 'plain'))

        # 创建附件
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment_content)
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename="{attachment_name}"'
        )
        message.attach(part)

        # 连接到 SMTP 服务器并发送邮件
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # 启用 TLS 加密
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())

        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")


# 需要配置的邮件参数
smtp_server = "smtp.qq.com"  # 替换为你的 SMTP 服务器
port = 465  # TLS 端口号
sender_email = "xio.work@foxmail.com"
sender_password = "kinoumudkcdedcfj"
recipient_email = "blisssun2010@163.com"
subject = "Test Email with Attachment"
body = "This is a test email with an attachment."
attachment_name = "./task_tracker.log"
attachment_content = "This is the content of the attachment.".encode('utf-8')

if __name__ == "__main__":
    # 发送邮件
    send_email_with_attachment(
        smtp_server, port, sender_email, sender_password, recipient_email,
        subject, body, attachment_name, attachment_content
    )

