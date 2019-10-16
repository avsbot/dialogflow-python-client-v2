# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dialogflow_v2/proto/context.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/dialogflow_v2/proto/context.proto",
    package="google.cloud.dialogflow.v2",
    syntax="proto3",
    serialized_options=_b(
        "\n\036com.google.cloud.dialogflow.v2B\014ContextProtoP\001ZDgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2;dialogflow\370\001\001\242\002\002DF\252\002\032Google.Cloud.Dialogflow.V2"
    ),
    serialized_pb=_b(
        '\n.google/cloud/dialogflow_v2/proto/context.proto\x12\x1agoogle.cloud.dialogflow.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto"\xd3\x01\n\x07\x43ontext\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x1b\n\x0elifespan_count\x18\x02 \x01(\x05\x42\x03\xe0\x41\x01\x12\x30\n\nparameters\x18\x03 \x01(\x0b\x32\x17.google.protobuf.StructB\x03\xe0\x41\x01:f\xea\x41\x63\n!dialogflow.googleapis.com/Context\x12>projects/{project}/agent/sessions/{session}/contexts/{context}"[\n\x13ListContextsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x16\n\tpage_size\x18\x02 \x01(\x05\x42\x03\xe0\x41\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0\x41\x01"f\n\x14ListContextsResponse\x12\x35\n\x08\x63ontexts\x18\x01 \x03(\x0b\x32#.google.cloud.dialogflow.v2.Context\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"L\n\x11GetContextRequest\x12\x37\n\x04name\x18\x01 \x01(\tB)\xe0\x41\x02\xfa\x41#\n!dialogflow.googleapis.com/Context"f\n\x14\x43reateContextRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x39\n\x07\x63ontext\x18\x02 \x01(\x0b\x32#.google.cloud.dialogflow.v2.ContextB\x03\xe0\x41\x02"\x87\x01\n\x14UpdateContextRequest\x12\x39\n\x07\x63ontext\x18\x01 \x01(\x0b\x32#.google.cloud.dialogflow.v2.ContextB\x03\xe0\x41\x02\x12\x34\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x03\xe0\x41\x01"O\n\x14\x44\x65leteContextRequest\x12\x37\n\x04name\x18\x01 \x01(\tB)\xe0\x41\x02\xfa\x41#\n!dialogflow.googleapis.com/Context"/\n\x18\x44\x65leteAllContextsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0\x41\x02\x32\xf2\x08\n\x08\x43ontexts\x12\xb5\x01\n\x0cListContexts\x12/.google.cloud.dialogflow.v2.ListContextsRequest\x1a\x30.google.cloud.dialogflow.v2.ListContextsResponse"B\x82\xd3\xe4\x93\x02\x33\x12\x31/v2/{parent=projects/*/agent/sessions/*}/contexts\xda\x41\x06parent\x12\x9b\x01\n\nGetContext\x12-.google.cloud.dialogflow.v2.GetContextRequest\x1a#.google.cloud.dialogflow.v2.Context"9\x82\xd3\xe4\x93\x02\x33\x12\x31/v2/{name=projects/*/agent/sessions/*/contexts/*}\x12\xaa\x01\n\rCreateContext\x12\x30.google.cloud.dialogflow.v2.CreateContextRequest\x1a#.google.cloud.dialogflow.v2.Context"B\x82\xd3\xe4\x93\x02<"1/v2/{parent=projects/*/agent/sessions/*}/contexts:\x07\x63ontext\x12\xb2\x01\n\rUpdateContext\x12\x30.google.cloud.dialogflow.v2.UpdateContextRequest\x1a#.google.cloud.dialogflow.v2.Context"J\x82\xd3\xe4\x93\x02\x44\x32\x39/v2/{context.name=projects/*/agent/sessions/*/contexts/*}:\x07\x63ontext\x12\x94\x01\n\rDeleteContext\x12\x30.google.cloud.dialogflow.v2.DeleteContextRequest\x1a\x16.google.protobuf.Empty"9\x82\xd3\xe4\x93\x02\x33*1/v2/{name=projects/*/agent/sessions/*/contexts/*}\x12\x9c\x01\n\x11\x44\x65leteAllContexts\x12\x34.google.cloud.dialogflow.v2.DeleteAllContextsRequest\x1a\x16.google.protobuf.Empty"9\x82\xd3\xe4\x93\x02\x33*1/v2/{parent=projects/*/agent/sessions/*}/contexts\x1ax\xca\x41\x19\x64ialogflow.googleapis.com\xd2\x41Yhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\x9b\x01\n\x1e\x63om.google.cloud.dialogflow.v2B\x0c\x43ontextProtoP\x01ZDgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2;dialogflow\xf8\x01\x01\xa2\x02\x02\x44\x46\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_api_dot_client__pb2.DESCRIPTOR,
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,
    ],
)


