
======================
Edit IoT Handlers Code
======================
.. tags:: iot box compatible, virtual iot compatible


As explained in the :doc:`../../technical/structure/index`, 
the handlers code is fetched from the connected Odoo server.

Possibility to modify your odoo instance source code
====================================================

If your IoT is synchronised to an odoo instance on which
you have the possibility to modify the source code of it.
For example; odoo.sh staging/dev branch or on-premise/local odoo installation.
Then it is easier to modify the source code of the handlers directly.

To synchronise the handlers code with the IoT, you can simply restart it  
or use the `Load Handlers` button at `IoT homepage > IoT Handlers`.

Not possible to modify the odoo instance source code
====================================================

If you don't have the possibility to modify the source code of the odoo instance,
for example; Odoo online/SAAS/odoo.sh production branch, 

#. On the odoo instance, go to the IoT form view on which you want to modify the Handlers
#. Deactivate `Automatic drivers update?`
#. Modify the handlers code manually, similar to core code modification

   .. seealso:: 
      :doc:`../../technical/edit/edit-core-box`
      
      :doc:`../../technical/edit/edit-core-virtual`

