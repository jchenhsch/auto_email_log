/* MYSQL-DATABASE: email_log_autosend
Table: email_log
Access: Through Python script mysql_connect.py (remote connection)
To connect to MYSQL locally in Linux Virtual Machine (local connection)

Use mysql -u root -p
*ENTER YOUR PASSWORD*

***** Security warning ****

To ensure the Navicat (mysql dbadmin tool) can remotely connect to Linux server

GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'ADMIN_PASSWORD';
FLUSH PRIVILEGES;

all root users have been granted the access to database


to modify use  ->sudo nano mysqld.cnf in /etc/mysql/mysql.conf.d and uncomment the listening port
and change back to 127.0.0.1 (localhost)
-> service mysql restart. # restart mysql to save configuration changes

skip-grant-tables also being used to skip authentication steps in NAVICAT connection to db.

*/

 CREATE TABLE email_log (
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR ( 255 ) DEFAULT NULL,
	`topic` VARCHAR ( 255 ) DEFAULT NULL,
    `recipient` VARCHAR ( 255 ) DEFAULT NULL,
	`send_time` DATE DEFAULT NULL,
PRIMARY KEY ( `id` ) 
) ENGINE = INNODB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8;