_CONTEXT = _descriptor.Descriptor(
    name="Context",
    full_name="google.cloud.dialogflow.v2.Context",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.dialogflow.v2.Context.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\002"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="lifespan_count",
            full_name="google.cloud.dialogflow.v2.Context.lifespan_count",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\001"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="parameters",
            full_name="google.cloud.dialogflow.v2.Context.parameters",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\001"),
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=_b(
        "\352Ac\n!dialogflow.googleapis.com/Context\022>projects/{project}/agent/sessions/{session}/contexts/{context}"
    ),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=287,
    serialized_end=498,
)


_LISTCONTEXTSREQUEST = _descriptor.Descriptor(
    name="ListContextsRequest",
    full_name="google.cloud.dialogflow.v2.ListContextsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.cloud.dialogflow.v2.ListContextsRequest.parent",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\002"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="page_size",
            full_name="google.cloud.dialogflow.v2.ListContextsRequest.page_size",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\001"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="page_token",
            full_name="google.cloud.dialogflow.v2.ListContextsRequest.page_token",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\001"),
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=500,
    serialized_end=591,
)


_LISTCONTEXTSRESPONSE = _descriptor.Descriptor(
    name="ListContextsResponse",
    full_name="google.cloud.dialogflow.v2.ListContextsResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="contexts",
            full_name="google.cloud.dialogflow.v2.ListContextsResponse.contexts",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="next_page_token",
            full_name="google.cloud.dialogflow.v2.ListContextsResponse.next_page_token",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=593,
    serialized_end=695,
)


_GETCONTEXTREQUEST = _descriptor.Descriptor(
    name="GetContextRequest",
    full_name="google.cloud.dialogflow.v2.GetContextRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.dialogflow.v2.GetContextRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b(
                "\340A\002\372A#\n!dialogflow.googleapis.com/Context"
            ),
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=697,
    serialized_end=773,
)


_CREATECONTEXTREQUEST = _descriptor.Descriptor(
    name="CreateContextRequest",
    full_name="google.cloud.dialogflow.v2.CreateContextRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.cloud.dialogflow.v2.CreateContextRequest.parent",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\002"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="context",
            full_name="google.cloud.dialogflow.v2.CreateContextRequest.context",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\002"),
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=775,
    serialized_end=877,
)


_UPDATECONTEXTREQUEST = _descriptor.Descriptor(
    name="UpdateContextRequest",
    full_name="google.cloud.dialogflow.v2.UpdateContextRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="context",
            full_name="google.cloud.dialogflow.v2.UpdateContextRequest.context",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\002"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="update_mask",
            full_name="google.cloud.dialogflow.v2.UpdateContextRequest.update_mask",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\001"),
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=880,
    serialized_end=1015,
)


_DELETECONTEXTREQUEST = _descriptor.Descriptor(
    name="DeleteContextRequest",
    full_name="google.cloud.dialogflow.v2.DeleteContextRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.dialogflow.v2.DeleteContextRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b(
                "\340A\002\372A#\n!dialogflow.googleapis.com/Context"
            ),
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1017,
    serialized_end=1096,
)


