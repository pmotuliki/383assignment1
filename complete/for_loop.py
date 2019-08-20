
import os
# read the csv file exp file:csv_example new csv file:csv_examples
import csv
import random,string
import pandas as pd

with open('StudentData.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        # create empty list
        list_of_students = []
        # for each student, append as list to list (list of lists)
        for row in reader:
                list_of_students.append(row)
                # Remove metadata from top row
        list_of_students.pop(0)
n=10000
m=1000000
num=len(list_of_students)
s = string.ascii_lowercase
adr=[]
pas=[]
for i in random.sample(range(1,n),n-1):
    if len(str(i))>=4 and len(adr)<num:
        adr.append(str(i)+random.choice(s))
for i in random.sample(range(1,m),m-1):
    if len(str(i))>=6 and len(pas)<num:
        pas.append(str(i))
data = pd.read_csv(r'StudentData.csv')
data1 = adr
data2 = pas
data['moodle_name'] = data1
data['password'] = data2
data.to_csv(r"StudentDatas.csv",mode = 'a',index =False)

with open('StudentDatas.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        # create empty list
        list_of_students = []
        # for each student, append as list to list (list of lists)
        for row in reader:
                list_of_students.append(row)
                # Remove metadata from top row
        list_of_students.pop(0)







# find external ip
r = os.popen("curl ifconfig.me")
ip = r.read()
r.close()

conn = pymysql.connect(host='127.0.0.1',port=3306, user='debian-sys-maint',passwd="lO5k3KdhTU0LoEey")
cursor=conn.cursor()





for i in list_of_students:
        SQLcmd1=cursor.execute("create database student%s default character set utf8 collate utf8_general_ci;",i[0])
        SQLcmd3=cursor.execute(" create user student%s@'%%' identified by %s;",(i[0],i[3]))
        SQLcmd4=cursor.execute("GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,CREATE TEMPORARY TABLES,DROP,INDEX,ALTER ON student%s.* TO student%s@'%%' IDENTIFIED BY %s;",(i[0],i[0],i[3]))
        SQLcmd6=cursor.execute("flush privileges;")
conn.commit()
cursor.close()
conn.close()

password=[]
for i in range(100000,999999):
    password.append(i)
password=random.sample(password,len(list_of_students))

for i in list_of_students:
        os.system("sudo cp -R /opt/moodle /var/www/html/"+str(i[0]))


        os.chdir("/var")
        if os.path.exists("data"+str(i[0])):
            print("exits")
        else:

            os.system("mkdir data"+str(i[0]))
            os.chdir("/var/www/html/")

            os.system("sudo chown -R www-data /var/data"+str(i[0]))
            os.system("sudo chmod -R 777 /var/data"+str(i[0]))
            os.chdir("/var/www/html/")
            os.chmod(str(i[0]),777)
            os.chdir(str(i[0]))
            if os.path.isfile("config.php"):
                    os.system("rm -rf config.php")

            os.system("touch config.php ")
            data="<?php  // Moodle configuration file\n" \
                    "unset($CFG);\n" \
                    "global $CFG;\n" \
                    "$CFG = new stdClass();\n" \
                    "$CFG->dbtype    = 'mysqli';\n" \
                    "$CFG->dblibrary = 'native';\n" \
                    "$CFG->dbhost    = 'localhost';\n" \
                    "$CFG->dbname    = 'student"+str(i[0])+"';\n" \
                    "$CFG->dbuser    = 'student"+str(i[0])+"';\n" \
                    "$CFG->dbpass    = '"+str(i[5])+"';\n" \
                    "$CFG->prefix    = 'mdl_';\n" \
                    "$CFG->dboptions = array (\n" \
                    "  'dbpersist' => 0,\n" \
                    "  'dbport' => '',\n" \
                    "  'dbsocket' => '',\n" \
                    "  'dbcollation' => 'utf8mb4_unicode_ci',\n" \
                    ");\n" \
                    "$CFG->wwwroot   = 'http://"+str(ip)+"/"+str(i[4])+"';\n" \
                    "$CFG->dataroot  = '/var/moodledata';\n" \
                    "$CFG->admin     = 'admin';\n" \
                    "$CFG->directorypermissions = 0777;\n" \
                    "require_once(__DIR__ . '/lib/setup.php');\n"
            content = data
            file = open('config.php', "w")
            file.write(content)
            file.close()

            os.system("useradd -m"+student[0])
            os.system("echo "+student[0]+":"+password[i]+"| chpasswd")
            os.system("chown -R " + student[0] + ":" + student[0] + "/var/www/html/" + student[5])
            os.system("chmod -R 777 /home/"+student[0])
            os.system("touch /etc/userconfig/"+student[0])
            user = open("/etc/userconfig/"+student[0], "w")
            user.write("local_root=/var/www/html/"+student[5])
            user.close()
            i=i+1


            #send an email with user login info
            message = MIMEMultipart("alternative")
            message["Subject"] = "Moodle account information"
            message["From"] = sender_email
            message["To"] = str(i[3])


            text = """\
                    Subject: Your Login info
            
                    Username: """ + 'student'+str(i[0]) + """
                    Password: """ + str(i[5]) + """
                    Access your Moodle site through this URL: """+'http://'+str(ip)+'/'+str(i[4])

            part1 = MIMEText(text, "plain")
            message.attach(part1)
            # Create secure connection with server and send email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(
                            sender_email, str(i[3]), message.as_string()
            )
