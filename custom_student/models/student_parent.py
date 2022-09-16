from odoo import models,fields

class StudentParent(models.Model):
    _name = 'student.parent'
    _inherits = {'customstudent': 'student_id'}
    _description = 'Student Parent Table'




    father_name = fields.Char(string="Father Name", required="True")
    mother_name = fields.Char(string="Mother Name", required="True")
    student_id = fields.Many2one('customstudent', string="Student ID")
    user_id = fields.Many2one('res.users', string="User ID")
    skill_id = fields.One2many('bio.skill', 'student_parend_id')
    education_id = fields.Many2one('edubackground', 'Education Id')


