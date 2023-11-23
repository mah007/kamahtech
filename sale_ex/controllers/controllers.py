# -*- coding: utf-8 -*-
# from odoo import http


# class SaleEx(http.Controller):
#     @http.route('/sale_ex/sale_ex', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_ex/sale_ex/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_ex.listing', {
#             'root': '/sale_ex/sale_ex',
#             'objects': http.request.env['sale_ex.sale_ex'].search([]),
#         })

#     @http.route('/sale_ex/sale_ex/objects/<model("sale_ex.sale_ex"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_ex.object', {
#             'object': obj
#         })
