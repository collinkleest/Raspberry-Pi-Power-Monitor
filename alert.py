# imports
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def getPhones():
    with open(str(os.getcwd()+"/phones.csv")) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        for row in csvReader:
            phone = row[0]
            carrier = row[1]
            name = row[2]
            try:
                sendEmail(phone, carrier, name)
            except:
                pass


def getCarrierAddr(carrier):
    carriers = {
        'verizon': 'vtext.com',
        'att': 'txt.att.net',
        'metro': 'mymetropcs.com',
        'sprint': 'messaging.sprintpcs.com',
        'virgin': 'vmobl.com',
        'tmobile': 'tmomail.net',
        'boost': 'myboostmobile.com',
        'cricket': 'mms.cricketwireless.net',
        'google': 'msg.fi.google.com',
        'uscell': 'email.uscc.net'
    }
    return carriers.get(carrier.lower())


def sendEmail(phone, carrier, name):
    msg = Email(phone, carrier, name)
    s.send_message(msg.constructEmail())

class Email:
    def __init__(self, phone, carrier, name):
        self.phone = phone
        self.carrier = carrier
        self.name = name

    def constructEmail(self):
        email = (str(self.phone) + '@') + (getCarrierAddr(self.carrier))
        finalmessage = (self.name+': \n'+message)
        msg = MIMEMultipart()
        msg['From'] = 'Rajant Alert'
        msg['To'] = str(email)
        msg.attach(MIMEText(str(finalmessage), 'plain'))
        return msg

if __name__=="__main__":
    mailServer = "172.20.0.50"
    message = input()
    s = smtplib.SMTP(host=mailServer, port=25)
    getPhones()
