import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_apt_conf_file(host):
    f = host.file('/etc/apt/apt.conf.d/30proxy')

    assert f.exists
    assert f.content_string == 'Acquire::http::Proxy "http://10.0.0.2:3142";'
