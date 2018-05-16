# pydhcpdparser

pydhcpdparser is a pure python based, DHCPD configuration parser.
Built using **ply**, lex and yacc parsing tool, pydhcpdparser can be used
to verify syntax of DHCPD configurations, parse and extract values from
configuration files and access them as python variables.

## Examples
If you input DHCPD configuration to pydhcpdparser as:
```
subnet 10.198.146.0 netmask 255.255.255.192 {
  pool {
     failover peer "az-dhcp-failover";
     range 10.198.146.4 10.198.146.62;
  }
  option routers 10.198.146.1;
  option broadcast-address 10.198.146.63;
  option domain-name "some.domain.net";
  option domain-name-servers 10.24.199.136,10.24.199.137;
}
```
**pydhcpdparser** verifies DHCPD syntax, parse and return back
pythonic result as:
```
[{'netmask': '255.255.255.192',
  'options': {'broadcast-address': '10.198.146.63',
              'domain-name': '"some.domain.net"',
              'domain-name-servers': '10.24.199.136,10.24.199.137',
              'routers': '10.198.146.1'},
  'pool': {'failover': ('peer', '"az-dhcp-failover"'),
           'range': ('10.198.146.4', '10.198.146.62')},
  'subnet': '10.198.146.0'}]
```

## Usage

```
import pydhcpdparser

conf = """
        subnet 10.198.146.0 netmask 255.255.255.192 {
          pool {
             failover peer "az-dhcp-failover";
             range 10.198.146.4 10.198.146.62;
          }
          option routers 10.198.146.1;
          option broadcast-address 10.198.146.63;
          option domain-name "some.domain.net";
          option domain-name-servers 10.24.199.136,10.24.199.137;
        }
"""
print pydhcpdparser.parse(conf)
```
OR
```
from pydhcpdparser import parse

conf = "zone 17.127.10.in-addr.arpa. { key DHCPUPDATE; }"
print parse(conf)
```

OR
```
from pydhcpdparser import *

with open("/etc/dhcp/dhcpd.conf) as f:
        conf = f.read()
        print parse(conf)
```


## Installing **pydhcpdparser**
```
pip install pydhcpdparser -r requirements.txt -r test-requirements.txt
```

## Supported configuration parser

1. Zone statements
2.  Subnet block declarations
3. Option statements

## Unit testing
```
python -m unittest discover
```
