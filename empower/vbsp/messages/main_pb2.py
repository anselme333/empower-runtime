# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: main.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import empower.vbsp.messages.hello_pb2 as hello__pb2
import empower.vbsp.messages.statistics_pb2 as statistics__pb2
import empower.vbsp.messages.configs_pb2 as configs__pb2
import empower.vbsp.messages.commands_pb2 as commands__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='main.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\nmain.proto\x1a\x0bhello.proto\x1a\x10statistics.proto\x1a\rconfigs.proto\x1a\x0e\x63ommands.proto\"?\n\x06header\x12\x0c\n\x04vers\x18\x01 \x02(\r\x12\x0c\n\x04\x62_id\x18\x02 \x02(\r\x12\x0b\n\x03seq\x18\x03 \x02(\r\x12\x0c\n\x04t_id\x18\x04 \x02(\r\"\xef\x01\n\x0csingle_event\x12\x18\n\x06mHello\x18\x01 \x01(\x0b\x32\x06.helloH\x00\x12\x1a\n\x07mUEs_id\x18\x02 \x01(\x0b\x32\x07.ues_idH\x00\x12.\n\x11mUE_rrc_meas_conf\x18\x03 \x01(\x0b\x32\x11.ue_rrc_meas_confH\x00\x12\"\n\x0bmCell_stats\x18\x04 \x01(\x0b\x32\x0b.cell_statsH\x00\x12*\n\nmCtrl_cmds\x18\x05 \x01(\x0b\x32\x14.controller_commandsH\x00\x12\x1f\n\tenb_cells\x18\x06 \x01(\x0b\x32\n.eNB_cellsH\x00\x42\x08\n\x06\x65vents\"\xbb\x01\n\x0eschedule_event\x12\x10\n\x08interval\x18\x01 \x01(\r\x12\x1d\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32\r.event_action\x12\x1a\n\x07mUEs_id\x18\x03 \x01(\x0b\x32\x07.ues_idH\x00\x12.\n\x11mUE_rrc_meas_conf\x18\x04 \x01(\x0b\x32\x11.ue_rrc_meas_confH\x00\x12\"\n\x0bmCell_stats\x18\x05 \x01(\x0b\x32\x0b.cell_statsH\x00\x42\x08\n\x06\x65vents\"\xe2\x01\n\rtrigger_event\x12\x1d\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\r.event_action\x12\x18\n\x06mHello\x18\x02 \x01(\x0b\x32\x06.helloH\x00\x12\x1a\n\x07mUEs_id\x18\x03 \x01(\x0b\x32\x07.ues_idH\x00\x12\x1e\n\tmRRC_meas\x18\x04 \x01(\x0b\x32\t.rrc_measH\x00\x12.\n\x11mUE_rrc_meas_conf\x18\x05 \x01(\x0b\x32\x11.ue_rrc_meas_confH\x00\x12\"\n\x0bmCell_stats\x18\x06 \x01(\x0b\x32\x0b.cell_statsH\x00\x42\x08\n\x06\x65vents\"\x8d\x01\n\temage_msg\x12\x15\n\x04head\x18\x01 \x02(\x0b\x32\x07.header\x12\x1b\n\x02se\x18\x02 \x01(\x0b\x32\r.single_eventH\x00\x12\x1f\n\x04sche\x18\x03 \x01(\x0b\x32\x0f.schedule_eventH\x00\x12\x1c\n\x02te\x18\x04 \x01(\x0b\x32\x0e.trigger_eventH\x00\x42\r\n\x0b\x65vent_types*&\n\x0c\x65vent_action\x12\n\n\x06\x45\x41_ADD\x10\x00\x12\n\n\x06\x45\x41_DEL\x10\x01')
  ,
  dependencies=[hello__pb2.DESCRIPTOR,statistics__pb2.DESCRIPTOR,configs__pb2.DESCRIPTOR,commands__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_EVENT_ACTION = _descriptor.EnumDescriptor(
  name='event_action',
  full_name='event_action',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EA_ADD', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EA_DEL', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=946,
  serialized_end=984,
)
_sym_db.RegisterEnumDescriptor(_EVENT_ACTION)

event_action = enum_type_wrapper.EnumTypeWrapper(_EVENT_ACTION)
EA_ADD = 0
EA_DEL = 1



_HEADER = _descriptor.Descriptor(
  name='header',
  full_name='header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vers', full_name='header.vers', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='b_id', full_name='header.b_id', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seq', full_name='header.seq', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='t_id', full_name='header.t_id', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=139,
)


_SINGLE_EVENT = _descriptor.Descriptor(
  name='single_event',
  full_name='single_event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mHello', full_name='single_event.mHello', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mUEs_id', full_name='single_event.mUEs_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mUE_rrc_meas_conf', full_name='single_event.mUE_rrc_meas_conf', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mCell_stats', full_name='single_event.mCell_stats', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mCtrl_cmds', full_name='single_event.mCtrl_cmds', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enb_cells', full_name='single_event.enb_cells', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='events', full_name='single_event.events',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=142,
  serialized_end=381,
)


_SCHEDULE_EVENT = _descriptor.Descriptor(
  name='schedule_event',
  full_name='schedule_event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='interval', full_name='schedule_event.interval', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='schedule_event.action', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mUEs_id', full_name='schedule_event.mUEs_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mUE_rrc_meas_conf', full_name='schedule_event.mUE_rrc_meas_conf', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mCell_stats', full_name='schedule_event.mCell_stats', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='events', full_name='schedule_event.events',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=384,
  serialized_end=571,
)


_TRIGGER_EVENT = _descriptor.Descriptor(
  name='trigger_event',
  full_name='trigger_event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='trigger_event.action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mHello', full_name='trigger_event.mHello', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mUEs_id', full_name='trigger_event.mUEs_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mRRC_meas', full_name='trigger_event.mRRC_meas', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mUE_rrc_meas_conf', full_name='trigger_event.mUE_rrc_meas_conf', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mCell_stats', full_name='trigger_event.mCell_stats', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='events', full_name='trigger_event.events',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=574,
  serialized_end=800,
)


_EMAGE_MSG = _descriptor.Descriptor(
  name='emage_msg',
  full_name='emage_msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='head', full_name='emage_msg.head', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='se', full_name='emage_msg.se', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sche', full_name='emage_msg.sche', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='te', full_name='emage_msg.te', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='event_types', full_name='emage_msg.event_types',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=803,
  serialized_end=944,
)

_SINGLE_EVENT.fields_by_name['mHello'].message_type = hello__pb2._HELLO
_SINGLE_EVENT.fields_by_name['mUEs_id'].message_type = configs__pb2._UES_ID
_SINGLE_EVENT.fields_by_name['mUE_rrc_meas_conf'].message_type = configs__pb2._UE_RRC_MEAS_CONF
_SINGLE_EVENT.fields_by_name['mCell_stats'].message_type = statistics__pb2._CELL_STATS
_SINGLE_EVENT.fields_by_name['mCtrl_cmds'].message_type = commands__pb2._CONTROLLER_COMMANDS
_SINGLE_EVENT.fields_by_name['enb_cells'].message_type = configs__pb2._ENB_CELLS
_SINGLE_EVENT.oneofs_by_name['events'].fields.append(
  _SINGLE_EVENT.fields_by_name['mHello'])
_SINGLE_EVENT.fields_by_name['mHello'].containing_oneof = _SINGLE_EVENT.oneofs_by_name['events']
_SINGLE_EVENT.oneofs_by_name['events'].fields.append(
  _SINGLE_EVENT.fields_by_name['mUEs_id'])
_SINGLE_EVENT.fields_by_name['mUEs_id'].containing_oneof = _SINGLE_EVENT.oneofs_by_name['events']
_SINGLE_EVENT.oneofs_by_name['events'].fields.append(
  _SINGLE_EVENT.fields_by_name['mUE_rrc_meas_conf'])
_SINGLE_EVENT.fields_by_name['mUE_rrc_meas_conf'].containing_oneof = _SINGLE_EVENT.oneofs_by_name['events']
_SINGLE_EVENT.oneofs_by_name['events'].fields.append(
  _SINGLE_EVENT.fields_by_name['mCell_stats'])
_SINGLE_EVENT.fields_by_name['mCell_stats'].containing_oneof = _SINGLE_EVENT.oneofs_by_name['events']
_SINGLE_EVENT.oneofs_by_name['events'].fields.append(
  _SINGLE_EVENT.fields_by_name['mCtrl_cmds'])
_SINGLE_EVENT.fields_by_name['mCtrl_cmds'].containing_oneof = _SINGLE_EVENT.oneofs_by_name['events']
_SINGLE_EVENT.oneofs_by_name['events'].fields.append(
  _SINGLE_EVENT.fields_by_name['enb_cells'])
_SINGLE_EVENT.fields_by_name['enb_cells'].containing_oneof = _SINGLE_EVENT.oneofs_by_name['events']
_SCHEDULE_EVENT.fields_by_name['action'].enum_type = _EVENT_ACTION
_SCHEDULE_EVENT.fields_by_name['mUEs_id'].message_type = configs__pb2._UES_ID
_SCHEDULE_EVENT.fields_by_name['mUE_rrc_meas_conf'].message_type = configs__pb2._UE_RRC_MEAS_CONF
_SCHEDULE_EVENT.fields_by_name['mCell_stats'].message_type = statistics__pb2._CELL_STATS
_SCHEDULE_EVENT.oneofs_by_name['events'].fields.append(
  _SCHEDULE_EVENT.fields_by_name['mUEs_id'])
_SCHEDULE_EVENT.fields_by_name['mUEs_id'].containing_oneof = _SCHEDULE_EVENT.oneofs_by_name['events']
_SCHEDULE_EVENT.oneofs_by_name['events'].fields.append(
  _SCHEDULE_EVENT.fields_by_name['mUE_rrc_meas_conf'])
_SCHEDULE_EVENT.fields_by_name['mUE_rrc_meas_conf'].containing_oneof = _SCHEDULE_EVENT.oneofs_by_name['events']
_SCHEDULE_EVENT.oneofs_by_name['events'].fields.append(
  _SCHEDULE_EVENT.fields_by_name['mCell_stats'])
_SCHEDULE_EVENT.fields_by_name['mCell_stats'].containing_oneof = _SCHEDULE_EVENT.oneofs_by_name['events']
_TRIGGER_EVENT.fields_by_name['action'].enum_type = _EVENT_ACTION
_TRIGGER_EVENT.fields_by_name['mHello'].message_type = hello__pb2._HELLO
_TRIGGER_EVENT.fields_by_name['mUEs_id'].message_type = configs__pb2._UES_ID
_TRIGGER_EVENT.fields_by_name['mRRC_meas'].message_type = statistics__pb2._RRC_MEAS
_TRIGGER_EVENT.fields_by_name['mUE_rrc_meas_conf'].message_type = configs__pb2._UE_RRC_MEAS_CONF
_TRIGGER_EVENT.fields_by_name['mCell_stats'].message_type = statistics__pb2._CELL_STATS
_TRIGGER_EVENT.oneofs_by_name['events'].fields.append(
  _TRIGGER_EVENT.fields_by_name['mHello'])
_TRIGGER_EVENT.fields_by_name['mHello'].containing_oneof = _TRIGGER_EVENT.oneofs_by_name['events']
_TRIGGER_EVENT.oneofs_by_name['events'].fields.append(
  _TRIGGER_EVENT.fields_by_name['mUEs_id'])
_TRIGGER_EVENT.fields_by_name['mUEs_id'].containing_oneof = _TRIGGER_EVENT.oneofs_by_name['events']
_TRIGGER_EVENT.oneofs_by_name['events'].fields.append(
  _TRIGGER_EVENT.fields_by_name['mRRC_meas'])
_TRIGGER_EVENT.fields_by_name['mRRC_meas'].containing_oneof = _TRIGGER_EVENT.oneofs_by_name['events']
_TRIGGER_EVENT.oneofs_by_name['events'].fields.append(
  _TRIGGER_EVENT.fields_by_name['mUE_rrc_meas_conf'])
_TRIGGER_EVENT.fields_by_name['mUE_rrc_meas_conf'].containing_oneof = _TRIGGER_EVENT.oneofs_by_name['events']
_TRIGGER_EVENT.oneofs_by_name['events'].fields.append(
  _TRIGGER_EVENT.fields_by_name['mCell_stats'])
_TRIGGER_EVENT.fields_by_name['mCell_stats'].containing_oneof = _TRIGGER_EVENT.oneofs_by_name['events']
_EMAGE_MSG.fields_by_name['head'].message_type = _HEADER
_EMAGE_MSG.fields_by_name['se'].message_type = _SINGLE_EVENT
_EMAGE_MSG.fields_by_name['sche'].message_type = _SCHEDULE_EVENT
_EMAGE_MSG.fields_by_name['te'].message_type = _TRIGGER_EVENT
_EMAGE_MSG.oneofs_by_name['event_types'].fields.append(
  _EMAGE_MSG.fields_by_name['se'])
_EMAGE_MSG.fields_by_name['se'].containing_oneof = _EMAGE_MSG.oneofs_by_name['event_types']
_EMAGE_MSG.oneofs_by_name['event_types'].fields.append(
  _EMAGE_MSG.fields_by_name['sche'])
_EMAGE_MSG.fields_by_name['sche'].containing_oneof = _EMAGE_MSG.oneofs_by_name['event_types']
_EMAGE_MSG.oneofs_by_name['event_types'].fields.append(
  _EMAGE_MSG.fields_by_name['te'])
_EMAGE_MSG.fields_by_name['te'].containing_oneof = _EMAGE_MSG.oneofs_by_name['event_types']
DESCRIPTOR.message_types_by_name['header'] = _HEADER
DESCRIPTOR.message_types_by_name['single_event'] = _SINGLE_EVENT
DESCRIPTOR.message_types_by_name['schedule_event'] = _SCHEDULE_EVENT
DESCRIPTOR.message_types_by_name['trigger_event'] = _TRIGGER_EVENT
DESCRIPTOR.message_types_by_name['emage_msg'] = _EMAGE_MSG
DESCRIPTOR.enum_types_by_name['event_action'] = _EVENT_ACTION

header = _reflection.GeneratedProtocolMessageType('header', (_message.Message,), dict(
  DESCRIPTOR = _HEADER,
  __module__ = 'main_pb2'
  # @@protoc_insertion_point(class_scope:header)
  ))
_sym_db.RegisterMessage(header)

single_event = _reflection.GeneratedProtocolMessageType('single_event', (_message.Message,), dict(
  DESCRIPTOR = _SINGLE_EVENT,
  __module__ = 'main_pb2'
  # @@protoc_insertion_point(class_scope:single_event)
  ))
_sym_db.RegisterMessage(single_event)

schedule_event = _reflection.GeneratedProtocolMessageType('schedule_event', (_message.Message,), dict(
  DESCRIPTOR = _SCHEDULE_EVENT,
  __module__ = 'main_pb2'
  # @@protoc_insertion_point(class_scope:schedule_event)
  ))
_sym_db.RegisterMessage(schedule_event)

trigger_event = _reflection.GeneratedProtocolMessageType('trigger_event', (_message.Message,), dict(
  DESCRIPTOR = _TRIGGER_EVENT,
  __module__ = 'main_pb2'
  # @@protoc_insertion_point(class_scope:trigger_event)
  ))
_sym_db.RegisterMessage(trigger_event)

emage_msg = _reflection.GeneratedProtocolMessageType('emage_msg', (_message.Message,), dict(
  DESCRIPTOR = _EMAGE_MSG,
  __module__ = 'main_pb2'
  # @@protoc_insertion_point(class_scope:emage_msg)
  ))
_sym_db.RegisterMessage(emage_msg)


# @@protoc_insertion_point(module_scope)
