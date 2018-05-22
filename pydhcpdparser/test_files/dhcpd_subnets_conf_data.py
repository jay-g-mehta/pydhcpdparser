multi_subnets = """
subnet 10.198.134.0 netmask 255.255.255.128 {
    pool {
        failover peer "az-dhcp-failover";
        range 10.198.134.4 10.198.134.126;
    }
    option broadcast-address 10.198.134.127;
    option routers 10.198.134.1;
    option domain-name-servers 10.24.199.136,10.24.199.137;
    option domain-name "some.domain.net";
}
subnet 10.198.133.0 netmask 255.255.255.128 {
    pool {
        failover peer "az-dhcp-failover";
        range 10.198.133.4 10.198.133.126;
    }
    option broadcast-address 10.198.133.127;
    option routers 10.198.133.1;
    option domain-name-servers 10.24.199.136,10.24.199.137, 10.24.199.138;
    option domain-name "some.domain.net";
}
"""
exp_multi_subnet = [{'netmask': '255.255.255.128',
    'option': {'broadcast-address': '10.198.134.127',
               'domain-name': '"some.domain.net"',
               'domain-name-servers': '10.24.199.136,10.24.199.137',
               'routers': '10.198.134.1'},
    'pool': {'failover': ('peer', '"az-dhcp-failover"'),
             'range': ('10.198.134.4', '10.198.134.126')},
    'subnet': '10.198.134.0'},
    {'netmask': '255.255.255.128',
     'option': {'broadcast-address': '10.198.133.127',
                'domain-name': '"some.domain.net"',
                'domain-name-servers': '10.24.199.136,10.24.199.137,10.24.199.138',
                'routers': '10.198.133.1'},
     'pool': {'failover': ('peer', '"az-dhcp-failover"'),
              'range': ('10.198.133.4', '10.198.133.126')},
     'subnet': '10.198.133.0'}]


subnet_pool_empty_block = """
subnet 10.198.146.0 netmask 255.255.255.192 {
    pool {
    }
    option routers 10.198.146.1;
    option broadcast-address 10.198.146.63;
    option domain-name "some.domain.net";
    option domain-name-servers 10.24.199.136,10.24.199.137;
}
"""
exp_subnet_pool_empty_block = [{'netmask': '255.255.255.192',
    'option': {'broadcast-address': '10.198.146.63',
               'domain-name': '"some.domain.net"',
               'domain-name-servers': '10.24.199.136,10.24.199.137',
               'routers': '10.198.146.1'},
    'pool': {},
    'subnet': '10.198.146.0'}]


subnet_pool_failover_only = """
subnet 10.198.146.0 netmask 255.255.255.192 {
    pool {
        failover peer "az-dhcp-failover";
    }
    option routers 10.198.146.1;
    option broadcast-address 10.198.146.63;
    option domain-name "some.domain.net";
    option domain-name-servers 10.24.199.136,10.24.199.137;
}
"""
exp_subnet_pool_failover_only = [
    {'netmask': '255.255.255.192',
     'option': {'broadcast-address': '10.198.146.63',
                'domain-name': '"some.domain.net"',
                'domain-name-servers': '10.24.199.136,10.24.199.137',
                'routers': '10.198.146.1'},
     'pool': {'failover': ('peer', '"az-dhcp-failover"')},
     'subnet': '10.198.146.0'}]


subnet_pool_range_only = """
subnet 10.198.146.0 netmask 255.255.255.192 {
    pool {
        range 10.198.146.4 10.198.146.62;
    }
    option routers 10.198.146.1;
    option broadcast-address 10.198.146.63;
    option domain-name "some.domain.net";
    option domain-name-servers 10.24.199.136,10.24.199.137;
}
"""
exp_subnet_pool_range_only = [
    {'netmask': '255.255.255.192',
     'option': {'broadcast-address': '10.198.146.63',
                'domain-name': '"some.domain.net"',
                'domain-name-servers': '10.24.199.136,10.24.199.137',
                'routers': '10.198.146.1'},
     'pool': {'range': ('10.198.146.4', '10.198.146.62')},
     'subnet': '10.198.146.0'}]


