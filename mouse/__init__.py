"""
``Mouse Recorder`` package, a cheap, modular, behavior recording program

===============================================================================
Overview
===============================================================================

The ``Mouse Recorder`` package is designed for the ease of recording and
singling out desired behavior of rodents, namely the events of interest in
reward-stimulus studies. Using these events as triggers (e.g., the press
of a lever), the program records the user-specified time before and after
a desired event. In addition to its primary recording feature, the package
contains two auxiliary programs that provide a preview of the camera and take a
photo of the background for ease of setup purposes. Additionally, the package
operates on a Raspberry Pi-based system, providing a cheaper alternative than
conventional recording apparatus used in behavioral studies.

===============================================================================
Standard Install
===============================================================================

To install, use standard python installation procedure:

.. code-block:: sh

    python setup.py install

Additionally, the program requires installation of _setuptools

===============================================================================
Development
===============================================================================

-------------------------------------------------------------------------------
Installing
-------------------------------------------------------------------------------
Enter the following into the terminal to install the program:

.. code-block:: sh

    git clone https://github.com/bnhwa/mouse_record
    python setup.py develop

-------------------------------------------------------------------------------
Updating
-------------------------------------------------------------------------------
To update the program, first specify the directory to where the `mouse_record`
file is saved to. Then, enter the ``git pull`` command.
An example is provided as follows:

.. code-block:: sh

    git pull

This will ensure that the software is up-to-date.

-------------------------------------------------------------------------------
Uninstalling
-------------------------------------------------------------------------------
Enter the following into the terminal to install the program:

.. code-block:: sh

    python setup.py develop --uninstall

===============================================================================
Testing
===============================================================================

When testing the program, the user should move to the directory to where
the ``mouse_record`` file is located. Then enter the following command:

.. code-block:: sh

    python setup.py tests

===============================================================================
Documentation
===============================================================================

Documentation can be built from source on any platform easily. To do this enter
the ``docs/`` directory. A number of different formats can be used. However,
the design target is HTML. To build the HTML docs, enter the following command.

.. code-block:: sh

    make html

Then, open the file ``_build/html/index.html`` within the ``docs/`` directory.

A list of other build targets is provided by running the following command.

.. code-block:: sh

    make help

If you wish to clean all of the generated documentation, simply run the
following command.

.. code-block:: sh

    make clean

===============================================================================
Usage
===============================================================================

-------------------------------------------------------------------------------
Picture Usage
-------------------------------------------------------------------------------
Execution of the program consists of the program name and a single argument,
the directory in which the picture is to be saved into.

.. code-block:: sh

    mouse-picture ~/Destkop

-------------------------------------------------------------------------------
Preview Usage
-------------------------------------------------------------------------------
Execution of the program consists of the program name and a single argument:
the time desired length of the camera preview (in seconds).
Additionally, the user can exit at any time by entering ``Ctrl + c``

.. code-block:: sh

    mouse-preview 60

-------------------------------------------------------------------------------
Recorder Usage
-------------------------------------------------------------------------------
Execution of the program consists of the program name and respectve arguments:
time to record before trigger event (in seconds), time to record after
(in seconds), and directory of the file to be saved into.
An example is shown below:

.. code-block:: sh

    sudo mouse-record 2 2 /home/pi/Desktop

Also, as mentioned before, the program will end when a
``KeyboardInterrupt``(Ctrl + c) is entered into the terminal.
"""

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
