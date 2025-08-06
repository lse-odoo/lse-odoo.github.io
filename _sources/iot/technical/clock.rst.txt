=====
Clock
=====

.. tags:: iot box compatible, virtual iot incompatible

The clock is a crucial part of the IoT box. It is used to keep track of time and date.
As the IoT box is made of a raspberry pi which does not have a battery, currrent date and time information is lost each time the IoT box is turned off.

How does the IoT box update its current time?
=============================================

When the IoT box is connected to the internet, it will automatically update its date and time information on boot.

.. note::
    Time information is fetched online from NTP time server as defined in raspian configuration (depends on the IoT box image version).

Consequences of not having the correct time ?
=============================================

It might interefere with any IoT operation which rely on date and time.

The most common one is having the SSL/HTTPS certificate not updating automatically.
This would happen as the IoT does update the certificate only if it is close to expiration.
If the IoT date is not correct, it will likely be set in a date in the past (generally, the one of the image build time).
As such, the IoT will not request for a new certificate as it will think the existing one didn't expired yet

Reason why the IoT box date and time is not correct ?
======================================================

- Lack of internet connection (for the IoT box)
- Firewall set on the network which prevent the IoT box to reach NTP time server
