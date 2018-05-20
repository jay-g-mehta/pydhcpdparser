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
