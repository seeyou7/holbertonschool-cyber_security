<h1>NMAP HOST DISCOVERY</h1>
<p>
  Nmap (<strong>Network Mapper</strong>) is a powerful, open-source tool used to discover hosts and services 
  on a computer network by sending packets and analyzing responses. This README aims to provide an overview 
  of various Nmap host discovery (or “ping”) techniques, explain what Nmap can detect, and suggest ways to 
  remain stealthy while scanning. We’ll also cover how to detect firewalls and some common firewall 
  evasion options.
</p>

<hr>

<h2>1. ARP Scan</h2>
<p>
  <strong>What It Is:</strong> ARP (Address Resolution Protocol) Scan is used on local networks (Ethernet/Wi-Fi) 
  to map IP addresses to MAC addresses. This is extremely reliable on a local LAN because devices must respond 
  to ARP requests for basic networking functions.
</p>
<p><strong>Usage Example:</strong></p>
<pre><code>sudo nmap -PR 192.168.0.0/24
</code></pre>
<ul>
  <li><code>-PR</code> tells Nmap to use ARP requests to discover active hosts on the same subnet.</li>
</ul>

<hr>

<h2>2. ICMP Echo Scan</h2>
<p>
  <strong>What It Is:</strong> The classic “ping” technique. It sends an ICMP Echo Request and waits for an 
  ICMP Echo Reply. Not all hosts respond to ICMP Echo Requests (some firewalls/hosts ignore them), so this method 
  can miss certain targets.
</p>
<p><strong>Usage Example:</strong></p>
<pre><code>sudo nmap -PE 192.168.0.100
</code></pre>
<ul>
  <li><code>-PE</code> sets ICMP Echo Request as the preferred discovery method.</li>
</ul>

<hr>

<h2>3. ICMP Timestamp Scan</h2>
<p>
  <strong>What It Is:</strong> Sends ICMP Timestamp Requests (Type 13). The target typically replies with a 
  Timestamp Reply (Type 14). Though less common than Echo Requests, some systems still respond to Timestamp 
  Queries even if they block Echo Requests.
</p>
<p><strong>Usage Example:</strong></p>
<pre><code>sudo nmap -PP 192.168.0.100
</code></pre>
<ul>
  <li><code>-PP</code> sets ICMP Timestamp Requests for the discovery method.</li>
</ul>

<hr>

<h2>4. ICMP Address Mask Scan</h2>
<p>
  <strong>What It Is:</strong> Sends an ICMP Address Mask Request (Type 17). Historically used by BOOTP clients 
  to determine subnet masks, but modern networks rarely rely on this. Some systems may still reply, giving 
  away their presence even if they drop Echo Requests.
</p>
<p><strong>Usage Example:</strong></p>
<pre><code>sudo nmap -PM 192.168.0.100
</code></pre>
<ul>
  <li><code>-PM</code> sets ICMP Address Mask Requests for the discovery method.</li>
</ul>

<hr>

<h2>5. TCP SYN Ping Scan</h2>
<p>
  <strong>What It Is:</strong> Uses a half-open TCP SYN packet to see if the port is listening. If the target 
  responds with a SYN/ACK, it implies the host is up. If it responds with RST or no response, it might be down 
  or the port is closed/filtered.
</p>
<p><strong>Usage Example:</strong></p>
<pre><code>sudo nmap -PS80,443 192.168.0.100
</code></pre>
<ul>
  <li><code>-PS</code> chooses TCP SYN Ping. Common ports like 80 (HTTP) or 443 (HTTPS) are often used to increase 
  detection reliability.</li>
</ul>

<hr>

<h2>6. TCP ACK Ping Scan</h2>
<p>
  <strong>What It Is:</strong> Sends a TCP packet with the ACK flag set. Some devices respond with RST if the 
  port is open or closed, implying the host is alive. This can bypass simple firewall rules that allow existing 
  (ACK) connections.
</p>
<p><strong>Usage Example:</strong></p>
<pre><code>sudo nmap -PA80,443 192.168.0.100
</code></pre>
<ul>
  <li><code>-PA</code> chooses TCP ACK Ping with specified ports.</li>
</ul>

<hr>

<h2>7. UDP Ping Scan</h2>
<p>
  <strong>What It Is:</strong> Sends a UDP packet to specific ports (e.g., 53 for DNS). If a device responds 
  with ICMP Port Unreachable, you know it’s alive. However, UDP scanning can be slower and less reliable due 
  to packet losses, no responses, and widespread firewall blocking.
</p>
<p><strong>Usage Example:</strong></p>
<pre><code>sudo nmap -PU53,123 192.168.0.100
</code></pre>
<ul>
  <li><code>-PU</code> sets UDP Ping for discovery, targeting common UDP ports like 53 (DNS) or 123 (NTP).</li>
</ul>

<hr>

<h2>8. What Can Nmap Detect?</h2>
<ul>
  <li><strong>Open/Closed/Filtered Ports:</strong> Determines if a port is open (listening), closed, or blocked 
  by a firewall.</li>
  <li><strong>Operating System Fingerprinting:</strong> Uses TTLs, TCP/IP stack behavior, and banner grabbing 
  for OS detection.</li>
  <li><strong>Service/Version Detection:</strong> Identifies the application running on the port 
  (e.g., Apache, nginx) and its version.</li>
  <li><strong>Firewall/IDS/IPS Presence:</strong> By analyzing scan responses, Nmap can reveal if a firewall 
  or intrusion detection system is interfering.</li>
