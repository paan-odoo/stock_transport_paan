from odoo import models, fields, api

class StockPicking(models.Model) :
    _inherit = "stock.picking"

    volume = fields.Float(compute = "_compute_weight_volume",default=0)
    weight = fields.Float(compute = "_compute_weight_volume",default=0)

    @api.depends("move_ids_without_package",'move_ids_without_package.product_uom_qty',"batch_id")
    def _compute_weight_volume(self) :
        for record in self :
            weight_sum = 0
            volume_sum = 0
            for line in record.move_ids_without_package :
                weight_sum += line.product_id.weight * line.quantity
                volume_sum += line.product_id.volume * line.quantity
            record.weight = weight_sum
            record.volume = volume_sum

    