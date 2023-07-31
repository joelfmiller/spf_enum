https://securitybyjoel.com
https://twitter.com/joelfmiller

Description:
SPF enumerator written in Python

Script retrieves the SPF record for a given domain and enumerates all IPs and includes to print out
a comprehensive list of IPv4 and IPv6 records.

Requires dnspython to be installed
i.e. pip install dnspython

Usage:
python spf_enum.py <domain>
i.e. python spf_enum.py twitter.com

Example Output
------------------------------------------
[+] Fetching SPF record for: twitter.com
  [-] 199.16.156.0/22
  [-] 199.59.148.0/22
  [-] 8.25.194.0/23
  [-] 8.25.196.0/23
  [-] 204.92.114.203/32
  [-] 204.92.114.204/31
  [+] Fetching SPF record for: _spf.google.com
    [+] Fetching SPF record for: _netblocks.google.com
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
    [+] Fetching SPF record for: _netblocks2.google.com
      [-] 2001:4860:4000::/36
      [-] 2404:6800:4000::/36
      [-] 2607:f8b0:4000::/36
      [-] 2800:3f0:4000::/36
      [-] 2a00:1450:4000::/36
      [-] 2c0f:fb50:4000::/36
    [+] Fetching SPF record for: _netblocks3.google.com
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
  [+] Fetching SPF record for: _thirdparty.twitter.com
    [-] 96.43.144.64/31
    [-] 96.43.148.64/31
    [-] 182.50.78.64/28
    [-] 204.14.232.64/28
    [-] 204.14.234.64/28
    [+] Fetching SPF record for: spf.mandrillapp.com
      [-] 198.2.128.0/24
      [-] 198.2.132.0/22
      [-] 198.2.136.0/23
      [-] 198.2.145.0/24
      [-] 198.2.186.0/23
      [-] 205.201.131.128/25
      [-] 205.201.134.128/25
      [-] 205.201.136.0/23
      [-] 205.201.139.0/24
      [-] 198.2.177.0/24
      [-] 198.2.178.0/23
      [-] 198.2.180.0/24
  [+] Fetching SPF record for: _oerp.twitter.com
    [-] 144.34.32.247/32
    [-] 144.34.33.247/32
    [-] 144.34.8.247/32
    [-] 144.34.9.247/32
  [+] Fetching SPF record for: spf.smtp2go.com
    [-] 207.58.147.64/28
    [-] 216.22.15.224/27
    [-] 43.228.184.0/22
    [-] 103.47.204.0/22
    [-] 103.2.140.0/22
    [-] 203.31.36.0/22
    [-] 170.10.68.0/22
    [-] 158.120.80.0/21

[+] SPF TXT Record for twitter.com:
  v=spf1 ip4:199.16.156.0/22 ip4:199.59.148.0/22 ip4:8.25.194.0/23 ip4:8.25.196.0/23 ip4:204.92.114.203 ip4:204.92.114.204/31 include:_spf.google.com include:_thirdparty.twitter.com include:_oerp.twitter.com include:spf.smtp2go.com -all

[+] Total number of IPv4 hosts: 343915
[+] Total number of IPv6 hosts: 29710560942849126597578981376
[+] Total number of hosts in the SPF record: 29710560942849126597579325291
