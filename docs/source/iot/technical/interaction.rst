
===========
Interaction
===========

.. tags:: iot box compatible, virtual iot compatible

In order for Odoo to interact with an IoT. We rely heavily on network requests.

Most of the time, it will be with HTTPS request from the client browser to the IoT using its LAN IP address.

.. uml::
   :align: center

   odoo -> IoT: IoT request
   IoT -> Device: Instructions
   Device -> IoT: Result
   IoT -> odoo: Result

.. admonition:: Example: Printing a receipt through the IoT
    :class: tip

    .. uml::

        actor Cashier

        Cashier -> odoo: print receipt
        odoo -> IoT: picture of receipt
        note over IoT: convert picture to Epson ESC/PoS format
        IoT -> "Epson Printer": ESC/PoS command
        "Epson Printer" -> IoT: OK
        IoT -> odoo: OK
        odoo -> Cashier: confirmation pop-up


Starting `Odoo 17 <https://github.com/odoo/odoo/pull/129164>`_, the IoT team is slowly moving toward websocket usage rather than HTTPS.