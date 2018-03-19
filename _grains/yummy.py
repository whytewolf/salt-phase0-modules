from __future__ import absolute_import

import logging

log = logging.getLogger(__name__)

try:
    import yum
    HAS_YUM = True
except ImportError:
    HAS_YUM = False

__virtualname__ = 'yum'

def __virtual__():
    if HAS_YUM:
        return __virtualname__
    return False

def yummy():
    yb= yum.YumBase()
    yum_conf = {}
    yum_pkgs = {}
    yum_repos = []
    # Repos First
    for i in yb.repos.listEnabled():
        yum_repos[] = i

    yum_grains = {
            "conf": yum_conf,
            "pkgs": yum_pkgs,
            "repos": yum_repos
            }
    return {"yum": yum_grains}

