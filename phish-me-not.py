#!/usr/bin/python3
import subprocess
import time
import smtplib
import os
from email.message import EmailMessage
from tkinter import *
from tkinter import filedialog  # import filedialog module
import xlsxwriter

subprocess.call("XXXX")

with open ("ngrokURL","r") as f:	# reading victim_url to include in the mail
	victim_url = f.read()

EMAIL_ADDRESS = os.environ.get('EMAILID')
EMAIL_PASS = os.environ.get('PASS')

print ("\n")
choice = input("[?] Do you want to create an employee-table?(y/n): ")
if choice == 'y':
	root = Tk()
	root.title('Phish-Me-Not')
	root.geometry("430x200+630+350")
	bg= PhotoImage(file="background.png")   #define bg image    

	#create a canvas
	my_canvas = Canvas(root, width=200, height=100, bd=0, highlightthickness=0)
	my_canvas.pack(fill="both", expand=True)

	#set image in canvas
	my_canvas.create_image(0,0, image=bg, anchor="nw")
	my_canvas.create_text(220,80, text="Welcome to", font=("Helvetica", 24,'bold'), fill="white")
	my_canvas.create_text(220,120, text="Phish-Me-Not", font=("Helvetica", 24,'bold'), fill="white")

	def destroy():
		root.destroy()
	root.after(2000, destroy)
	root.mainloop()
	
	root = Tk()
	root.title('Phish-Me-Not')
	root.geometry("430x200+630+350")
	bg= PhotoImage(file="background.png")   #define bg image    

	my_canvas = Canvas(root, width=200, height=100, bd=0, highlightthickness=0)
	my_canvas.pack(fill="both", expand=True)

	#set image in canvas
	my_canvas.create_image(0,0, image=bg, anchor="nw")
	my_canvas.create_text(220,40, text="Enter number of employees:", font=("Helvetica", 16,'bold'), fill="white")



	entry1 = Entry(root, font=("Helvitica",12),width=13, fg="black", bd=0)

	entry1_window = my_canvas.create_window(160,70,anchor='nw', window=entry1)

	def myClick():
	    global noe
	    noe=entry1.get()
	    root.destroy()
	button1=Button(root, text="Done",font=("times",15),width=5,padx=15, pady=7, fg='white', bg='black', bd=0, command=myClick)
	button1_window = my_canvas.create_window(183,120,anchor='nw', window=button1)

	#root.bind('<Configure>',resizer)
	root.mainloop()
	file = open("employee-table.txt", "w")
	global path
	path ='employee-table.txt'
	file.write("Name Email IP_Address Recent_Project\n")
	for i in range(0,int(noe)):
	    root = Tk()
	    root.title('Phish-Me-Not')
	    root.geometry("430x200+630+350")
	    bg= PhotoImage(file="background.png")   #define bg image    
	   
	    #create a canvas
	    my_canvas = Canvas(root, width=200, height=100, bd=0, highlightthickness=0)
	    my_canvas.pack(fill="both", expand=True)

	    #set image in canvas
	    my_canvas.create_image(0,0, image=bg, anchor="nw")
	    my_canvas.create_text(100,25, text="Employee:"+str(i+1), font=("Helvetica", 13,'bold'), fill="white")
	    my_canvas.create_text(100,50, text="Name:", font=("Helvetica", 13,'bold'), fill="white")
	    my_canvas.create_text(100,75, text="Email:", font=("Helvetica", 13,'bold'), fill="white")
	    my_canvas.create_text(100,100, text="IP address:", font=("Helvetica", 13,'bold'), fill="white")
	    my_canvas.create_text(100,125, text="Recent Project:", font=("Helvetica", 13,'bold'), fill="white")
	    
	    entry1 = Entry(root, font=("Helvitica",14),width=20, fg="black", bd=0)
	    entry2 = Entry(root, font=("Helvitica",14),width=20, fg="black", bd=0)
	    entry3 = Entry(root, font=("Helvitica",14),width=20, fg="black", bd=0)
	    entry4 = Entry(root, font=("Helvitica",14),width=20, fg="black", bd=0)

	    entry1_window = my_canvas.create_window(165,35,anchor='nw', window=entry1)
	    entry2_window = my_canvas.create_window(165,60,anchor='nw', window=entry2)
	    entry3_window = my_canvas.create_window(165,85,anchor='nw', window=entry3)
	    entry4_window = my_canvas.create_window(165,110,anchor='nw', window=entry4)
	    
	    def myClick():
	        name=entry1.get()
	        email=entry2.get()
	        ip=entry3.get()
	        project=entry4.get()
	        
	        file.write(name.replace(" ","_"))
	        file.write(" "+email)
	        file.write(" "+ip)
	        file.write(" "+project.replace(" ","_")+"\n")
	        root.destroy()
	    if(int(i)==int(noe)-1):
	        button1=Button(root, text="Finish",font=("times",15),width=5, fg='white', bg='black', bd=0, command=myClick)
	        button1_window = my_canvas.create_window(250,150,anchor='nw', window=button1)
	    else:
	        button1=Button(root, text="Next",font=("times",15),width=5, fg='white', bg='black', bd=0, command=myClick)
	        button1_window = my_canvas.create_window(250,150,anchor='nw', window=button1)
	    
	    #root.bind('<Configure>',resizer)
	    root.mainloop() 
	file.close()
