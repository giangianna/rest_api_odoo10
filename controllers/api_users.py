import odoo.http as http
from odoo.http import Response
import json
from datetime import datetime, timedelta
import werkzeug
from odoo import models, fields, api
import urllib3.request
import simplejson as json
import requests
import ssl
from pprint import pprint
import base64
import ast
import itertools as it


class UsersApi(http.Controller):
    
    @http.route('/api/users', csrf=False, type='http', methods=["GET"], token=None, auth='public')
    # print('test')
    def get_users(self, **args):
        request.env.cr.execute("""
                        SELECT * FROM res_users 
                        """)
        data = []
        q_result = request.env.cr.dictfetchall()
        for line in q_result:

            id_user = line.get('id')
            active = line.get('active')
            company_id = line.get('company_id')
            partner_id = line.get('partner_id')

            data.append({
                    "id_user":id_user,
                    "active":active,
                    "company_id":company_id,
                    "partner_id":partner_id
                })
        return json.dumps(data)