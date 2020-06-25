Ansible role for cmake
==================================

Installs cmake

[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-cmake/workflows/Molecule%20Test/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-cmake/actions?query=workflow%3A%22Molecule+Test%22)
[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-cmake/workflows/Release/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-cmake/actions?query=workflow%3A%22Release%22)

Requirements
------------

None

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| `cmake_version` | Version of cmake to download | string | "" | `true` |

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-cmake
      vars:
        cmake_version: v3.16.8
```

License
-------

[Apache License](LICENSE)
