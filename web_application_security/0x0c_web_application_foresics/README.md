# 🛡️ Web Application Forensics Report – Entry #1

## Title: **Incident Analysis, Response, and Mitigation Strategy**

---

## 🔰 **Introduction**

In cybersecurity, understanding and mitigating the risks associated with web application vulnerabilities is vital for maintaining organizational integrity and preventing data breaches. Log files serve as a crucial source of forensic evidence, helping analysts understand how an attacker operated, what vulnerabilities were exploited, and which parts of the system were affected.

This report presents an initial entry in a broader web application forensics investigation. It focuses on **analyzing authentication logs**, identifying suspicious activity, and outlining security strategies to prevent further compromise.

---

## 🚨 **Incident Report**

### 🗞 Summary of Key Findings

- **Brute-force attack detected** via the `sshd` service with over 34,000 authentication attempts.
- Multiple **failed login attempts** were followed by **successful authentication events**, indicating at least one **account compromise**.
- The **user 'root'** was identified as a compromised account, having experienced multiple failed attempts before a successful login.
- A total of **18 distinct IP addresses** successfully accessed the system, representing the confirmed attackers.
- Several **unauthorized user accounts** were created (e.g., `Kayn`, `Jax`, `Aphelios`), some of which were later deleted—suggesting attacker privilege escalation and lateral movement.
- **Firewall rules** were added post-intrusion, with **6 new rules**, potentially to maintain access or prevent further detection.

### 🔴 Impact

- **Unauthorized root access** puts the entire system at risk.
- The creation of new users indicates **persistent access** was attempted.
- Attackers may have altered security configurations (e.g., firewalls).
- System integrity and data confidentiality are considered compromised.

---

## 🛠️ **Implementation Plan: Mitigation & Hardening Steps**

To remediate this incident and prevent recurrence, the following step-by-step plan is proposed:

### ✅ Step 1: Account and Access Audit

- Lock or delete all unauthorized accounts (`Jax`, `Aphelios`, etc.).
- Rotate passwords for all privileged accounts, including `root`.
- Enable **two-factor authentication (2FA)** where applicable.

### ✅ Step 2: SSH Hardening

- Restrict SSH access to a **whitelist of IP addresses**.
- Disable root login via SSH (`PermitRootLogin no` in `sshd_config`).
- Change the default SSH port from `22` to a non-standard port.

### ✅ Step 3: Firewall Review and Reset

- Review and reset firewall rules.
- Implement **default-deny** policy and allow only known services.

### ✅ Step 4: Log Configuration & Centralization

- Enable verbose logging for authentication and privilege escalation.
- Centralize logs to a **secure SIEM** (Security Information and Event Management) system.

### ✅ Step 5: Patch and Update

- Run a full system update: `apt update && apt upgrade` (or distro equivalent).
- Patch all web applications and backend services.

---

## 📊 **Monitoring Protocol**

To maintain a strong security posture, ongoing monitoring is critical. The following protocol is to be implemented:

### 🔍 1. Real-Time Log Monitoring

- Implement tools like **Fail2Ban** or **Wazuh** to monitor SSH brute-force attacks in real-time.
- Set up alerts for repeated failed login attempts or unauthorized user creations.

### 📉 2. Weekly Security Reports

- Generate automated reports of:
  - New users added
  - SSH login patterns
  - Firewall changes

### 🧪 3. File Integrity Monitoring

- Use tools like **Tripwire** or **AIDE** to detect unauthorized changes to critical files (e.g., `/etc/passwd`, firewall configs).

### ⚠️ 4. Incident Response Readiness

- Maintain an up-to-date **incident response playbook**.
- Conduct monthly **security drills** to test team response efficiency.

---

## 📌 **Conclusion**

This incident highlights the need for proactive monitoring, access control, and response readiness. While this report marks the first entry in our web application forensics initiative, the findings have already helped identify major weaknesses in the authentication and user management mechanisms of the system.

The next phase will focus on analyzing **web server access logs**, detecting lateral movement, and hunting for potential data exfiltration.

Author Younes : github.com/seeyou7

