import pandas as pd
from marshmallow import fields, Schema, validate
from marshmallow.validate import OneOf


# input schema validation for json requests
class DataSchema(Schema):
    id = fields.Str(required=True)
    received_at = fields.Str(required=True)
    anonymous_id = fields.Str(required=True)
    context_app_version = fields.Str(required=False)
    context_device_ad_tracking_enabled = fields.Bool(required=False)
    context_device_manufacturer = fields.Str(required=True)
    context_device_model = fields.Str(required=True)
    context_device_type = fields.Str(required=True)
    context_library_name = fields.Str(required=False)
    context_library_version = fields.Str(required=False)
    context_locale = fields.Str(required=True)
    context_network_wifi = fields.Bool(required=True)
    context_os_name = fields.Str(required=True)
    context_timezone = fields.Str(required=False)
    event = fields.Str(required=True)
    event_text = fields.Str(required=True)
    original_timestamp = fields.Str(required=True)
    sent_at = fields.Str(required=True)
    timestamp = fields.Str(required=True)
    user_id = fields.Str(required=False)
    context_network_carrier = fields.Str(required=True)
    context_device_token = fields.Str(required=False, allow_none=True)
    context_traits_taxfix_language = fields.Str(required=True)
