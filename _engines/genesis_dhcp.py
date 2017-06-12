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
