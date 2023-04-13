#!/Users/james/opt/anaconda3/bin/python

# Running instruction: sudo init_cron_job_lst.py
# ! Full disk access needs to be turned on in order to make cronjob work
# shift-command-G to go to folder usr/sbin/cron
# and pull cron into Full disk access to allow it to execute python script
# All file and python used has to be absolute file address 
# Doesn't work well with getpass.getpass() [user prompted password]


# ! Set up the crontab module
# Be sure to pip3 install python-crontab DO NOT INSTALL crontab
# Make sure you are in the right env
# If you get an error message like "got an unexpected keyword argument 'user'"
# wrong module installed !

# Basic crontab command
# crontab -l --> list the scheduled jobs 
# crontab -r --> remove all scheduled jobs
# sudo crontab -u [user] -r remove the user's scheduled jobs 

# Be careful of using Mac built in username vs. root
# root may still run cronjob while you perform crontab -r for your username account
# always check root cron is all terminated or not

from crontab import CronTab
import time
import datetime

# Create the crontab object
cron = CronTab(user='Jiaxuan Chen')

# Remove all the previous residual jobs in the cron for the user
cron.remove_all()

# Set up a new job to run the auto_send_email.py every minute
# redirect the output of cron to be safe !
job  = cron.new(command= '/Users/james/opt/anaconda3/bin/python /Users/james/Desktop/COMP411/computer_network/auto_send_email.py >> /Users/james/Desktop/COMP411/computer_network/log.txt ')
#print (job)
job.minute.every(1)


# Write and activate the task
cron.write()
job.enable()
#job.run()

#Verify the job status
print("Automated Job enabled ?", job.is_enabled())

# you may use crontab -r to remove the scheduled email task manually

#reset the log file
with open('log.txt', 'w') as myFile:
          myFile.truncate(0)

# with open('append.txt', 'w') as myFile:
#           myFile.truncate(0)


# with open('append.txt', 'a') as myFile:
#     print("append file opened")
#     myFile.write('\nAccessed on ' + str(datetime.datetime.now()))

#Stop after 2 automation for our purposes and remove the job from cron
# time.sleep(120)
# cron.remove(job)

