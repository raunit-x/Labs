# Q.9 Write a script to send/receive an e-mail using SMTP protocol.
import smtplib
from email.message import EmailMessage
import imghdr

password = 'í!ÃmÎ#Só}ß¬F§ç³ãSó½¤38Àa'  # Password encrypted using RSA


def get_content():
    msg = EmailMessage()
    msg['Subject'] = "HELLO FROM PYTHON!"
    msg['From'] = 'raunitd.it.17@nsit.net.in'
    msg['To'] = 'raunit88@gmail.com'
    msg.set_content("THIS EMAIL IS GENERATED USING RAUNIT'S PYTHON SCRIPT.")
    with open('/Users/raunit_x/Desktop/cansat.jpeg') as file:
        file_type = imghdr.what(file)
        file_name = file.name
        file_data = file.read()
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
    return msg


def main():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('raunitd.it.17@nsit.net.in', decrypt(password, 'RSA'))
        smtp.send_message(get_content())
        smtp.close()


if __name__ == '__main__':
    main()
