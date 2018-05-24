from unittest import TestCase
import ddt
from . import dhcp_conf_parser
from test_files.dhcpd_subnets_conf_data import *
from test_files.dhcpd_conf_data import *
from test_files.dhcpd_global_stmt_data import *
from test_files.dhcpd_host_stmt_data import *


@ddt.ddt
class TestDHCPConfParser(TestCase):

    @ddt.file_data("test_files/dhcpd_zone_conf.json")
    def test_zone_stmt(self, conf, exp):
        value = dhcp_conf_parser.parser.parse(conf)
        self.assertEqual(exp, str(value))

    @ddt.data((multi_subnets, exp_multi_subnet),
              (subnet_pool_empty_block, exp_subnet_pool_empty_block),
              (subnet_pool_failover_only, exp_subnet_pool_failover_only),
              (subnet_pool_range_only, exp_subnet_pool_range_only),
              (subnet_pool_range_failover, exp_subnet_pool_range_failover),
              (subnet_with_options, exp_subnet_with_options)
    )
    @ddt.unpack
    def test_subnet_stmt(self, conf, exp):
        value = dhcp_conf_parser.parser.parse(conf)
        self.assertEqual(exp, value)

    @ddt.data((key_decl, exp_key_decl),
              (multi_key_decl, exp_multi_key_decl),)
    @ddt.unpack
    def test_key_decl(self, conf, exp):
        value = dhcp_conf_parser.parser.parse(conf)
        self.assertEqual(exp, value)

    @ddt.data({'conf': 'include "dhcp_other_file.conf" ;',
               'exp': [{'include': '"dhcp_other_file.conf"'}]}
    )
    @ddt.unpack
    def test_include_stmt(self, conf, exp):
        value = dhcp_conf_parser.parser.parse(conf)
        self.assertEqual(exp, value)

    @ddt.data((pool_with_allow, exp_pool_with_allow),
              (pool_with_multi_allow, exp_pool_with_multi_allow),
              (pool_with_exhaustive_allow, exp_pool_with_exhaustive_allow),
              (pool_with_exhaustive_deny, exp_pool_with_exhaustive_deny),
              (pool_with_allow_deny, exp_pool_with_allow_deny)
    )
    @ddt.unpack
    def test_allow_deny_pool_ctxt(self, conf, exp):
        value = dhcp_conf_parser.parser.parse(conf)
        self.assertEqual(exp, value)

    @ddt.data((allow_decl, exp_allow_decl),
              (allow_all_decl, exp_allow_all_decl),
              (deny_decl, exp_deny_decl),
              (deny_all_decl, exp_deny_all_decl),
              (ignore_decl, exp_ignore_decl),
              (ignore_all_decl, exp_ignore_all_decl),
              (allow_deny_ignore_decl, exp_allow_deny_ignore_decl)
    )
    @ddt.unpack
    def test_allow_deny_ignore_scope_ctxt(self, conf, exp):
        value = dhcp_conf_parser.parser.parse(conf)
        self.assertEqual(exp, value)

    @ddt.data((global_stmts, exp_global_stmts),
              (db_time_local, exp_db_time_local),
              (ddns_update_interim, exp_ddns_update_interim)
    )
    @ddt.unpack
    def test_global_stmts(self, conf, exp):
        value = dhcp_conf_parser.parser.parse(conf)
        self.assertEqual(exp, value)

    @ddt.data((one_host_stmt, exp_one_host_stmt),
              #(one_host_stmt_with_host_identifier, exp_one_host_stmt_with_host_identifier),
              (multi_host_stmts, exp_multi_host_stmts)
    )
    @ddt.unpack
    def test_host_stmts(self, conf, exp):
        value = dhcp_conf_parser.parser.parse(conf)
        self.assertEqual(exp, value)
