
======================
IoT-box Password (IoT)
======================

.. tags:: iot box compatible, virtual iot incompatible

Depending on your IoT-box version, the password value/generation process may differ.

Oldest IoT-boxes will always have a fixed password: **raspberry**.

Newest version will generate a new random password each time the IoT-box is rebooted.
While there is no way to know this password, you can generate a new known one on-demand.

Get/Generate a new password
===========================

Steps:
------

1. Connect to your IoT-box homepage (using the link on the IoT app)

    .. image:: /_static/images/iot/21.10/iot-homepage.avif
        :alt: IoT box homepage
        
2. Click on the `Remote Debug` button
3. The `Remote Debuging` page will open
4. If you have a text field with `pi user password` and a `Generate password` button, click it

    .. image:: /_static/images/iot/24.01/iot-remote-debugging.avif
        :alt: Remote Debugging page

    .. note::
        If you don't have this field, you are on an old version of the IoT-box and the password is fixed to ``raspberry``.  
        
        .. image:: /_static/images/iot/21.10/iot-remote-debugging.avif
            :alt: Remote Debugging page

5. Copy the new password generated

    .. admonition:: Example
        :class: tip

        .. image:: /_static/images/iot/24.01/iot-generate-password.avif
            :alt: Generate password example