else:
	root = Tk()
	root.title('Phish-Me-Not')
	root.geometry("430x200+630+350")
	bg= PhotoImage(file="background.png")   #define bg image    

	#create a canvas
	my_canvas = Canvas(root, width=200, height=100, bd=0, highlightthickness=0)
	my_canvas.pack(fill="both", expand=True)

	#set image in canvas
	my_canvas.create_image(0,0, image=bg, anchor="nw")
	my_canvas.create_text(220,80, text="Welcome to", font=("Helvetica", 24,'bold'), fill="white")
	my_canvas.create_text(220,120, text="Phish-Me-Not", font=("Helvetica", 24,'bold'), fill="white")

	def destroy():
	  root.destroy()
	root.after(2000, destroy)
	root.mainloop()  
	# Function for opening the 
	# file explorer window

	def browseFiles():
	    global path
	    path = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
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
	my_canvas.create_text(220,60, text='Choose "Employee-Table" Location', font=("Helvetica",18,'bold'), fill="white")
	#label_file_explorer.grid(column = 1, row = 1)

	#button_explore = Button(window, text = "Browse Files", command = browseFiles) 
	button_explore=Button(root, text="Browse Files",font=("times",15),width=5,padx=40, pady=10, fg='white', bg='black', bd=0, command=browseFiles)
	button_explore_window = my_canvas.create_window(150,100,anchor='nw', window=button_explore)

	root.mainloop()

with open (path,"r") as f:
        with open ("employee_table.txt","w+") as w:
                w.write(f.read())

print ("\n")
with open ("employee_table.txt","r") as employee_table:
	email=[]
	name=[]
	ip=[]
	recent_project=[]
	
	for i in employee_table:
		employee_intel = employee_table.readlines()[:]
		for employee in employee_intel:
			name.append(employee.strip().split()[0])
			email.append(employee.strip().split()[1])
			ip.append(employee.strip().split()[2])
			recent_project.append(employee.strip().split()[3])
print ("[+] Sending phishing email to employees...")
for emp in range(len(email)):
	print (f'[+] Sending mail to: {name[emp].replace("_"," ")}')
	msg = EmailMessage()
	msg['Subject'] = "EMPLOYEE BONUS REWARD" #subject
	msg['From'] = EMAIL_ADDRESS
	msg['To'] = email[emp]
	msg.add_alternative("""\
	<!DOCTYPE html>
	<html>
		<body>
		<p>Dear {name},<br><br>On behalf of company's management, I would like to extend our appreciation towards your amazing work on the project <b>{project}</b>. We appreciate your contribution and it is always a pleasure to work with brilliant and dedicated people like you.<br><br>As a sign of our appreciation, we would like to reward you for your dedication towards your work. As part of our new fiscal period, kindly accept the enclosed cheque as a token of appreciation for your praisworthy contributions to the company.<br><br>We are proud to have you onboard. Keep up the good work!<br><br>Regards,<br><br>Dhruv Kandpal<br>Manager<br>Human Resource.<br><br>P.S.-  To view the complete payment details, you may <a href={victim_url}>click here</a>. You are most welcome to contact the HR department to seek any clarification.</p>
		</body>
	</html>
		""".format(victim_url=victim_url,name=name[emp].replace("_"," "),project=recent_project[emp]),subtype='html')

	with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:	
		smtp.login(EMAIL_ADDRESS,EMAIL_PASS)
		smtp.send_message(msg)

