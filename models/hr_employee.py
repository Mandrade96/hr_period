

from odoo import api, fields, models


class HrEmployee(models.AbstractModel):
    _inherit = "hr.employee.base"

    contract_id = fields.Many2one(search="_search_contract")

    @api.model
    def _search_contract(self, operator, value):
        res = []
        contract_ids = self.env["hr.contract"].search(
            [("employee_id", operator, value)]
        )
        res.append(("id", "in", contract_ids.ids))
        return res
