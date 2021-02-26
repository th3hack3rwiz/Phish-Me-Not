#!/bin/bash
sudo mv index.html /var/www/html/
chmod +x configure-phishing-simulator.sh
chmod +x retrieve-phished-employee-intel.sh
sudo apt get install jq
sed -i "s#XXXX#$(pwd)/configure-phishing-simulator.sh#" phish-me-not.py
sed -i "s#YYYY#$(pwd)/retrieve-phished-employee-intel.sh#" phish-me-not.py
read -p "Enter the sender's email-ID. All phishing mails will be sent with this email address: " email
read -p "Enter the password of that email account: " pass
echo "export EMAILID='$email'" >> ~/.bashrc
echo "export PASS='$pass'" >> ~/.bashrc
echo "export EMAILID='$email'" >> ~/.zshrc
echo "export PASS='$pass'" >> ~/.zshrc
source ~/.bashrc
go get -u github.com/tomnomnom/anew
