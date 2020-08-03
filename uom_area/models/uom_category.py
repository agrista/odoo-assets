# -*- coding: utf-8 -*-

from odoo import models, fields


class UoMCategory(models.Model):
    _inherit = 'uom.category'

    measure_type = fields.Selection(selection_add=[('area', 'Default Area')])
