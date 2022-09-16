# -*- coding: utf-8 -*-

from odoo import models, api, tools
from odoo.tools.translate import _

import base64
import io



class SampleBiographyExcelReport(models.Model):
    _name = 'report.custom_student.sample_biography_excel_report_template'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        name_format = workbook.add_format({'font_size': 16, 'bold': True,
                                           'align': 'center', 'valign': 'vcenter'})
        header_format = workbook.add_format({'font_size': 14, 'bold': True,
                                             'bg_color': 'blue', 'color': 'white'})
        label_format = workbook.add_format({'font_size': 11, 'bold': True})
        # sheet name
        sheet = workbook.add_worksheet("Sample Biography")
        # column 0 to 5 ,A to F width define 20
        sheet.set_column(0, 5, 20)
        sheet.set_row(0, 110)

        sheet.merge_range('A1:E1', lines.name, name_format)

        # image is binary
        #image_profile = lines.image
        # change decode
        #image_data = base64.b64decode(image_profile)
        # change bye to show image data
        #image = io.BytesIO(image_data)
        #sheet.insert_image('F1' 'image_profile.png', {'image_data': image, 'x_scale': 0.6, 'y_scale': 0.6})

        sheet.merge_range('A2:F2', 'Biography Information', header_format)
        sheet.write('A3', _("Phone"), label_format)
        sheet.merge_range('B3:F3', lines.phone)
        sheet.write('A4', _('NRC'), label_format)
        sheet.merge_range('B4:F4', lines.nrc)

        sheet.write('A5', _('Email'), label_format)
        sheet.merge_range('B5:F5', lines.email)

        sheet.write('A6', _('Facebook'), label_format)
        sheet.merge_range('B6:F6', lines.facebook)

        sheet.write('A7', _('Date of Birth'), label_format)
        sheet.merge_range('B7:F7', lines.date_of_birth,
                          workbook.add_format({'align': 'left', 'num_format': 'dd mmm yyyy'}))

        sheet.write('A8', _('Religion'), label_format)
        sheet.merge_range('B8:F8', lines.nationality)

        row = 9
        column = 0
        sheet.merge_range(row, column, row, column+5, 'Education Background', header_format)

        row += 1
        sheet.write(row, column, _('Name'), label_format)
        column += 1
        sheet.write(row, column, _('Location'), label_format)
        column += 1
        sheet.write(row, column, _('Certification'), label_format)
        column += 1
        sheet.write(row, column, _('From Date'), label_format)
        column += 1
        sheet.write(row, column, _('To Date'), label_format)
        column += 1
        sheet.write(row, column, _('Description'), label_format)

        row += 1
        column = 0
        for eb1 in lines.education_background:
            sheet.write(row, column, eb1.name)
            column += 1
            sheet.write(row, column, eb1.location)
            column += 1
            sheet.write(row, column, eb1.certification)
            column += 1
            sheet.write(row, column, eb1.from_date, workbook.add_format({'align': 'left', 'num_format': 'dd mmm yyyy'}))
            column += 1
            sheet.write(row, column, eb1.to_date, workbook.add_format({'align': 'left', 'num_format': 'dd mmm yyyy'}))
            column += 1
            sheet.write(row, column, eb1.description)
            row += 1
            column = 0














