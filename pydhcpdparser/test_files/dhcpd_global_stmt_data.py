global_stmts = """
abandon-lease-time 5000;
adaptive-lease-time-threshold 99;
always-broadcast on;
always-reply-rfc1048 off;
not authoritative;
boot-unknown-clients true;
db-time-format default;
ddns-domainname mydomain.net;
ddns-rev-domainname in-addr.arpa.;
ddns-update-style ad-hoc;
ddns-updates off;
default-lease-time 3600;
delayed-ack 28;
max-ack-delay 250000;
do-forward-updates on;
dynamic-bootp-lease-cutoff 0 2018/05/23 11:14:29;
dynamic-bootp-lease-length 200;
filename "ubuntu16.04.img";
get-lease-hostnames true;
infinite-is-reserved on;
lease-file-name test_dhcpd_lease.db;
limit-addrs-per-ia 2;
dhcpv6-lease-file-name test_dhcpv6_lease.db;
local-port 67;
local-address 10.20.21.39;
log-facility local7;
max-lease-time 86400;
min-lease-time 300;
min-secs 255;
next-server ftpserver1.mydomain.net;
omapi-port 9000;
one-lease-per-client true;
pid-file-name dhcpd.pid;
dhcpv6-pid-file-name dhcpdv6.pid;
ping-check true;
ping-timeout 1;
preferred-lifetime 1;
remote-port 68;
server-identifier dhcpd_1;
server-duid LLT;
server-name bootserver1;
dhcpv6-set-tee-times off;
site-option-space "pxelinux";
stash-agent-options true;
update-conflict-detection true;
update-optimization true;
update-static-leases true;
use-host-decl-names on;
use-lease-addr-for-default-route true;
vendor-option-space PXE;
option routers 204.254.239.1;
option domain-name-servers ns1.isc.org, ns2.isc.org;
"""

exp_global_stmts = [{'abandon-lease-time': '5000'},
    {'adaptive-lease-time-threshold': '99'},
    {'always-broadcast': 'on'},
    {'always-reply-rfc1048': 'off'},
    {'not authoritative': None},
    {'boot-unknown-clients': 'true'},
    {'db-time-format': 'default'},
    {'ddns-domainname': 'mydomain.net'},
    {'ddns-rev-domainname': 'in-addr.arpa.'},
    {'ddns-update-style': 'ad-hoc'},
    {'ddns-updates': 'off'},
    {'default-lease-time': '3600'},
    {'delayed-ack': '28'},
    {'max-ack-delay': '250000'},
    {'do-forward-updates': 'on'},
    {'dynamic-bootp-lease-cutoff': '0 2018/05/23 11:14:29'},
    {'dynamic-bootp-lease-length': '200'},
    {'filename': '"ubuntu16.04.img"'},
    {'get-lease-hostnames': 'true'},
    {'infinite-is-reserved': 'on'},
    {'lease-file-name': 'test_dhcpd_lease.db'},
    {'limit-addrs-per-ia': '2'},
    {'dhcpv6-lease-file-name': 'test_dhcpv6_lease.db'},
    {'local-port': '67'},
    {'local-address': '10.20.21.39'},
    {'log-facility': 'local7'},
    {'max-lease-time': '86400'},
    {'min-lease-time': '300'},
    {'min-secs': '255'},
    {'next-server': 'ftpserver1.mydomain.net'},
    {'omapi-port': '9000'},
    {'one-lease-per-client': 'true'},
    {'pid-file-name': 'dhcpd.pid'},
    {'dhcpv6-pid-file-name': 'dhcpdv6.pid'},
    {'ping-check': 'true'},
    {'ping-timeout': '1'},
    {'preferred-lifetime': '1'},
    {'remote-port': '68'},
    {'server-identifier': 'dhcpd_1'},
    {'server-duid': 'LLT'},
    {'server-name': 'bootserver1'},
    {'dhcpv6-set-tee-times': 'off'},
    {'site-option-space': '"pxelinux"'},
    {'stash-agent-options': 'true'},
    {'update-conflict-detection': 'true'},
    {'update-optimization': 'true'},
    {'update-static-leases': 'true'},
    {'use-host-decl-names': 'on'},
    {'use-lease-addr-for-default-route': 'true'},
    {'vendor-option-space': 'PXE'},
    {'option': {'routers': '204.254.239.1', 'domain-name-servers': 'ns1.isc.org,ns2.isc.org'}}]


db_time_local = """
db-time-format local;
"""
exp_db_time_local = [
    {'db-time-format': 'local'}
]

ddns_update_interim = """
ddns-update-style interim;
"""
exp_ddns_update_interim = [
    {'ddns-update-style': 'interim'}
]
