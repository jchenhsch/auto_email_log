# Data base connector, send files to the mysql database in my virtual machine
import pymysql as psql
import getpass
import datetime

def update_mysql_email_log(name,topic,recipient, send_time):

    #pin=getpass.getpass()
    pin="" # since the MySQL is using skip-grant-table, no password needed to access the mysql
    conn = psql.connect(host='', user='root', password=pin, charset='utf8', db='autoemail') # Your host
    cur = conn.cursor()
    print("connection succeeded")

    sql = """INSERT INTO `email_log` (name, topic, recipient,send_time)
            VALUES (%s, %s, %s, %s) 
    """
    cur.execute(sql,(name,topic,recipient,send_time))
    conn.commit()
    print("updated")

#id=2
# name="James"
# topic="How are you?"
# send_time=datetime.datetime.now()

# update_mysql_email_log(name,topic,send_time)
