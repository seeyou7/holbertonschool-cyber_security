# ACTIVE INFORMATION GATHERING TOOLS

## Overview
This README outlines the purpose, commands, and uses of active information gathering tools. Active reconnaissance is critical in cybersecurity to identify potential vulnerabilities and gather intelligence on a target system or network.

---

## Table of Contents
1. [What is a Ping?](#what-is-a-ping)
2. [What Does Traceroute Do?](#what-does-traceroute-do)
3. [Top 8 Nmap Commands](#top-8-nmap-commands)
4. [How Hackers Use Reconnaissance](#how-hackers-use-reconnaissance)
5. [SQLMap Cheat Sheet](#sqlmap-cheat-sheet)
6. [Traceroute](#traceroute)
7. [Telnet](#telnet)
8. [Netcat](#netcat)
9. [Wappalyzer](#wappalyzer)
10. [References](#references)
11. [Learning Objectives](#learning-objectives)

---

## What is a Ping?
Ping is a network utility used to test the reachability of a host on an IP network. It measures the round-trip time for packets sent from the origin to the destination.

### Famous Commands
```bash
ping <target>
```
- **Example**: `ping google.com`
- **Purpose**: Check connectivity and measure response time.

---

## What Does Traceroute Do?
Traceroute maps the path data takes to reach a specific network destination. It identifies each hop and measures the time taken for the round trip to each hop.

### Famous Commands
```bash
traceroute <target>
```
- **Example**: `traceroute google.com`
- **Purpose**: Identify the route and locate bottlenecks or failures.

---

## Top 8 Nmap Commands
1. **Basic Scan**:
   ```bash
   nmap <target>
   ```
2. **Scan Specific Ports**:
   ```bash
   nmap -p 80,443 <target>
   ```
3. **Aggressive Scan**:
   ```bash
   nmap -A <target>
   ```
4. **Operating System Detection**:
   ```bash
   nmap -O <target>
   ```
5. **Service Version Detection**:
   ```bash
   nmap -sV <target>
   ```
6. **Scan All Ports**:
   ```bash
   nmap -p- <target>
   ```
7. **Detect Firewalls**:
   ```bash
   nmap -sA <target>
   ```
8. **Export Results**:
   ```bash
   nmap -oN output.txt <target>
   ```

---

## How Hackers Use Reconnaissance
Hackers use reconnaissance to collect data about targets, such as their IP address, operating systems, and open ports, for identifying vulnerabilities and planning attacks. Tools like Nmap, Wappalyzer, and netcat are commonly used.

---

## SQLMap Cheat Sheet
SQLMap is a penetration testing tool used for automating SQL injection attacks and database security assessments.

### Famous Commands
- **Basic Usage**:
  ```bash
  sqlmap -u "http://example.com/vulnerable"
  ```
- **Enumerate Databases**:
  ```bash
  sqlmap -u "http://example.com/vulnerable" --dbs
  ```
- **Dump a Database**:
  ```bash
  sqlmap -u "http://example.com/vulnerable" -D <database_name> --dump
  ```
- **Bypass WAF**:
  ```bash
  sqlmap -u "http://example.com/vulnerable" --tamper=<tamper_script>
  ```

---

## Traceroute
Traceroute is a tool used to determine the route packets take to reach a destination. It helps identify network delays and locate bottlenecks.

### Famous Commands
```bash
traceroute <target>
```
- **Example**: `traceroute example.com`
- **Purpose**: Map the path packets take and measure delays at each hop.

---

## Telnet
Telnet is a command-line tool used for communication with remote devices or servers. It is commonly used for testing open ports and services.

### Famous Commands
```bash
telnet <target> <port>
```
- **Example**: `telnet example.com 80`
- **Purpose**: Test connectivity to a specific port or service.

---

## Netcat
Netcat (nc) is a versatile networking tool used for port scanning, banner grabbing, and establishing connections.

### Famous Commands
```bash
nc -zv <target> <port_range>
```
- **Example**: `nc -zv example.com 20-80`
- **Purpose**: Check open ports.

```bash
nc -lvp <port>
```
- **Example**: `nc -lvp 4444`
- **Purpose**: Start a listener on a specific port.

---

## Wappalyzer
Wappalyzer is a tool that identifies the technologies and frameworks used on websites. It can be used for active reconnaissance.

### Famous Usage
- **Browser Extension**: Install the Wappalyzer extension for Chrome or Firefox.
- **Command Line**:
  ```bash
  wappalyzer https://example.com
  ```
- **Purpose**: Detect technologies, programming languages, and CMS platforms used by a website.

---

## References
- **ping**
- **traceroute**
- **telnet**
- **netcat**
- **Wappalyzer**

---

## Author
Younes SABER  
GitHub: [seeyou7](https://github.com/seeyou7)

