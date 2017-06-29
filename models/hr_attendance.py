# -*- encoding: utf-8 -*-
from openerp import api, models, fields, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
import logging

_logger = logging.getLogger(__name__)

class hr_attendance(models.Model):
	_name = "hr.attendance"
	_inherit = "hr.attendance"


	def updateAttendance(self):
	    scheduler_line_obj = self.env['biometric.machine']
            scheduler_lines = self.env['biometric.machine'].search([])
            for scheduler_line in scheduler_lines:
		    for att in scheduler_line.atten_ids:
			    employee = self.env['hr.employee'].search([('barcode','=',att.emp_code)])
			    #entrada creo nueva entrada
			    #raise Warning((employee.attendance_state,att.state))
			    if employee.attendance_state == 'checked_out' and att.state == 'pending':
				    _logger.debug('creada entrada %s para %s', att.name,employee.barcode)
			            self.create({'employee_id':employee.id,'check_in':att.name})
				    att.state='count'
			    #salida grabo salida en ultima entrada
			    elif employee.attendance_state == 'checked_in' and att.state == 'pending':
				    _logger.debug('creada salida %s para %s', att.name,employee.barcode)
				    attendance = self.search([('employee_id','=',employee.id)])
				    _logger.debug('salida %s para %s hora entrada %s', attendance[0],employee.barcode,attendance[0].check_in)
				    attendance[0].check_out=att.name
				    att.state='count'


	#Dowload attendence data regularly
	@api.model
	def schedule_attendance(self):
	    self.updateAttendance()

