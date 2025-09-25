from odoo import api, fields, models, _


class HrJobInherit(models.Model):
    _inherit = 'hr.job'

    status = fields.Selection(
        [
            ("en_cours", "En cours"),
            ("annule", "Annulé"),
            ("cloture", "Clôturé"),
        ],
        string=_("Statut du suivi"),
        help=("État d'avancement du recrutement"),
        required=False
    )

    # Document requirements for administrative validation
    copy_cin = fields.Boolean(
        string="2 copies de la CIN légalisées & attestation CNSS",
        help="Document requis pour la validation administrative",
    )
    doc_cv = fields.Boolean(
        string="Curriculum Vitae (CV)",
        help="Document requis pour la validation administrative",
    )
    doc_diplomes = fields.Boolean(
        string="Copies légalisées des diplômes",
        help="Document requis pour la validation administrative",
    )
    doc_demission = fields.Boolean(
        string="Copie légalisée de la démission",
        help="Document requis pour la validation administrative",
    )
    doc_bulletins_paie = fields.Boolean(
        string="3 derniers bulletins de paie cachetés",
        help="Document requis pour la validation administrative",
    )
    doc_attestation_libre = fields.Boolean(
        string="Attestation de travail précisant que vous êtes libre de tout engagement",
        help="Document requis pour la validation administrative",
    )
    doc_certificats_travail = fields.Boolean(
        string="Certificats de travail",
        help="Document requis pour la validation administrative",
    )
    doc_rib = fields.Boolean(
        string="RIB ou attestation bancaire",
        help="Document requis pour la validation administrative",
    )
    doc_acte_mariage = fields.Boolean(
        string="Acte de mariage + copie CIN de l'époux(se) (si marié(e))",
        help="Document requis pour la validation administrative",
    )
    doc_extraits_naissance = fields.Boolean(
        string="Extrait(s) de naissance des enfants (le cas échéant)",
        help="Document requis pour la validation administrative",
    )
    doc_anthropometrique = fields.Boolean(
        string="Fiche anthropométrique récente",
        help="Document requis pour la validation administrative",
    )
    doc_radiologie = fields.Boolean(
        string="Radio pulmonaire",
        help="Document requis pour la validation administrative",
    )
