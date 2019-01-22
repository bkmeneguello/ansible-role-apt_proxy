Ansible Role - APT Proxy
========================

An Ansible Role to configure APT Proxy

Requirements
------------

None.

Role Variables
--------------

    apt_cache_http_proxy:
    apt_cache_conf_file_priority: 30
    apt_cache_conf_file_suffix: proxy

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: all
  vars:
    apt_cache_http_proxy: http://10.0.0.2:3142
  roles:
     - bkmeneguello.apt_proxy
```

License
-------

MIT
