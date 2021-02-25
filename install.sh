mv index.html /var/www/html/
read -p "Enter the emailID of the sender with which you wish to send all your phishing emails from: " email
read -p "Enter the password of that email account: " pass
echo "export EMAILID='$email'" >> ~/.bashrc
echo "export PASS='$pass'" >> ~/.bashrc
source ~/.bashrc
go get -u github.com/tomnomnom/anew

