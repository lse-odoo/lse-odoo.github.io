Basics
======

====
Code
====
The Point of Sales (PoS) code is primarily writen in Javascript (using OWL starting Odoo 16).
As a PoS session should be able to operate without an internet connection, 
the code was written in order to be executed by the user browser.
It was also thought to avoid making request to Odoo's server, as much as possible and to be resilient to network failures.

.. admonition:: Example: Validating an order
    :class: tip

    .. uml::

        actor Cashier

        Cashier -> odoo !!: validation with order details
        note right #salmon: internet disconnection (before Odoo server reached)
        Cashier --> Cashier : storing order in client browser local storage
        note over Cashier #lime: internet reconection
        Cashier -> odoo: validation with stored order details
        odoo -> Cashier: confirmation

===============
Initial Loading
===============

An internet connection is required whenever a PoS session is started.
During the session loading, all necessary PoS datas are fetched from the server 
and store in a Javascript object in the browser memory.

If you open your browser devtools network tab, you will see the server request to fetch the PoS datas.
Since Odoo 17, there is one request `load_pos_data` that fetches all the datas in one go.
The response to the request is a JSON object containing all the datas like:

- products
- categories
- customers
- payment methods
- taxes
- pricelist
- etc.

.. TODO: add a section regarding the computation of the receipt index: "Order XXXXX-YYY-ZZZZ"