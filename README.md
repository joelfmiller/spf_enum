Usage:
python spf_enum.py <domain>
i.e. python spf_enum.py twitter.com

Example Output
------------------------------------------
Fetching SPF record for: twitter.com
  Fetching SPF record for: _spf.google.com
    Fetching SPF record for: _netblocks.google.com
    Fetching SPF record for: _netblocks2.google.com
    Fetching SPF record for: _netblocks3.google.com
  Fetching SPF record for: _thirdparty.twitter.com
    Fetching SPF record for: spf.mandrillapp.com
  Fetching SPF record for: _oerp.twitter.com
  Fetching SPF record for: spf.smtp2go.com

IPv4 Networks found in the SPF record:
199.16.156.0/22
199.59.148.0/22
8.25.196.0/23
8.25.194.0/23
35.190.247.0/24
64.233.160.0/19
66.102.0.0/20
66.249.80.0/20
72.14.192.0/18
74.125.0.0/16
108.177.8.0/21
209.85.128.0/17
35.191.0.0/16
144.34.32.247/32
172.217.192.0/19
144.34.33.247/32
144.34.8.247/32
144.34.9.247/32
103.47.204.0/22
205.201.136.0/23
172.217.160.0/20
172.217.128.0/19
198.2.186.0/23
205.201.139.0/24
43.228.184.0/22
172.253.112.0/20
108.177.96.0/19
182.50.78.64/28
204.14.232.64/28
204.92.114.204/31
204.14.234.64/28
204.92.114.203/32
216.239.32.0/19
172.217.32.0/20
172.253.56.0/21
172.217.0.0/19
96.43.144.64/31
96.43.148.64/31
198.2.132.0/22
203.31.36.0/22
170.10.68.0/22
158.120.80.0/21
173.194.0.0/16
205.201.134.128/25
216.58.192.0/19
198.2.136.0/23
207.58.147.64/28
198.2.180.0/24
216.22.15.224/27
130.211.0.0/22
205.201.131.128/25
198.2.178.0/23
103.2.140.0/22
198.2.145.0/24
198.2.177.0/24
198.2.128.0/24

IPv6 Networks found in the SPF record:
2800:3f0:4000::/36
2001:4860:4000::/36
2404:6800:4000::/36
2607:f8b0:4000::/36
2a00:1450:4000::/36
2c0f:fb50:4000::/36

Total number of IPv4 hosts: 343915
Total number of IPv6 hosts: 29710560942849126597578981376
Total number of hosts in the SPF record: 29710560942849126597579325291
