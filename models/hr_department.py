from odoo import fields, models

from .hr_fiscal_year import get_schedules

class HrDepartment(models.Model):
    
    _inherit = "hr.department"
    project_id = fields.Many2one('project.project')
    code = fields.char(copy=false, default= 'new')
    User_partner_id= fields.Many2one('res.users')
    Is_tech= fields.Boolean()
    Description= fields.Char()