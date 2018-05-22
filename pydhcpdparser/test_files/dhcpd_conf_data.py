key_decl = """
key DHCP_UPDATER{
algorithm HMAC-MD5.SIG-ALG.REG.INT;
secret pRP5FapFoJ95JEL06sv4PQ==;
};
"""
exp_key_decl = [
    {'key': 'DHCP_UPDATER',
     'algorithm': 'HMAC-MD5.SIG-ALG.REG.INT',
     'secret': 'pRP5FapFoJ95JEL06sv4PQ=='}
]

multi_key_decl = """
key DHCP_UPDATE1{
algorithm HMAC-MD5.SIG-ALG.REG.INT;
secret pRP5FapFoJ95JEL06sv4PQ==;
};
key DHCP_UPDATE2{
algorithm HMAC-MD5.SIG-ALG.REG.INT;
secret MoFijkoJ00897L06sJay==;
};
"""
exp_multi_key_decl = [
    {'key': 'DHCP_UPDATE1',
     'algorithm': 'HMAC-MD5.SIG-ALG.REG.INT',
     'secret': 'pRP5FapFoJ95JEL06sv4PQ=='},
    {'key': 'DHCP_UPDATE2',
     'algorithm': 'HMAC-MD5.SIG-ALG.REG.INT',
     'secret': 'MoFijkoJ00897L06sJay=='}
]

# DATA for allow in scope context

allow_decl = """
allow declines;
"""
exp_allow_decl = [
    {
        'allow': ['declines'],
        'deny': [],
        'ignore': []
    }
]


allow_all_decl = """
allow unknown-clients;
allow bootp;
allow booting;
allow duplicates;
allow declines ;
allow client-updates;
allow leasequery ;
"""
exp_allow_all_decl = [
    {
        'allow': ['unknown-clients', 'bootp', 'booting',
                   'duplicates', 'declines',
                   'client-updates', 'leasequery'],
        'deny': [],
        'ignore': []
    }
]


# DATA for deny in scope context

deny_decl = """
deny declines;
"""
exp_deny_decl = [
    {
        'deny': ['declines'],
        'allow': [],
        'ignore': []
    }
]


deny_all_decl = """
deny unknown-clients;
deny bootp;
deny booting;
deny duplicates;
deny declines ;
deny client-updates;
deny leasequery ;
"""
exp_deny_all_decl = [
    {
        'deny': ['unknown-clients', 'bootp', 'booting',
                 'duplicates', 'declines',
                 'client-updates', 'leasequery'],
        'allow': [],
        'ignore': []
    }
]

# DATA for ignore in scope context

ignore_decl = """
ignore unknown-clients;
"""
exp_ignore_decl = [
    {
        'ignore': ['unknown-clients'],
        'allow': [],
        'deny': []
    }
]


ignore_all_decl = """
ignore unknown-clients;
ignore bootp;
ignore booting;
ignore declines ;
"""
exp_ignore_all_decl = [
    {
        'ignore': ['unknown-clients', 'bootp', 'booting',
                   'declines'],
        'allow': [],
        'deny': []
    }
]

allow_deny_ignore_decl = """
allow unknown-clients;
allow bootp;
deny duplicates;
deny client-updates;
deny leasequery ;
ignore booting;
ignore declines ;
"""
exp_allow_deny_ignore_decl = [
    {
        'ignore': ['booting', 'declines'],
        'allow': ['unknown-clients', 'bootp'],
        'deny': ['duplicates', 'client-updates', 'leasequery']
    }
]
