# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo
#    Copyright (C) 2013-2020 CodUP (<http://codup.com>).
#
##############################################################################

from odoo import api, fields, models
from odoo import tools

STATE_COLOR_SELECTION = [
    ('0', 'Red'),
    ('1', 'Green'),
    ('2', 'Blue'),
    ('3', 'Yellow'),
    ('4', 'Magenta'),
    ('5', 'Cyan'),
    ('6', 'Black'),
    ('7', 'White'),
    ('8', 'Orange'),
    ('9', 'SkyBlue')
]


class AssetState(models.Model):
    """ 
    Model for asset states.
    """
    _name = 'asset.state'
    _description = 'State of Asset'
    _order = "sequence"

    STATE_SCOPE_TEAM = [
        ('0', 'Finance'),
        ('1', 'Warehouse'),
        ('2', 'Manufacture'),
        ('3', 'Maintenance'),
        ('4', 'Accounting')
    ]

    name = fields.Char('State', size=64, required=True, translate=True)
    sequence = fields.Integer('Sequence', help="Used to order states.", default=1)
    state_color = fields.Selection(STATE_COLOR_SELECTION, 'State Color')
    team = fields.Selection(STATE_SCOPE_TEAM, 'Scope Team')

    def change_color(self):
        color = int(self.state_color) + 1
        if (color > 9): color = 0
        return self.write({'state_color': str(color)})


class AssetCategory(models.Model):
    _description = 'Asset Tags'
    _name = 'asset.category'

    name = fields.Char('Tag', required=True, translate=True)
    asset_ids = fields.Many2many('asset.asset', id1='category_id', id2='asset_id', string='Assets')


class AssetAsset(models.Model):
    """
    Assets
    """
    _name = 'asset.asset'
    _description = 'Asset'
    _inherit = ['mail.thread', 'image.mixin']

    def _read_group_state_ids(self, domain, read_group_order=None, access_rights_uid=None, team='3'):
        access_rights_uid = access_rights_uid or self.uid
        stage_obj = self.env['asset.state']
        order = stage_obj._order
        # lame hack to allow reverting search, should just work in the trivial case
        if read_group_order == 'stage_id desc':
            order = "%s desc" % order
        # write the domain
        # - ('id', 'in', 'ids'): add columns that should be present
        # - OR ('team','=',team): add default columns that belongs team
        search_domain = []
        search_domain += ['|', ('team', '=', team)]
        search_domain += [('id', 'in', ids)]
        stage_ids = stage_obj._search(search_domain, order=order, access_rights_uid=access_rights_uid)
        result = stage_obj.name_get(access_rights_uid, stage_ids)
        # restore order of the search
        result.sort(lambda x, y: cmp(stage_ids.index(x[0]), stage_ids.index(y[0])))
        return result, {}

    def _read_group_finance_state_ids(self, domain, read_group_order=None, access_rights_uid=None):
        return self._read_group_state_ids(domain, read_group_order, access_rights_uid, '0')

    def _read_group_warehouse_state_ids(self, domain, read_group_order=None, access_rights_uid=None):
        return self._read_group_state_ids(domain, read_group_order, access_rights_uid, '1')

    def _read_group_manufacture_state_ids(self, domain, read_group_order=None, access_rights_uid=None):
        return self._read_group_state_ids(domain, read_group_order, access_rights_uid, '2')

    def _read_group_maintenance_state_ids(self, domain, read_group_order=None, access_rights_uid=None):
        return self._read_group_state_ids(domain, read_group_order, access_rights_uid, '3')

    def _read_group_accounting_state_ids(self, domain, read_group_order=None, access_rights_uid=None):
        return self._read_group_state_ids(domain, read_group_order, access_rights_uid, '4')

    CRITICALITY_SELECTION = [
        ('0', 'General'),
        ('1', 'Important'),
        ('2', 'Very important'),
        ('3', 'Critical')
    ]

    name = fields.Char('Asset Name', size=64, required=True, translate=True)
    finance_state_id = fields.Many2one('asset.state', 'Finance State', domain=[('team', '=', '0')])
    warehouse_state_id = fields.Many2one('asset.state', 'Warehouse State', domain=[('team', '=', '1')])
    manufacture_state_id = fields.Many2one('asset.state', 'Manufacture State', domain=[('team', '=', '2')])
    maintenance_state_id = fields.Many2one('asset.state', 'Maintenance State', domain=[('team', '=', '3')])
    accounting_state_id = fields.Many2one('asset.state', 'Accounting State', domain=[('team', '=', '4')])
    maintenance_state_color = fields.Selection(related='maintenance_state_id.state_color',
                                               selection=STATE_COLOR_SELECTION, string="Color", readonly=True)
    criticality = fields.Selection(CRITICALITY_SELECTION, 'Criticality')
    user_id = fields.Many2one('res.users', 'Assigned to', track_visibility='onchange')
    active = fields.Boolean('Active', default=True)
    asset_number = fields.Char('Asset Number', size=64)
    start_date = fields.Date('Start Date')
    purchase_date = fields.Date('Purchase Date')
    category_ids = fields.Many2many('asset.category', id1='asset_id', id2='category_id', string='Tags')
    location = fields.GeoPoint('Location')

    _group_by_full = {
        'finance_state_id': _read_group_finance_state_ids,
        'warehouse_state_id': _read_group_warehouse_state_ids,
        'manufacture_state_id': _read_group_manufacture_state_ids,
        'maintenance_state_id': _read_group_maintenance_state_ids,
        'accounting_state_id': _read_group_accounting_state_ids,
    }

    @api.model
    def create(self, vals):
        return super(AssetAsset, self).create(vals)

    def write(self, vals):
        if 'image_1920' in vals:
            self.env['asset.asset'].invalidate_cache(fnames=[
                'image_1920',
                'image_1024',
                'image_512',
                'image_256',
                'image_128',
                'can_image_1024_be_zoomed',
            ])
        return super(AssetAsset, self).write(vals)
