from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

email = '#####'
senha = '####'

with open('template.html', 'r') as html: # abrindo o html para ler no python
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.safe_substitute(nome='####', data=data_atual)

msg = MIMEMultipart()
msg['from'] = '#####'
msg['to'] = email # estou recebendo no meu email
msg['subject']= 'Atenção, e-mail de teste com PYTHON'

corpo = MIMEText(corpo_msg, 'html') #colocando o html buscado do template
msg.attach(corpo)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp: # porta do provedor de email/ Isso são as configs do email e a segurança
    smtp.ehlo() #metodo para enviar msg
    smtp.starttls() #segurança do gmail
    smtp.login(email, senha) # meu email
    smtp.send_message(msg)
    print('Email enviado com sucesso')

