from odoo import models, api
# for image file
import base64
import io

class CustomStudentExcelReport(models.Model):
    #module name and report name in custom_student_excel_report.xml
    _name = 'report.custom_student.custom_student_excel_report_id'
    #start with report and report_xlsx download excel report
    _inherit = 'report.report_xlsx.abstract'


    #decoratetor
    @api.multi
    def generate_xlsx_report(self, workbook, data, lines):
        header_format = workbook.add_format({'font_size': 14, 'bold': True, 'align': 'center', 'valign': 'vcenter'})
        label_format = workbook.add_format({'font_size': 11, 'bold': True})

        # take sheet
        sheet = workbook.add_worksheet("Student Report")
        # take 3 column and width
        sheet.set_column(0, 0, 25)
        sheet.set_column(1, 1, 50)
        sheet.set_column(2, 2, 20)
        # row height
        sheet.set_row(0, 100)
        sheet.merge_range('A1:B1', 'Student Report', header_format)

        # take image name from db
        image_file = lines.image
        #change base64 using decode method
        image_data = base64.b64decode(image_file)
        #write with bye using io.bye
        image = io.BytesIO(image_data)
        sheet.insert_image('C1', 'image_file.png', {'image_data': image, 'x_scale': 0.6, 'y_scale': 0.6})

        sheet.write('A2', 'Name', label_format)
        sheet.merge_range('B2:C2', lines.name)

        sheet.write('A3', 'NRC', label_format)
        sheet.merge_range('B3:C3', lines.nrc)