</ul>

<hr>

<h2>9. Major Nmap Commands to Use Without Being Detected</h2>
<p>
  Complete stealth is never guaranteed, but the following techniques reduce noise:
</p>

<ol>
  <li>
    <p><strong>SYN Stealth Scan (<code>-sS</code>)</strong><br>
    Sends half-open SYN packets. It’s less likely to be logged by the target.</p>
    <pre><code>sudo nmap -sS &lt;target&gt;
</code></pre>
  </li>

  <li>
    <p><strong>Slow Timing Options (<code>-T0</code> or <code>-T1</code>)</strong><br>
    Scans slowly to avoid triggering detection or intrusion prevention systems.</p>
    <pre><code>sudo nmap -sS -T0 &lt;target&gt;
</code></pre>
    <ul>
      <li><code>-T0</code> (Paranoid) or <code>-T1</code> (Sneaky) drastically slows the scan.</li>
    </ul>
  </li>

  <li>
    <p><strong>Decoy Scans (<code>-D</code>)</strong><br>
    Spoof multiple source addresses, masking your true IP.</p>
    <pre><code>sudo nmap -sS -D RND:10 &lt;target&gt;
</code></pre>
    <ul>
      <li><code>-D RND:10</code> uses 10 random decoys.</li>
    </ul>
  </li>

  <li>
    <p><strong>Fragmentation (<code>-f</code>)</strong><br>
    Splits the probe packets into tiny fragments, potentially evading simple signature-based firewalls.</p>
    <pre><code>sudo nmap -sS -f &lt;target&gt;
</code></pre>
  </li>

  <li>
    <p><strong>Randomize Target &amp; Port Order (<code>--randomize-hosts</code>, <code>-r</code>)</strong><br>
    Avoid scanning targets in sequential order to reduce predictable patterns.</p>
  </li>
</ol>

<hr>

<h2>10. How to Detect Firewalls</h2>
<ol>
  <li>
    <strong>Compare SYN vs. ACK Scans:</strong><br>
    If SYN (<code>-PS</code>) scans show ports as filtered but ACK (<code>-PA</code>) scans always return 
    RST or no response, there may be a stateful firewall in place.
  </li>
  <li>
    <strong>Use Version Detection (<code>-sV</code>):</strong><br>
    If a firewall/proxy is intercepting connections, the service version may show unexpected banners 
    or generic error pages.
  </li>
  <li>
    <strong>TTL &amp; Traceroute Checks (<code>--traceroute</code>):</strong><br>
    Intermediate hops or sudden TTL changes can signal firewall or NAT behavior.
  </li>
</ol>

<hr>

<h2>11. Firewall Evasion Techniques and Commands</h2>
<p>
  While these should only be used on networks you have permission to test, they demonstrate some of 
  Nmap’s advanced features:
</p>

<ol>
  <li>
    <strong>Fragment Packets (<code>-f</code> or <code>--mtu</code>)</strong><br>
    Forces packets to be split, occasionally evading detection:
    <pre><code>sudo nmap -sS -f 192.168.0.100
</code></pre>
    or
    <pre><code>sudo nmap -sS --mtu 24 192.168.0.100
</code></pre>
  </li>

  <li>
    <strong>Decoy Scans (<code>-D</code>)</strong><br>
    Creates multiple decoys:
    <pre><code>sudo nmap -sS -D 10.0.0.10,10.0.0.11,ME,10.0.0.12 192.168.0.100
</code></pre>
  </li>

  <li>
    <strong>Idle (Zombie) Scan (<code>-sI</code>)</strong><br>
    Exploits a “zombie” host to measure increments in IPID, hiding your real source:
    <pre><code>sudo nmap -sI zombie_host:80 &lt;target&gt;
</code></pre>
  </li>

  <li>
    <strong>Source Port Manipulation (<code>-g</code> or <code>--source-port</code>)</strong><br>
    Some firewalls allow traffic if it appears to be from a trusted port (like 53 DNS):
    <pre><code>sudo nmap -sS --source-port 53 192.168.0.100
</code></pre>
  </li>

  <li>
    <strong>Scan with a Custom IP TTL/Flags</strong><br>
    Adjusting TTL or TCP flags can fool simpler firewall rules.
  </li>
</ol>

<hr>

<h2>Legal and Ethical Disclaimer</h2>
<p>
  <strong>Always ensure you have explicit permission to scan any network or host.</strong> 
  Unauthorized scanning is often illegal and unethical. Using these techniques can trigger alarms 
  on intrusion detection systems or even break local regulations. Practice responsible disclosure 
  and respect privacy laws.
</p>

<hr>

<h2>Conclusion</h2>
<p>
  Nmap provides various host discovery techniques—ranging from ARP and ICMP-based methods to 
  TCP and UDP-based “pings.” It can detect open, closed, or filtered ports, identify operating 
  systems, and reveal firewall behaviors. While advanced scanning and evasion features exist, they 
  must be used responsibly and within the confines of the law.
</p>
<p>
  For official documentation and the most up-to-date information, refer to the 
  <a href="https://nmap.org/book/man.html" target="_blank">Nmap Reference Guide</a>.
</p>

<p><strong>Happy scanning (legally and responsibly)!</strong></p>


<h2> Author </h2>

<p>
**Younes Saber**  
GitHub: [seeyou7](https://github.com/seeyou7) 
</p>

</body>
</html

