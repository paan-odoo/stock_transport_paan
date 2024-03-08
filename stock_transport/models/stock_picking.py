from odoo import models, fields, api

class StockPicking(models.Model) :
    _inherit = "stock.picking"

    volume = fields.Float(compute = "_compute_weight_volume",default=0)
    weight = fields.Float(compute = "_compute_weight_volume",default=0)

    @api.depends("move_ids_without_package.quantity",'move_ids_without_package.product_uom_qty',"batch_id")
    def _compute_weight_volume(self) :
        for record in self :
            for line in record.move_ids_without_package :
                record.weight += line.product_id.weight * line.quantity
                record.volume += line.product_id.volume * line.quantity