# # -*- coding: utf-8 -*-
# ###############################################################################
# #
# #    Trey, Kilobytes de Soluciones
# #    Copyright (C) 2014-Today Trey, Kilobytes de Soluciones <www.trey.es>
# #
# #    This program is free software: you can redistribute it and/or modify
# #    it under the terms of the GNU Affero General Public License as
# #    published by the Free Software Foundation, either version 3 of the
# #    License, or (at your option) any later version.
# #
# #    This program is distributed in the hope that it will be useful,
# #    but WITHOUT ANY WARRANTY; without even the implied warranty of
# #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# #    GNU Affero General Public License for more details.
# #
# #    You should have received a copy of the GNU Affero General Public License
# #    along with this program.  If not, see <http://www.gnu.org/licenses/>.
# #
# ###############################################################################
# from openerp import models, exceptions, _
# from functools import partial
# from reportlab.graphics.barcode import createBarcodeDrawing

# import logging

# _log = logging.getLogger(__name__)


# class ProductLabelReport(models.AbstractModel):
#     _inherit = 'report.product_label.label'

#     # def render_html(self, cr, uid, ids, data=None, context=None):
#     #     # return super(ProductLabelReport, self).render_html(
#     #     #     cr, uid, ids, data, context)
#     #     render = super(ProductLabelReport, self).render_html(
#     #         cr, uid, ids, data, context)

#     #     #### como heredoel render_html??
#     #     _log.info('=>>render: %s' % render)
#     #     _log.info('=>>data: %s' % data)
#     #     return render
#     #     # _log.info('=>>render: %s' % render)
#     #     # render.update(
#     #     #     'get_partner': partial(self.get_partner, cr, uid, context=context),
#     #     #     'get_products': partial(
#     #     #         self.get_products, cr, uid, context=context))
#     #     # return render

#     # @TODO Sobreescrito porque no he encontrado manera de heredarlo y anadirle
#     # las nuevas funciones
#     def render_html(self, cr, uid, ids, data=None, context=None):

#         # prerender???



#         report_obj = self.pool['report']
#         product_obj = self.pool['product.product']
#         report = report_obj._get_report_from_name(
#             cr, uid, 'product_label.label')
#         selected_orders = product_obj.browse(cr, uid, ids, context=context)

#         docargs = {
#             'doc_ids': ids,
#             'doc_model': report.model,
#             'docs': selected_orders,
#             'formatCurrency': self.formatCurrency,
#             'getPricelist': partial(self.getPricelist, cr,
#                                      uid, context=context),
#             'printBarcode': partial(self.printBarcode, cr,
#                                      uid, context=context),
#             'get_products': partial(self.get_products, cr,
#                                     uid, context=context),
#             'get_partner': partial(self.get_partner, cr,
#                                    uid, context=context)
#         }

#         return report_obj.render(
#             cr, uid, ids,
#             'product_label.label', docargs,
#             context=context)

#     def get_partner(self, cr, uid, picking, context=None):
#         partner = None

#         # Si el albaran es de entrada
#         if picking.picking_type_id and \
#            picking.picking_type_id.code == 'incoming':

#             # Obtener el cliente a traves del grupo de abastecimiento del alb
#             # de entrada (si partner_id es cliente, proviene del pedido de un
#             # cliente, por lo que sera bajo demanda)
#             if picking.group_id and picking.group_id.partner_id and \
#                picking.group_id.partner_id.customer is True:
#                 partner = picking.group_id.partner_id

#         return partner

#     def get_products(self, cr, uid, picking, context=None):
#         _log.info('='*100)
#         _log.info('picking: %s' % picking)
#         move_ids = self.pool['stock.move'].search(
#             cr, uid, [('picking_id', '=', picking.id)])
#         _log.info('move_ids: %s' % move_ids)

#         moves = self.pool['stock.move'].browse(cr, uid, move_ids)
#         _log.info('moves: %s' % moves)

#         # wiz = self.pool.get('wiz.product.label.picking').browse(
#         #     cr, uid, context['active_id'], context=context)
#         wiz = self.pool.get('wiz.product.label').browse(
#             cr, uid, context['active_id'], context=context)

#         _log.info('context: %s' % context)
#         _log.info('context[active_id]: %s' % context['active_id'])
#         _log.info('wiz.quantity: %s' % wiz.quantity)

#         product_ids = []
#         if wiz.quantity == 'one':
#             product_ids = [m.product_id.id for m in moves]
#             product_ids = list(set(product_ids))
#         elif wiz.quantity == 'line':
#             product_ids = [m.product_id.id for m in moves]
#         elif wiz.quantity == 'total':
#             for m in moves:
#                 _log.info('m.product_id: %s' % m.product_id)
#                 product_ids = product_ids + (
#                     [m.product_id.id] * int(m.product_qty))

#         products = filter(
#             lambda x: x, self.pool.get('product.product').browse(
#                 cr, uid, product_ids, context=context))

#         if not products:
#             raise exceptions.Warning(_('No labels for print'))
#         else:
#             return products

#     # def render_html(self, cr, uid, ids, data=None, context=None):
#     #     report_obj = self.pool['report']
#     #     picking_obj = self.pool['stock.picking']
#     #     report = report_obj._get_report_from_name(
#     #         cr, uid, 'product_label_picking.label_picking')
#     #     selected_orders = picking_obj.browse(cr, uid, ids, context=context)

#     #     docargs = {
#     #         'doc_ids': ids,
#     #         'doc_model': report.model,
#     #         'docs': selected_orders,
#     #         'get_partner': partial(self.get_partner, cr, uid, context=context),
#     #         'get_products': partial(
#     #             self.get_products, cr, uid, context=context)
#     #     }

#     #     return report_obj.render(
#     #         cr, uid, ids,
#     #         'product_label_picking.label_picking', docargs,
#     #         context=context)
