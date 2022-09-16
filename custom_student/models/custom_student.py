from odoo import models,fields

class CustomStudent(models.Model):
    _name = 'customstudent'
    _description = 'custom student sample'

    #inherit for chapter
    _inherit = ['mail.thread', 'mail.activity.mixin']


    #active means archive and unarchive
    #track visibility mean check history who click active button
    active = fields.Boolean(string="Active", default=True, track_visibility="always")

    image = fields.Binary(string="Profile", attachment=True)

    school_type = fields.Selection(
        selection=[
            ("0", "University of Computer Studied YGN"),
            ("1", "University of Computer Studied Mdy"),

        ],
        string="School",
        default="0",
        required="True",

    )

    name = fields.Char(string="Name")
    student_name = fields.Char(string="Student Name", required="True")
    nrc = fields.Char(string="NRC")
    date_of_birth = fields.Date(string="Date of Birth")
    nationality = fields.Char(string="Nationality")
    gender = fields.Selection(
        selection=[
            ("0", "Female"),
            ("1", "Male"),
            ("2", "Other"),
        ],
        string="Gender",
        default="0",
        required="True",
    )

    qualification = fields.Char(string="Qualification")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    facebook = fields.Char(string="Facebook")
    address = fields.Char(string="Home Address")
    # parent_id = fields.One2many('student.parent', 'Parent ID')






