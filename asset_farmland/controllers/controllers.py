# -*- coding: utf-8 -*-
# from odoo import http


# class AssetFarmland(http.Controller):
#     @http.route('/asset_farmland/asset_farmland/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/asset_farmland/asset_farmland/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('asset_farmland.listing', {
#             'root': '/asset_farmland/asset_farmland',
#             'objects': http.request.env['asset_farmland.asset_farmland'].search([]),
#         })

#     @http.route('/asset_farmland/asset_farmland/objects/<model("asset_farmland.asset_farmland"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('asset_farmland.object', {
#             'object': obj
#         })
