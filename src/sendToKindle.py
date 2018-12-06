import smtplib,os,sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
print("My kindle tools: Send Files To Kindle Mailbox")
print("Created by Ueino Hakono")
print("v1.0")
try:
    f = open("EmailSetting.txt", "r", encoding="utf-8")
    lines = f.readlines()
    f.close()
except (FileNotFoundError,FileExistsError) as e:
    print("输入用来发送邮件的邮箱地址(sender@example.com)：")
    my_sender = input()
    print("输入邮箱的登陆密码：")
    my_pass = input()
    print("输入邮箱的smtp服务器地址(example.smtp.com)：")
    smtp_server = input()
    print("输入你kindle推送邮箱（youkindle@kindle.com)")
    my_user = input()

    f = open("EmailSetting.txt","w",encoding="utf-8")
    f.writelines([my_sender+'\n',my_pass+'\n',smtp_server+'\n',my_user])
    f.close()
    print()
    print("保存到EmailSetting.txt成功，如果今后需要修改相关y邮箱，可编辑EmailSetting.txt文件")
    print("按回车退出")
    os._exit(0)




my_sender = lines[0].replace("\n","") # 发件人邮箱账号
my_pass = lines[1].replace("\n","") # 发件人邮箱密码
smtp_server = lines[2].replace("\n","")
my_user = lines[3].replace("\n","") # 收件人邮箱账号，我这边发送给自己

print("开始登陆邮箱SMTP...")
print("  ",my_sender)
print("  To:",my_user)
server = smtplib.SMTP_SSL(smtp_server, 465)  # 发件人邮箱中的SMTP服务器，端口是25
server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码

def sendMail(file_path):
    file_name = os.path.basename(file_path)
    msg = MIMEMultipart()
    msg['From'] = formataddr(["tang", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To'] = formataddr(["Kindle", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject'] = file_name  # 邮件的主题，也可以说是标题

    att1 = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1.add_header('Content-Disposition', 'attachment', filename=file_name)
    #att1["Content-Disposition"] = 'attachment; filename="%s"' % file_name
    msg.attach(att1)

    global server
    server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件


send_file_list = []
print("待发送文件：")
for idx,arg in enumerate(sys.argv):
    if idx == 0: continue
    file_path = arg
    print(arg)
    send_file_list.append(arg)
print()
print("开始发送文件")
for idx,file_path in enumerate(send_file_list):
    file_size = os.path.getsize(file_path)/1024/1024

    print("%d/%d正在发送文件...\n  %s\n size:%.1fMB" % (idx+1,len(send_file_list),file_path,
                                                  file_size))
    # if file_size >=25:
    #     print("要发送的文件太大，跳过此文件！")
    #
    try:
        sendMail(file_path)
    except Exception as e :
        print(e)
print("发送完毕！")
input()