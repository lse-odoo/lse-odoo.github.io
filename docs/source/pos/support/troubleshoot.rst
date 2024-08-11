
===============
Troubleshooting
===============

As Odoo Point of Sale is a complex system and thought to work offline,
only the nessesary informations are send to the Odoo server.

For this reasons, the information that Odoo's support have is limited 
and might lack the information needed to troubleshoot the issue.

Devices in your network (printers, payment terminals, etc.) might also cause issues
which will not report to Odoo's server.


Generating a HAR file for Troubleshooting
=========================================

Odoo's Support may occasionally need additional information about the network requests that are generated in your browser.
A member of the team may ask you to record a HAR file, while that issue occurs.

.. danger::
   A HAR file contains sensitive information about the network requests that are generated in your browser.
   Do **NOT** share this file with anyone other than Odoo's support team

Generating a HAR file with Google Chrome
----------------------------------------

.. important::
   Make sure that the issue is reproducible **before** generating the HAR file.
   The issue **must** happen while the HAR file is being recorded, 
   otherwise the file will not contain the necessary information.

#. Open Google Chrome and browse to the page where the issue occurs
#. Open the Chrome Developer Tools by either:

   - Pressing ``F12``
   - *OR* pressing ``Ctrl + Shift + I``
   - *OR* right-clicking on the page and selecting ``Inspect``
   - *OR* look for the ``⋮`` button and select ``More Tools > Developer Tools.``

   This should open the Developer Tools in a separate window or in the side of the page.
#. From this pannel select the ``Network`` tab. You must keep the menu open while you reproduce the issue.
#. Look for a round record button in the upper left corner of the tab, and make sure it is red. If it is grey, click the button once to start recording.
#. Reproduce the issue by following the steps that cause the problem.
#. Take note of the exact time when the issue occurs (to forward it to the support service later on as well).
#. Once the issue has been reproduced, export the HAR file by either:
   
   - Right-clicking anywhere in the list of network requests and selecting ``Save all as HAR with content``.
   - *OR* Clicking the ``Export HAR`` button |export-har-btn| in the upper right corner of the tab.

   .. image:: /_static/images/other/chrome-download-har.png
      :alt: Export HAR screenshot

.. |export-har-btn| image:: /_static/images/other/chrome-download-har-icon.png
   :alt: Export HAR button

#. Save the file to your computer and send it to the support service with the time when the issue occurred (do not forget to mention the timezone).

Console Log
^^^^^^^^^^^
The HAR file contains a lot of information about the network requests that are generated in your browser.
However, it might lack some particular informations that can be  needed to troubleshoot the issue.

#. Assuming the chrome developer tools are still open, click on the ``Console`` tab.
#. Save a screenshot of the console and right-click ``Save as...`` to save the console content into a ``log`` file.
#. Send the screenshot and console log file to the support service as well.
