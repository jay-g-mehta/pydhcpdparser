one_host_stmt = """
host jbox {
    hardware ethernet 01:d0:06:b8:68:34;
    fixed-address 192.168.0.5;
    ddns-hostname "jbox";
    ddns-domainname "home";
    option host-name "jbox";
    option domain-name "home";
}
"""
exp_one_host_stmt = [
    {'host': {'jbox ': {
                         'ddns-domainname': '"home"',
                         'ddns-hostname': '"jbox"',
                         'fixed-address': '192.168.0.5',
                         'hardware': {'ethernet': '01:d0:06:b8:68:34'},
                         'option': {'domain-name': '"home"',
                                    'host-name': '"jbox"'}
                        }
              }
     }
]


one_host_stmt_with_host_identifier = """
host jbox {
    hardware ethernet 01:d0:06:b8:68:34;
    fixed-address6 2001:0db8:2a:1::5;
    ddns-hostname "jbox";
    ddns-domainname "home";
    option host-name "jbox";
    option domain-name "home";
    host-identifier option host-name "jbox";
    host-identifier option domain-name "dom";
}
"""
exp_one_host_stmt_with_host_identifier = [{}]


multi_host_stmts = """
host jbox {
    hardware ethernet 01:d0:06:b8:68:34;
    fixed-address 192.168.0.5;
    ddns-hostname "jbox";
    ddns-domainname "home";
    option host-name "jbox";
    option domain-name "home";
}
host pbox {
    hardware ethernet 01:d0:07:b9:67:44;
    fixed-address 192.168.0.25;
    ddns-hostname "pbox";
    ddns-domainname "home";
    option host-name "pbox";
    option domain-name "home";
}
"""
exp_multi_host_stmts = [
    {'host':
         {'jbox ': {'ddns-domainname': '"home"',
                    'ddns-hostname': '"jbox"',
                    'fixed-address': '192.168.0.5',
                    'hardware': {'ethernet': '01:d0:06:b8:68:34'},
                    'option': {'domain-name': '"home"',
                               'host-name': '"jbox"'}},
          'pbox ': {'ddns-domainname': '"home"',
                    'ddns-hostname': '"pbox"',
                    'fixed-address': '192.168.0.25',
                    'hardware': {'ethernet': '01:d0:07:b9:67:44'},
                    'option': {'domain-name': '"home"',
                               'host-name': '"pbox"'}}
          }
     }
]
