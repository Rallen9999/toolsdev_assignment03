import logging

import pymel.core as pmc
from pymel.core.system import Path
from pymel.core.system import versions
import os


class SceneFile(object):
    def __init__(self, dir=''):
            self._dir = Path(dir)

    @property
    def dir(self):
        return self._dir

    @dir.setter
    def dir(self, val):
        self._dir = Path(val)

    def basename(self):
        """Returns the DCC scene file's name"""
        return name

    def path(self):
        """The function returns a path to scene file.
        This includes the drive letter, any directory path and the file name.
        Returns:
            Path: The path to the scene file.
        """
        return Path(self.dir) / self.basename()
