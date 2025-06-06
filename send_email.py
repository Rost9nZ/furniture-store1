import smtplib
from email.mime.text import MIMEText

def send_test_email(to_email):
    smtp_server = 'smtp.mail.ru'
    smtp_port = 587
    username = 'ku.markus@mail.ru'
    password = 'JKrBGDtvSp0HRvvVYpM4'  # пароль приложения

    msg = MIMEText('Тестовое письмо')
    msg['Subject'] = 'Тест'
    msg['From'] = username
    msg['To'] = to_email

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # TLS
        server.login(username, password)
        server.sendmail(username, [to_email], msg.as_string())
        print('Письмо отправлено успешно')
    except Exception as e:
        print('Ошибка:', e)
    finally:
        server.quit()

send_test_email('boch.rost@mail.ru')
