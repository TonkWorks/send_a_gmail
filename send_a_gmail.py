#!/usr/bin/env python

import argparse



#Script Info goes here.
__info__ = {
    'title': "Send a gmail",
    'description': "Send a gmail",
    'url': "http://github.com/TonkWorks/send_a_gmail/archive/master.zip",
    'input': [
    {
        'label': 'Youtube URL',
        'type': 'text',
        'map': 'youtube_url',
    }
    ]

}


#And the actual script.
def script():
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.MIMEBase import MIMEBase
    from email import Encoders
    import smtplib

    parser=argparse.ArgumentParser()
    parser.add_argument('--username')
    parser.add_argument('--password')
    parser.add_argument('--subject')
    parser.add_argument('--sender')
    parser.add_argument('--recipient')
    parser.add_argument('--body')
    args=parser.parse_args()


    msg = MIMEMultipart('alternative')
    msg['Subject'] = args.subject
    msg['From'] =  args.sender
    msg['To'] = args.recipient

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(args.body, 'plain')
    part2 = MIMEText(args.body, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(args.username, args.password)
    server.sendmail(sender, recipient,  msg.as_string())
    server.quit()


if __name__ == '__main__':
    script()


