from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HrCandidateInherit(models.Model):
    _inherit = 'hr.candidate'

    blacklisted = fields.Boolean(
        string='Blacklisté',
        default=False,
        tracking=True,
        help="Marquer ce candidat comme blacklisté pour empêcher les futures candidatures"
    )
    
    motif_blackliste = fields.Char(
        string='Motif de Blackliste',
        help="Raison pour laquelle le candidat a été blacklisté"
    )
    
    @api.onchange('blacklisted')
    def _onchange_blacklisted(self):
        """Clear the blacklist reason if blacklisted is unchecked"""
        if not self.blacklisted:
            self.motif_blackliste = False

