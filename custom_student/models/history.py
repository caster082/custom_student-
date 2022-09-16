from odoo import models,fields

class History(models.Model):
    _name = 'bio.history'
    _description = 'Bio History'

    image = fields.Binary(string="Image", attachment=True)
    name = fields.Char(string="Name",required=True)
    position = fields.Char(string="Position")
    responsibilities = fields.Char(string="Responsibilities")
    from_date = fields.Date(string="From Date")
    to_date = fields.Date(string="To Date")
    description = fields.Char(string="Description")
    sample_biography_id = fields.Many2one('samplebiography')