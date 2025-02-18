#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


def setup():
    shelltools.export("PYTHON", "/usr/bin/python3")
    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-fiv")
    autotools.configure("--disable-static \
                         --prefix=/usr \
                         --with-x \
                         --enable-nls \
                         --sysconfdir=/etc \
                         --libexecdir=/usr/lib/openbox \
                         --enable-startup-notification \
                         --docdir=/%s/%s" % (get.docDIR(), get.srcNAME()))

    pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    # GNOME Panel is no longer available in the official repositories
    pisitools.remove("/usr/bin/gdm-control")
    pisitools.remove("/usr/bin/gnome-panel-control")
    pisitools.remove("/usr/bin/openbox-gnome-session")
    pisitools.remove("/usr/share/man/man1/openbox-gnome-session.1")
    pisitools.remove("/usr/share/xsessions/openbox-gnome.desktop")
    pisitools.removeDir("/usr/share/gnome-session")

    pisitools.dodoc("AUTHORS", "CHANGELOG", "COPYING", "README")
