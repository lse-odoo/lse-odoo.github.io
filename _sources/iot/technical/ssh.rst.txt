
=========
SSH (IoT)
=========

.. tags:: iot box compatible, virtual iot incompatible


Connecting through SSH to your IoT-box is a powerful tool to interact with it.
It allows you to run commands on your IoT box from your computer.

It is generally used for troubleshooting or modify the IoT-box code arbirarily.

Connect in SSH locally
======================

Assuming you are on the same network as your IoT-box, you can connect to it using SSH.

Pre-requisite
-------------

- Be on the same network as your IoT-box
- Know the IP address of your IoT-box 
- Having a device capable of running SSH (generally, a computer)
- Know the password of your IoT-box 
    .. seealso:: :doc:`password`

Steps (Locally)
---------------

1. Open a terminal on your computer
2. Type the following command:

.. code:: console

    $ ssh pi@<IP_ADDRESS>

Replace ``<IP_ADDRESS>`` with the IP address of your IoT-box

.. admonition:: Example
    :class: tip

    Assuming the IoT box IP address is ``192.168.0.116``, the command would be:
    ``ssh pi@192.168.0.116``

3. Enter the password of your IoT-box when prompted


Connect in SSH remotely
=======================

If you are not on the same network as your IoT-box, you can still connect to it using SSH.
With extra steps.

Pre-requisite
-------------
- Having Remote Debugging enabled on your IoT-box 
    .. seealso:: :doc:`../support/remote-debug`
- Having a device capable of running SSH (generally, a computer)
- Know the password of your IoT-box
    .. seealso:: :doc:`password`

Steps (Remotely)
----------------

1. Open a terminal on your computer
2. Type the following command:

.. code:: console

    ssh pi@<TUNNEL_HOSTNAME> -p <TUNNEL_PORT>

Replace ``<TUNNEL_HOSTNAME>`` with the tunnel URL hostname given on ngrok and ``<TUNNEL_PORT>`` with the tunnel port number

.. admonition:: Example
    :class: tip

    If the Ngrok tunnel is: ``tcp://0.tcp.ngrok.io:12345``
    The TUNNEL_HOSTNAME is ``0.tcp.ngrok.io`` and the TUNNEL_PORT is ``12345``.
    Resulting in:  
    ``ssh pi@0.tcp.ngrok.io -p 12345``

3. Enter the password of your IoT-box when prompted
