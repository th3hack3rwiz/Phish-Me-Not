#!/bin/bash
sudo mv index.html /var/www/html/
chmod +x configure-phishing-simulator.sh
chmod +x retrieve-phished-employee-intel.sh
sudo apt-get install jq
sed -i "s#XXXX#$(pwd)/configure-phishing-simulator.sh#" phish-me-not.py
sed -i "s#YYYY#$(pwd)/retrieve-phished-employee-intel.sh#" phish-me-not.py
read -p "Enter the sender's email-ID. All phishing mails will be sent with this email address: " email
read -s -p "Enter the password of that email account: " pass
if [[ -f ~/.zshrc ]]; then 
        echo "export EMAILID='$email'" >> ~/.zshrc
        echo "export PASS='$pass'" >> ~/.zshrc
        source ~/.zshrc >/dev/null 2>&1
else
        echo "export EMAILID='$email'" >> ~/.bashrc
        echo "export PASS='$pass'" >> ~/.bashrc
        source ~/.bashrc >/dev/null 2>&1
fi
sudo pip3 install xlsxwriter --upgrade 
sudo apt-get install libreoffice
go get -u github.com/tomnomnom/anew
