# 🛡️ Server-Side Request Forgery (SSRF) – Explanation & Examples

## 📌 What is SSRF?

**Server-Side Request Forgery (SSRF)** is a type of vulnerability where an attacker is able to make a server-side application send HTTP requests to an arbitrary domain or IP address, often **bypassing access restrictions**.

> SSRF vulnerabilities are dangerous because they allow attackers to interact with internal systems or services that are **not accessible from the outside**.

---

## 🚨 Why is SSRF Dangerous?

- Access to **localhost-only services** (e.g., `127.0.0.1`)
- Exposure of **internal APIs and metadata services**
- Potential to **read files**, interact with **databases**, or even **bypass firewalls**
- In cloud environments (like AWS), attackers can access the **metadata endpoint** and steal IAM credentials.

---

## 🔎 Basic SSRF Example

Suppose a web app has a feature to fetch content from a user‑provided URL:

```http
POST /check-reduction HTTP/1.1
Host: vulnerable-app.com
Content-Type: application/x-www-form-urlencoded

articleApi=http://external-site.com/info
```

If the server blindly fetches this URL, an attacker can change the `articleApi` to:

```bash
articleApi=http://127.0.0.1:3000/admin
```

💥 This allows them to access an **internal admin interface** that is **not exposed to the public**.

---

## 🎯 Bypassing Filters – IP Tricks

Even if the server blocks `localhost` or `127.0.0.1`, we can use **alternate IP representations**:

| Format      | Representation            |
|-------------|---------------------------|
| Decimal     | `http://2130706433:3000`  |
| Octal       | `http://0177.0.0.1:3000`  |
| Hexadecimal | `http://0x7f000001:3000`  |
| Dotted Hex  | `http://0x7f.0x0.0x0.0x1` |

✅ All of them resolve to `127.0.0.1`.

---

## 🔗 Advanced SSRF: Chained SSRF via Nested Parameters

Sometimes the SSRF doesn't go directly to the target. Instead, it passes through **another vulnerable endpoint**, such as a proxy or redirect handler.

### Example

```http
articleApi=http://web0x08.hbtn:8080/app4-1/product/nextProduct?path=http://127.0.0.1:8080/admin
```

### What Happens

1. The server fetches the URL provided in `articleApi`.
2. That intermediary endpoint (`nextProduct`) then fetches the URL provided in its `path` parameter.
3. The internal system ends up making a request to `http://127.0.0.1:8080/admin`.

> This is a classic **chained SSRF** where one service helps pivot to another.

---

## 📂 Real‑World SSRF Targets

| Target Endpoint                               | Purpose                             |
|----------------------------------------------|-------------------------------------|
| `http://127.0.0.1:3000/admin`                | Internal admin panel                |
| `http://localhost:8080/debug`                | Debug info for internal apps        |
| `http://169.254.169.254/latest/meta-data/`   | Cloud metadata (AWS, GCP, etc.)     |
| `file:///etc/passwd`                         | Local file read (if `file://` allowed) |

---

## 🧪 How to Test SSRF

1. Use **Burp Suite** to intercept the request.
2. Replace the vulnerable parameter (e.g., `articleApi`) with an internal target.
3. Observe:
   - Status code (200, 403, 500)
   - Content returned
   - Headers (e.g., `X-Powered-By: Express`)
4. Use **Collaborator/OAST** to check for out‑of‑band interactions.

---

## 🛡️ Mitigations

- ✅ Use an **allowlist** for external URLs.
- ❌ Never allow user input to be directly passed to a fetcher or proxy.
- 🔍 Validate the resolved IP address (block private/internal ranges).
- 🧱 Restrict egress traffic from the server using a firewall.
- 🧪 Regular security testing for SSRF in internal tools and microservices.

---

## 🏁 Final Thoughts

SSRF is one of the most powerful web vulnerabilities when chained properly. Always validate user inputs, control where your servers are allowed to connect, and never trust parameters blindly.

> 💥 One SSRF can lead to total server compromise in the cloud ☁️

---

## 🧰 References

- [PortSwigger: SSRF explained](https://portswigger.net/web-security/ssrf)
- [OWASP SSRF Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)



Younes.S ([@seeyou7](https://github.com/seeyou7))
