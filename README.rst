==============
pydhcpdparser
==============

**pydhcpdparser** is a pure python based, DHCPD configuration parser.
Built using **ply**, lex and yacc parsing tool, pydhcpdparser can be used
to verify syntax of DHCPD configurations, parse and extract values from
configuration files and access them as python variables.

Examples
---------
If you input DHCPD configuration to pydhcpdparser as

::

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

**pydhcpdparser** verifies DHCPD syntax, parse and return back
pythonic result as

::

    [{'netmask': '255.255.255.192',
     'option': {'broadcast-address': '10.198.146.63',
                'domain-name': '"some.domain.net"',
                'domain-name-servers': '10.24.199.136,10.24.199.137',
                'routers': '10.198.146.1'},
     'pool': {'failover': ('peer', '"az-dhcp-failover"'),
              'range': ('10.198.146.4', '10.198.146.62')},
     'subnet': '10.198.146.0'}]


Usage
-----

.. code:: python

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
    print pydhcpdparser.parser.parse(conf)


OR

.. code:: python

    from pydhcpdparser import parser

    conf = "zone 17.127.10.in-addr.arpa. { key DHCPUPDATE; }"
    print parser.parse(conf)


OR

.. code:: python

    from pydhcpdparser import *

    with open("/etc/dhcp/dhcpd.conf) as f:
        conf = f.read()
        print parser.parse(conf)


Installing **pydhcpdparser**
----------------------------

.. code:: bash

    $ pip install pydhcpdparser


Development installation **pydhcpdparser**
-------------------------------------------

.. code:: bash

    $ pip install pydhcpdparser -r test-requirements.txt


Supported configuration parser
------------------------------

1. Subnet statements

   ::

     subnet subnet-number netmask netmask {
       [ parameters ]
       [ declarations ]
     }

2. pool declaration

3. range statement
   ::

     range [ dynamic-bootp ] low-address [ high-address];

4. Option statements
   ::

     option name value1[, value2...];

5. Zone declaration

6. Key declaration
   ::

     key name {
         algorithm algo;
         secret value;
     };

7. Include statement
   ::

     include "filename";

8. Allow and Deny declarations within pool declarations
   ::

     known-clients;
     unknown-clients;
     dynamic bootp clients;
     authenticated clients;
     unauthenticated clients;
     all clients;
     after time;
     members of "class";

9. Allow, Deny and Ignore declarations at global scope
   ::

     unknown-clients
     bootp
     duplicates
     client-updates
     leasequery
     booting
     declines

10. Global parameters declaration statement
   ::

     adandon-lease-time time;
     adaptive-lease-time-threshold percentage;
     always-broadcast flag;
     always-reply-rfc1048 flag;
     authoritative;
     not authoritative;
     boot-unknown-clients flag;
     db-time-format [ default | local ] ;
     ddns-domainname name;
     ddns-rev-domainname name;
     ddns-update-style style;
     ddns-updates flag;
     default-lease-time time;
     delayed-ack count;
     max-ack-delay microseconds;
     do-forward-updates flag;
     dynamic-bootp-lease-cutoff date;
     dynamic-bootp-lease-length length;
     filename "filename";
     get-lease-hostnames flag;
     infinite-is-reserved flag;
     lease-file-name name;
     limit-addrs-per-ia number;
     dhcpv6-lease-file-name name;
     local-port port;
     local-address address;
     log-facility facility;
     max-lease-time time;
     min-lease-time time;
     min-secs seconds;
     next-server server-name;
     omapi-port port;
     one-lease-per-client flag;
     pid-file-name name;
     dhcpv6-pid-file-name name;
     ping-check flag;
     ping-timeout seconds;
     preferred-lifetime seconds;
     remote-port port;
     server-identifier hostname;
     server-duid LLT [ hardware-type timestamp hardware-address ] ;
     server-duid EN enterprise-number enterprise-identifier ;
     server-duid LL [ hardware-type hardware-address ] ;
     server-name name ;
     dhcpv6-set-tee-times flag;
     site-option-space name ;
     stash-agent-options flag;
     update-conflict-detection flag;
     update-optimization flag;
     update-static-leases flag;
     use-host-decl-names flag;
     use-lease-addr-for-default-route flag;
     vendor-option-space string;


11. Host block declaration statements
   ::

     always-reply-rfc1048 flag;
     ddns-hostname name;
     ddns-domainname name;
     fixed-address address [, address ... ];
     fixed-address6 ip6-address ;
     fixed-prefix6 low-address / bits;
     hardware hardware-type hardware-address;



Unit testing
-------------

.. code:: bash

    $ python -m unittest discover
