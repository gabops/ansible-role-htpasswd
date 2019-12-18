import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_passwd_file(host):
    f = host.file('/root/passwd')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.contains == 'john.doe'


def test_another_passwd_file(host):
    f = host.file('/opt/another_passwd_file')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.contains == 'devops'
