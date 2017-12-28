# -*- coding: utf-8 -*-
'''
Saltstack genesis 2: the reserection.
'''

from __future__ import absolute_import
import json
import logging

import salt.utils.event

log = logging.getLogger(__name__)

def start():
    '''
    Setup dnsmasq for pxe boot
    '''
    if __opts__['__role'] == 'master':
        event_bus = salt.utils.event.get_master_event(
                __opts__,
                __opts__['sock_dir'],
                listen=True)
        while True:
            event = event_bus.get_event()
            jevent = json.dumps(event)
            if event:
                log.debug(jevent)
    else:
        log.error('genesis_dhcp: this is only meant to run on master')
