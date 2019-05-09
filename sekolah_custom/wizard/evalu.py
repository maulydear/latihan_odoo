from odoo import api, fields, models, _

class EvaluWizard(models.TransientModel):
	_name = 'sekolah.custom.evalu.wizard'

	name = fields.Char(string="Name")
	ekskul_id = fields.Many2one('sekolah.custom.ekskul', string="Ekskul", required=False)
	trainer_id = fields.Many2one('sekolah.custom.trainer', string="Trainer", required=False)
	siswa_ids = fields.One2many('sekolah.custom.evalu.det.wizard', 'evalu_id')

	def add_evalu_wizard(self):
		self.ensure_one()
		siswa_list = []
		for siswa in self.siswa_ids:
			siswa_list.append([0,0, {
				'siswa_id' : siswa.siswa_id.id,
				'nilai' : siswa.nilai,
				}])

		create_eval = self.env["sekolah.custom.evaluasi"].create({
    		"evaluasi_det_ids" : siswa_list,
			"ekskul_id" : self.ekskul_id.id,
			"trainer_id" : self.trainer_id.id
    		})

		return {
				'type': 'ir.actions.act_window',
		        'name': 'Evaluasi',
		        'res_model': 'sekolah.custom.evaluasi',
		        'res_id': create_eval.id,
		        'view_type': 'form',
		        'view_mode': 'form',
		        'target': 'self',
		        'context': {'parent_obj': self.id}
		        }

class EvaluDetWizard(models.TransientModel):
	_name = 'sekolah.custom.evalu.det.wizard'

	nilai = fields.Integer(string="Nilai", required=False)
	evalu_id = fields.Many2one('sekolah.custom.evalu.wizard')
	siswa_id = fields.Many2one('sekolah.siswa')