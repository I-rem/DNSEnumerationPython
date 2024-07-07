# DNS Enumeration With Python
Our goal is to perform zone transfer.
## Usage
`chmod +x DNS-AXFR.py`

`DNS-AXFR.py [options] -d <DOMAIN>`

## Options
`-h`, `--help`    show help message
 
`-d` **Domain:**        Target Domain. Example: inlanefreight.htb

`-n` **Nameserver:**    Nameservers separated by a comma. Example: ns1.inlanefreight.htb,ns2.inlanefreight.htb

`-v`               Prints the version of DNS-AXFR.py
  
**Example:** `./dns-axfr.py -d inlanefreight.com -n ns1.inlanefreight.com,ns2.inlanefreight.com`
## [dnspython](https://dnspython.readthedocs.io/en/latest/)
Dnspython is a DNS toolkit for Python. 

It can be used for queries, zone transfers, dynamic updates, nameserver testing, and many other things.
