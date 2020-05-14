# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AssetFarmland(models.Model):
    _name = 'asset.farmland'
    _description = 'Farmland Assets'
    _inherits = {'asset.asset': 'asset_id'}

    asset_id = fields.Many2one('asset.asset', required=True, ondelete='cascade')
    registrar = fields.Many2one('res.partner', string='Registrar')
    boundary = fields.GeoMultiPolygon('Boundary')
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
