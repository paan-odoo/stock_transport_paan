from odoo import models, fields

class DockDock(models.Model) :
    _name = "dock.dock"
    _description = "model dock dock"

    name = fields.Char("Name",default="new")