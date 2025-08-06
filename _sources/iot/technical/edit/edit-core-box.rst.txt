
============================
Edit IoT Core Code (IoT Box)
============================
.. tags:: iot box compatible, virtual iot incompatible

#. Connect in SSH to your IoT box

   .. seealso:: :doc:`../../technical/ssh`

#. Stop the IoT Odoo service

   .. code:: console

      $ sudo service odoo stop

#. Mount the IoT box in write mode

   .. code:: console

      $ sudo mount -o remount,rw /

#. Edit the core code (located in `~/odoo/` folder). You can use `nano` or `vim` to edit the files.
#. Restart the IoT Odoo service for the changes to take effect

   .. code:: console

      $ sudo service odoo start
