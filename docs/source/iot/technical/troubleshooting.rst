
===============
Troubleshooting
===============
.. tags:: iot box compatible, virtual iot compatible

Understanding the IoT structure is important in order to troubleshoot it.  
   .. seealso:: :doc:`../technical/structure/index`

Troubleshooting Core
====================

Windows virtual IoT
-------------------
.. tags:: iot box incompatible, virtual iot compatible

If you want to modify the core code of the Windows virtual IoT box, it is quite easy.
You can simply update the code in the virtual IoT folder. Odoo's code is inside the `server` folder.
Then, you can restart the Odoo service in order to apply the changes.

IoT box
-------
.. tags:: iot box compatible, virtual iot incompatible

#. Connect in SSH to your IoT box

   .. seealso:: :doc:`../technical/ssh`

#. Stop the IoT Odoo service

   .. code:: console

      $ sudo service odoo stop

#. Mount the IoT box in write mode

   .. code:: console

      $ sudo mount -o remount,rw /

#. Edit the core code (located in `~/odoo/` folder). You can use `nano` or `vim` to edit the files.
#. Restart the IoT Odoo service for the changes to take effect

   .. code:: console

      $ sudo service odoo restart


Troubleshooting Hanlders
========================
.. tags:: iot box compatible, virtual iot compatible


As explained in the :doc:`../technical/structure/index`, 
the handlers code is fetched from the connected Odoo server.
As such, if your Iot is synchronised with a database AND 
you have the possibility to modify the source code of it 
(odoo.sh staging/dev branch or on-premise/local odoo installation),
then it is easier to modify the source code of the handlers directly.

To synchronise the handlers code with the IoT, you can simply restart it  
or use the `Load Handlers` button at `IoT homepage > IoT Handlers`.

.. TODO: disallow server update, etc.