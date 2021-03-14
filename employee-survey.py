#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
import smtplib
import os
from email.message import EmailMessage
from tkinter import *
from tkinter import filedialog  # import filedialog module

EMAIL_ADDRESS = os.environ.get('EMAILID')
EMAIL_PASS = os.environ.get('PASS')

with open('employee-table.txt', 'r') as employee_table:
    email = []
    name = []
    ip = []
    recent_project = []

    for i in employee_table:
        employee_intel = employee_table.readlines()[:]
        for employee in employee_intel:
            name.append(employee.strip().split()[0])
            email.append(employee.strip().split()[1])
            ip.append(employee.strip().split()[2])
            recent_project.append(employee.strip().split()[3])


def browseFiles():
	global pathcsv
	pathcsv = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("CSV files", "*.csv*"), ("all files", "*.*")))
	root.destroy()

root = Tk()
root.title('Select file')
root.geometry("430x200+630+350")
bg= PhotoImage(file="background.png")    

#create a canvas
my_canvas = Canvas(root, width=200, height=100, bd=0, highlightthickness=0)
my_canvas.pack(fill="both", expand=True)

#set image in canvas
my_canvas.create_image(0,0, image=bg, anchor="nw")
  
# Create a File Explorer label
#label_file_explorer = Label(root, text = "", width = 100, height = 4, fg = "blue")
my_canvas.create_text(220,60, text='Choose "Feedback file" Location', font=("Helvetica",18,'bold'), fill="white")
#label_file_explorer.grid(column = 1, row = 1)

#button_explore = Button(window, text = "Browse Files", command = browseFiles) 
button_explore=Button(root, text="Browse Files",font=("times",15),width=5,padx=40, pady=10, fg='white', bg='black', bd=0, command=browseFiles)
button_explore_window = my_canvas.create_window(150,100,anchor='nw', window=button_explore)

root.mainloop()

emailID = []
mcq_score = []
try:
	with open(pathcsv) as csvfile:
	    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	    line_count = 0
	    for row in csv_reader:
	        if line_count == 0:
	            line_count += 1
	            continue
	        else:
	            emailID.append(row[1])
	            mcq_score.append(row[2])
except NameError:
    print ("[+] Feedback file not selected!")
    exit()
pass_emp_email = []
fail_emp_email = []
for i in range(len(emailID)):
    a=mcq_score[i]
    b,c=a.strip().strip("\"").split("/")
    outcome=int(float(b)/float(c))

    if outcome == 1:
        pass_emp_email.append(emailID[i].strip("\""))
    else:
        fail_emp_email.append(emailID[i].strip("\""))

print ("\n[+] Sending appreciation emails!")
for i in pass_emp_email:
	print (f'[+] Sending appreciation email to: {name[email.index(i)].replace("_"," ")} ')
	msg = EmailMessage()
	msg['Subject'] = "Feedback: Phishing Simulation Assessment." #subject
	msg['From'] = EMAIL_ADDRESS
	msg['To'] = i
	msg.add_alternative("""\
	<!DOCTYPE html>
	<html>
		<body>
		<p>Dear {name},<br><br><b>Congratulations on clearing the final stage of phishing simulation!</b><br><br>I am writing to you to let you know that we are exceedingly satisfied with your performance in employee phishing training assessment. You deserve this token of appreciation for your sincere participation.<br><br>Keep up the good work!<br><br>Regards,<br><br>th3hack3rwiz<br>HR Head.<br></p>
		</body>
	</html>
		""".format(name=name[email.index(i)].replace("_"," ")),subtype='html')
	
	with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:	
		smtp.login(EMAIL_ADDRESS,EMAIL_PASS)
		smtp.send_message(msg)

	
print ("\n[+] Sending awareness email to employeed who failed the test!")
for j in fail_emp_email:
	print(f'[+] Sending awareness email to: {name[email.index(j)].replace("_"," ")}')	
	msg = EmailMessage()
	msg['Subject'] = "Feedback: Phishing Simulation Assessment." #subject
	msg['From'] = EMAIL_ADDRESS
	msg['To'] = j
	msg.add_alternative("""\
	<!DOCTYPE html>
	<html>
		<body>
		<p>Dear {name},<br><br>In an effort to further enhance our company’s cyber defenses, a phishing mail was sent to you. <b>The bad news is that you were not able to meet the criterion to pass the phishing simulation assessment.</b> The good news is that we are here to help you.<br><br><b>Although we maintain controls to help protect our networks and computers from cyber threats, we rely on you to be our first line of defense.</b><br><br><i>To avoid such phishing schemes in future, please observe the following email best practices:</i><br><ul><li><b>Do not click on links</b> or <b>attachments</b> from senders that you do not recognize. Be especially wary of .zip or other compressed or executable file types.<li><b>Do not provide sensitive personal information</b>(like usernames and passwords) over email.<li><b>Watch for email senders</b> that use <b>suspicious or misleading domain names.</b><li><b>Inspect URLs carefully</b> to make sure they’re legitimate and not imposter sites.<li><b>Do not try to open any shared document</b> that you’re <b>not expecting to receive.</b></ul><br><br>If you receive an e-mail that <b>you suspect to be a phishing attempt</b>, or if you are <b>unsure of an e-mail’s legitimacy, please do not respond</b>. Remember that <b>our company will never request personal information</b>, usernames, passwords, or money <b>from you via email.</b><br><br>Don't feel demoralized, instead feel happy that now you are much more aware about malicious phishing schemes. Thanks for helping to keep our networks and our people safe from these threats.<br><br>P.S- Call It a <b>reinforcement or awareness drill</b>, no simulated phishing program is complete without supporting content.<br><br> Do read the attached phishing prevention guide!<br><br>Regards,<br><br>ABC<br>HR Head.<br></p>
		</body>
	</html>
		""".format(name=name[email.index(j)].replace("_"," ")),subtype='html')

	files = ['phishing_awareness_guide.pdf']
	for j in files:
		with open (j,'rb') as f:
			file_data = f.read()
			file_name = f.name
		msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

	with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:	
		smtp.login(EMAIL_ADDRESS,EMAIL_PASS)
		smtp.send_message(msg)

width = 169
print("\n")
print ('Thank you for using Phish-Me-Not'.center(width, '-'))
