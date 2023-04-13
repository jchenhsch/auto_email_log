from email.utils import parseaddr, formataddr
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import datetime as dt
import time
from dateutil import parser
import smtplib


class AutoEmail:
    def __init__(self):
        self.from_name = 'default'
        self.from_mail = ''
        self.from_password = ''
        self.to_address = ''
        self.sender_name = ''
        self.cc_address = ''
        self.bcc_address= ''
        self.subject = 'default subject'
        self.body = '%s default body text'
        self.enclosure_names = 'attachment%s.txt'
        self.enclosure_affirm = '' 
        self.schedule_send_time=''
        self.email_undo_timer=''

    def __set_send(self):
        smt_set = smtplib.SMTP('smtp.office365.com', port=587)
        try:
            smt_set.starttls()
            smt_set.login(self.from_mail, self.from_password)
            #print("here")
        except:
            print('Account authentication failed')
            return '001'
        from_address = self.__format_address(self.from_name+'<'+self.from_mail)
        msg = MIMEMultipart()
        msg['Subject'] = self.subject
        msg['From'] = from_address
        msg['Cc']  = self.__format_address(self.cc_address)
        msg['Bc'] = self.__format_address(self.bcc_address)
        msg['To'] = self.to_address
        msg.attach(MIMEText(self.body,'plain','utf-8'))
        if self.enclosure_affirm == '':
            try:
                for enclosure in self.enclosure_names.split(';'):
                    enclosure_name = enclosure
                    enclosure = MIMEApplication(open(enclosure_name, 'rb').read())
                    enclosure.add_header('content-disposition', 'attachment', filename=('gbk', '', enclosure_name))
                    msg.attach(enclosure)
            except:
                print('Attachment setting failed')
                return '002'
        print("sending")
        smt_set.sendmail(from_address, self.to_address.split(',') + self.cc_address.split(',')+self.bcc_address.split(","), msg.as_string())
        smt_set.quit()

    def send_email(self, to_addresses):
        if to_addresses == {}:
            print('please add recipients')
        else:
            i = 1
            body = self.body
            for name, addresses in to_addresses.items():
                self.sender_name = name
                try:
                    self.body = body % self.sender_name
                except:
                    print('email body parsing needs to contain %s')
                    return
                self.to_address = self.__format_address(addresses)
                print('Sending No.%d email to %s' % (i,self.sender_name))
                if self.schedule_send_time != '':
                    wait_time=self.date_difference()
                    print(wait_time)
                    time.sleep(wait_time)
                key = self.__set_send()
                
                if key == '001':
                    print('Account authentication failed')
                    break
                elif key == '002':
                    print('Attachment setting failed')
                    break
                else:
                    print('Sent successfully')
                i += 1
    
    def date_difference(self):
        #print(self.schedule_send_time)
        now_time=dt.datetime.now()
        #send_time=dt.datetime.strptime(self.schedule_send_time,'%y-%m-%d %H:%M:%S.%f')
        send_time= parser.parse(self.schedule_send_time)

        if send_time<= now_time:
            print("scheduled time seems not correct")
            usr_decide=input("proceed to S[end] now or Press any keys and enter a new time")
            if usr_decide =="S":
                return 0
            else:
                self.schedule_send_time=input("please enter the new time")
                self.date_difference(self)
                 
        return round((send_time-now_time).total_seconds())



    def __format_address(self, addr):
        addresses_str = ''
        for address in addr.split(';'):
            name, addr = parseaddr(address)
            if addresses_str == '':
                addresses_str = formataddr((Header(name, 'utf-8').encode(), addr))
            else:
                addresses_str = ','.join((formataddr((Header(name, 'utf-8').encode(), addr)), addresses_str))
        return addresses_str
