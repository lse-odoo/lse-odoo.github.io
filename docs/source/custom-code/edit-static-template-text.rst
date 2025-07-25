
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

.. important::

   Static QWeb translations are loaded based on the source term in modules name alphabetical order
   So your custom module name should be **alphabetically AFTER** the standard module you plan to override the translations
   (ideally prefixed with the module it extends, for example `website_sale_custom`).

Add/Edit your custom module `.po` and `.pot` files in the `i18n` folder to override the original translation.

.. note::

    If you plan to modify the original text itself, you can modify the translation of the `en_US` language.
