from odoo import models, fields, api


class Cinema(models.Model):
    _name = "cinema"
    _description = "cinema  model"
    _rec_name = "title"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    active = fields.Boolean(default=True)
    title = fields.Char(required=True, default="Untitled")
    genre = fields.Char()
    language = fields.Char(required=True)
    director = fields.Many2many(
        'crew',
        'movie_director_rel',
        'cinema_id',
        'crew_id')
    writer = fields.Many2many(
        'crew',
        'movie_writer_rel',
        'cinema_id',
        'crew_id')
    actor = fields.Many2many(
        'crew',
        'movie_actor_rel',
        'cinema_id',
        'crew_id')
    releases = fields.Date()
    user_closed = fields.Boolean(default=False)
    rating = fields.Integer()
    price = fields.Integer(required=True)
    poster = fields.Binary()
    avatar_128 = fields.Binary(compute="_compute_image_128", store=False)
    overview = fields.Text()
    status = fields.Selection([
        ('announced', 'Announced'),
        ('released', 'Released'),
        ('closed', 'Closed'),
        ], store=True, compute='_compute_status', default="announced")

    @api.depends("poster")
    def _compute_image_128(self):
        for rec in self:
            rec.avatar_128 = rec.poster

    @api.depends('releases')
    def _compute_status(self):
        movie_ids = self.search([])
        for rec in movie_ids:
            if rec.releases and rec.releases >= fields.Date.today() and rec.user_closed is False:
                rec.status = 'announced'
            elif rec.releases and rec.releases < fields.Date.today() and rec.user_closed is False:
                rec.status = 'released'

    @api.depends('status')
    def _compute_active_closed(self):
        movie_ids = self.search([])
        for rec in movie_ids:
            if rec.status and rec.status == "closed":
                rec.active = False

    def action_closed(self):
        for rec in self:
            rec.status = "closed"
            rec.user_closed = True

    def action_open(self):
        for rec in self:
            rec.status = "announced"
            rec.user_closed = False
