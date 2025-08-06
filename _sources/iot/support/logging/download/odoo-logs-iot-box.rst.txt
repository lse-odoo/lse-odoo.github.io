==========================
Download IoT Box Log Files
==========================
.. tags:: iot box compatible, virtual iot incompatible

.. versionadded:: image->24.01

On latest IoT box version, there is an URL which allow you to download the logs file of your IoT box.
This will enable you to download IoT logs from any date.

.. danger::

    The IoT box logs files are automatically deleted if the IoT box is turned off or rebooted.
    If you are looking for older logs than available on the page, they are lost.


To download the logs, you can use the following URL:

.. code::

    http://<IOT_IP_ADDRESS>/odoo-logs/

Replace ``<IOT_IP_ADDRESS>`` with the IP address of your IoT box.

.. image:: /_static/images/iot/24.01/iot-odoo-logs-page.avif
   :alt: IoT Box Logs URL example

.. tip::

    This will work even if the IoT box homepage is down as this URL is not handled
    by the same code than the one of the homepage.
