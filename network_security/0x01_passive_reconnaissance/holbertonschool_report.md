# Holberton School Domain Analysis Report

## 1. Overview
This report provides detailed information on the `holbertonschool.com` domain, including:
- IP ranges within the domain.
- Technologies and frameworks used by subdomains.
- A summary of findings.

---

## 2. IP Ranges
The following IPs and their corresponding locations have been identified within the `holbertonschool.com` domain:

| IP Address        | Hostname                                              | Provider                   | Location               |
|--------------------|------------------------------------------------------|----------------------------|------------------------|
| 35.180.27.154     | ec2-35-180-27-154.eu-west-3.compute.amazonaws.com     | Amazon Data Services France| France, Paris          |
| 52.47.143.83      | ec2-52-47-143-83.eu-west-3.compute.amazonaws.com      | Amazon Data Services France| France, Paris          |
| 13.38.216.13      | lvl2-discourse-staging.holbertonschool.com            | leakix                     | Unknown                |
| 35.152.119.144    | webflow.holbertonschool.com                           | leakix                     | Unknown                |
| 13.38.122.220     | staging-apply-forum.holbertonschool.com               | subdomaincenter            | Unknown                |
| 18.155.129.90     | assets.holbertonschool.com                            | subdomaincenter            | Unknown                |
| 54.157.56.129     | alpha.holbertonschool.com                             | subdomaincenter            | Unknown                |
| 52.222.169.18     | staging-rails-assets-apply.holbertonschool.com        | alienvault                 | Unknown                |
| 34.203.198.145    | v2.holbertonschool.com                                | leakix                     | Unknown                |
| 51.20.161.157     | www.holbertonschool.com                               | leakix                     | Unknown                |
| 54.89.246.137     | v3.holbertonschool.com                                | leakix                     | Unknown                |
| 13.39.252.4       | staging-apply.holbertonschool.com                     | subdomaincenter            | Unknown                |
| 192.0.78.230      | blog.holbertonschool.com                              | leakix                     | Unknown                |
| 52.47.145.169     | apply.holbertonschool.com                             | leakix                     | Unknown                |
| 3.214.214.66      | beta.holbertonschool.com                              | subdomaincenter            | Unknown                |
| 104.17.201.193    | fr.webflow.holbertonschool.com                        | alienvault                 | Unknown                |
| 108.156.39.87     | rails-assets.holbertonschool.com                      | subdomaincenter            | Unknown                |
| 15.237.230.24     | read.holbertonschool.com                              | subdomaincenter            | Unknown                |
| 75.2.70.75        | holbertonschool.com                                   | crtsh                      | Unknown                |
| 216.198.54.1      | support.holbertonschool.com                           | leakix                     | Unknown                |
| 54.86.136.129     | v1.holbertonschool.com                                | leakix                     | Unknown                |
| 13.50.141.112     | fr.holbertonschool.com                                | subdomaincenter            | Unknown                |
| 18.102.16.191     | smile2021.holbertonschool.com                         | alienvault                 | Unknown                |

---

## 3. Technologies and Frameworks
The following subdomains and their respective technologies were identified:

| Subdomain                           | IP Address     | Server/Technology        | Framework/SSL Details                        |
|-------------------------------------|----------------|--------------------------|----------------------------------------------|
| holbertonschool.com                 | 35.180.27.154  | nginx/1.18.0 (Ubuntu)    | HTTP 301 Redirect to `http://holbertonschool.com` |
| yriry2.holbertonschool.com          | 52.47.143.83   | nginx                    | Let's Encrypt SSL (TLSv1.2, TLSv1.3)         |
| lvl2-discourse-staging.holbertonschool.com | 13.38.216.13 | Unknown                 | Leakix                                        |
| webflow.holbertonschool.com         | 35.152.119.144 | Unknown                  | Leakix                                        |
| staging-apply-forum.holbertonschool.com | 13.38.122.220 | Unknown                 | SubdomainCenter                              |
| alpha.holbertonschool.com           | 54.157.56.129  | Unknown                  | SubdomainCenter                              |
| v2.holbertonschool.com              | 34.203.198.145 | Unknown                  | Leakix                                        |
| blog.holbertonschool.com            | 192.0.78.230   | Unknown                  | Leakix                                        |

---

## 4. Observations
- The main domain and its subdomains are hosted on Amazon Data Services in France, with multiple subdomains using nginx servers.
- SSL certificates are provided by Let's Encrypt for some subdomains, supporting modern TLS versions (TLSv1.2 and TLSv1.3).
- Some subdomains redirect to the main domain (`holbertonschool.com`) or other internal resources.
- Various technologies and frameworks are in use across different subdomains, as observed from headers and SSL information.

---

## 5. Tools and Commands Used
The following tools and commands were used to gather this information:
1. **Shodan CLI**:
   - `shodan search "holbertonschool.com"`
2. **Subfinder**:
   - `subfinder -d holbertonschool.com`

---

## 6. Author
**Younes SABER**  
- **GitHub**: [seeyou7](https://github.com/seeyou7)

