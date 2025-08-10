from odoo import fields, models, api


class Crew(models.Model):
    _name = 'crew'
    _description = 'crew model'

    name = fields.Char(required=True, default="folan")
    photo = fields.Binary()
    avatar_128 = fields.Binary(compute="_compute_image_128", store=False)
    director_of = fields.Many2many(
        'cinema',
        'movie_director_rel',
        'crew_id',
        'cinema_id')
    producer_of = fields.Many2many(
        'cinema',
        'movie_producer_rel',
        'crew_id',
        'cinema_id')
    writer_of = fields.Many2many(
        'cinema',
        'movie_writer_rel',
        'crew_id',
        'cinema_id')
    actor_on = fields.Many2many(
        'cinema',
        'movie_actor_rel',
        'crew_id',
        'cinema_id')
    age = fields.Integer(required=True)
    biography = fields.Text()
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], required=True)

    @api.depends("photo")
    def _compute_image_128(self):
        for rec in self:
            rec.avatar_128 = rec.photo
