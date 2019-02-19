from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(full_name,receiver,comment):
    # Creating message subject and sender
    subject = 'Thank you'
    sender = 'pythonapps2018@gmail.com'
    comment = '%s %s' %(comment,full_name)

    #passing in the context vairables
    text_content = render_to_string('email/contactemail.txt',{"full_name": full_name})
    html_content = render_to_string('email/contactemail.html',{"full_name": full_name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
