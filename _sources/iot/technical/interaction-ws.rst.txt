
======================
Websockets Interaction
======================

.. tags:: iot box compatible, virtual iot compatible

Since Odoo 17, the IoT team is slowly moving toward websocket usage rather than HTTPS.
This was introduced by the following `Pull Request <https://github.com/odoo/odoo/pull/129164>`_.

It is important to notice that websockets in Odoo are not designed for real-time communication.
Odoo will only accept incoming websocket request (message) to subscribe to a channel.
A message can be sent only from the server to a channel and will be received by any client connected to this channel.

.. uml::
   :align: center

    participant "Client Browser" as Client
    participant "Odoo Server" as Server
    participant "IoT" as IoT


   Client -> Server: HTTP request for operation
   Client -> Client: Waiting for operation completion. Timeout after X seconds
   activate Client 
   Server -> IoT: websocket request with operation elements
   IoT -> Server: websocket (empty response) reception confirmation
   IoT -> IoT: Handling operation
   note over Client #FFAAAA
   If timeout reached,
   will display an error message
   end note
   IoT -> Server: HTTP request for operation completion
   Server -> Client: confirmation of operation completion
   deactivate Client
