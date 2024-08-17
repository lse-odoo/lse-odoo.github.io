
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

.. image:: /_static/images/iot/24.01/iot-restart.avif
   :alt: IoT Restart IoT Button

Depending on the case that you have. The issue might already be solved in the latest version of IoT code.
In particular if you installed it from a long time ago.
Try to update your IoT code as a first step to see if it solves your issue.

.. seealso::
    `Odoo's Documentation Windows Virtual IoT update <(https://www.odoo.com/documentation/17.0/applications/general/iot/config/updating_iot.html#windows-iot-update)>`_

    `Odoo's Documentation IoT box update <(https://www.odoo.com/documentation/17.0/applications/general/iot/config/updating_iot.html#update-from-the-iot-box-home-page)>`_


Troubleshoot
============
If the issue persist despite the step on the previous section, 
you can send some deeper information to your support service to help them troubleshoot the issue.
Please follow these steps:

#. Connect to your IoT homepage
#. Click the "handlers list" button
#. On "Odoo log level ..." dropdown, change the value to "Debug"

   .. image:: /_static/images/iot/24.01/iot-logging-switch-odoo-debug.avif
      :alt: IoT change odoo log level to Debug
    
   .. attention::
      If you let "Odoo log level ..." in debug, this can increase a lot the size of the logs.
      Feel free to change it back to "Info" or "Warning" once done with troubleshooting.

#. Click the "Update Logs Configuration" button on the bottom to save the change
#. Restart the IoT using the "Restart Odoo service" button on the top right corner of the IoT home page.

   .. image:: /_static/images/iot/24.01/iot-restart.avif
      :alt: IoT Restart IoT Button

#. Perform again the operation to print the report on odoo's side


In theory, the issue should persist (as we just asked for more logs).

If it is the case forward this information to the support service:

#. The exact time when you performed the operation (please precise the timezone)
#. AND if the printer printed or not. Even if the message appear, it could be a false positive
#. AND the logs from the IoT 
    .. include:: /iot/support/logging/download/from-odoo-server.rst
