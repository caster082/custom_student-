# -*- coding: utf-8 -*-
{
    'name': "MIT School Management System",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Thandar",
    'maintainer': 'Khant Sithu Aung',
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'student testing module',
    'version': '0.1',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': [
        'base_setup',
        'mail',
        'report_xlsx',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/sample_biography_security.xml',

        'views/custom_student_view.xml',
        'views/custom_student_form_view.xml',
        'reports/custom_student_report.xml',

        'reports/sample_biography_report.xml',
        'reports/sample_biography_excel_report.xml',


        'views/sample_biography_view.xml',
        'views/sample_biography_tree_view.xml',
        'views/search_sample_biog_view.xml',
        'views/sample_biography_form_view.xml',
        'views/sample_biography_kanban_view.xml',
        'views/sample_biography_activity_view.xml',
        'views/sample_biography_graph_view.xml',

        'views/education_background.xml',
        'views/education_background_tree_view.xml',
        'views/education_form_view.xml',

        'views/history.xml',
        'views/history_tree_view.xml',
        'views/history_form_view.xml',

        'views/skill.xml',
        'views/skill_tree.xml',
        'views/skill_form_view.xml',

        'wizard/reporting_wizard.xml',
        'wizard/reporting_simple_biography_pdf.xml',
        'wizard/reporting_simple_biography_excel.xml',

        'data/sequence.xml',
        'data/mail_template.xml',
        'data/cron.xml',

        'views/res_config_settings_views.xml',

        'views/student_parent.xml',
        'views/student_parent_form.xml',


        # 'views/language_selection.xml',

    ],

    # 'qweb': ['static/src/xml/base.xml'],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

}
