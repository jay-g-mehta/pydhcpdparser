from unittest import TestCase
import ddt
from . import dhcp_conf_parser
from test_files.dhcpd_subnets_conf_data import *


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
