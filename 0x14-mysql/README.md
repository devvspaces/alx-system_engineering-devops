# MySQL management

## Install MySQL 5.7.x

```bash
wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb
-- Select Ubuntu Bionic
-- select the MySQL Server & Cluster option. Then, select mysql-5.7 and finally select Ok.
sudo apt update
-- If you encounter the 'NO_PUBKEY 467B942D3A79BD29' then run the command below:
-- sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 467B942D3A79BD29
sudo apt update -- again
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*
mysql --version
```

## Create User holberton_user with hostname localhost and password projectcorrection280hbtn

```sql
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
```

## Make sure that holberton_user has permission to check the primary/replica status of your databases

```sql
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
```

## Create a database named tyrell_corp

```sql
CREATE DATABASE IF NOT EXISTS tyrell_corp;

CREATE TABLE IF NOT EXISTS tyrell_corp.nexus6 (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO tyrell_corp.nexus6 (name) VALUES ('Leon');
INSERT INTO tyrell_corp.nexus6 (name) VALUES ('Michael');
```

## Create replica_user

- replica_user must have the appropriate permissions to replicate your primary MySQL server.
- holberton_user will need SELECT privileges on the mysql.user table in order to check that replica_user was created with the correct permissions.

```sql
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'root';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
```

mysql> SHOW MASTER STATUS;
+------------------+----------+--------------+------------------+-------------------+
| File             | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+------------------+----------+--------------+------------------+-------------------+
| mysql-bin.000001 |      154 |              |                  |                   |
+------------------+----------+--------------+------------------+-------------------+
1 row in set (0.00 sec)


## Set slave to talk to master

```sql
CHANGE MASTER TO
MASTER_HOST='3.85.168.234',
MASTER_USER='replica_user',
MASTER_PASSWORD='root',
MASTER_LOG_FILE='mysql-bin.000001',
MASTER_LOG_POS=154;
```