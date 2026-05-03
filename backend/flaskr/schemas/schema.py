from marshmallow import fields
from flaskr.schemas.plain_schema import (
<<<<<<< HEAD
    PlainPermissionOverrideSchema,
    PlainRoleUpdateSchema,
=======
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
    PlainSignInSchema,
    PlainTagSchema,
    PlainTaskSchema,
    PlainUserSchema,
)


class UserSchema(PlainUserSchema):
    pass


class SignInSchema(PlainSignInSchema):
    pass


<<<<<<< HEAD
class CurrentUserSchema(PlainUserSchema):
    pass


=======
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
class TagSchema(PlainTagSchema):
    pass


class TaskSchema(PlainTaskSchema):
    tag_name = fields.Str(dump_only=True, data_key="tagName")
    tag_id = fields.Int(required=True, load_only=True, data_key="tagId")


class AdminTaskSchema(TaskSchema):
    user_id = fields.Int(dump_only=True, data_key="userId")
    username = fields.Str(dump_only=True)
    user_email = fields.Email(dump_only=True, data_key="userEmail")


class UpdateTaskSchema(PlainTaskSchema):
    pass
<<<<<<< HEAD


class RoleUpdateSchema(PlainRoleUpdateSchema):
    pass


class PermissionOverrideSchema(PlainPermissionOverrideSchema):
    pass
=======
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
