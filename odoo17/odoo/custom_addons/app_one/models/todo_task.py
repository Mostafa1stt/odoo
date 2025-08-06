from odoo import models, fields


class Todo(models.Model):
    _name = "todo.task"

    task_name = fields.Char(required=1, default="Untitled")
    assign_to = fields.One2many('user', 'work_on', store=1)
    description = fields.Text()
    due_date = fields.Date(required=1)
    status = fields.Selection([
        ('new_in', 'New In'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ], default="new_in")

    def action_new_in(self):
        for rec in self:
            rec.status = 'new_in'

    def action_in_progress(self):
        for rec in self:
            rec.status = 'in_progress'

    def action_completed(self):
        for rec in self:
            rec.status = 'completed'


class User(models.Model):
    _name = "user"

    name = fields.Char(required=1, default="Untitled")
    phone = fields.Char()
    address = fields.Char()
    work_on = fields.Many2one('todo.task')
