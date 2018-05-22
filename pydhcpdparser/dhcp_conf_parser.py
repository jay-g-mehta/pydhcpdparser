"""
DHCPD Configuration parser
"""

import ply.lex
import ply.yacc


generic_tokens = (
    'IPADDR', 'SEMICOLON', 'BRACE_OPEN', 'BRACE_CLOSE', 'COMMA',
    'EQUAL',
    'STRING_ENCLOSED_DOUBLE_QUOTE',
    'STRING'
)

ddns_tokens = (
    'ZONE',
    'PRIMARY',
    'KEY',
    'ALGORITHM',
    'SECRET'
)

subnet_tokens = (
    'SUBNET', 'NETMASK', 'POOL', 'FAILOVER', 'PEER', 'RANGE',
    'OPTION', 'BROADCAST_ADDR', 'ROUTERS', 'DOMAIN_NAME_SERVERS', 'DOMAIN_NAME',
)

allow_deny_pool_ctxt_tokens = (
    'MEMBERS_OF',
    'KNOWN_CLIENTS',
    'UNKNOWN_CLIENTS',
    'DYNAMIC_BOOTP_CLIENTS',
    'AUTHENTICATED_CLIENTS',
    'UNAUTHENTICATED_CLIENTS',
    'ALL_CLIENTS',
    'AFTER',
    )

additional_tokens = ('INCLUDE', 'DYNAMIC_BOOTP',
                     'BOOTING', 'BOOTP', 'DUPLICATES',
                     'DECLINES', 'CLIENT_UPDATES', 'LEASEQUERY',
                     'ALLOW', 'DENY', 'IGNORE')


tokens = generic_tokens + ddns_tokens + subnet_tokens + allow_deny_pool_ctxt_tokens + additional_tokens


t_ignore = ' \t'
t_EQUAL = '='
t_BRACE_OPEN = r'{'
t_BRACE_CLOSE = r'}'
t_SEMICOLON = ';'
t_COMMA = ','
t_ignore_COMMENT = r'[#][^\n]*'
t_STRING = r'[^{},;]+'


def t_LEASEQUERY(t):
    r'leasequery'
    return t


def t_UNKNOWN_CLIENTS(t):
    r'unknown-clients'
    return t


def t_KNOWN_CLIENTS(t):
    r'known-clients'
    return t


def t_CLIENT_UPDATES(t):
    r'client-updates'
    return t


def t_UNAUTHENTICATED_CLIENTS(t):
    r'unauthenticated\ clients'
    return t


def t_AUTHENTICATED_CLIENTS(t):
    r'authenticated\ clients'
    return t


def t_ALL_CLIENTS(t):
    r'all\ clients'
    return t


def t_MEMBERS_OF(t):
    r'members\ of'
    return t


def t_DYNAMIC_BOOTP_CLIENTS(t):
    r'dynamic\ bootp\ clients'
    return t


def t_DYNAMIC_BOOTP(t):
    r'dynamic-bootp'
    return t


def t_INCLUDE(t):
    r'include'
    return t

def t_ZONE(t):
    r'zone'
    return t


def t_PRIMARY(t):
    r'primary'
    return t


def t_KEY(t):
    r'key'
    return t


def t_ALGORITHM(t):
    r'algorithm'
    return t


def t_SECRET(t):
    r'secret'
    return t


def t_SUBNET(t):
    r'subnet'
    return t


def t_NETMASK(t):
    r'netmask'
    return t


def t_POOL(t):
    r'pool'
    return t


def t_FAILOVER(t):
    r'failover'
    return t


def t_PEER(t):
    r'peer'
    return t


def t_RANGE(t):
    r'range'
    return t


def t_OPTION(t):
    r'option'
    return t


def t_BROADCAST_ADDR(t):
    r'broadcast-address'
    return t


def t_ROUTERS(t):
    r'routers'
    return t


def t_DOMAIN_NAME_SERVERS(t):
    r'domain-name-servers'
    return t


def t_DOMAIN_NAME(t):
    r'domain-name'
    return t


def t_AFTER(t):
    r'after'
    return t


def t_ALLOW(t):
    r'allow'
    return t


def t_DENY(t):
    r'deny'
    return t


def t_IGNORE(t):
    r'ignore'
    return t


def t_BOOTING(t):
    r'booting'
    return t


def t_BOOTP(t):
    r'bootp'
    return t


def t_DUPLICATES(t):
    r'duplicates'
    return t


def t_DECLINES(t):
    r'declines'
    return t


def t_IPADDR(t):
    r'([0-2]?[0-9]?[0-9][.]){3}[0-2]?[0-9]?[0-9]'
    return t


def t_STRING_ENCLOSED_DOUBLE_QUOTE(t):
    r'"([^"]|\\")*"'
    #t.value = t.value[1:-1]
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print t
    raise Exception("Lexical error at %r line %d" % (t.value, t.lineno))


