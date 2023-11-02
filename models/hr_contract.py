
from odoo import fields, models

from .hr_fiscal_year import get_schedules


class HrContract(models.Model):
    _inherit = "hr.contract"

    # Add semi-monthly to payroll schedules
    schedule_pay = fields.Selection(
        get_schedules, "Scheduled Pay", oldname="shedule_pay", index=True
    )

        