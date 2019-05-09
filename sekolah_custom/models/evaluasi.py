from odoo import api, fields, models, _

class Evaluasi(models.Model):
	_name = 'sekolah.custom.evaluasi'

	rata_rata = fields.Integer(compute='_compute_average')
	ekskul_id = fields.Many2one('sekolah.custom.ekskul', string="Ekskul", required=False)
	trainer_id = fields.Many2one('sekolah.custom.trainer', string="Trainer", required=False)
	evaluasi_det_ids = fields.One2many('sekolah.custom.evaluasi.det', 'evaluasi_id')

	@api.depends('evaluasi_det_ids')
	def _compute_average(self):	
		for rec in self:
			list_detail=[]

			for detail in rec.evaluasi_det_ids:
		
				list_detail.append(detail.nilai)
				
			if len(rec.evaluasi_det_ids) > 0:	
				rec.rata_rata= sum(list_detail)/len(rec.evaluasi_det_ids)

	@api.multi
	def name_get(self):
		result = []
		for rec in self:
			result.append((rec.id, "%s" % (rec.ekskul_id.name)))

		return result