_DELETEALLCONTEXTSREQUEST = _descriptor.Descriptor(
    name="DeleteAllContextsRequest",
    full_name="google.cloud.dialogflow.v2.DeleteAllContextsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.cloud.dialogflow.v2.DeleteAllContextsRequest.parent",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\002"),
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1098,
    serialized_end=1145,
)

_CONTEXT.fields_by_name[
    "parameters"
].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_LISTCONTEXTSRESPONSE.fields_by_name["contexts"].message_type = _CONTEXT
_CREATECONTEXTREQUEST.fields_by_name["context"].message_type = _CONTEXT
_UPDATECONTEXTREQUEST.fields_by_name["context"].message_type = _CONTEXT
_UPDATECONTEXTREQUEST.fields_by_name[
    "update_mask"
].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
DESCRIPTOR.message_types_by_name["Context"] = _CONTEXT
DESCRIPTOR.message_types_by_name["ListContextsRequest"] = _LISTCONTEXTSREQUEST
DESCRIPTOR.message_types_by_name["ListContextsResponse"] = _LISTCONTEXTSRESPONSE
DESCRIPTOR.message_types_by_name["GetContextRequest"] = _GETCONTEXTREQUEST
DESCRIPTOR.message_types_by_name["CreateContextRequest"] = _CREATECONTEXTREQUEST
DESCRIPTOR.message_types_by_name["UpdateContextRequest"] = _UPDATECONTEXTREQUEST
DESCRIPTOR.message_types_by_name["DeleteContextRequest"] = _DELETECONTEXTREQUEST
DESCRIPTOR.message_types_by_name["DeleteAllContextsRequest"] = _DELETEALLCONTEXTSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Context = _reflection.GeneratedProtocolMessageType(
    "Context",
    (_message.Message,),
    dict(
        DESCRIPTOR=_CONTEXT,
        __module__="google.cloud.dialogflow_v2.proto.context_pb2",
        __doc__="""Represents a context.
  
  
  Attributes:
      name:
          Required. The unique identifier of the context. Format:
          ``projects/<Project ID>/agent/sessions/<Session
          ID>/contexts/<Context ID>``.  The ``Context ID`` is always
          converted to lowercase, may only contain characters in
          [a-zA-Z0-9\_-%] and may be at most 250 bytes long.
      lifespan_count:
          Optional. The number of conversational query requests after
          which the context expires. If set to ``0`` (the default) the
          context expires immediately. Contexts expire automatically
          after 20 minutes if there are no matching queries.
      parameters:
          Optional. The collection of parameters associated with this
          context. Refer to `this doc
          <https://cloud.google.com/dialogflow/docs/intents-actions-
          parameters>`__ for syntax.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.Context)
    ),
)
_sym_db.RegisterMessage(Context)

ListContextsRequest = _reflection.GeneratedProtocolMessageType(
    "ListContextsRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_LISTCONTEXTSREQUEST,
        __module__="google.cloud.dialogflow_v2.proto.context_pb2",
        __doc__="""The request message for
  [Contexts.ListContexts][google.cloud.dialogflow.v2.Contexts.ListContexts].
  
  
  Attributes:
      parent:
          Required. The session to list all contexts from. Format:
          ``projects/<Project ID>/agent/sessions/<Session ID>``.
      page_size:
          Optional. The maximum number of items to return in a single
          page. By default 100 and at most 1000.
      page_token:
          Optional. The next\_page\_token value returned from a previous
          list request.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.ListContextsRequest)
    ),
)
_sym_db.RegisterMessage(ListContextsRequest)

