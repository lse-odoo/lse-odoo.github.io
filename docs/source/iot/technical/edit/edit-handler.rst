
======================
Edit IoT Handlers Code
======================
.. tags:: iot box compatible, virtual iot compatible


As explained in the :doc:`../../technical/structure/index`, 
the handlers code is fetched from the connected Odoo server.
As such, if your Iot is synchronised with a database AND 
you have the possibility to modify the source code of it 
(odoo.sh staging/dev branch or on-premise/local odoo installation),
then it is easier to modify the source code of the handlers directly.

To synchronise the handlers code with the IoT, you can simply restart it  
or use the `Load Handlers` button at `IoT homepage > IoT Handlers`.

.. TODO: disallow server update, etc.