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
    yum_pkgs = pkgs = [{i.name: i.version} for i in  yb.doPackageLists('installed')]
    yum_repos = [str(i) for i in yb.repos.listEnabled()]
    # Repos First

    yum_grains = {
            "conf": yum_conf,
            "pkgs": yum_pkgs,
            "repos": yum_repos
            }
    return {"yum": yum_grains}