subprocess.call("YYYY")
IP = []
Port = []
Country = []
State = []
City = []
Latitude = []
Longitude = []
Zip_Code = []
Time_Zone = []
ISP = []
Domain = []
Is_Proxy = []
Proxy_Type = []
Victim_Employee = []
Geo_URL = []
try:
	with open ("results.txt","r") as results_table:
		for j in results_table:
			result_data=results_table.readlines()[:]
			for phished_employee in result_data:
				try:
					Victim_Employee.append(phished_employee.strip().split()[0])
					IP.append(phished_employee.strip().split()[1])
					Port.append(phished_employee.strip().split()[2])
					Country.append(phished_employee.strip().split()[3])
					State.append(phished_employee.strip().split()[4])
					City.append(phished_employee.strip().split()[5])
					Latitude.append(phished_employee.strip().split()[6])
					Longitude.append(phished_employee.strip().split()[7])
					Zip_Code.append(phished_employee.strip().split()[8])
					Time_Zone.append(phished_employee.strip().split()[9])
					ISP.append(phished_employee.strip().split()[10])
					Domain.append(phished_employee.strip().split()[11])
					Is_Proxy.append(phished_employee.strip().split()[12])
					Proxy_Type.append(phished_employee.strip().split()[13])
					Geo_URL.append(phished_employee.strip().split()[14])
				except IndexError:
					print ("[-] Some information could not be fetched...\nYour API calls have exhausted!")
except FileNotFoundError:
	pass

victims = []
for index,flag_emp in enumerate(IP):
	if flag_emp in ip:
 		victims.append(name[ip.index(flag_emp)].replace("_"," "))
print ("\n[+] The following employees were phished!")
print (str(index+1)+")","\n".join(victims))

data = ["Victim_Employee","IP","Port","Country","State","City","Latitude","Longitude","Zip_Code","Time_Zone","ISP","Domain","Is_Proxy","Proxy_Type","Geo_URL"]
phi_emp_data= []
email_data=str()
dictionary = dict()
try:
	for i in range(len(victims)):
		victims[i]=victims[i].strip()
		print (f'[+] Sending awareness mail to {victims[i]}')
		phi_emp_data.extend([Victim_Employee[Victim_Employee.index(victims[i].replace(" ","_"))],IP[Victim_Employee.index(victims[i].replace(" ","_"))],Port[Victim_Employee.index(victims[i].replace(" ","_"))],Country[Victim_Employee.index(victims[i].replace(" ","_"))],State[Victim_Employee.index(victims[i].replace(" ","_"))],City[Victim_Employee.index(victims[i].replace(" ","_"))],Latitude[Victim_Employee.index(victims[i].replace(" ","_"))],Longitude[Victim_Employee.index(victims[i].replace(" ","_"))],Zip_Code[Victim_Employee.index(victims[i].replace(" ","_"))],Time_Zone[Victim_Employee.index(victims[i].replace(" ","_"))],ISP[Victim_Employee.index(victims[i].replace(" ","_"))],Domain[Victim_Employee.index(victims[i].replace(" ","_"))],Is_Proxy[Victim_Employee.index(victims[i].replace(" ","_"))],Proxy_Type[Victim_Employee.index(victims[i].replace(" ","_"))],Geo_URL[Victim_Employee.index(victims[i].replace(" ","_"))]])
		#print(f'{phi_emp_data}')
		for j in data:
			dictionary[j]=phi_emp_data[data.index(j)]
		for j in dictionary.items():
			email_data+="\n"+str(j).replace(",",":").strip("(").strip(")").replace("\'","").replace("_"," ")+"<br>"
		#print(email_data)	
		msg = EmailMessage()
		msg['Subject'] = "URGENT: YOU HAVE BEEN PHISHED!" #subject
		msg['From'] = EMAIL_ADDRESS
		msg['To'] = email[name.index(victims[i].replace(" ","_"))]
		msg.add_alternative("""\
		<!DOCTYPE html>
		<html>
			<body>
			<p>Dear {name},<br><br>In an effort to further enhance our company’s cyber defenses, a phishing mail was sent to you. The bad news is that you fell prey to it. The good news is that we are here to help you.<br><br><b><i>Although we maintain controls to help protect our networks and computers from cyber threats, we rely on you to be our first line of defense.</i></b><br><br><i><b>With your one wrong click, the following data was leaked.<br><br>{data}<br><br></b>To avoid such phishing schemes in future, please observe the following email best practices:</i><ul><li><b>Do not click on links</b> or <b>attachments</b> from senders that you do not recognize. Be especially wary of .zip or other compressed or executable file types.</li><li><b>Do not provide sensitive personal information</b> (like usernames and passwords) over email.</li><li><b>Watch for email senders</b> that use <b>suspicious or misleading domain names.</b></li><li><b>Inspect URLs carefully</b> to make sure they’re legitimate and not imposter sites.</li><li><b>Do not try to open any shared document</b> that you’re <b>not expecting to receive</b>.</li></ul><br>If you receive an e-mail that <b>you suspect to be a phishing attempt</b>, or if you are <b>unsure of an e-mail’s legitimacy, please do not respond.</b> Remember that <b>our company will never request personal information</b>, usernames, passwords, or money <b>from you via email.</b><br><br>Do not feel demoralized, instead feel happy that now you are much more aware about malicious phishing schemes. Thanks for helping to keep our networks and our people safe from these threats.<br><br>P.S-Call It a <b>reinforcement or awareness drill</b>, no simulated phishing program is complete without supporting content.<br><br>Kindly find the guide attached with this email on <b>how to spot and report suspected phishing attempts</b> to protect yourself and the company from cybercriminals, hackers, and other bad actors.<br><br>Please let us know if you have any questions.<br><br>Regards,<br>th3hack3rw!z<br>HR Head</p>
			</body>
		</html>
			""".format(name=victims[i],data=email_data),subtype='html')

		files = ['phishing_awareness_guide.pdf']
		for j in files:
			with open (j,'rb') as f:
				file_data = f.read()
				file_name = f.name
			#	print(file_type)
			msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

		with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:	
			smtp.login(EMAIL_ADDRESS,EMAIL_PASS)
			smtp.send_message(msg)
		email_data=""
		dictionary.clear()
		phi_emp_data.clear()
