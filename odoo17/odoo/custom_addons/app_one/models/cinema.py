from odoo import models, fields, api


class Cinema(models.Model):
    _name = "cinema"
    _description = "cinema  model"
    _rec_name = "title"

    title = fields.Char(required=True, default="Untitled")
    genre = fields.Char()
    language = fields.Char(required=True)
    director = fields.Many2many(
        'crew',
        'movie_director_rel',
        'cinema_id',
        'crew_id')
    producer = fields.Many2many(
        'crew',
        'movie_producer_rel',
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
    rating = fields.Integer()
    price = fields.Integer(required=True)
    poster = fields.Binary()
    avatar_128 = fields.Binary(compute="_compute_image_128", store=False)
    overview = fields.Text()
    status = fields.Selection([
        ('announced', 'Announced'),
        ('premiered', 'Premiered'),
        ('release', 'Release'),
        ('closed', 'Closed'),
    ], default="announced")

    @api.depends("poster")
    def _compute_image_128(self):
        for rec in self:
            rec.avatar_128 = rec.poster
