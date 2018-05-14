from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit
import imghdr
import smtplib
from email.message import EmailMessage
import getpass

class ShareButtonWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.my_lineedit = QLineEdit("Enter Email")

        self.my_lineedit.selectAll()

        my_layout = QVBoxLayout()
        my_layout.addWidget(self.my_lineedit)
        self.setLayout(my_layout)

        self.my_lineedit.setFocus()
        self.my_lineedit.returnPressed.connect(self.sendEmail)

        self.show()

    def sendEmail(self):
        email = self.my_lineedit.text()
        self.close()
        try:
          server = smtplib.SMTP('smtp.gmail.com', 587)
          server.ehlo()
        except:
          print("Something went wrong")

        # make connection secure
        server.starttls()

        mypwd = getpass.getpass('Enter your password: ')

        my_email = "artengine01@gmail.com"

        msg = EmailMessage()
        msg['Subject'] = "Your new image!"
        msg['From'] = my_email
        msg['To'] = email

        with open('Images/lol.png', 'rb') as fp:
            img_data = fp.read()


        msg.add_attachment(img_data, maintype='image', subtype=imghdr.what(None,img_data))

        server.login(my_email, mypwd)

        server.send_message(msg)
        server.quit()
