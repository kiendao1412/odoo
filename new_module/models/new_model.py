from odoo import fields, models
class NewModel(models.Model):
_name = "new.model"
_description = “New Model”

def _default_display_price(self):
    return self.env['ir.config_parameter'].sudo().get_param('new_module.display_price')

name = fields.Char()
price = fields.Float()
display_price = fields.Boolean(string='Display Price',compute='_get_display_price',default=_default_display_price)

def _get_display_inpatient(self):
     for object in self:
         object.display_price = self.env['ir.config_parameter'].sudo().get_param('new_module.display_price')
