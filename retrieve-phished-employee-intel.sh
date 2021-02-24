#!/bin/bash
rm results.txt>/dev/null 2>&1
rm ips>/dev/null 2>&1
# rm adminURL >/dev/null 2>&1
# rm victimURL > /dev/null 2>&1
RED='\e[38;5;196m'
GREEN='\e[38;5;46m' 
GOLD='\e[38;5;226m'
GREY='\033[0;37m'
CYAN='\e[38;5;14m'
# echo -e "${RED}${BOLD}$(figlet -f slant  'PHISH-ME-NOT!')"
count=0 
# pingb=$(curl pingb.in 2>&1 | cut -d "\"" -f 2 | xargs | sed "s/.*\//\//g" | xargs -I{} echo {})
url=$(cat adminURL)
# victimURL="http://pingb.in/p$pingb"
# echo ${victimURL} > victimURL
# echo -e "${GOLD}[+] Send this to victim: ${RED}${victimURL}${GOLD}"
while true; do
	 printf "\n"
	 read -p '[?] Press / 1 to REFRESH the LIST / 2 to EXIT: ' user_input 
	 if [ $user_input -eq 1 ]; then
		  count=$((count+1))
		  wget $url --wait=3 -U 'Mozilla/5.0 (X11; Linux i686 (x86_64)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36' --no-http-keep-alive --no-check-certificate --tries=1 -O test1.html > /dev/null 2>&1 
		  cat test1.html | grep -E '([0-9]{1,3}[\.]){3}[0-9]{1,3}' | sed 's/<td>//g' | sed 's/<\/td>//g' | sed 's/^[[:space:]]*//g' | sed 's/:/ /g' | sort -u | anew ips_ports > new_ips_ports ; echo -e "\n${GREEN}[+] Log $(echo $count):" 
		  if [ ! -s results.txt ] ; then
			echo "IP Port Country State City Latitude Longitude Zip_Code Time_Zone ISP Domain Is_Proxy? Proxy_Type" > results.txt
	      fi
		  while read i; do # to fetch only new IPs info
		  	ip=$(echo $i | awk '{print $1}')
		  	port=$(echo $i | awk '{print $2}')
			echo -e "${GREEN}[+] Updating proxy info..."
		  	wget "https://api.ip2proxy.com/?key=demo&ip=${ip}&package=PX10&format=json&&addon=geotargeting" --wait=3 -U 'Mozilla/5.0 (X11; Linux i686 (x86_64)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36' --no-http-keep-alive --no-check-certificate --tries=1 -O test3.html > /dev/null 2>&1

		  	cat test3.html | anew apiProxy > oxy
		  	proxyType=$(cat oxy | awk 'BEGIN{RS=","}{print $0}' | grep -i proxy | sed 's/"//g' | awk -F: '{print $2}' | sed 's/}//g' | xargs | awk '{print $1}') 
		  	isProxy=$(cat oxy | awk 'BEGIN{RS=","}{print $0}' | grep -i proxy | sed 's/"//g' | awk -F: '{print $2}' | sed 's/}//g' | xargs | awk '{print $2}') ; #echo "$proxyType $isProxy"
			echo -e "${GREEN}[+] Updating geo-location and other trivial intel..."
		  	wget "https://api.ip2location.com/v2/?ip=$ip&key=demo&package=WS24&addon=continent,country,region,city,geotargeting,country_groupings,time_zone_info" --wait=3 -U 'Mozilla/5.0 (X11; Linux i686 (x86_64)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36' --no-http-keep-alive --no-check-certificate --tries=1 -O test4.html > /dev/null 2>&1
		  	cat test4.html | anew apiGeo-Location > geo

		  	intel=$(cat geo | jq | grep -E '"country_name":|"city_name":|"zip_code":|"time_zone":|"isp":|"domain":|"region_name"|"latitude"|"longitude"' | sed 's/,//g'  | sed 's/"//g' | awk -F ": " '{print $2}' | sed 's/[[:space:]]/_/g' | xargs)	  	
		    echo "$ip $port $intel $isProxy $proxyType" | anew -q results.txt 
		  done < new_ips_ports
		  printf "\n"
		  cat results.txt | column -t
		  printf '\n' 
	 else rm test1.html >/dev/null 2>&1
	 	  rm test2.html >/dev/null 2>&1
	 	  rm test3.html >/dev/null 2>&1
	 	  rm test4.html >/dev/null 2>&1
	 	  rm new_ips_ports >/dev/null 2>&1
	 	  rm ips_ports >/dev/null 2>&1
	 	  rm geo >/dev/null 2>&1
	 	  rm oxy >/dev/null 2>&1
	 	  rm adminURL >/dev/null 2>&1
 	 	  x=$(cat victimURL)
		  rm victimURL > /dev/null 2>&1
	 	  rm apiGeo-Location > /dev/null 2>&1 
	 	  rm apiProxy > /dev/null 2>&1
		  rm ngrokURL > /dev/null 2>&1
		  rm ngrok.log > /dev/null 2>&1
		  echo -e "\n${RED}[-] Terminating Simulator...${CYAN}"
		  sed -i "s#${x}#REPLACE_ME#g" /var/www/html/index.html
		  killall -9 ngrok &>/dev/null
		  exit
	 fi
done
