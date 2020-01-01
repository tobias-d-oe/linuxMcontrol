#!/usr/bin/env python

from distutils.core import setup
from setuptools.command.install import install
from subprocess import check_call


class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        check_call("systemctl daemon-reload".split())
        check_call("systemctl enable linuxMcontrol".split())
        install.run(self)

setup(name='linuxMcontrol',
      version='1.0',
      description='mcontrol Gateway server for Linux',
      author='Tobias D. Oestreicher',
      author_email='lists@oestreicher.com.de',
      url='https://github.com/tobias-d-oe/linuxMcontrol/',
      data_files=[('/etc/linuxMcontrol', ['conf/linuxMcontrol.cfg', 'conf/linuxMcontrolServer.xml']),
                  ('/usr/bin/', ['src/linuxMcontrolServer']),
                  ('/lib/systemd/system/', ['conf/linuxMcontrol.service'])],
      cmdclass={'install': PostInstallCommand,},
     )