def p_dhcp_conf(p):
    ''' dhcp_conf : stmt
                  | empty
                  | dhcp_conf stmt
    '''

    p[0] = p[1]
    if type(p[0]) != list:
        p[0] = [p[0]]
    if len(p) > 2:
       p[0].append(p[2])


def p_empty(p):
    ''' empty :
    '''
    p[0] = {}


def p_stmt(p):
    ''' stmt : subnet_decl
             | zone_decl
             | key_decl
             | include_stmt
             | allow_deny_ignore_in_scope_decls
    '''
    p[0] = p[1]


# Subnet block declaration
def p_subnet_decl(p):
    ''' subnet_decl : SUBNET IPADDR NETMASK IPADDR BRACE_OPEN subnet_block BRACE_CLOSE'''
    p[0] = {
        'subnet': p[2],
        'netmask': p[4],
    }
    p[0].update(p[6])


def p_subnet_block(p):
    ''' subnet_block : pool_decl
                     | option_decls
                     | pool_decl option_decls
                     | option_decls pool_decl
    '''
    p[0] = {}
    for i in range(1, len(p)):
        p[0].update(p[i])


# Pool block declaration
def p_pool_decl(p):
    ''' pool_decl : POOL BRACE_OPEN pool_content BRACE_CLOSE '''
    p[0] = {p[1]: p[3]}


def p_pool_content(p):
    ''' pool_content : failover_stmt pool_content
                     | range_stmt pool_content
                     | pool_allow_deny_decls pool_content
                     | empty
    '''
    p[0] = p[1]
    if len(p) > 2:
        p[0].update(p[2])


def p_failover_stmt(p):
    ''' failover_stmt : FAILOVER PEER STRING SEMICOLON
                      | FAILOVER PEER STRING_ENCLOSED_DOUBLE_QUOTE SEMICOLON
    '''
    p[0] = {p[1]: (p[2], p[3])}


def p_range_stmt(p):
    ''' range_stmt : RANGE range_addr_stmt SEMICOLON
                   | RANGE DYNAMIC_BOOTP range_addr_stmt SEMICOLON
    '''
    if len(p) > 4:
        p[0] = {p[1]: p[3]}
    else:
        p[0] = {p[1]: p[2]}


def p_range_addr_stmt(p):
    ''' range_addr_stmt : IPADDR
                        | IPADDR IPADDR
    '''
    if len(p) > 2:
        p[0] = (p[1], p[2])
    else:
        p[0] = (p[1], None)


# Pool allow deny declarations

def p_pool_allow_deny_decls(p):
    ''' pool_allow_deny_decls : pool_allow_deny_decl
                              | pool_allow_deny_decl pool_allow_deny_decls
    '''
    p[0] = {'allow': [], 'deny': []}

    if 'allow' in p[1]:
        p[0]['allow'].append(p[1]['allow'])
    if 'deny' in p[1]:
        p[0]['deny'].append(p[1]['deny'])

    if len(p) > 2:
        p[0]['allow'] = p[0]['allow'] + p[2]['allow']
        p[0]['deny'] = p[0]['deny'] + p[2]['deny']

    # Should we delete allow or deny from p[0] if it is  equal to []


def p_pool_allow_deny_decl(p):
    ''' pool_allow_deny_decl : ALLOW allow_deny_params_pool_ctxt SEMICOLON
                             | DENY allow_deny_params_pool_ctxt SEMICOLON
    '''
    p[0] = {p[1]: p[2]}


def p_allow_deny_params_pool_ctxt(p):
    ''' allow_deny_params_pool_ctxt : MEMBERS_OF STRING_ENCLOSED_DOUBLE_QUOTE
                                    | KNOWN_CLIENTS
                                    | UNKNOWN_CLIENTS
                                    | DYNAMIC_BOOTP_CLIENTS
                                    | AUTHENTICATED_CLIENTS
                                    | UNAUTHENTICATED_CLIENTS
                                    | ALL_CLIENTS
                                    | AFTER date_time
    '''
    p[0] = " ".join(p[1:])


def p_date_time(p):
    ''' date_time : STRING'''
    p[0] = p[1]


# option statements

def p_option_decls(p):
    ''' option_decls : option_decl
                     | option_decl option_decls
    '''
    p[0] = {'option': p[1]}
    if len(p) > 2:
        p[0]['option'].update(p[2]['option'])


def p_option_decl(p):
    ''' option_decl : OPTION option_expr SEMICOLON '''
    p[0] = p[2]


def p_option_expr(p):
    ''' option_expr : op_key op_value
                    | op_key EQUAL op_value
    '''
    if len(p) > 3:
        p[0] = {p[1]: p[3]}
    else:
        p[0] = {p[1]: p[2]}


