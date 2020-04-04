# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AssetVME(models.Model):
    _inherit = 'asset.asset'
    _description = 'VME Asset'

    model = fields.Char('Model', size=64)
    serial = fields.Char('Serial no.', size=64)
    vendor_id = fields.Many2one('res.partner', 'Vendor')
    manufacturer_id = fields.Many2one('res.partner', 'Manufacturer')
    warranty_start_date = fields.Date('Warranty Start')
    warranty_end_date = fields.Date('Warranty End')

