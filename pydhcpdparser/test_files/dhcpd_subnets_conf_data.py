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
  'options': {'broadcast-address': '10.198.134.127',
              'domain-name': '"some.domain.net"',
              'domain-name-servers': '10.24.199.136,10.24.199.137',
              'routers': '10.198.134.1'},
  'pool': {'failover': ('peer', '"az-dhcp-failover"'),
           'range': ('10.198.134.4', '10.198.134.126')},
  'subnet': '10.198.134.0'},
 {'netmask': '255.255.255.128',
  'options': {'broadcast-address': '10.198.133.127',
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
  'options': {'broadcast-address': '10.198.146.63',
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
exp_subnet_pool_failover_only = [{'netmask': '255.255.255.192',
  'options': {'broadcast-address': '10.198.146.63',
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
exp_subnet_pool_range_only = [{'netmask': '255.255.255.192',
  'options': {'broadcast-address': '10.198.146.63',
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
exp_subnet_pool_range_failover = [{'netmask': '255.255.255.192',
  'options': {'broadcast-address': '10.198.146.63',
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
  'options': {'broadcast-address': '10.198.146.63',
              'domain-name': '"some.domain.net"',
              'domain-name-servers': '10.24.199.136,10.24.199.137',
              'routers': '10.198.146.1'},
  'pool': {'failover': ('peer', '"az-dhcp-failover"'),
           'range': ('10.198.146.4', '10.198.146.62')},
  'subnet': '10.198.146.0'}]
