from odoo import models, fields, api
import base64
class StockPickingBatch(models.Model) :
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one('dock.dock')
    fleet_id = fields.Many2one('fleet.vehicle', "Vehicle")
    vehicle_category = fields.Many2one('fleet.vehicle.model.category')
    driver_id = fields.Many2one(related="fleet_id.driver_id")
    driver_image = fields.Binary(related="driver_id.image_1920")
    driver_name = fields.Char(related="driver_id.complete_name")
    weight = fields.Integer(compute="_compute_weight_volume", default=0,store=True)
    volume = fields.Integer(compute = "_compute_weight_volume",default=0,store=True)
    total_weight = fields.Float(compute = "_compute_total_weight_volume")
    total_volume = fields.Float(compute = "_compute_total_weight_volume")
    picking_ids_count = fields.Integer("#Transfers",compute = "_compute_move_count",default=0,store=True)
    move_line_ids_count = fields.Integer("#lines",compute = "_compute_move_count",default=0,store=True)
    
    @api.depends('picking_ids','move_line_ids')
    def _compute_move_count(self) :
        for record in self :
            record.picking_ids_count = len(record.picking_ids)
            record.move_line_ids_count = len(record.move_line_ids)
    
    @api.depends('picking_ids.weight','picking_ids.volume','vehicle_category')
    def _compute_weight_volume(self) :
        for record in self :
            if record.vehicle_category and record.vehicle_category.max_weight > 0 and record.vehicle_category.max_volume > 0 :
                record.weight = (record.total_weight)/(record.vehicle_category.max_weight)
                record.volume = (record.total_volume)/(record.vehicle_category.max_volume)
            
    @api.depends('picking_ids')
    def _compute_total_weight_volume(self) :
        for record in self :
            if record.picking_ids :
                for line in record.picking_ids :
                    record.total_weight += line.weight
                    record.total_volume += line.volume
            else :
                record.total_weight =0
                record.total_volume =0

            

