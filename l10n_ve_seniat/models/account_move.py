from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class AccountMove(models.Model):
    _inherit = "account.move"

    l10n_ve_control_number = fields.Char(
        "Control Number",
        help="Number used to manage pre-printed invoices, by venezuelan law",
        copy=False,
        tracking=True,
    )

    marck_paper = fields.Boolean("Voided Document", default=False)

    maq_fiscal_p = fields.Boolean("Fiscal Machine", default=False)

    @api.constrains("l10n_ve_control_number")
    def _check_unique_l10n_ve_control_number_insensitive(self):
        """
        Check if another invoice/bill (as appropiate) has the same
        l10n_ve_control_number and the same commercial_partner_id than
        the current record. If so, raise a ValidationError.
        """
        for record in self:
            include_receipts = True
            if record.l10n_ve_control_number and record.is_invoice():
                move_type_range = (
                    record.is_sale_document(include_receipts)
                    and record.get_sale_types(include_receipts)
                    or record.get_purchase_types(include_receipts)
                )
                same_control_number = record.search(
                    [
                        ("commercial_partner_id", "=", record.commercial_partner_id.id),
                        ("move_type", "in", move_type_range),
                        (
                            "l10n_ve_control_number",
                            "=ilike",
                            record.l10n_ve_control_number,
                        ),
                        ("id", "!=", record.id),
                    ],
                    limit=1,
                )
                if same_control_number:
                    raise ValidationError(
                        _(
                            "The journal entry with control number %(number)s "
                            "already exists in Odoo under the number %(same)s "
                            "for supplier %(supplier)s.",
                            number=same_control_number.l10n_ve_control_number,
                            same=same_control_number.name or "-",
                            supplier=same_control_number.partner_id.display_name,
                        )
                    )

    def action_post(self):
        result = super().action_post()
        country_ve = self.env.ref("base.ve")
        for record in self.filtered(
            lambda it: it.is_invoice()
            and it.company_id.country_id == country_ve
            and not it.l10n_ve_control_number
        ):
            record.l10n_ve_control_number = self.env["ir.sequence"].next_by_code(
                "l10n_ve_seniat.control.number"
            )
        return result