def p_op_key(p):
    ''' op_key : BROADCAST_ADDR
               | ROUTERS
               | DOMAIN_NAME_SERVERS
               | DOMAIN_NAME '''
    p[0] = p[1]


def p_op_value(p):
    ''' op_value : STRING
                 | STRING_ENCLOSED_DOUBLE_QUOTE
                 | IPADDR
                 | op_value COMMA op_value
    '''
    p[0] = "".join(p[1:])


# Zone declarations

def p_zone_decl(p):
    ''' zone_decl : ZONE zone_name BRACE_OPEN zone_block BRACE_CLOSE '''
    tmp = {'name': p[2]}
    tmp.update(p[4])
    p[0] = {p[1]: tmp}


def p_zone_name(p):
    ''' zone_name : STRING '''
    p[0] = p[1]


def p_zone_block(p):
    ''' zone_block : dns_stmt
                   | ddns_key_stmt
                   | ddns_key_stmt dns_stmt
                   | dns_stmt ddns_key_stmt
                   | empty
    '''
    p[0] = {}
    for i in range(1, len(p)):
        p[0].update(p[i])


def p_dns_stmt(p):
    ''' dns_stmt : PRIMARY IPADDR SEMICOLON'''
    p[0] = {p[1]: p[2]}


def p_ddns_key_stmt(p):
    ''' ddns_key_stmt : KEY STRING SEMICOLON
    '''
    p[0] = {p[1]: p[2]}


# Key declaration block:

def p_key_decl(p):
    ''' key_decl : KEY STRING BRACE_OPEN key_decl_block BRACE_CLOSE SEMICOLON '''
    p[0] = {p[1]: p[2]}
    p[0].update(p[4])


def p_key_decl_block(p):
    ''' key_decl_block : algorithm_stmt secret_stmt
                       | secret_stmt algorithm_stmt
    '''
    p[0] = p[1]
    p[0].update(p[2])


def p_algorithm_stmt(p):
    ''' algorithm_stmt : ALGORITHM STRING SEMICOLON '''
    p[0] = {p[1]: p[2]}


def p_secret_stmt(p):
    ''' secret_stmt : SECRET STRING SEMICOLON'''
    p[0] = {p[1]: p[2]}


# Include statement:

def p_include_stmt(p):
    ''' include_stmt : INCLUDE inc_filename SEMICOLON '''
    p[0] = {p[1]: p[2]}


def p_inc_filename(p):
    ''' inc_filename : STRING_ENCLOSED_DOUBLE_QUOTE '''
    p[0] = p[1]


# ALLOW, DENY, IGNORE in scope

def p_allow_deny_ignore_in_scope_decls(p):
    ''' allow_deny_ignore_in_scope_decls : allow_deny_ignore_in_scope_decl
                                         | allow_deny_ignore_in_scope_decl allow_deny_ignore_in_scope_decls
    '''
    p[0] = {'allow': [], 'deny': [], 'ignore': []}

    if 'allow' in p[1]:
        p[0]['allow'].append(p[1]['allow'])
    if 'deny' in p[1]:
        p[0]['deny'].append(p[1]['deny'])
    if 'ignore' in p[1]:
        p[0]['ignore'].append(p[1]['ignore'])

    if len(p) > 2:
        p[0]['allow'] = p[0]['allow'] + p[2]['allow']
        p[0]['deny'] = p[0]['deny'] + p[2]['deny']
        p[0]['ignore'] = p[0]['ignore'] + p[2]['ignore']
    # Should we delete allow or deny from p[0] if it is  equal to []


def p_allow_deny_ignore_in_scope_decl(p):
    ''' allow_deny_ignore_in_scope_decl : ALLOW allow_deny_ignore_params_scope_ctxt SEMICOLON
                                        | DENY allow_deny_ignore_params_scope_ctxt SEMICOLON
                                        | IGNORE allow_deny_ignore_params_scope_ctxt SEMICOLON
                                        | ALLOW allow_deny_params_scope_ctxt SEMICOLON
                                        | DENY allow_deny_params_scope_ctxt SEMICOLON
    '''
    p[0] = {p[1]: p[2]}


def p_allow_deny_params_scope_ctxt(p):
    ''' allow_deny_params_scope_ctxt : DUPLICATES
                                     | CLIENT_UPDATES
                                     | LEASEQUERY
    '''
    p[0] = p[1]


def p_allow_deny_ignore_params_scope_ctxt(p):
    ''' allow_deny_ignore_params_scope_ctxt : UNKNOWN_CLIENTS
                                            | BOOTP
                                            | BOOTING
                                            | DECLINES
    '''
    p[0] = p[1]


def p_error(p):
    print("Syntax error in input!", p)
    # ply.yacc.errok()


ply.lex.lex(debug=0)
parser = ply.yacc.yacc(debug=0)
