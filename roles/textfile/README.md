Role Name
=========

Creates a .txt file on given path with given content.

Requirements
------------

None.

Role Variables
--------------

Requires 2 arguments:
  - textfile_path: relative/absolute path(str)
  - textfile_content: content(str)

Dependencies
------------

None.

Example Playbook
----------------

- name: Create a text file
  hosts: localhost
  connection: local
  roles:
  - role: my_own_namespace.yandex_cloud_elk.textfile
    vars:
      textfile_path: "/path/to/testfile.txt"
      textfile_content: "some content"

License
-------

MIT
