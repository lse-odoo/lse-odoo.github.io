
===================
Structure (IoT box)
===================
.. tags:: iot box compatible, virtual iot incompatible


The structure of the IoT box can be splitted into 3 parts which are related to each other:
 1. :ref:`Image`
 2. :ref:`Core`
 3. :ref:`Handlers`

.. image:: /_static/images/iot/diagrams/iot-structure.svg
    :alt: IoT structure

.. TODO: add a diagram using graphviz rather than svg ? https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html

Image
=====
The image of the IoT box is the base of the IoT box. 
It is the image that is flashed on the SD card.  

This image is a modified version of the `Raspberry Pi OS <https://www.raspberrypi.com/software/operating-systems/>`_
on which some elements were installed and configured to make it work with the IoT app.

This image is generated manually when needed. This is done bu running the 
`posbox_create_image.sh <https://github.com/odoo/odoo/blob/17.0/addons/point_of_sale/tools/posbox/posbox_create_image.sh>`_ script.

.. note::

    The most common case which decide the IoT team to build an image is when Odoo change of minimum version of python.
    The IoT team generally build a new image when this happens with an updated version of the Raspberry Pi OS.

The main element added to the image is what I will call the [**core**](#core)

Core
====

The "core" is the main part of the image. It is composed of odoo's community code.  
The core logic of the IoT box is handled by some odoo apps that can not be installed on a standard odoo instance.
But that are part of the community code. The IoT run odoo in such a way that only this module are loaded.
Thus, you can't install regular app like Sales, CRM, etc. on the IoT box.

Core Odoo version
-----------------

On each IoT image, the core code is pre-installed, the version of odoo code used depends on the image version.

.. admonition:: Example
    :class: tip

    Current latest version (`24_01`) use odoo community 17.0 code by default

Once an odoo database is synchronised with the IoT box, the odoo's version is changed to match the one of the database.
The core odoo code is always pulled from https://github.com/odoo/odoo

.. admonition:: Example
    :class: tip

    After synchronising the database with my database ``i-love-iot.odoo.com`` which is on 16.0,
    the IoT box core odoo code will change to 16.0

Each time the IoT box started, it checks the odoo version of the database and update the core odoo code to match it if needed.
In other words, if the synchronised odoo database upgrade, the IoT box will upgrade the core odoo code to match it.

Handlers
========

The "Handlers" regroup both the Interfaces and the Drivers of the IoT box.

More information on what it is and how to develop them at:
`Odoo IoT developer documentation <https://www.odoo.com/documentation/17.0/developer/howtos/connect_device.html>`_
    
.. epigraph::

    At each IoT box boot, it will load all of the Interfaces and Drivers that can be located on the connected Odoo server. 
    Each Odoo module can contain an ``iot_handlers`` directory that will be copied to the IoT Box.

.. note::
    Apart from rebooting the IoT box, the handlers can also be reloaded as describe in:
    `Odoo's documentation IoT update handlers <https://www.odoo.com/documentation/17.0/applications/general/iot/config/updating_iot.html#handler-driver-update>`_

Unlike the core code that will be fetched from the odoo repository, the handlers are fetched from the connected Odoo server.
This ease the developement process as you don't need to create a pull request on odoo github repository and 
can easily reload them. It can be useful for troubleshooting as well by modifying the server IoT handler files directly.  
But, it can complicate the stability as if your code modify core code, it might not be of the same version on other IoT boxes.

As `hw_drivers <https://github.com/odoo/odoo/tree/17.0/addons/hw_drivers/iot_handlers>`_ 
community module have an `iot_handlers` directory, the IoT box comes with pre-installed handlers.
Once an odoo database is synchronised with the IoT box, the handlers are updated to match the one of the database.
