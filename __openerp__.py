{
    "name" : "Biometric Device Integration",
    "version" : "1.0",
    "author" : "Gaurav Sahu",
    "category" : "Custom",
    "website" : "gauravsahu.odoo.com",
    "description": "A Module for Biometric Device Integration",
    "depends" : ["base","hr"],
    "init_xml" : [],
    "data" : [
        "views/biometric_machine_view.xml",
        "views/hr_employee_view.xml",
        #"views/hr_attendance_view.xml",
        #"report/daily_attendance_view.xml",
        "schedule.xml",
        "wizard/schedule_wizard.xml",
    ],
    "active": False,
    "installable": True
}
