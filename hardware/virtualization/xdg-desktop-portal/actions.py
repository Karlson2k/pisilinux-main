#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2018 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.autoreconf("-fi")
    autotools.configure("--with-systemd=no \
                         --disable-geoclue \
                         --disable-docbook-docs \
                         --disable-libportal \
                         --with-systemduserunitdir=no \
                         --enable-pipewire")
#--with-systemduserunitdir=none \
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosed("%s/usr/share/dbus-1/services/*.service" % get.installDIR(), "SystemdService", deleteLine=True )

    pisitools.dodoc("COPYING", "README*", "NEWS")
