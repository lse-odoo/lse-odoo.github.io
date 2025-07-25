
====================================
"Connection to printer failed" error
====================================

Since Odoo 17, the IoT is using different method to interact with printers to print reports.

As a consequence, you might encounter the error message "Connection to printer failed" when trying to print a report.

.. image:: /_static/images/odoo/odoo-iot-printer-error-pop-up.avif
   :alt: Odoo IoT Printer Error Pop-up

This issue can happen for multiple different reasons.
This guide will help you to troubleshoot the issue and provide the necessary information to your support service.

Solution Attempt
================

.. TODO: have a dedication section to restart IoT as it can be performed on homepage or from IoT app
Try to restart your IoT, you can use the "Restart Odoo service" button on the top right corner of the IoT home page. 


.. image:: /_static/images/iot/25.04/iot-restart.avif
   :alt: IoT Restart IoT Button

Depending on the case that you have. The issue might already be solved in the latest version of IoT code.
In particular if you installed it from a long time ago.
Try to update your IoT code as a first step to see if it solves your issue.

.. seealso::
    `Odoo's Documentation IoT update <(https://www.odoo.com/documentation/18.0/applications/general/iot/iot_advanced/updating_iot.html#image-and-core-code-update)>`_


Troubleshoot
============
If the issue persist despite the step on the previous section, 
you can send some deeper information to your support service to help them troubleshoot the issue.
Please follow these steps:

#. Connect to your IoT homepage (using the link on the IoT app)

   .. image:: /_static/images/iot/25.04/iot-homepage.avif
      :alt: IoT homepage

#. Click the gears icon button on the top right corner of the page to enable debugger mode

   .. image:: /_static/images/iot/25.04/iot-homepage-debug.avif
      :alt: IoT homepage

#. Click on the `Log level` button at the bottom of the page

   .. caution::
      The `Log level` button will only be visible if the IoT is in debug mode.
      If you do not see it, you need to enable the debug mode first by clicking on the gears icon button.

   .. image:: /_static/images/iot/25.04/iot-logging.avif
      :alt: IoT homepage

#. On the following dialog, change the value of `iot-logging-odoo` to "Debug"

   .. image:: /_static/images/iot/25.04/iot-logging_odoo_debug.avif
      :alt: IoT change odoo log level to Debug
    
   .. attention::
      If you let iot-logging-odoo` in debug, this can increase a lot the size of the logs.
      Feel free to change it back to "Info" or "Warning" once done with troubleshooting.

#. Click the `Close` button on the bottom right to exit the dialog
#. Restart the IoT using the "Restart Odoo service" button on the top right corner of the IoT home page.

   .. image:: /_static/images/iot/25.04/iot-restart.avif
      :alt: IoT Restart IoT Button

#. Perform again the operation to print the report on odoo's side


In theory, the issue should persist (as we just asked for more logs).

If it is the case forward this information to the support service:

#. The exact time when you performed the operation (please precise the timezone)
#. AND if the printer printed or not. Even if the message appear, it could be a false positive
#. AND the logs from the IoT 
    .. include:: /iot/support/logging/download/_from-odoo-server.rst
