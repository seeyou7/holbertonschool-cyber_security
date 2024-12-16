# Linux Fundamentals Guide

Welcome to the **Linux Fundamentals Guide**! This repository is designed to help you understand and master essential Linux concepts and commands. By the end of this guide, you will be able to explain key aspects of Linux to anyone without the need for external references.

## Table of Contents

1. [Introduction](#introduction)
2. [Learning Outcomes](#learning-outcomes)
3. [Detailed Topics](#detailed-topics)
    - [What is Linux](#what-is-linux)
    - [What is a Linux Command](#what-is-a-linux-command)
    - [Structure of the Linux Operating System](#structure-of-the-linux-operating-system)
    - [Filesystem Hierarchy Standard (FHS)](#filesystem-hierarchy-standard-fhs)
    - [Linux File System Directories](#linux-file-system-directories)
    - [Protecting Files and Directories](#protecting-files-and-directories)
    - [Monitoring and Investigating System Activity](#monitoring-and-investigating-system-activity)
    - [Securely Transferring Files and Data](#securely-transferring-files-and-data)
    - [Configuring and Managing a Firewall](#configuring-and-managing-a-firewall)
    - [Identifying and Terminating Malicious Processes](#identifying-and-terminating-malicious-processes)
    - [Working with Commands](#working-with-commands)
        - [Using `ps` and `kill` Commands](#using-ps-and-kill-commands)
        - [Using `netstat` and `ss` Commands](#using-netstat-and-ss-commands)
        - [Using `nmap`, `lynis`, and `tcpdump` Commands](#using-nmap-lynis-and-tcpdump-commands)
        - [Using `iptables` and `ufw` to Manage Firewall Rules](#using-iptables-and-ufw-to-manage-firewall-rules)
4. [Author](#author)
5. [License](#license)

## Introduction

Linux is a powerful and versatile operating system widely used in various environments, from personal computers to servers and embedded systems. Understanding Linux fundamentals is crucial for anyone pursuing a career in IT, system administration, or cybersecurity. This guide provides comprehensive explanations of key Linux concepts and commands, enabling you to confidently discuss and utilize Linux in practical scenarios.

## Learning Outcomes

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

1. What is Linux
2. What is a Linux Command
3. What is the structure of the Linux operating system
4. What is the purpose of the FHS and what are the benefits of using it
5. What are the different directories in the Linux file system, and what are their purposes
6. How to protect files and directories
7. How to monitor and investigate system activity
8. How to securely transfer files and data
9. How to configure and manage a firewall
10. How to identify and terminate malicious processes
11. Working with Commands:
    - How to use the `ps` and `kill` commands to identify and terminate malicious processes
    - How to use the `netstat` and `ss` commands to monitor network traffic for suspicious activity
    - How to use the `nmap`, `lynis`, and `tcpdump` commands to analyze network traffic for suspicious behavior
    - How to use `iptables` and `ufw` to manage the firewall rules on Linux systems

## Detailed Topics

### What is Linux

**Linux** is an open-source, Unix-like operating system kernel first released by Linus Torvalds in 1991. It serves as the foundation for numerous operating systems, collectively known as Linux distributions (distros), such as Ubuntu, Fedora, and CentOS. Linux is renowned for its stability, security, and flexibility, making it a preferred choice for servers, desktops, and various embedded systems.

- **Open Source:** Linux's source code is freely available, allowing users to modify and distribute it.
- **Kernel:** The core component that manages system resources, hardware communication, and provides essential services for other software.
- **Distributions:** Customized versions of Linux tailored for specific purposes, combining the kernel with software packages, desktop environments, and tools.

### What is a Linux Command

A **Linux command** is an instruction entered into the command-line interface (CLI) to perform specific tasks within the Linux operating system. Commands allow users to interact with the system, manage files, execute programs, and configure settings efficiently.

- **Syntax:** Typically follows the structure `command [options] [arguments]`.
- **Options:** Modify the behavior of commands (e.g., `-l` for long listing in `ls`).
- **Arguments:** Specify the target of the command (e.g., file names, directories).

**Example:**
```bash
ls -l /home/user

### Structure of the Linux Operating System
The Linux operating system is structured into several layers, each responsible for specific functionalities. Understanding this structure is key to effective system management and troubleshooting.

-Kernel: The core component managing hardware, memory, processes, and system calls.
-System Libraries: Provide standard functions for applications to interact with the kernel.
-System Utilities: Basic tools for system management and maintenance.
-User Interface: Interfaces like the command-line interface (CLI) or graphical user interface (GUI) that allow user interaction.
-Applications: Software programs that perform user-oriented tasks.

#Layers:

-Hardware: Physical components of the computer.
-Kernel: Manages resources and system operations.
-System Libraries and Utilities: Interface between the kernel and applications.
-User Interface and Applications: Direct interaction with users.

###Filesystem Hierarchy Standard (FHS)
The Filesystem Hierarchy Standard (FHS) defines the directory structure and directory contents in Linux. It ensures consistency across different Linux distributions, making it easier for users and developers to navigate and manage the system.

-Purpose: Standardize the placement of files and directories.
--Benefits:
1-Consistency: Simplifies navigation and management across distributions.
2-Predictability: Users know where to find specific files and directories.
3- Interoperability: Facilitates software compatibility and development.

# Linux File System Directories
Linux organizes files into a hierarchical directory structure. Each directory serves a specific purpose, housing related files and subdirectories.

/ (Root): The top-level directory from which all other directories branch.
/bin: Essential binary executables for system booting and single-user mode.
/boot: Static files required for booting the system, including the kernel.
/dev: Device files representing hardware components.
/etc: Configuration files for the system and installed applications.
/home: User home directories containing personal files and settings.
/lib: Essential shared libraries and kernel modules.
/media: Mount points for removable media like USB drives.
/mnt: Temporary mount points for filesystems.
/opt: Optional software packages.
/proc: Virtual filesystem providing process and system information.
/root: Home directory for the root user.
/sbin: System binaries essential for system administration.
/tmp: Temporary files created by applications.
/usr: Secondary hierarchy for user utilities and applications.
/var: Variable data like logs, databases, and spool files.

##Protecting Files and Directories
Protecting files and directories involves setting appropriate permissions and ownership to control access and prevent unauthorized modifications.

- Permissions: Define read (r), write (w), and execute (x) rights for the owner, group, and others.
- Commands:
chmod: Change file permissions.
chown: Change file ownership.
chgrp: Change group ownership.
- Ownership: Assign files to specific users and groups to manage access.
---Advanced Protections: Utilize Access Control Lists (ACLs) for more granular permission settings.
**Example:**

bash:
chmod 755 script.sh
chown user:group file.txt

### Monitoring and Investigating System Activity

Monitoring and investigating system activity ensures the system operates smoothly and helps detect and troubleshoot issues promptly.

- System Logs: Store records of system events and activities.
      - Locations: /var/log/
      - Tools: tail, less, grep to view and search logs.
- Process Monitoring: Track active processes and resource usage.
       - Commands: top, htop, ps
- Resource Usage: Monitor CPU, memory, disk, and network utilization.
        - Tools: vmstat, iostat, netstat, ss
- Automated Monitoring: Use tools like Nagios, Zabbix, or Prometheus for continuous monitoring and alerts.


###Securely Transferring Files and Data

Securely transferring files and data involves using protocols and tools that ensure data confidentiality, integrity, and authentication during transfer.

- SSH (Secure Shell): Provides encrypted communication for remote access and file transfers.
       - Tools: scp, sftp
- rsync: Efficiently synchronizes files and directories between systems, supporting encryption.
- FTP over SSL/TLS (FTPS): Adds security to traditional FTP.
- Secure Copy Protocol (SCP): Facilitates secure file transfers between hosts.
**Example:**

bash

scp file.txt user@remote_host:/path/to/destination/


###Configuring and Managing a Firewall

Configuring and managing a firewall protects the system from unauthorized access and network threats by controlling incoming and outgoing traffic based on predefined rules.

iptables: A powerful command-line firewall utility for configuring Linux kernel firewall.
Basic Commands:
iptables -L: List current rules.
iptables -A INPUT -p tcp --dport 22 -j ACCEPT: Allow SSH.
ufw (Uncomplicated Firewall): Simplifies firewall management with an easy-to-use interface.
Basic Commands:
ufw enable: Activate the firewall.
ufw allow 22/tcp: Allow SSH.
ufw status: Check firewall status.
firewalld: Dynamic firewall management tool with support for network zones.
Basic Commands:
firewall-cmd --state: Check if firewalld is running.
firewall-cmd --add-service=http --permanent: Allow HTTP traffic.
firewall-cmd --reload: Apply changes.
Identifying and Terminating Malicious Processes
Identifying and terminating malicious processes is crucial for maintaining system security and integrity.

Identifying Malicious Processes:
Commands: ps, top, htop
Indicators: Unusual resource usage, unknown process names, unexpected network connections.
Terminating Malicious Processes:
Commands: kill, killall, pkill
Usage:
kill PID: Terminate a specific process by its Process ID (PID).
killall process_name: Terminate all processes with the specified name.
Example:

bash
Copy code
ps aux | grep suspicious_process
kill 1234
Working with Commands
Using ps and kill Commands
ps (Process Status): Displays information about active processes.
Usage:
ps aux: List all running processes.
ps -ef: Another format to list processes.
kill: Sends signals to terminate or control processes.
Usage:
kill PID: Send the default SIGTERM signal to terminate.
kill -9 PID: Forcefully terminate a process with SIGKILL.
Example:

bash

ps aux | grep firefox
kill 5678
Using netstat and ss Commands
netstat: Displays network connections, routing tables, interface statistics.
Usage:
netstat -tuln: Show listening ports.
netstat -anp: Show all connections with associated processes.
ss (Socket Statistics): A modern replacement for netstat, providing more detailed information.
Usage:
ss -tuln: Show listening ports.
ss -anp: Show all connections with associated processes.
Example:

bash

ss -tuln
netstat -anp | grep LISTEN
Using nmap, lynis, and tcpdump Commands
nmap (Network Mapper): Scans networks to discover hosts and services.
Usage:
nmap -sP 192.168.1.0/24: Ping scan to discover active hosts.
nmap -sV target_host: Service version detection.
lynis: A security auditing tool for Linux systems.
Usage:
lynis audit system: Perform a security audit.
tcpdump: Captures and analyzes network traffic.
Usage:
tcpdump -i eth0: Capture traffic on interface eth0.
tcpdump -w capture.pcap: Save captured traffic to a file.
Example:

bash

nmap -sP 192.168.1.0/24
lynis audit system
tcpdump -i eth0
Using iptables and ufw to Manage Firewall Rules
iptables: Configures packet filtering rules within the Linux kernel.
Basic Commands:
iptables -A INPUT -p tcp --dport 80 -j ACCEPT: Allow HTTP traffic.
iptables -D INPUT -p tcp --dport 80 -j ACCEPT: Remove the rule.
ufw (Uncomplicated Firewall): Simplifies firewall management.
Basic Commands:
ufw allow 22/tcp: Allow SSH.
ufw deny 23: Deny Telnet.
ufw enable: Activate the firewall.
Example:

bash

iptables -A INPUT -p tcp --dport 443 -j ACCEPT
ufw allow 443/tcp



## Author

**Younes Saber**  
GitHub: [seeyou7](https://github.com/seeyou7)
 
