
==================
Client longpolling
==================

.. tags:: iot box compatible, virtual iot compatible

In order for Odoo to interact with an IoT. We rely heavily on network requests.

Most of the time, it will be with HTTPS request from the client browser to the IoT using the IoT LAN IP address.

.. uml::
   :align: center

    participant "Client Browser" as Client

   Client -> IoT: IoT request
   IoT -> Device: Instructions
   Device -> IoT: Result
   IoT -> Client: Result

.. admonition:: Example: Printing a receipt through the IoT
    :class: tip

    .. uml::

        actor Cashier
        participant "Client Browser" as Client

        Cashier -> Client: print receipt
        Client -> IoT: picture of receipt
        note over IoT: convert picture to Epson ESC/PoS format
        IoT -> "Epson Printer": ESC/PoS command
        "Epson Printer" -> IoT: OK
        IoT -> Client: OK
        Client -> Cashier: confirmation pop-up

.. note::
    This interation does not use Odoo server. It was originally thought to be used without the need for an internet connection (as the PoS was meant to work offline).

Starting Odoo 17, the IoT team is slowly moving toward websocket usage rather than HTTPS.

.. seealso:: :doc:`/iot/technical/interaction/websocket`
