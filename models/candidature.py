# -*- coding: utf-8 -*-
from odoo import fields, models, api

class HrApplicant(models.Model):
    _inherit = "hr.applicant"

    
    # Fixed One2many field with proper inverse_name
    scorecard_ids = fields.One2many(
        comodel_name="softy.scorecard", 
        inverse_name="applicant_id",  # This is the field in rhs.scorecard that points back to hr.applicant
        string="Scorecard de Recrutement – Entretien RH"
    )
    historique_ids=fields.One2many(
        comodel_name="softy.hist",
        inverse_name="applicant_id",
        string="Historique des Etapes de Recrutement"
    )
    phone_screening_ids=fields.One2many(
        comodel_name="softy.phone.screening",
        inverse_name="applicant_id",
        string="Screening Telephonique"
    )

    is_candidate_blacklisted = fields.Boolean(compute="_compute_is_candidate_blacklisted", store=True)
    @api.depends('candidate_id.blacklisted')
    def _compute_is_candidate_blacklisted(self):
        for record in self:
            record.is_candidate_blacklisted = record.candidate_id.blacklisted if record.candidate_id else False