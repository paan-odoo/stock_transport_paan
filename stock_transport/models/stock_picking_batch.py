from odoo import models, fields, api
import base64
class StockPickingBatch(models.Model) :
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one('dock.dock')
    fleet_id = fields.Many2one('fleet.vehicle', "Vehicle")
    driver_id = fields.Many2one(related="fleet_id.driver_id")
    driver_image = fields.Binary(related="driver_id.image_1920")
    vehicle_category = fields.Many2one('fleet.vehicle.model.category')
    weight = fields.Integer(compute="_compute_weight_volume", default=0,store=True)
    volume = fields.Integer(compute = "_compute_weight_volume",default=0,store=True)
    total_weight = fields.Float(compute = "_compute_total_weight_volume")
    total_volume = fields.Float(compute = "_compute_total_weight_volume")
    transfers = fields.Integer("#Transfers",compute = "_compute_move_count",default=0,store=True)
    lines = fields.Integer("#Lines",compute = "_compute_move_count",default=0,store=True)
    
    @api.depends('picking_ids','move_line_ids')
    def _compute_move_count(self) :
        for record in self :
            record.transfers = len(record.picking_ids)
            record.lines = len(record.move_line_ids)
    
    @api.depends('picking_ids.weight','picking_ids.volume','vehicle_category')
    def _compute_weight_volume(self) :
        for record in self :
            if record.vehicle_category :
                record.weight =  (record.total_weight)/(record.vehicle_category.max_weight) if record.vehicle_category.max_weight > 0 else 0
                record.volume = (record.total_volume)/(record.vehicle_category.max_volume) if record.vehicle_category.max_volume > 0 else 0
            
    @api.depends('picking_ids','vehicle_category')
    def _compute_total_weight_volume(self) :
        for record in self :
            record.total_weight = sum(line.weight for line in record.picking_ids)
            record.total_volume = sum(line.volume for line in record.picking_ids)
            

