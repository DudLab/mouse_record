__author__ = "Bailey Nozomu Hwa <hwab@janelia.hhmi.org>"
__date__ = "$Aug 10, 2015, 3:47 PM$"

import os
import ctypes
import shutil
import tempfile
import threading
import mock

import mouse
from mouse.record import main


class TestRecord(object):
    def setup(self):
        self.cwd = os.getcwd()
        self.tempdir = ""
        self.tempdir = tempfile.mkdtemp()
        os.chdir(self.tempdir)

        print("tempdir = \"%s\"" % self.tempdir)

    def teardown(self):
        os.chdir(self.cwd)
        shutil.rmtree(self.tempdir)
        self.tempdir = ""
        self.cwd = ""

    @mock.patch("mouse.record.Trigger")
    def test_main_0(self, mock_class):
        mock_class.wait = lambda _: time.sleep(1)

        t = threading.Thread(target=main, args=(
            "",
            "1",
            "1",
            "."
        ))
        t.daemon = True
        t.start()
        t.join(2)
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(t.ident), ctypes.py_object(KeyboardInterrupt))

        filenames = []
        for each_filename in os.listdir(self.tempdir):
            filenames.append(os.path.join(self.tempdir, each_filename))
        filenames.sort()
        print(filenames)

        assert len(filenames) == 1
        assert ".h264" in filenames[0]
