# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\"1\n\x0b\x41uthRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"!\n\x0eSignupResponse\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"F\n\rLoginResponse\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\x12\x15\n\rrefresh_token\x18\x03 \x01(\t\"\x1e\n\rVerifyRequest\x12\r\n\x05token\x18\x01 \x01(\t\"A\n\x0eVerifyResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\r\n\x05valid\x18\x02 \x01(\x08\x12\x0f\n\x07user_id\x18\x03 \x01(\t\"%\n\x0cRefreshToken\x12\x15\n\rrefresh_token\x18\x01 \x01(\t\" \n\rLogoutRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"0\n\x0eLogoutResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\r\n\x05valid\x18\x02 \x01(\x08\x32\xe6\x01\n\x14\x41uthenticationServer\x12\'\n\x06Signup\x12\x0c.AuthRequest\x1a\x0f.SignupResponse\x12%\n\x05Login\x12\x0c.AuthRequest\x1a\x0e.LoginResponse\x12)\n\x06Verify\x12\x0e.VerifyRequest\x1a\x0f.VerifyResponse\x12(\n\x07Refresh\x12\x0e.VerifyRequest\x1a\r.RefreshToken\x12)\n\x06Logout\x12\x0e.LogoutRequest\x1a\x0f.LogoutResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_AUTHREQUEST']._serialized_start=17
  _globals['_AUTHREQUEST']._serialized_end=66
  _globals['_SIGNUPRESPONSE']._serialized_start=68
  _globals['_SIGNUPRESPONSE']._serialized_end=101
  _globals['_LOGINRESPONSE']._serialized_start=103
  _globals['_LOGINRESPONSE']._serialized_end=173
  _globals['_VERIFYREQUEST']._serialized_start=175
  _globals['_VERIFYREQUEST']._serialized_end=205
  _globals['_VERIFYRESPONSE']._serialized_start=207
  _globals['_VERIFYRESPONSE']._serialized_end=272
  _globals['_REFRESHTOKEN']._serialized_start=274
  _globals['_REFRESHTOKEN']._serialized_end=311
  _globals['_LOGOUTREQUEST']._serialized_start=313
  _globals['_LOGOUTREQUEST']._serialized_end=345
  _globals['_LOGOUTRESPONSE']._serialized_start=347
  _globals['_LOGOUTRESPONSE']._serialized_end=395
  _globals['_AUTHENTICATIONSERVER']._serialized_start=398
  _globals['_AUTHENTICATIONSERVER']._serialized_end=628
# @@protoc_insertion_point(module_scope)
