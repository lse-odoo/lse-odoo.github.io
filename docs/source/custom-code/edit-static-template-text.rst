
=============================================================
Modify text value of a QWeb static template of another module
=============================================================

.. tags:: 18.0 approved

For this example we will use a template from the standard module `website_sale`:

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" ?>
    <templates xml:space="preserve">
        <t t-inherit="sale.ProductConfiguratorDialog" t-inherit-mode="extension">
            ...
            <button name="sale_product_configurator_confirm_button" position="after">
                <button
                    name="website_sale_product_configurator_continue_button"
                    class="btn btn-secondary"
                    t-if="showShopButtons()"
                    t-on-click="() => this.onConfirm({goToCart: false})"
                    t-att-disabled="!isPossibleConfiguration() || !canBeSold()"
                >
                    Continue Shopping <!-- This text will be edited -->
                </button>
            </button>
            ...
        </t>
    </templates>

Source: https://github.com/odoo/odoo/blob/d380a3a42dc39451fa26f161cc0b955b2f0098fd/addons/website_sale/static/src/js/product_configurator_dialog/product_configurator_dialog.xml


Solution 1: Overriding the template
===================================

This one is pretty straightforward, you need to create a new module that overrides the template and changes the text.

Xpath does not support direct text replacement. But fortunately there is some workaround.

Using `t-out` attribute
-----------------------

Don't forget to put the value in quotes, otherwise it will be interpreted as a variable and will cause an error if the variable does not exist.

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" ?>
    <templates xml:space="preserve">
        <t t-inherit="sale.ProductConfiguratorDialog" t-inherit-mode="extension">
            <xpath expr="//button[@name='website_sale_product_configurator_continue_button']" position="attributes">
                <attribute name="t-out">"New Text"</attribute>
            </xpath>
        </t>
    </templates>

.. warning::

    Using raw text like this is not recommended, as it will NOT be taken into account in translations.

.. note::

    `t-esc` and `t-raw` are both deprecated and should not be used anymore. See: 
    https://www.odoo.com/documentation/18.0/developer/reference/frontend/qweb.html#deprecated-output-directives

Overriding the whole element
----------------------------

.. warning::

   This method  is harder to maintain, as the element attributes are not inherited and may change with bug fixes.

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" ?>
    <templates xml:space="preserve">
        <t t-inherit="sale.ProductConfiguratorDialog" t-inherit-mode="extension">
            <xpath expr="//button[@name='website_sale_product_configurator_continue_button']" position="replace">
                <button
                    name="website_sale_product_configurator_continue_button"
                    class="btn btn-secondary"
                    t-if="showShopButtons()"
                    t-on-click="() => this.onConfirm({goToCart: false})"
                    t-att-disabled="!isPossibleConfiguration() || !canBeSold()"
                >
                    New Text
                </button>
            </xpath>
        </t>
    </templates>

Solution 2: Manipulating translations
=====================================

Add/Edit your custom module `.po` and `.pot` files in the `i18n` folder to override the original translation.

.. important::

   Static QWeb translations are loaded based on the source term in the order set by `ir.http` model `_get_translation_frontend_modules_names` method.
   So your custom module name should be AFTER the one you plan to override the translation of the standard module if you want to crush its translations.

   .. caution:: 
        If your module name is prefixed with `website`, it will be automatically loaded in the translations due to:
        https://github.com/odoo/odoo/blob/8f24da78f60529ea0b1840e48de30e15d17ddb77/addons/website/models/ir_http.py#L299
        
        BUT, the order in which it is loaded there is random (as it reads from a set).
        So if you plan to override translations from a module prefixed with `website` and your custom module is also prefixed with `website`, you should not rely on the order of loading and use the first solution instead.

.. important::

    The translations of static templates are loaded from a JS fetch request calling the route `website/translations`.
    
    The request result is cached in the browser, so if you change the translation, you need to clear the cache to see the changes.
    If you are developing, you can also enable `Disable Cache` through the developer tools `Network` panel in your browser to avoid this issue.

    You can also check the request result to make sure your translations are loaded correctly.

    .. caution:: 
        Be careful that your Network panel response `Preview` might order the dictionary keys alphabetically.
        This will bias the real order of the translations (as the one that loaded last will override the previous ones).

.. note::

    If you plan to modify the original text itself, you can modify the translation of the `en_US` language.
