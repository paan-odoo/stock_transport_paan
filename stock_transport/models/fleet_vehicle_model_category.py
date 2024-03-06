from odoo import models, fields, api

class FleetVehicleModelCategory(models.Model) :
    _inherit = 'fleet.vehicle.model.category'

    max_weight = fields.Integer("Max Weight (Kg)")
    max_volume = fields.Integer("Max Volume (m\xb3)")

    @api.depends('max_weight','max_volume')
    def _compute_display_name(self) :
        res = super()._compute_display_name()
        for record in self : 
            record.display_name = f"{record.name} ({record.max_weight} Kg, {record.max_volume} m\xb3)"
        return res