except IndexError:
	pass
print ("\n[+] Generating Results")
workbook = xlsxwriter.Workbook('results.xlsx') 
worksheet1 = workbook.add_worksheet() 
bold = workbook.add_format({'bold': 1}) 
  
# create a data list . 
headings1 = ['Name', 'Phished'] 
worksheet1.write_row('A1', headings1, bold)

phishedemp=[]
phishedemp.extend(victims)
for i in range(len(victims)):
    phishedemp[i]=phishedemp[i].replace(' ','_')

i=0
pemp=0
with open(path, "r") as file: 
    emplist = file.readlines()[1:]
    for line in emplist: 
        tmplist = line.rstrip('\n').split(' ') 
        emplist[i]=tmplist
        if emplist[i][0] in phishedemp:
            lst=[emplist[i][0],'YES']
            newlst=[ele.replace('_',' ') for ele in lst if ele]
            worksheet1.write_row('A'+str(i+2), newlst)
            pemp+=1
        else:
            lst=[emplist[i][0],'NO']
            newlst=[ele.replace('_',' ') for ele in lst if ele]
            worksheet1.write_row('A'+str(i+2), newlst)
        i+=1
totalemp=len(name)
typelabel=['Phished','Not phished']
no=[pemp,totalemp-pemp]
per=[str(round((pemp/totalemp)*100,2)),str(round((totalemp-pemp)/totalemp*100,2))]
headings2 = ['Type', 'No. of employees','Percentage'] 
worksheet1.write_row('M1', headings2, bold)
worksheet1.write_column('M2', typelabel)
worksheet1.write_column('N2', no)
worksheet1.write_column('O2', per)

worksheet1.set_column(0, 0, 20)
worksheet1.set_column(12, 12, 12)
worksheet1.set_column(13, 13, 16)
worksheet1.set_column(14, 14, 10)

print ("[+] Generating Pie-chart")
chart = workbook.add_chart({'type': 'pie'})
chart.add_series({'name':'Percentage Phished', 
        'categories': ['Sheet1', 1, 12, 2, 12],   
        'values':     ['Sheet1', 1, 13, 2, 13],
        'data_labels': {'percentage': True}})
chart.set_title({'name': 'Percentage Phished'})
chart.set_style(10)
worksheet1.insert_chart('D1', chart, {'x_offset': 20, 'y_offset': 10})
 
