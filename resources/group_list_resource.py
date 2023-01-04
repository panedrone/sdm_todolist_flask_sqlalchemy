import json

import flask
import marshmallow as mm
from flask import Response
from flask_restful import Resource
from marshmallow.validate import Length

from services.groups_service import *


# noinspection PyTypeChecker
class NewGroupSchema(mm.Schema):
    # https://stackoverflow.com/questions/54345070/python-marshmallow-not-detecting-error-in-required-field
    # "required" just means "exists in JSON"
    g_name = mm.fields.Str(required=True,
                           allow_none=False,
                           validate=Length(min=1, error="Group name is missing"))

    # class Meta:
    #     fields = ("g_name",)


class GroupLiSchema(mm.Schema):
    class Meta:
        fields = ("g_id", "g_name", "g_tasks_count")


class GroupListResource(Resource):
    @staticmethod
    def get():
        res = get_all_groups()
        return GroupLiSchema().dump(res, many=True)

    @staticmethod
    def post():
        req_json = flask.request.json
        try:
            data = NewGroupSchema().load(req_json)
        except mm.ValidationError as error:
            return Response(
                json.dumps(error.messages),
                status=400,
            )
        g_name = data["g_name"]
        create_group(g_name)
