import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_makeinfo_in_path(host):
    assert host.exists("cmake")
    cmd = host.run("cmake --version")
    assert cmd.succeeded
