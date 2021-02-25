mv index.html /var/www/html/
read -p "Enter the sender's email-ID. All phishing mails will be sent with this email address: " email
read -p "Enter the password of that email account: " pass
echo "export EMAILID='$email'" >> ~/.bashrc
echo "export PASS='$pass'" >> ~/.bashrc
source ~/.bashrc
go get -u github.com/tomnomnom/anew

