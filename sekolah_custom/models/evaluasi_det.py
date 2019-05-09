from odoo import api, fields, models, _

class Evaluasi_det(models.Model):
	_name = 'sekolah.custom.evaluasi.det'

	evaluasi_id = fields.Many2one('sekolah.custom.evaluasi')
	nilai = fields.Integer(string="nilai", required=False)
	siswa_id = fields.Many2one('sekolah.siswa')
	