#!/bin/bash
clear
rm -f results.txt > /dev/null 2>&1
rm -f ips > /dev/null 2>&1
rm -f results.xlsx > /dev/null 2>&1
RED='\e[38;5;196m'
GREEN='\e[38;5;46m' 
GOLD='\e[38;5;226m'
GREY='\033[0;37m'
echo -e "${GOLD}${BOLD}$(figlet -f slant  PHISH-ME-NOT!)"
echo -e "${RED}${BOLD}\t\t\t\t-Employee Phishing Simulator."
echo -e "${GREEN}[+] Starting Apache server"
service apache2 start
echo -e "${GREEN}[+] Hosting the local server on the internet through NGROK"
ngrok tcp 80 --log=stdout >log & sleep 7 >/dev/null 2>&1  
cat log| grep url= | awk -F "=" '{print $8}' >ngrokURL
rm -f log
sed -i 's/tcp:/http:/g' ngrokURL
if [ ! -s ngrokURL ]; then
        echo -e "${RED}[-] NGROK operation failed! :( Try again."
        disown
	sudo killall -9 ngrok &>/dev/null
        rm -f ngrokURL
        exit 1
fi
echo -e "${GREEN}[+] Creating a unique pingB URL and embedding it inside an iframe in index.html file."
pingb=$(curl pingb.in 2>&1 | cut -d "\"" -f 2 | xargs | sed "s/.*\//\//g" | xargs -I{} echo {})

if [ -z $pingb ]; then
echo -e "${RED}[-] Failed to create a unique phishing URL! :( Try again."
sudo killall -9 ngrok &>/dev/null
exit 1
fi

url="http://pingb.in$pingb"
victimURL="http://pingb.in/p$pingb"
echo ${url} > adminURL
echo $victimURL > victimURL
sudo sed -i "s#REPLACE_ME#${victimURL}#g" /var/www/html/index.html
