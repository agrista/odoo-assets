============================
Assigning Assets to Partners
============================

This module allows to manage the relationship between assets and partners (company or individual).

* Currently Owned
* Rented
* Previously Owned
* Grew Up
* Business Interest

**Table of contents**

.. contents::
   :local:

TODO
====

Configuration
=============

Configure all relationship types you need in Assets > Configuration > Asset Relationship Categories.
For example, we create a category 'Owner':

Name:
  Name of this ID type. For example, 'Driver License'
Code:
  Code, abbreviation or acronym of this ID type. For example, 'driver_license'
Python validation code:
  Optional python code called to validate ID numbers of this ID type. This functionality can be
  overridden by setting ``id_no_validate`` to ``True`` in the context, such as:

  .. code-block:: python

     partner.with_context(id_no_validate=True).write({
        'name': 'Bad Value',
        'category_id': self.env.ref('id_category_only_numerics').id,
     })

Usage
=====

In partner form you will see another tab called 'ID Numbers'. You can add
any IDs to this partner, defining:

Category:
  ID type defined in configuration. For example, Driver License
ID Number:
  The ID itself. For example, Driver License number of this person
Issued by:
  Another partner, who issued this ID. For example, Traffic National Institution
Place of Issuance:
  The place where the ID has been issued. For example the country for passports and visa
Valid from:
  Issued date. For example, date when person approved his driving exam, 21/10/2009
Valid until:
  Expiration date. For example, date when person needs to renew his driver license, 21/10/2019
Status:
  ID status. For example new/to renew/expired
Notes:
  Any further information related with this ID. For example, vehicle types this person can drive

Known issues / Roadmap
======================

* If you want to search a partner by ID you will use advance search form.
  You can't search by issuer, valid dates, category or notes.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/partner-contact/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/OCA/partner-contact/issues/new?body=module:%20partner_identification%0Aversion:%2013.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* ChriCar Beteiligungs- und Beratungs- GmbH
* Tecnativa
* Camptocamp
* ACSONE SA/NV
* LasLabs
* Onestein

Contributors
~~~~~~~~~~~~

* Antonio Espinosa <antonio.espinosa@tecnativa.com>
* Ferdinand Gassauer <office@chrcar.at>
* Gerhard Könighofer <gerhard.koenighofer@swing-system.com>
* Laurent Mignon <laurent.mignon@acsone.eu>
* Jairo Llopis <jairo.llopis@tecnativa.com>
* Dave Lasley <dave@laslabs.com>
* Simone Orsi <simone.orsi@camptocamp.com>
* Dennis Sluijk <d.sluijk@onestein.nl>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/partner-contact <https://github.com/OCA/partner-contact/tree/13.0/partner_identification>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
