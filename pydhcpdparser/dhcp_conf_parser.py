"""
DHCPD Configuration parser
"""

import ply.lex
import ply.yacc


generic_tokens = (
    'IPADDR', 'SEMICOLON', 'BRACE_OPEN', 'BRACE_CLOSE', 'COMMA',
    'EQUAL',
    'STRING_ENCLOSED_DOUBLE_QUOTE',
    'STRING',
    #'MULTI_CHARS'
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

host_tokens = ('HOST', 'HOST_NAME')

additional_tokens = ('INCLUDE', 'DYNAMIC_BOOTP',
                     'BOOTING', 'BOOTP', 'DUPLICATES',
                     'DECLINES', 'CLIENT_UPDATES', 'LEASEQUERY',
                     'ALLOW', 'DENY', 'IGNORE')

global_stmt_tokens = ('ABANDON_LEASE_TIME',
                      'ADAPTIVE_LEASE_TIME_THRESHOLD',
                      'ALWAYS_BROADCAST',
                      'ALWAYS_REPLY_RFC1048',
                      'AUTHORITATIVE',
                      'NOT_AUTHORITATIVE',
                      'BOOT_UNKNOWN_CLIENTS',
                      'DB_TIME_FORMAT',
                      'LOCAL',
                      'DEFAULT',
                      'DDNS_HOSTNAME',
                      'DDNS_DOMAINNAME',
                      'DDNS_REV_DOMAINNAME',
                      'DDNS_UPDATE_STYLE',
                      'AD_HOC',
                      'INTERIM',
                      'NONE',
                      'DDNS_UPDATES',
                      'DEFAULT_LEASE_TIME',
                      'DELAYED_ACK',
                      'MAX_ACK_DELAYED',
                      'DO_FORWARD_UPDATES',
                      'DYNAMIC_BOOTP_LEASE_CUTOFF',
                      'DYNAMIC_BOOTP_LEASE_LENGTH',
                      'FILENAME',
                      'FIXED_ADDRESS6',
                      'FIXED_ADDRESS',
                      'FIXED_PREFIX6',
                      'GET_LEASE_HOSTNAMES',
                      'HARDWARE',
                      'ETHERNET',
                      'TOKEN_RING',
                      'HOST_IDENTIFIER',
                      'INFINITE_IS_RESERVED',
                      'LEASE_FILE_NAME',
                      'LIMIT_ADDRS_PER_IA',
                      'DHCPV6_LEASE_FILE_NAME',
                      'LOCAL_PORT',
                      'LOCAL_ADDRESS',
                      'LOG_FACILITY',
                      'MAX_LEASE_TIME',
                      'MIN_LEASE_TIME',
                      'MIN_SECS',
                      'NEXT_SERVER',
                      'OMAPI_PORT',
                      'ONE_LEASE_PER_CLIENT',
                      'PID_FILE_NAME',
                      'DHCPV6_PID_FILE_NAME',
                      'PING_CHECK',
                      'PING_TIMEOUT',
                      'PREFERRED_LIFETIME',
                      'REMOTE_PORT',
                      'SERVER_IDENTIFIER',
                      'SERVER_DUID',
                      'SERVER_NAME',
                      'DHCPV6_SET_TEE_TIMES',
                      'SITE_OPTION_SPACE',
                      'STASH_AGENT_OPTIONS',
                      'UPDATE_CONFLICT_DETECTION',
                      'UPDATE_OPTIMIZATION',
                      'UPDATE_STATIC_LEASE',
                      'USE_HOST_DECL_NAMES',
                      'USE_LEASE_ADDR_FOR_DEFAULT_ROUTE',
                      'VENDOR_OPTION_SPACE',
                      'ON',
                      'OFF',
                      'TRUE',
                      'FALSE',
                      )

tokens = generic_tokens + ddns_tokens + subnet_tokens \
         + allow_deny_pool_ctxt_tokens + additional_tokens\
         + global_stmt_tokens + host_tokens


t_ignore = ' \t'
t_EQUAL = '='
t_BRACE_OPEN = r'{'
t_BRACE_CLOSE = r'}'
t_SEMICOLON = ';'
t_COMMA = ','
t_ignore_COMMENT = r'[#][^\n]*'
#t_MULTI_CHARS = r'[^{},;\ ]+'
t_STRING = r'[^{},;]+'


def t_USE_LEASE_ADDR_FOR_DEFAULT_ROUTE(t):
    r'use-lease-addr-for-default-route'
    return t


def t_ADAPTIVE_LEASE_TIME_THRESHOLD(t):
    r'adaptive-lease-time-threshold'
    return t


def t_DYNAMIC_BOOTP_LEASE_CUTOFF(t):
    r'dynamic-bootp-lease-cutoff'
    return t


def t_DYNAMIC_BOOTP_LEASE_LENGTH(t):
    r'dynamic-bootp-lease-length'
    return t


def t_UPDATE_CONFLICT_DETECTION(t):
    r'update-conflict-detection'
    return t


def t_UNAUTHENTICATED_CLIENTS(t):
    r'unauthenticated\ clients'
    return t


def t_AUTHENTICATED_CLIENTS(t):
    r'authenticated\ clients'
    return t


def t_DHCPV6_LEASE_FILE_NAME(t):
    r'dhcpv6-lease-file-name'
    return t


def t_DYNAMIC_BOOTP_CLIENTS(t):
    r'dynamic\ bootp\ clients'
    return t


def t_DHCPV6_SET_TEE_TIMES(t):
    r'dhcpv6-set-tee-times'
    return t


def t_ONE_LEASE_PER_CLIENT(t):
    r'one-lease-per-client'
    return t


def t_ALWAYS_REPLY_RFC1048(t):
    r'always-reply-rfc1048'
    return t


def t_DHCPV6_PID_FILE_NAME(t):
    r'dhcpv6-pid-file-name'
    return t


def t_INFINITE_IS_RESERVED(t):
    r'infinite-is-reserved'
    return t


def t_BOOT_UNKNOWN_CLIENTS(t):
    r'boot-unknown-clients'
    return t


def t_STASH_AGENT_OPTIONS(t):
    r'stash-agent-options'
    return t


def t_UPDATE_STATIC_LEASE(t):
    r'update-static-leases'
    return t


def t_USE_HOST_DECL_NAMES(t):
    r'use-host-decl-names'
    return t


def t_VENDOR_OPTION_SPACE(t):
    r'vendor-option-space'
    return t


def t_UPDATE_OPTIMIZATION(t):
    r'update-optimization'
    return t


def t_PREFERRED_LIFETIME(t):
    r'preferred-lifetime'
    return t


def t_LIMIT_ADDRS_PER_IA(t):
    r'limit-addrs-per-ia'
    return t


def t_ABANDON_LEASE_TIME(t):
    r'abandon-lease-time'
    return t


def t_DDNS_REV_DOMAINNAME(t):
    r'ddns-rev-domainname'
    return t


def t_GET_LEASE_HOSTNAMES(t):
    r'get-lease-hostnames'
    return t


def t_DEFAULT_LEASE_TIME(t):
    r'default-lease-time'
    return t


def t_DOMAIN_NAME_SERVERS(t):
    r'domain-name-servers'
    return t


def t_NOT_AUTHORITATIVE(t):
    r'not\ authoritative'
    return t


def t_SITE_OPTION_SPACE(t):
    r'site-option-space'
    return t


def t_SERVER_IDENTIFIER(t):
    r'server-identifier'
    return t


def t_ALWAYS_BROADCAST(t):
    r'always-broadcast'
    return t


def t_DDNS_UPDATE_STYLE(t):
    r'ddns-update-style'
    return t


def t_DO_FORWARD_UPDATES(t):
    r'do-forward-updates'
    return t


def t_LEASE_FILE_NAME(t):
    r'lease-file-name'
    return t


def t_DDNS_DOMAINNAME(t):
    r'ddns-domainname'
    return t


def t_UNKNOWN_CLIENTS(t):
    r'unknown-clients'
    return t


def t_HOST_IDENTIFIER(t):
    r'host-identifier'
    return t


def t_CLIENT_UPDATES(t):
    r'client-updates'
    return t


def t_FIXED_ADDRESS6(t):
    r'fixed-address6'
    return t


def t_MAX_ACK_DELAYED(t):
    r'max-ack-delay'
    return t


def t_MAX_LEASE_TIME(t):
    r'max-lease-time'
    return t


def t_MIN_LEASE_TIME(t):
    r'min-lease-time'
    return t


def t_DDNS_HOSTNAME(t):
    r'ddns-hostname'
    return t


def t_PID_FILE_NAME(t):
    r'pid-file-name'
    return t


def t_DB_TIME_FORMAT(t):
    r'db-time-format'
    return t


def t_FIXED_ADDRESS(t):
    r'fixed-address'
    return t


def t_KNOWN_CLIENTS(t):
    r'known-clients'
    return t


def t_LOCAL_ADDRESS(t):
    r'local-address'
    return t


def t_DDNS_UPDATES(t):
    r'ddns-updates'
    return t


def t_LOG_FACILITY(t):
    r'log-facility'
    return t


def t_BROADCAST_ADDR(t):
    r'broadcast-address'
    return t


def t_AUTHORITATIVE(t):
    r'authoritative'
    return t


def t_DYNAMIC_BOOTP(t):
    r'dynamic-bootp'
    return t


def t_PING_TIMEOUT(t):
    r'ping-timeout'
    return t


def t_FIXED_PREFIX6(t):
    r'fixed-prefix6'
    return t


def t_REMOTE_PORT(t):
    r'remote-port'
    return t


def t_DELAYED_ACK(t):
    r'delayed-ack'
    return t


def t_LOCAL_PORT(t):
    r'local-port'
    return t


def t_TOKEN_RING(t):
    r'token-ring'
    return t


def t_SERVER_NAME(t):
    r'server-name '
    return t


def t_MIN_SECS(t):
    r'min-secs'
    return t


def t_SERVER_DUID(t):
    r'server-duid'
    return t


def t_NEXT_SERVER(t):
    r'next-server'
    return t


def t_OMAPI_PORT(t):
    r'omapi-port'
    return t


def t_PING_CHECK(t):
    r'ping-check'
    return t


def t_ALL_CLIENTS(t):
    r'all\ clients'
    return t


def t_MEMBERS_OF(t):
    r'members\ of'
    return t


def t_DOMAIN_NAME(t):
    r'domain-name'
    return t


def t_HOST_NAME(t):
    r'host-name'
    return t


def t_FILENAME(t):
    r'filename'
    return t


def t_HARDWARE(t):
    r'hardware'
    return t


def t_ETHERNET(t):
    r'ethernet'
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


def t_ROUTERS(t):
    r'routers'
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


def t_AD_HOC(t):
    r'ad-hoc'
    return t


def t_INTERIM(t):
    r'interim'
    return t


def t_LEASEQUERY(t):
    r'leasequery'
    return t


def t_LOCAL(t):
    r'local'
    return t


def t_DEFAULT(t):
    r'default'
    return t


def t_HOST(t):
    r'host'
    return t


def t_ON(t):
    r'on'
    return t


def t_OFF(t):
    r'off'
    return t


def t_TRUE(t):
    r'true'
    return t


def t_FALSE(t):
    r'false'
    return t


def t_NONE(t):
    r'none'
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
             | global_stmt
             | host_blocks
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
               | DOMAIN_NAME
               | HOST_NAME
    '''
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


# global statements

def p_global_stmt(p):
    ''' global_stmt : global_param_value SEMICOLON'''
    p[0] = p[1]


def p_global_param_value(p):
    ''' global_param_value : global_param_str str_value
                           | global_param_str IPADDR
                           | global_param_flag global_param_flag_value
                           | DB_TIME_FORMAT DEFAULT
                           | DB_TIME_FORMAT LOCAL
                           | DDNS_UPDATE_STYLE AD_HOC
                           | DDNS_UPDATE_STYLE INTERIM
                           | DDNS_UPDATE_STYLE NONE
                           | global_param_no_val
    '''
    if len(p) > 2:
        p[0] = {p[1]: p[2]}
    else:
        p[0] = {p[1]: None}


def p_global_param_no_val(p):
    ''' global_param_no_val : AUTHORITATIVE
                            | NOT_AUTHORITATIVE
    '''
    p[0] = p[1]


def p_global_param_str(p):
    ''' global_param_str : ABANDON_LEASE_TIME
                         | ADAPTIVE_LEASE_TIME_THRESHOLD
                         | DDNS_DOMAINNAME
                         | DDNS_REV_DOMAINNAME
                         | DEFAULT_LEASE_TIME
                         | DELAYED_ACK
                         | MAX_ACK_DELAYED
                         | DYNAMIC_BOOTP_LEASE_CUTOFF
                         | DYNAMIC_BOOTP_LEASE_LENGTH
                         | FILENAME
                         | LEASE_FILE_NAME
                         | LIMIT_ADDRS_PER_IA
                         | DHCPV6_LEASE_FILE_NAME
                         | LOCAL_PORT
                         | LOCAL_ADDRESS
                         | LOG_FACILITY
                         | MAX_LEASE_TIME
                         | MIN_LEASE_TIME
                         | MIN_SECS
                         | NEXT_SERVER
                         | OMAPI_PORT
                         | PID_FILE_NAME
                         | DHCPV6_PID_FILE_NAME
                         | PING_TIMEOUT
                         | PREFERRED_LIFETIME
                         | REMOTE_PORT
                         | SERVER_IDENTIFIER
                         | SERVER_DUID
                         | SERVER_NAME
                         | SITE_OPTION_SPACE
                         | VENDOR_OPTION_SPACE
    '''
    p[0] = p[1]


def p_global_param_flag(p):
    ''' global_param_flag : ALWAYS_BROADCAST
                          | ALWAYS_REPLY_RFC1048
                          | BOOT_UNKNOWN_CLIENTS
                          | DDNS_UPDATES
                          | DO_FORWARD_UPDATES
                          | GET_LEASE_HOSTNAMES
                          | ONE_LEASE_PER_CLIENT
                          | INFINITE_IS_RESERVED
                          | PING_CHECK
                          | DHCPV6_SET_TEE_TIMES
                          | STASH_AGENT_OPTIONS
                          | UPDATE_CONFLICT_DETECTION
                          | UPDATE_OPTIMIZATION
                          | UPDATE_STATIC_LEASE
                          | USE_HOST_DECL_NAMES
                          | USE_LEASE_ADDR_FOR_DEFAULT_ROUTE
    '''
    p[0] = p[1]


def p_global_param_flag_value(p):
    ''' global_param_flag_value : ON
                                | OFF
                                | TRUE
                                | FALSE
    '''
    p[0] = p[1]


# host statement
def p_host_blocks(p):
    ''' host_blocks : host_block_decl
                    | host_block_decl host_blocks
    '''
    p[0] = p[1]
    if len(p) > 2:
        p[0]['host'].update(p[2]['host'])


def p_host_block_decl(p):
    ''' host_block_decl : HOST STRING BRACE_OPEN host_stmts BRACE_CLOSE'''
    p[0] = {p[1]: {p[2]: p[4]}}


def p_host_stmts(p):
    ''' host_stmts : host_stmt
                   | host_stmt host_stmts
    '''
    p[0] = p[1]
    if len(p) > 2:
        p[0].update(p[2])


def p_host_stmt(p):
    ''' host_stmt : host_param_value SEMICOLON
                  | option_decls
                  | host_identifier_option_decls
    '''
    p[0] = p[1]


def p_host_identifier_option_decls(p):
    ''' host_identifier_option_decls : HOST_IDENTIFIER option_decl
                                     | HOST_IDENTIFIER option_decl host_identifier_option_decls
    '''
    p[0] = {p[1]: p[2]}
    if len(p) > 3:
        p[0][p[1]].update(p[3][p[1]])


def p_host_param_value(p):
    ''' host_param_value : ALWAYS_REPLY_RFC1048 global_param_flag_value
                         | DDNS_HOSTNAME str_value
                         | DDNS_DOMAINNAME str_value
                         | FIXED_ADDRESS IPADDR
                         | FIXED_ADDRESS6 str_value
                         | FIXED_PREFIX6 str_value
                         | HARDWARE ETHERNET str_value
                         | HARDWARE TOKEN_RING str_value
    '''

    len_p = len(p)
    if len_p == 5:
        p[0] = {p[1]: {p[2]: {p[3]: p[4]}}}
    elif len_p == 4:
        p[0] = {p[1]: {p[2]: p[3]}}
    elif len_p == 3:
        p[0] = {p[1]: p[2]}
    else:
        p[0] = {p[1]: None}


# General used string value function
def p_str_value(p):
    ''' str_value : STRING
                  | STRING_ENCLOSED_DOUBLE_QUOTE
    '''
    p[0] = p[1]


def p_str_value_error(p):
    ''' str_value : error STRING
                  | error STRING_ENCLOSED_DOUBLE_QUOTE
    '''
    print("Trying to handle error!", p[1])
    if p[1].type in tokens:
        parser.errok()
        p[0] = p[1].value + p[2]
        print "Error probably handled"
    else:
        print "Exception at handling Syntax error in input "
        p_error(p[1])
        raise SyntaxError


def p_error(p):
    print("Syntax error in input!", p)
    # parser.errok()
    # ply.yacc.errok()


ply.lex.lex(debug=0)
parser = ply.yacc.yacc(debug=0)
