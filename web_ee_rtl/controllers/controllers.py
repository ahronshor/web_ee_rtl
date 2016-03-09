# -*- coding: utf-8 -*-
from openerp import http

# class WebEeRtl(http.Controller):
#     @http.route('/web_ee_rtl/web_ee_rtl/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/web_ee_rtl/web_ee_rtl/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('web_ee_rtl.listing', {
#             'root': '/web_ee_rtl/web_ee_rtl',
#             'objects': http.request.env['web_ee_rtl.web_ee_rtl'].search([]),
#         })

#     @http.route('/web_ee_rtl/web_ee_rtl/objects/<model("web_ee_rtl.web_ee_rtl"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('web_ee_rtl.object', {
#             'object': obj
#         })