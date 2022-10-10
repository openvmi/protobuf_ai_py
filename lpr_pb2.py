# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf_ai_py/lpr.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18protobuf_ai_py/lpr.proto\" \n\x0fLprInferRequest\x12\r\n\x05image\x18\x01 \x01(\t\"\x9b\x01\n\x10LprInferResponse\x12(\n\x07results\x18\x01 \x03(\x0b\x32\x17.LprInferResponse.Entry\x1a]\n\x05\x45ntry\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0c\n\x04\x63onf\x18\x03 \x01(\x02\x12\t\n\x01x\x18\x04 \x01(\x02\x12\t\n\x01y\x18\x05 \x01(\x02\x12\t\n\x01w\x18\x06 \x01(\x02\x12\t\n\x01h\x18\x07 \x01(\x02\x32\x45\n\x13LprInferenceService\x12.\n\x05infer\x12\x10.LprInferRequest\x1a\x11.LprInferResponse\"\x00\x42\x0cZ\n./image/pbb\x06proto3')



_LPRINFERREQUEST = DESCRIPTOR.message_types_by_name['LprInferRequest']
_LPRINFERRESPONSE = DESCRIPTOR.message_types_by_name['LprInferResponse']
_LPRINFERRESPONSE_ENTRY = _LPRINFERRESPONSE.nested_types_by_name['Entry']
LprInferRequest = _reflection.GeneratedProtocolMessageType('LprInferRequest', (_message.Message,), {
  'DESCRIPTOR' : _LPRINFERREQUEST,
  '__module__' : 'protobuf_ai_py.lpr_pb2'
  # @@protoc_insertion_point(class_scope:LprInferRequest)
  })
_sym_db.RegisterMessage(LprInferRequest)

LprInferResponse = _reflection.GeneratedProtocolMessageType('LprInferResponse', (_message.Message,), {

  'Entry' : _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), {
    'DESCRIPTOR' : _LPRINFERRESPONSE_ENTRY,
    '__module__' : 'protobuf_ai_py.lpr_pb2'
    # @@protoc_insertion_point(class_scope:LprInferResponse.Entry)
    })
  ,
  'DESCRIPTOR' : _LPRINFERRESPONSE,
  '__module__' : 'protobuf_ai_py.lpr_pb2'
  # @@protoc_insertion_point(class_scope:LprInferResponse)
  })
_sym_db.RegisterMessage(LprInferResponse)
_sym_db.RegisterMessage(LprInferResponse.Entry)

_LPRINFERENCESERVICE = DESCRIPTOR.services_by_name['LprInferenceService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\n./image/pb'
  _LPRINFERREQUEST._serialized_start=28
  _LPRINFERREQUEST._serialized_end=60
  _LPRINFERRESPONSE._serialized_start=63
  _LPRINFERRESPONSE._serialized_end=218
  _LPRINFERRESPONSE_ENTRY._serialized_start=125
  _LPRINFERRESPONSE_ENTRY._serialized_end=218
  _LPRINFERENCESERVICE._serialized_start=220
  _LPRINFERENCESERVICE._serialized_end=289
# @@protoc_insertion_point(module_scope)
