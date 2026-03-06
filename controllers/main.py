
from odoo import http
from odoo.http import request



class WarehouseStockAPI(http.Controller):
    @http.route('/api/warehouse_stock/<int:product_id>',
                type='json', auth='public', methods=['POST'], csrf=False)


    def get_warehouse_stock(self, product_id):
        product = request.env['product.product'].sudo().browse(product_id)

        if not product.exists():
            return {'error': 'Product not found'}

        warehouses = request.env['stock.warehouse'].sudo().search([])

        result = []

        for warehouse in warehouses:
            location = warehouse.lot_stock_id

            qty = product.with_context(
                location=location.id
            ).qty_available

            result.append({
                'warehouse': warehouse.name,
                'available_qty': qty,
                'Disponible': 'disponible' if qty > 0 else 'indisponible'
            })

        return {
            'product_id': product.id,
            'product_name': product.name,
            'warehouses': result
        }
