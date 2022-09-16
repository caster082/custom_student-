# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # after save value >>custom student>>setting>> check >>technical >>system parameter and external identifier

    register_days = fields.Integer(string='Register Days',config_parameter='custom_student.register_days')
