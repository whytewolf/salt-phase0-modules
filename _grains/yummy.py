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
    # Grab package list and parse it into nice clean list
    yum_pkgs = [{pkg.name: pkg.version} for pkg in  yb.doPackageLists('installed')]
    # grab enabled repo list
    yum_repos = [str(repo) for repo in yb.repos.listEnabled()]
    yum_grains = {
            "pkgs": yum_pkgs,
            "repos": yum_repos
            }
    return {"yum": yum_grains}
