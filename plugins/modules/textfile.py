#!/usr/bin/python

# Copyright: (c) 2026, Mikhail Nikitin
# MIT
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: textfile

short_description: Creates a text file on the remote host

version_added: "1.0.0"

description: Creates a text file on the remote host, described in "path" argument with value from "content" argument.

options:
    path:
        description: Absolute path to the file that would be created
        required: true
        type: str
    content:
        description: Text that will be written in file
        required: true
        type: str

author:
    - Mikhail Nikitin (@MikhailNikitin99)
'''

EXAMPLES = r'''
# Creating a file and writting in it
- name: Create txt file
  my_own_namespace.yandex_cloud_elk.textfile:
      path: /path/to/file.txt
      content: "Hello world!"

'''

RETURN = r'''
changed:
    description: Check if the file was created or its content was changed
    type: bool
    returned: always
    sample: true
path:
    description: Path to the file.txt
    type: str
    returned: always
    sample: /path/to/file.txt
'''

import os
from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        path='',
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']
    path = os.path.expanduser(path)
    result['path'] = path

    old_content = None
    if os.path.exists(path):
        with open(path, 'r',encoding='utf-8') as file:
            old_content = file.read()

    if old_content != content:
        result['changed'] = True
        if not module.check_mode:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)

    module.exit_json(**result)

def main():
    run_module()


if __name__ == '__main__':
    main()
