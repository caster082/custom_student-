from odoo import models,fields

class EduBackGroung(models.Model):
    _name = 'edubackground'
    _description = 'Education Background'

    image = fields.Binary(string="Image", attachment=True)
    name = fields.Char(string="Name")
    location = fields.Char(string="Location")
    certification = fields.Char(string="Certification")
    description = fields.Char(string="Description")
    from_date = fields.Date(string="From Date")
    to_date = fields.Date(string="To Date")
    sample_biography_id = fields.Many2one('samplebiography')