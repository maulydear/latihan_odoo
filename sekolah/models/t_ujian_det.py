from odoo import api, fields, models, _

class T_ujian_det(models.Model):
	_name = 'sekolah.t_ujian_det'

	nilai = fields.Integer(string="nilai", required=False, )

	t_ujian_id = fields.Many2one('sekolah.t_ujian',)
	matapelajaran_id = fields.Many2one(comodel_name="sekolah.matapelajaran", required=True, )