ListContextsResponse = _reflection.GeneratedProtocolMessageType(
    "ListContextsResponse",
    (_message.Message,),
    dict(
        DESCRIPTOR=_LISTCONTEXTSRESPONSE,
        __module__="google.cloud.dialogflow_v2.proto.context_pb2",
        __doc__="""The response message for
  [Contexts.ListContexts][google.cloud.dialogflow.v2.Contexts.ListContexts].
  
  
  Attributes:
      contexts:
          The list of contexts. There will be a maximum number of items
          returned based on the page\_size field in the request.
      next_page_token:
          Token to retrieve the next page of results, or empty if there
          are no more results in the list.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.ListContextsResponse)
    ),
)
_sym_db.RegisterMessage(ListContextsResponse)

GetContextRequest = _reflection.GeneratedProtocolMessageType(
    "GetContextRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_GETCONTEXTREQUEST,
        __module__="google.cloud.dialogflow_v2.proto.context_pb2",
        __doc__="""The request message for
  [Contexts.GetContext][google.cloud.dialogflow.v2.Contexts.GetContext].
  
  
  Attributes:
      name:
          Required. The name of the context. Format: ``projects/<Project
          ID>/agent/sessions/<Session ID>/contexts/<Context ID>``.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.GetContextRequest)
    ),
)
_sym_db.RegisterMessage(GetContextRequest)

CreateContextRequest = _reflection.GeneratedProtocolMessageType(
    "CreateContextRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_CREATECONTEXTREQUEST,
        __module__="google.cloud.dialogflow_v2.proto.context_pb2",
        __doc__="""The request message for
  [Contexts.CreateContext][google.cloud.dialogflow.v2.Contexts.CreateContext].
  
  
  Attributes:
      parent:
          Required. The session to create a context for. Format:
          ``projects/<Project ID>/agent/sessions/<Session ID>``.
      context:
          Required. The context to create.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.CreateContextRequest)
    ),
)
_sym_db.RegisterMessage(CreateContextRequest)

UpdateContextRequest = _reflection.GeneratedProtocolMessageType(
    "UpdateContextRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_UPDATECONTEXTREQUEST,
        __module__="google.cloud.dialogflow_v2.proto.context_pb2",
        __doc__="""The request message for
  [Contexts.UpdateContext][google.cloud.dialogflow.v2.Contexts.UpdateContext].
  
  
  Attributes:
      context:
          Required. The context to update.
      update_mask:
          Optional. The mask to control which fields get updated.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.UpdateContextRequest)
    ),
)
_sym_db.RegisterMessage(UpdateContextRequest)

DeleteContextRequest = _reflection.GeneratedProtocolMessageType(
    "DeleteContextRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_DELETECONTEXTREQUEST,
        __module__="google.cloud.dialogflow_v2.proto.context_pb2",
        __doc__="""The request message for
  [Contexts.DeleteContext][google.cloud.dialogflow.v2.Contexts.DeleteContext].
  
  
  Attributes:
      name:
          Required. The name of the context to delete. Format:
          ``projects/<Project ID>/agent/sessions/<Session
          ID>/contexts/<Context ID>``.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.DeleteContextRequest)
    ),
)
_sym_db.RegisterMessage(DeleteContextRequest)

DeleteAllContextsRequest = _reflection.GeneratedProtocolMessageType(
    "DeleteAllContextsRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_DELETEALLCONTEXTSREQUEST,
        __module__="google.cloud.dialogflow_v2.proto.context_pb2",
        __doc__="""The request message for
  [Contexts.DeleteAllContexts][google.cloud.dialogflow.v2.Contexts.DeleteAllContexts].
  
  
  Attributes:
      parent:
          Required. The name of the session to delete all contexts from.
          Format: ``projects/<Project ID>/agent/sessions/<Session ID>``.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.DeleteAllContextsRequest)
    ),
)
_sym_db.RegisterMessage(DeleteAllContextsRequest)


