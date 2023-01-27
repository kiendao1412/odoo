from odoo import api, fields, models, _
class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    display_price = fields.Boolean(string='Display Price', config_parameter='new_module.display_price', default=True)
