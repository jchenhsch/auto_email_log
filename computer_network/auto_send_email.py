from auto_email_module import AutoEmail
import datetime as dt
import getpass
import datetime
import mysql_connect as db_update


"""
before running, 
use  netstat -apn|grep 3306 in Linux VM to check if the mysql server is running
0.0.0.0 binding address to make sure every root host can connect
two password entry
1. first one for email authentication
2. second one for database authentication
"""

receivers_dic = {
     'Professor Manfredi': "vumanfredi@wesleyan.edu"
}


a = AutoEmail()
a.from_name = 'Jiaxuan Chen'  

a.from_mail = 'jchenhsch@wesleyan.edu'  

a.from_password =getpass.getpass()
#for cron automation: Use
#a.from_password="Your Password"

a.cc_address = ''

a.bcc_address = ''

a.subject = 'The final project test[cronjob enabled] '  # Subject mail, if empty goes by default

a.body = "Dear %s, This is automated email system. The script will send you emails every minute!" 

#Email Body, %s name of the recipient in the email.



a.enclosure_names = ''#'/Users/james/Desktop/COMP411/icmp_traceroute.png'  # Attachment name

a.enclosure_affirm = 'no'  # Attachment confirmation, if empty goes by default: attach. No attachment needs to assign the value to no

a.schedule_send_time= '' # Schedule send time, if empty goes by default: do not schedule

a.email_undo_timer= 'no' # undo timer, client can undo the send if error, default no

a.send_email(receivers_dic)  # Send the email

send_time=datetime.datetime.now()

#  write the scheduled sent time 

# if a.schedule_send_time != send_time:
#       send_time=a.schedule_send_time

# update the database
db_update.update_mysql_email_log(a.from_name,a.subject,str(receivers_dic),send_time)

# log for the init_cron_lst.py. Everytime we runs the auto_send_email.py, it autosends the email. 

# with open('append.txt', 'a') as myFile:
#     print("append file opened")
#     myFile.write('\nAccessed on ' + str(datetime.datetime.now()))