subnet_pool_range_failover = """
subnet 10.198.146.0 netmask 255.255.255.192 {
    pool {
        range 10.198.146.4 10.198.146.62;
        failover peer "az-dhcp-failover";
    }
    option routers 10.198.146.1;
    option broadcast-address 10.198.146.63;
    option domain-name "some.domain.net";
    option domain-name-servers 10.24.199.136,10.24.199.137;
    }
"""
exp_subnet_pool_range_failover = [
    {'netmask': '255.255.255.192',
     'option': {'broadcast-address': '10.198.146.63',
                'domain-name': '"some.domain.net"',
                'domain-name-servers': '10.24.199.136,10.24.199.137',
                'routers': '10.198.146.1'},
     'pool': {'failover': ('peer', '"az-dhcp-failover"'),
              'range': ('10.198.146.4', '10.198.146.62')},
     'subnet': '10.198.146.0'}]


subnet_with_options = """
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
exp_subnet_with_options = [{'netmask': '255.255.255.192',
  'option': {'broadcast-address': '10.198.146.63',
             'domain-name': '"some.domain.net"',
             'domain-name-servers': '10.24.199.136,10.24.199.137',
             'routers': '10.198.146.1'},
  'pool': {'failover': ('peer', '"az-dhcp-failover"'),
           'range': ('10.198.146.4', '10.198.146.62')},
  'subnet': '10.198.146.0'}]


pool_with_allow = """
subnet 10.198.146.0 netmask 255.255.255.192 {
    pool {
        allow known-clients;
    }
}
"""
exp_pool_with_allow = [
    {'netmask': '255.255.255.192',
     'pool': {'allow': ['known-clients'], 'deny': []},
     'subnet': '10.198.146.0'}
]

pool_with_multi_allow = """
subnet 10.198.146.0 netmask 255.255.255.192 {
    pool {
        allow known-clients;
        allow unknown-clients;
    }

}
"""
exp_pool_with_multi_allow = [
    {'netmask': '255.255.255.192',
     'pool': {'allow': ['known-clients', 'unknown-clients'], 'deny': []},
     'subnet': '10.198.146.0'}
]


pool_with_exhaustive_allow = """
subnet 10.198.146.0 netmask 255.255.255.192 {
    pool {
        allow known-clients;
        allow unknown-clients;
        allow dynamic bootp clients;
        allow authenticated clients;
        allow unauthenticated clients;
        allow all clients;
        allow after 4 2007/08/24 09:14:32;
        allow members of "test-class";
    }
}
"""
exp_pool_with_exhaustive_allow = [
    {'netmask': '255.255.255.192',
     'pool': {'allow': ['known-clients',
                        'unknown-clients',
                        'dynamic bootp clients',
                        'authenticated clients',
                        'unauthenticated clients',
                        'all clients',
                        'after 4 2007/08/24 09:14:32',
                        'members of "test-class"'],
              'deny': []},
     'subnet': '10.198.146.0'}]


pool_with_exhaustive_deny = """
subnet 10.198.146.0 netmask 255.255.255.192 {
    pool {
        deny known-clients;
        deny unknown-clients;
        deny dynamic bootp clients;
        deny authenticated clients;
        deny unauthenticated clients;
        deny all clients;
        deny after 4 2007/08/24 09:14:32;
        deny members of "test-class";
    }
}
"""
exp_pool_with_exhaustive_deny = [
    {'netmask': '255.255.255.192',
     'pool': {'deny': ['known-clients',
                       'unknown-clients',
                       'dynamic bootp clients',
                       'authenticated clients',
                       'unauthenticated clients',
                       'all clients',
                       'after 4 2007/08/24 09:14:32',
                       'members of "test-class"'],
              'allow': []},
     'subnet': '10.198.146.0'}]


pool_with_allow_deny = """
subnet 10.198.146.0 netmask 255.255.255.192 {
    pool {
        deny known-clients;
        deny unknown-clients;
        deny dynamic bootp clients;
        allow authenticated clients;
        deny unauthenticated clients;
        allow all clients;
        deny after 4 2007/08/24 09:14:32;
        allow members of "test-class";
    }
}
"""
exp_pool_with_allow_deny = [
    {'netmask': '255.255.255.192',
     'pool': {'allow': ['authenticated clients',
                        'all clients',
                        'members of "test-class"'],
              'deny': ['known-clients',
                       'unknown-clients',
                       'dynamic bootp clients',
                       'unauthenticated clients',
                       'after 4 2007/08/24 09:14:32']},
     'subnet': '10.198.146.0'}]
