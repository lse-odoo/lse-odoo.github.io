================
Remote Debugging
================

.. TODO: add a custom directive/command like furo {versionadded} or {versionchanged}
:octicon:`container` :bdg-info:`IoT box only` 


Enabling this feature of your IoT box will allow remote connections to your IoT box.
Generally use to solve technical issue or troubleshooting.

.. danger::
    Do **NOT** enable this feature if you do not trust the other party as it would
    give then an administration access on your IoT box which could create security
    issue in your network.
    More details in the Security_ section.

Security
========
The remote debugging feature is a powerful tool but can cause some security risks.

While the feature is on, it will create an unlisted `ngrok <https://ngrok.com>`__ tunnel/URL to your IoT box.
Anyone with this URL and your IoT password could access it and run **any** command.
This is already an issue in it-self, but it could also be used to pivot to other devices in your network.

Thus, we do recommend to disable this feature while it is not needed to don't take any risks.

Enable Remote Debugging
=======================

Pre-requisite
-------------
- You need to have a **token** provided by the person who will connect to your IoT box
- The IoT-box homepage should be accessible

Steps
-----

#. Connect to your IoT box homepage (using the link on the IoT app)

    .. image:: /_static/images/iot/21.10/iot-homepage.avif

#. Click on the `Remote Debug` button

#. The `Remote Debuging` page will open

#. In the "Authentification Token" field, enter the token provided by the person who will connect to your IoT box

#. Click on the `Enable Remote Debugging` button

    .. image:: /_static/images/iot/21.10/iot-remote-debugging.avif

#. If you have a text field with `pi user password` and a `Generate password` button, click the button and copy the password generated

    .. image:: /_static/images/iot/24.01/iot-remote-debugging.avif

#. Share the password copied from the previous step with the person who will connect to your IoT box. They will need it to connect to your IoT box


Disable Remote Debugging
------------------------
Shuting down the IoT box will disable the remote debugging feature.
You can do so from the IoT-box homepage, or by unplugging the power supply.