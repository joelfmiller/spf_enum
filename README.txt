https://securitybyjoel.com
https://twitter.com/joelfmiller

Description:
SPF enumerator written in Python

Script retrieves the SPF record for a given domain and enumerates all IPs and includes to print out a comprehensive list of IPv4 and IPv6 records.

Requires dnspython to be installed
i.e. pip install dnspython

Usage:
python spf_enum.py <domain>
i.e. python spf_enum.py twitter.com

Example Output
------------------------------------------
[+] Fetching SPF record for: x.com all: -all
  [+] Fetching SPF record for: _spf.google.com all: ~all
    [+] Fetching SPF record for: _netblocks.google.com all: ~all
      [-] 35.190.247.0/24
      [-] 64.233.160.0/19
      [-] 66.102.0.0/20
      [-] 66.249.80.0/20
      [-] 72.14.192.0/18
      [-] 74.125.0.0/16
      [-] 108.177.8.0/21
      [-] 173.194.0.0/16
      [-] 209.85.128.0/17
      [-] 216.58.192.0/19
      [-] 216.239.32.0/19
    [+] Fetching SPF record for: _netblocks2.google.com all: ~all
      [-] 2001:4860:4000::/36
      [-] 2404:6800:4000::/36
      [-] 2607:f8b0:4000::/36
      [-] 2800:3f0:4000::/36
      [-] 2a00:1450:4000::/36
      [-] 2c0f:fb50:4000::/36
    [+] Fetching SPF record for: _netblocks3.google.com all: ~all
      [-] 172.217.0.0/19
      [-] 172.217.32.0/20
      [-] 172.217.128.0/19
      [-] 172.217.160.0/20
      [-] 172.217.192.0/19
      [-] 172.253.56.0/21
      [-] 172.253.112.0/20
      [-] 108.177.96.0/19
      [-] 35.191.0.0/16
      [-] 130.211.0.0/22

[+] SPF TXT Record for x.com:
  [-] v=spf1 include:_spf.google.com -all

[+] Total number of IPv4 hosts: 328960
[+] Total number of IPv6 hosts: 29710560942849126597578981376
[+] Total number of hosts in the SPF record: 29710560942849126597579310336
