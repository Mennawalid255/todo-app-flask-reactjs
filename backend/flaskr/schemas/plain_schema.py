from marshmallow import Schema, fields, validate


class PlainUserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)
    role = fields.Str(dump_only=True)
<<<<<<< HEAD
    permissions = fields.List(fields.Str(), dump_only=True)
    custom_permissions = fields.Dict(dump_only=True, data_key="customPermissions")
=======
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f


class PlainSignInSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)


class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class PlainTaskSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    status = fields.Str(
        validate=validate.OneOf(["PENDING", "IN_PROGRESS", "COMPLETED"]), required=True
    )
    created_at = fields.DateTime(dump_only=True, data_key="createdAt")
<<<<<<< HEAD


class PlainRoleUpdateSchema(Schema):
    role = fields.Str(required=True)


class PlainPermissionOverrideSchema(Schema):
    grants = fields.List(fields.Str(), required=False, load_default=[])
    revokes = fields.List(fields.Str(), required=False, load_default=[])
=======
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
