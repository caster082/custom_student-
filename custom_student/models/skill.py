from odoo import models,fields

class Skill(models.Model):
    _name = 'bio.skill'
    _description = 'Bio Skill'
    #not insert default field (create_uid,create_date)
    # _log_access = False

    image = fields.Binary(string="Image", attachment=True)
    name = fields.Char(string="Name")
    position = fields.Char(string="Position", trim=False)
    responsibilities = fields.Char(string="Responsibilities")
    language = fields.Char(string="Language")
    from_date = fields.Date(string="From Date")
    to_date = fields.Date(string="To Date")
    price = fields.Float(string="Price",digits='Product Price')
    description = fields.Char(string="Description")
    sample_biography_id = fields.Many2one('samplebiography')
    student_parend_id = fields.Many2one('student.parent')

