import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()


letter = """\
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
"""
referral_link = 'https://dvmn.org/profession-ref-program/linalleks/6tfFI/'
title_website = 'Devman.org'
email_from = 'a_alleks@mail.ru'
email_to = 'linallex@yandex.ru'
friend_name = 'Клим'
sender_name = 'Ангелина'

letter = letter.replace('%website%', referral_link, 1)
letter = letter.replace('%website%', title_website)
letter = letter.replace('%friend_name%', friend_name)
letter = letter.replace('%my_name%', sender_name)
# letter = letter.encode("UTF-8")

msg = MIMEMultipart()
msg['Subject'] = 'Приглашение!'
msg['From'] = email_from
msg['To'] = email_to
msg['Reply-To'] = email_from
msg['Return-Path'] = email_from
msg.attach(MIMEText(letter))

server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.login(os.environ['LOGIN'], os.environ['PASSWORD'])
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()

print(server)
