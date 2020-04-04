# -*- coding: utf-8 -*-
# from odoo import http


# class AssetVme(http.Controller):
#     @http.route('/asset_vme/asset_vme/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/asset_vme/asset_vme/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('asset_vme.listing', {
#             'root': '/asset_vme/asset_vme',
#             'objects': http.request.env['asset_vme.asset_vme'].search([]),
#         })

#     @http.route('/asset_vme/asset_vme/objects/<model("asset_vme.asset_vme"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('asset_vme.object', {
#             'object': obj
#         })