worksheet2 = workbook.add_worksheet() 
bold = workbook.add_format({'bold': 1}) 
  
# create a data list . 
headings = ['Victim Employee', 'IP','Port','Country','State','City','Latitude','Longitude','Zip Code','Time Zone','ISP','Domain','Is_Proxy?','Proxy Type','Geo_URL'] 
worksheet2.write_row('A1', headings, bold) 
  
# Write a column of data starting from 
# A2, B2, C2 respectively. 
worksheet2.set_column(0, 0, 20)
worksheet2.set_column(1, 1, 15)
worksheet2.set_column(4, 4, 13)
worksheet2.set_column(5, 5, 15)
worksheet2.set_column(6, 6, 10)
worksheet2.set_column(7, 7, 10)
worksheet2.set_column(9, 9, 9)
worksheet2.set_column(10, 10, 25)
worksheet2.set_column(11, 11, 20)
worksheet2.set_column(13, 13, 10)
worksheet2.set_column(14, 14, 75)

i=0
try:
	with open("results.txt", "r") as file: 
	    emplist = file.readlines()[1:]
	    for line in emplist: 
	        tmplist = line.strip().split(' ')
	        emplist[i]=tmplist
	        newlst=[ele.replace('_',' ') for ele in tmplist if ele]
	        worksheet2.write_row('A'+str(i+2), newlst)
	        i+=1
except FileNotFoundError:
	pass

workbook.close()
print ("\n[+] Results Generated!")
print ("\n[+] Sending assessment emails to non-phished employees now!")

# Separating IPs of non-phished employees
root = Tk()
root.title('Phish-Me-Not')
root.geometry("430x200+630+350")
bg= PhotoImage(file="background.png")   #define bg image    

my_canvas = Canvas(root, width=200, height=100, bd=0, highlightthickness=0)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0,0, image=bg, anchor="nw")
my_canvas.create_text(220,40, text="Enter the Employee-survey form link:", font=("Helvetica", 16,'bold'), fill="white")

entry1 = Entry(root, font=("Helvitica",12),width=13, fg="black", bd=0)
entry1_window = my_canvas.create_window(160,70,anchor='nw', window=entry1)

def myClick():
	global formlink
	formlink=entry1.get()
	root.destroy()
button1=Button(root, text="Done",font=("times",15),width=5,padx=15, pady=7, fg='white', bg='black', bd=0, command=myClick)
button1_window = my_canvas.create_window(183,120,anchor='nw', window=button1)
root.mainloop()

not_victims = ip.copy()
for flag_emp in IP: # iterating through phished employees again
	if flag_emp in not_victims:
		not_victims.remove(flag_emp)

for emp in not_victims:
	print(f'[+] Sending assessment email to: {name[ip.index(emp)].replace("_"," ")}')
	#print(f'{email[ip.index(emp)].replace("_"," ")}')

	msg = EmailMessage()
	msg['Subject'] = "URGENT: Phishing Simulation Assessment." #subject
	msg['From'] = EMAIL_ADDRESS
	msg['To'] = email[ip.index(emp)]
	msg.add_alternative("""\
	<!DOCTYPE html>
	<html>
		<body>
		<p>Dear {name},<br><br><b>We are happy to inform you that you have cleared the first round of employee phishing training assessment.</b><br><br>To further enhance our company’s cyber defences, a phishing email was sent to you. Simulations go beyond phishing awareness guides and training. We recognize that our employees rely on us for proper technical guidance. To evaluate your performance in the recent phishing-simulation assessment kindly fill the following <a href={form}>mandatory form</a>. <b>This assessment will reflect on the bigger picture of your performance.</b><br><br>If you have any questions, concerns, or feedback, you can direct them to your manager or get in touch with me directly.<br><br>Regards,<br><br>th3hack3rwiz<br>Manager<br>HR Head.<br></p>
		</body>
	</html>
		""".format(name=name[ip.index(emp)].replace("_"," "),form=formlink),subtype='html')

	with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:	
		smtp.login(EMAIL_ADDRESS,EMAIL_PASS)
		smtp.send_message(msg)

#print ("\n[~] Thank you for using Phish-Me-Not!")

time.sleep(1.5)

subprocess.call(['libreoffice','results.xlsx'])
subprocess.call(['python3','employee-survey.py'])
