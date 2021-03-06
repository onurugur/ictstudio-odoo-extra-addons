# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#
#    Copyright (c) 2015 ICTSTUDIO (www.ictstudio.eu).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    moves_available_count = fields.Integer(
            string='Available Moves',
            compute='_get_moves_count',
    )
    moves_waiting_count = fields.Integer(
            string='Waiting Moves',
            compute='_get_moves_count',
    )

    @api.one
    @api.depends('move_lines')
    def _get_moves_count(self):
        self.moves_available_count = self.move_lines.search_count(
                [
                    ('state', '=', 'assigned'),
                    ('picking_id', '=', self.id)
                ]
        )
        self.moves_waiting_count = self.move_lines.search_count(
                [
                    ('state', '=', 'confirmed'),
                    ('picking_id', '=', self.id)
                ]
        )