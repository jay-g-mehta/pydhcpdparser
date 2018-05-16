
"""
DHCPD Configuration parser
"""

import ply.lex
import ply.yacc


generic_tokens = (
    'IPADDR', 'SEMICOLON', 'BRACE_OPEN', 'BRACE_CLOSE', 'COMMA',
    'EQUAL',
    #'STRING_ENCLOSED_DOUBLE_QUOTE',
    'STRING'
)

ddns_tokens = (
    'ZONE',
    'PRIMARY',
    'KEY',
)

subnet_tokens = (
    'SUBNET', 'NETMASK', 'POOL', 'FAILOVER', 'PEER', 'RANGE',
    'OPTION', 'BROADCAST_ADDR', 'ROUTERS', 'DOMAIN_NAME_SERVERS', 'DOMAIN_NAME',
)

tokens = generic_tokens + ddns_tokens + subnet_tokens


t_ignore = ' \t'
t_EQUAL = '='
t_BRACE_OPEN = r'{'
t_BRACE_CLOSE = r'}'
t_SEMICOLON = ';'
t_COMMA = ','
t_ignore_COMMENT = r'[#][^\n]*'
t_STRING = r'[^{},;]+'


def t_ZONE(t):
    r'zone'
    return t


def t_PRIMARY(t):
    r'primary'
    return t


def t_KEY(t):
    r'key'
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


def t_IPADDR(t):
    r'([0-2]?[0-9]?[0-9][.]){3}[0-2]?[0-9]?[0-9]'
    return t


def STRING_ENCLOSED_DOUBLE_QUOTE(t):
    r'"([^"]|\\")*"'
    t.value = t.value[1:-1]
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
    '''
    p[0] = p[1]


def p_subnet_decl(p):
    ''' subnet_decl : SUBNET IPADDR NETMASK IPADDR subnet_block '''
    p[0] = {
        'subnet': p[2],
        'netmask': p[4],
    }
    p[0].update(p[5])


def p_subnet_block(p):
    ''' subnet_block : BRACE_OPEN pool_decl option_decls BRACE_CLOSE'''
    p[0] = {'pool': p[2], 'options': p[3]}


def p_pool_decl(p):
    ''' pool_decl : POOL BRACE_OPEN pool_content BRACE_CLOSE '''
    p[0] = p[3]


def p_pool_content(p):
    ''' pool_content : failover_stmt range_stmt
                     | range_stmt failover_stmt
                     | failover_stmt
                     | range_stmt
                     | empty
    '''
    p[0] = p[1]
    if len(p) > 2:
        p[0].update(p[2])


def p_failover_stmt(p):
    ''' failover_stmt : FAILOVER PEER STRING SEMICOLON'''
    p[0] = {p[1]: (p[2], p[3])}


def p_range_stmt(p):
    ''' range_stmt : RANGE IPADDR IPADDR SEMICOLON'''
    p[0] = {p[1]: (p[2], p[3])}


def p_option_decls(p):
    ''' option_decls : option_decl
                     | option_decl option_decls
    '''
    p[0] = dict(p[1])
    if len(p) > 2:
       p[0].update(p[2])


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
                 | IPADDR
                 | op_value COMMA op_value
    '''
    p[0] = "".join(p[1:])


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


def p_error(p):
    print("Syntax error in input!", p)
    # ply.yacc.errok()


ply.lex.lex(debug=0)
parser = ply.yacc.yacc(debug=0)
