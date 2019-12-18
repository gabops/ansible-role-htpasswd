gabops.htpasswd
=========
[![Build Status](https://travis-ci.org/gabops/ansible-role-htpasswd.svg?branch=master)](https://travis-ci.org/gabops/ansible-role-htpasswd)

Configures htpasswd files.

Requirements
------------

None.

Role Variables
--------------

| Variable | Default value | Description |
| :--- | :--- | :--- |
| htpasswd_packages | "" | Defines the packages to be installed in order to make htpasswd to work. Please note that this role handles the packages to install already ( [Debian](./vars/Debian.yml), [RedHat](./vars/RedHat.yml)), however, this variable exist to allow you to overwrite if required. |
| htpasswd_enable_repo | "" | Defines the `yum` repo to be used when installing the htpasswd packages. |
| htpasswd_suppress_output | true | Defines if the output must be suppressed or not when configuring passwords. |
| htpasswd_files | [] | Defines the htpasswd file and users. Have a look to `Example playbook` to get an idea of the possible content of this variable. |

Dependencies
------------

None.

Example Playbook
----------------

```yaml
    - hosts: servers
      vars:
        htpasswd_files:
          - path: /root/passwd
            owner: root
            group: root
            mode: "0600"
            users:
              - username: john.doe
                password: 123456789

              - username: foo
                password: 123456789
                crypt_scheme: des_crypt

              - username: bar
                password: hello_world!
                crypt_scheme: plaintext

          - path: /opt/another_passwd_file
            owner: root
            group: root
            mode: "0700"
            users:
              - username: devops
                password: 123456789

              - username: engineers
                password: 123456789
                crypt_scheme: des_crypt

              - username: another_user
                password: p4ssw0rd!
                crypt_scheme: plaintext
      roles:
         - role: gabops.htpasswd
```

License
-------

[MIT]((./LICENSE))

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops))
