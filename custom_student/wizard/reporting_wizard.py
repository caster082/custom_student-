from odoo import models,fields,api

class ReportingWizard(models.Model):
    _name = 'reporting.wizard'

    bio_type = fields.Selection(
        selection=[
            ("simple", 'Simple'),
            ("standard", "Standard"),
        ],
        string="Sample Biography Type",
        default="standard",
    )

   # bind job type and image when choose name in wizard
    @api.depends('simple_bio')
    def _get_simple_bio_data(self):
        for rec in self:
            rec.simple_job_type = rec.simple_bio.school_type
            rec.simple_gender = rec.simple_bio.gender
            rec.simple_image = rec.simple_bio.image

    # domain mean for filter
    simple_bio = fields.Many2one('samplebiography', string="Simple Bio", domain=[('state', '=', 'done')])
    simple_job_type = fields.Char(string="Job Type", compute="_get_simple_bio_data")
    simple_gender = fields.Char(string="Gender", compute="_get_simple_bio_data")
    simple_image = fields.Binary(string="Image", compute="_get_simple_bio_data")

    @api.depends('standard_bio')
    def _get_standard_bio_data(self):
        for rec in self:
            rec.standard_job_type = rec.standard_bio.school_type
            rec.standard_gender = rec.standard_bio.gender
            rec.standard_image = rec.standard_bio.image

    standard_bio = fields.Many2one('customstudent', string="Standard Simple Bio")
    standard_job_type = fields.Char(string="Job Type", compute="_get_standard_bio_data")
    standard_gender = fields.Char(string="Gender", compute="_get_standard_bio_data")
    standard_image = fields.Binary(string="Image", compute="_get_standard_bio_data")

# print pdf from wizard
    def print_sample_biography_pdf(self):
        for rec in self:
            if rec.bio_type == 'simple':
                return self.env.ref('custom_student.reporting_simple_bio_pdf').report_action(self)

    def print_sample_biography_excel(self):
        for rec in self:
            if rec.bio_type == 'simple':
                return self.env.ref('custom_student.reporting_simple_bio_excel').report_action(self)