DESCRIPTOR._options = None
_CONTEXT.fields_by_name["name"]._options = None
_CONTEXT.fields_by_name["lifespan_count"]._options = None
_CONTEXT.fields_by_name["parameters"]._options = None
_CONTEXT._options = None
_LISTCONTEXTSREQUEST.fields_by_name["parent"]._options = None
_LISTCONTEXTSREQUEST.fields_by_name["page_size"]._options = None
_LISTCONTEXTSREQUEST.fields_by_name["page_token"]._options = None
_GETCONTEXTREQUEST.fields_by_name["name"]._options = None
_CREATECONTEXTREQUEST.fields_by_name["parent"]._options = None
_CREATECONTEXTREQUEST.fields_by_name["context"]._options = None
_UPDATECONTEXTREQUEST.fields_by_name["context"]._options = None
_UPDATECONTEXTREQUEST.fields_by_name["update_mask"]._options = None
_DELETECONTEXTREQUEST.fields_by_name["name"]._options = None
_DELETEALLCONTEXTSREQUEST.fields_by_name["parent"]._options = None

_CONTEXTS = _descriptor.ServiceDescriptor(
    name="Contexts",
    full_name="google.cloud.dialogflow.v2.Contexts",
    file=DESCRIPTOR,
    index=0,
    serialized_options=_b(
        "\312A\031dialogflow.googleapis.com\322AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow"
    ),
    serialized_start=1148,
    serialized_end=2286,
    methods=[
        _descriptor.MethodDescriptor(
            name="ListContexts",
            full_name="google.cloud.dialogflow.v2.Contexts.ListContexts",
            index=0,
            containing_service=None,
            input_type=_LISTCONTEXTSREQUEST,
            output_type=_LISTCONTEXTSRESPONSE,
            serialized_options=_b(
                "\202\323\344\223\0023\0221/v2/{parent=projects/*/agent/sessions/*}/contexts\332A\006parent"
            ),
        ),
        _descriptor.MethodDescriptor(
            name="GetContext",
            full_name="google.cloud.dialogflow.v2.Contexts.GetContext",
            index=1,
            containing_service=None,
            input_type=_GETCONTEXTREQUEST,
            output_type=_CONTEXT,
            serialized_options=_b(
                "\202\323\344\223\0023\0221/v2/{name=projects/*/agent/sessions/*/contexts/*}"
            ),
        ),
        _descriptor.MethodDescriptor(
            name="CreateContext",
            full_name="google.cloud.dialogflow.v2.Contexts.CreateContext",
            index=2,
            containing_service=None,
            input_type=_CREATECONTEXTREQUEST,
            output_type=_CONTEXT,
            serialized_options=_b(
                '\202\323\344\223\002<"1/v2/{parent=projects/*/agent/sessions/*}/contexts:\007context'
            ),
        ),
        _descriptor.MethodDescriptor(
            name="UpdateContext",
            full_name="google.cloud.dialogflow.v2.Contexts.UpdateContext",
            index=3,
            containing_service=None,
            input_type=_UPDATECONTEXTREQUEST,
            output_type=_CONTEXT,
            serialized_options=_b(
                "\202\323\344\223\002D29/v2/{context.name=projects/*/agent/sessions/*/contexts/*}:\007context"
            ),
        ),
        _descriptor.MethodDescriptor(
            name="DeleteContext",
            full_name="google.cloud.dialogflow.v2.Contexts.DeleteContext",
            index=4,
            containing_service=None,
            input_type=_DELETECONTEXTREQUEST,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=_b(
                "\202\323\344\223\0023*1/v2/{name=projects/*/agent/sessions/*/contexts/*}"
            ),
        ),
        _descriptor.MethodDescriptor(
            name="DeleteAllContexts",
            full_name="google.cloud.dialogflow.v2.Contexts.DeleteAllContexts",
            index=5,
            containing_service=None,
            input_type=_DELETEALLCONTEXTSREQUEST,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=_b(
                "\202\323\344\223\0023*1/v2/{parent=projects/*/agent/sessions/*}/contexts"
            ),
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_CONTEXTS)

DESCRIPTOR.services_by_name["Contexts"] = _CONTEXTS

# @@protoc_insertion_point(module_scope)
