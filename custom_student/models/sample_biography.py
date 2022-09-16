import random
from odoo import models,fields,api, _
from odoo.exceptions import ValidationError
from datetime import date
# from dateutil.relativedelta import relativedelta


class SampleBiography(models.Model):
    _name = 'samplebiography'
    _description = 'Sample Biography'
    #drag and drop
    _order = 'id'

    #inherit for chapter
    _inherit = ['mail.thread', 'mail.activity.mixin']



    #active means archive and unarchive
    #track visibility mean check history who click active button
    active = fields.Boolean(string="Active", default=True, track_visibility="always")
    toggle_active = fields.Boolean(string ="Toggle Active", default=True)
    html_description = fields.Html(string="HTML Description")
    study_date = fields.Date(string="Study Date",default=date.today(), help="Remind for study")
    planning_date = fields.Datetime(string="Planning Date", default=fields.Datetime.now)
    #to use in calendar view
    duration = fields.Float(string="Duration")
    # auto generate field
    reference = fields.Char(string="Reference", required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))


    image = fields.Binary(string="Profile", attachment=True)

    school_type = fields.Selection(
        selection=[
            ("ucsy_ygn", "University of Computer Studied YGN"),
            ("ucsy_mdy", "University of Computer Studied Mdy"),

        ],
        string="School",
        default="ucsy_ygn",
        required="True",

    )

    name = fields.Char(string="Name", translate=True)
    nrc = fields.Char(string="NRC", translate=True)

    # date of birth constrain
    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth > date.today():
                raise ValidationError("Date must not over today")

    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            today = date.today()
            dob = record.date_of_birth
            number_of_year = today.year - dob.year
            record.age = number_of_year
        #     age = 0
        #     if record.date_of_birth:
        #         age = relativedelta(fields.Date.today(), record.date_of_birth).years
        #     record.age = age

    age = fields.Integer(string="Age", group_operator=False, compute="_compute_age")
    date_of_birth = fields.Date(string="Date of Birth", required=True, default=date.today())
    nationality = fields.Char(string="Nationality")
    gender = fields.Selection(
        selection=[
            ("female", "Female"),
            ("male", "Male"),
            ("other", "Other"),
        ],
        string="Gender",
        default="female",
        required="True",
    )

    qualification = fields.Char(string="Qualification")
    phone = fields.Char(string="Phone", translate=True)
    email = fields.Char(string="Email", translate=True)
    facebook = fields.Char(string="Facebook", translate=True)
    address = fields.Char(string="Address", translate=True)
    education_background = fields.One2many('edubackground', 'sample_biography_id',
                                           states={'done': [('readonly', True)]})
    bio_history = fields.One2many('bio.history', 'sample_biography_id',
                                  states={'done': [('readonly', True)]})
    skill = fields.One2many('bio.skill', 'sample_biography_id')
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("confirm", "Confirm"),
            ("done", "Done"),
        ],
        string="Status", readonly=True, default='draft'
    )
    student_id = fields.Many2one('customstudent', string ='Student ID')
    student_nrc = fields.Char(string="Student NRC", related='student_id.nrc')

    # report print with object type
    def print_sample_biography_report(self):
        return self.env.ref('custom_student.sample_biography_report').report_action(self)

    # excel export
    def print_sample_biography_excel_report(self):
        return self.env.ref('custom_student.sample_biography_excel_report_id').report_action(self)

    # draft action
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    # confirm action
    # def action_confirm(self):
    #     message = 'Confirmed Successfully!!'
    #     for rec in self:
    #         rec.state = 'confirm'

    def action_confirm(self):
        message = 'Confirmed Successfully!!'
        self.state = 'confirm'
        #for rec in self:
            #rec.state = 'confirm'
        return {
            # self.state: 'confirm',
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
            'message': message,
            'type': 'success',
            'sticky': False,

            }

        }

    # done action
    # def action_done(self):
    #     for rec in self:
    #         rec.state = 'done'

    def action_done(self):
        self.state='done'
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }


    # ebl count is education count
    def _compute_ebl_count(self):
        count = self.env['edubackground'].search_count([('sample_biography_id', '=', self.id)])
        for rec in self:
            rec.ebl_count = count

    ebl_count = fields.Integer(string ="EBL count", compute=_compute_ebl_count)

    # go to the education page when click eduction count
    def open_education_background(self):
        return {
            'name': 'Ecuation Background',
            'type': 'ir.actions.act_window',
            'res_model': 'edubackground',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'domain': [['sample_biography_id', '=', self.id]]
        }


    #progress bar
    progress = fields.Integer(string="Progress", compute='_compute_progress')
    #priority
    priority = fields.Selection(
        selection=[
            ("0", "Normal"),
            ("1", "Low"),
            ("2", "High"),
            ("3", "Very High"),
        ],
        string="Priority"
    )
    #color picker
    color = fields.Char(string="Color")

 # progress bar
    @api.depends('state')
    def _compute_progress(self):
        for rec in self:
            if rec.state == 'draft':
                # progress = random.randrange(0,25)
                progress = 25
            elif rec.state == 'confirm':
                # progress = random.randrange(0,50)
                progress = 50

            elif rec.state == 'done':
                progress = 100
            else:
                progress =0
            rec.progress = progress


    # sequence(auto genereate field)
    @api.model
    def create(self, vals):
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('samplebiography') or _('New')
        res = super(SampleBiography,self).create(vals)
        return res

    # whatsapp integration
    def action_share_whatsapp(self):
        if not self.phone:
            raise ValidationError(_("Missing phone number in student"))
        message = 'Hi %s' % self.name
        whatsapp_api_url = 'https://api.whatsapp.com/send?phone=%s&text=%s' %(self.phone, message)
        return{
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': whatsapp_api_url
        }

    # send email
    def action_send_email(self):
        template_id = self.env.ref('custom_student.sample_biography_email_template').id
        #print("Template Id",template_id) 52 (can check setting>>template>>find student registration>>metadata)

        # mail.template is model check from view form
        template=self.env['mail.template'].browse(template_id)
        # print("Template",template)
        template.send_mail(self.id, force_send=True)

    # cron job
    def sample_cron(self):
        print("cron is working")















