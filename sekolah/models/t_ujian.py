from odoo import api, fields, models, _
from datetime import datetime
from odoo.exceptions import UserError

class T_ujian(models.Model):
	_name = 'sekolah.t_ujian'

	tgl_ujian = fields.Date(required=False)
	rata_rata = fields.Integer(compute='_compute_average')
	siswa_id = fields.Many2one("sekolah.siswa", required=False)
	t_ujian_det_ids = fields.One2many('sekolah.t_ujian_det', 't_ujian_id')

	def valid_date(self):
		rec = self.ensure_one()
		today = fields.Date.today()
		if rec.tgl_ujian <= today:
			new = self.env["sekolah.t_ujian"].create({
	    		"tgl_ujian" : rec.tgl_ujian,
	    		"siswa_id" : rec.siswa_id.id
	    		})
		elif rec.tgl_ujian > today:
			raise UserError(_("Tanggal Harus <= Hari ini"))


	@api.depends('t_ujian_det_ids')
	def _compute_average(self):	
		for rec in self:
			list_detail=[]

			for detail in rec.t_ujian_det_ids:
		
				list_detail.append(detail.nilai)
				
			if len(rec.t_ujian_det_ids) > 0:	
				rec.rata_rata= sum(list_detail)/len(rec.t_ujian_det_ids)

			