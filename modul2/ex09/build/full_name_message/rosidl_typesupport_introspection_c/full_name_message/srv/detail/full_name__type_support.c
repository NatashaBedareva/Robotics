// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from full_name_message:srv/FullName.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "full_name_message/srv/detail/full_name__rosidl_typesupport_introspection_c.h"
#include "full_name_message/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "full_name_message/srv/detail/full_name__functions.h"
#include "full_name_message/srv/detail/full_name__struct.h"


// Include directives for member types
// Member `last_name`
// Member `name`
// Member `first_name`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void full_name_message__srv__FullName_Request__rosidl_typesupport_introspection_c__FullName_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  full_name_message__srv__FullName_Request__init(message_memory);
}

void full_name_message__srv__FullName_Request__rosidl_typesupport_introspection_c__FullName_Request_fini_function(void * message_memory)
{
  full_name_message__srv__FullName_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember full_name_message__srv__FullName_Request__rosidl_typesupport_introspection_c__FullName_Request_message_member_array[3] = {
  {
    "last_name",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(full_name_message__srv__FullName_Request, last_name),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "name",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(full_name_message__srv__FullName_Request, name),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "first_name",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(full_name_message__srv__FullName_Request, first_name),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers full_name_message__srv__FullName_Request__rosidl_typesupport_introspection_c__FullName_Request_message_members = {
  "full_name_message__srv",  // message namespace
  "FullName_Request",  // message name
  3,  // number of fields
  sizeof(full_name_message__srv__FullName_Request),
  false,  // has_any_key_member_
  full_name_message__srv__FullName_Request__rosidl_typesupport_introspection_c__FullName_Request_message_member_array,  // message members
  full_name_message__srv__FullName_Request__rosidl_typesupport_introspection_c__FullName_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  full_name_message__srv__FullName_Request__rosidl_typesupport_introspection_c__FullName_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t full_name_message__srv__FullName_Request__rosidl_typesupport_introspection_c__FullName_Request_message_type_support_handle = {
  0,
  &full_name_message__srv__FullName_Request__rosidl_typesupport_introspection_c__FullName_Request_message_members,
  get_message_typesupport_handle_function,
  &full_name_message__srv__FullName_Request__get_type_hash,
  &full_name_message__srv__FullName_Request__get_type_description,
  &full_name_message__srv__FullName_Request__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_full_name_message
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, full_name_message, srv, FullName_Request)() {
  if (!full_name_message__srv__FullName_Request__rosidl_typesupport_introspection_c__FullName_Request_message_type_support_handle.typesupport_identifier) {
    full_name_message__srv__FullName_Request__rosidl_typesupport_introspection_c__FullName_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &full_name_message__srv__FullName_Request__rosidl_typesupport_introspection_c__FullName_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "full_name_message/srv/detail/full_name__rosidl_typesupport_introspection_c.h"
// already included above
// #include "full_name_message/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "full_name_message/srv/detail/full_name__functions.h"
// already included above
// #include "full_name_message/srv/detail/full_name__struct.h"


// Include directives for member types
// Member `full_name`
// already included above
// #include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void full_name_message__srv__FullName_Response__rosidl_typesupport_introspection_c__FullName_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  full_name_message__srv__FullName_Response__init(message_memory);
}

void full_name_message__srv__FullName_Response__rosidl_typesupport_introspection_c__FullName_Response_fini_function(void * message_memory)
{
  full_name_message__srv__FullName_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember full_name_message__srv__FullName_Response__rosidl_typesupport_introspection_c__FullName_Response_message_member_array[1] = {
  {
    "full_name",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(full_name_message__srv__FullName_Response, full_name),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers full_name_message__srv__FullName_Response__rosidl_typesupport_introspection_c__FullName_Response_message_members = {
  "full_name_message__srv",  // message namespace
  "FullName_Response",  // message name
  1,  // number of fields
  sizeof(full_name_message__srv__FullName_Response),
  false,  // has_any_key_member_
  full_name_message__srv__FullName_Response__rosidl_typesupport_introspection_c__FullName_Response_message_member_array,  // message members
  full_name_message__srv__FullName_Response__rosidl_typesupport_introspection_c__FullName_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  full_name_message__srv__FullName_Response__rosidl_typesupport_introspection_c__FullName_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t full_name_message__srv__FullName_Response__rosidl_typesupport_introspection_c__FullName_Response_message_type_support_handle = {
  0,
  &full_name_message__srv__FullName_Response__rosidl_typesupport_introspection_c__FullName_Response_message_members,
  get_message_typesupport_handle_function,
  &full_name_message__srv__FullName_Response__get_type_hash,
  &full_name_message__srv__FullName_Response__get_type_description,
  &full_name_message__srv__FullName_Response__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_full_name_message
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, full_name_message, srv, FullName_Response)() {
  if (!full_name_message__srv__FullName_Response__rosidl_typesupport_introspection_c__FullName_Response_message_type_support_handle.typesupport_identifier) {
    full_name_message__srv__FullName_Response__rosidl_typesupport_introspection_c__FullName_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &full_name_message__srv__FullName_Response__rosidl_typesupport_introspection_c__FullName_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "full_name_message/srv/detail/full_name__rosidl_typesupport_introspection_c.h"
// already included above
// #include "full_name_message/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "full_name_message/srv/detail/full_name__functions.h"
// already included above
// #include "full_name_message/srv/detail/full_name__struct.h"


// Include directives for member types
// Member `info`
#include "service_msgs/msg/service_event_info.h"
// Member `info`
#include "service_msgs/msg/detail/service_event_info__rosidl_typesupport_introspection_c.h"
// Member `request`
// Member `response`
#include "full_name_message/srv/full_name.h"
// Member `request`
// Member `response`
// already included above
// #include "full_name_message/srv/detail/full_name__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__FullName_Event_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  full_name_message__srv__FullName_Event__init(message_memory);
}

void full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__FullName_Event_fini_function(void * message_memory)
{
  full_name_message__srv__FullName_Event__fini(message_memory);
}

size_t full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__size_function__FullName_Event__request(
  const void * untyped_member)
{
  const full_name_message__srv__FullName_Request__Sequence * member =
    (const full_name_message__srv__FullName_Request__Sequence *)(untyped_member);
  return member->size;
}

const void * full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__get_const_function__FullName_Event__request(
  const void * untyped_member, size_t index)
{
  const full_name_message__srv__FullName_Request__Sequence * member =
    (const full_name_message__srv__FullName_Request__Sequence *)(untyped_member);
  return &member->data[index];
}

void * full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__get_function__FullName_Event__request(
  void * untyped_member, size_t index)
{
  full_name_message__srv__FullName_Request__Sequence * member =
    (full_name_message__srv__FullName_Request__Sequence *)(untyped_member);
  return &member->data[index];
}

void full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__fetch_function__FullName_Event__request(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const full_name_message__srv__FullName_Request * item =
    ((const full_name_message__srv__FullName_Request *)
    full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__get_const_function__FullName_Event__request(untyped_member, index));
  full_name_message__srv__FullName_Request * value =
    (full_name_message__srv__FullName_Request *)(untyped_value);
  *value = *item;
}

void full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__assign_function__FullName_Event__request(
  void * untyped_member, size_t index, const void * untyped_value)
{
  full_name_message__srv__FullName_Request * item =
    ((full_name_message__srv__FullName_Request *)
    full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__get_function__FullName_Event__request(untyped_member, index));
  const full_name_message__srv__FullName_Request * value =
    (const full_name_message__srv__FullName_Request *)(untyped_value);
  *item = *value;
}

bool full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__resize_function__FullName_Event__request(
  void * untyped_member, size_t size)
{
  full_name_message__srv__FullName_Request__Sequence * member =
    (full_name_message__srv__FullName_Request__Sequence *)(untyped_member);
  full_name_message__srv__FullName_Request__Sequence__fini(member);
  return full_name_message__srv__FullName_Request__Sequence__init(member, size);
}

size_t full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__size_function__FullName_Event__response(
  const void * untyped_member)
{
  const full_name_message__srv__FullName_Response__Sequence * member =
    (const full_name_message__srv__FullName_Response__Sequence *)(untyped_member);
  return member->size;
}

const void * full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__get_const_function__FullName_Event__response(
  const void * untyped_member, size_t index)
{
  const full_name_message__srv__FullName_Response__Sequence * member =
    (const full_name_message__srv__FullName_Response__Sequence *)(untyped_member);
  return &member->data[index];
}

void * full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__get_function__FullName_Event__response(
  void * untyped_member, size_t index)
{
  full_name_message__srv__FullName_Response__Sequence * member =
    (full_name_message__srv__FullName_Response__Sequence *)(untyped_member);
  return &member->data[index];
}

void full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__fetch_function__FullName_Event__response(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const full_name_message__srv__FullName_Response * item =
    ((const full_name_message__srv__FullName_Response *)
    full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__get_const_function__FullName_Event__response(untyped_member, index));
  full_name_message__srv__FullName_Response * value =
    (full_name_message__srv__FullName_Response *)(untyped_value);
  *value = *item;
}

void full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__assign_function__FullName_Event__response(
  void * untyped_member, size_t index, const void * untyped_value)
{
  full_name_message__srv__FullName_Response * item =
    ((full_name_message__srv__FullName_Response *)
    full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__get_function__FullName_Event__response(untyped_member, index));
  const full_name_message__srv__FullName_Response * value =
    (const full_name_message__srv__FullName_Response *)(untyped_value);
  *item = *value;
}

bool full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__resize_function__FullName_Event__response(
  void * untyped_member, size_t size)
{
  full_name_message__srv__FullName_Response__Sequence * member =
    (full_name_message__srv__FullName_Response__Sequence *)(untyped_member);
  full_name_message__srv__FullName_Response__Sequence__fini(member);
  return full_name_message__srv__FullName_Response__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__FullName_Event_message_member_array[3] = {
  {
    "info",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(full_name_message__srv__FullName_Event, info),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "request",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    true,  // is array
    1,  // array size
    true,  // is upper bound
    offsetof(full_name_message__srv__FullName_Event, request),  // bytes offset in struct
    NULL,  // default value
    full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__size_function__FullName_Event__request,  // size() function pointer
    full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__get_const_function__FullName_Event__request,  // get_const(index) function pointer
    full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__get_function__FullName_Event__request,  // get(index) function pointer
    full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__fetch_function__FullName_Event__request,  // fetch(index, &value) function pointer
    full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__assign_function__FullName_Event__request,  // assign(index, value) function pointer
    full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__resize_function__FullName_Event__request  // resize(index) function pointer
  },
  {
    "response",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    true,  // is array
    1,  // array size
    true,  // is upper bound
    offsetof(full_name_message__srv__FullName_Event, response),  // bytes offset in struct
    NULL,  // default value
    full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__size_function__FullName_Event__response,  // size() function pointer
    full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__get_const_function__FullName_Event__response,  // get_const(index) function pointer
    full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__get_function__FullName_Event__response,  // get(index) function pointer
    full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__fetch_function__FullName_Event__response,  // fetch(index, &value) function pointer
    full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__assign_function__FullName_Event__response,  // assign(index, value) function pointer
    full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__resize_function__FullName_Event__response  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__FullName_Event_message_members = {
  "full_name_message__srv",  // message namespace
  "FullName_Event",  // message name
  3,  // number of fields
  sizeof(full_name_message__srv__FullName_Event),
  false,  // has_any_key_member_
  full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__FullName_Event_message_member_array,  // message members
  full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__FullName_Event_init_function,  // function to initialize message memory (memory has to be allocated)
  full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__FullName_Event_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__FullName_Event_message_type_support_handle = {
  0,
  &full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__FullName_Event_message_members,
  get_message_typesupport_handle_function,
  &full_name_message__srv__FullName_Event__get_type_hash,
  &full_name_message__srv__FullName_Event__get_type_description,
  &full_name_message__srv__FullName_Event__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_full_name_message
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, full_name_message, srv, FullName_Event)() {
  full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__FullName_Event_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_msgs, msg, ServiceEventInfo)();
  full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__FullName_Event_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, full_name_message, srv, FullName_Request)();
  full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__FullName_Event_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, full_name_message, srv, FullName_Response)();
  if (!full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__FullName_Event_message_type_support_handle.typesupport_identifier) {
    full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__FullName_Event_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__FullName_Event_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "full_name_message/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "full_name_message/srv/detail/full_name__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers full_name_message__srv__detail__full_name__rosidl_typesupport_introspection_c__FullName_service_members = {
  "full_name_message__srv",  // service namespace
  "FullName",  // service name
  // the following fields are initialized below on first access
  NULL,  // request message
  // full_name_message__srv__detail__full_name__rosidl_typesupport_introspection_c__FullName_Request_message_type_support_handle,
  NULL,  // response message
  // full_name_message__srv__detail__full_name__rosidl_typesupport_introspection_c__FullName_Response_message_type_support_handle
  NULL  // event_message
  // full_name_message__srv__detail__full_name__rosidl_typesupport_introspection_c__FullName_Response_message_type_support_handle
};


static rosidl_service_type_support_t full_name_message__srv__detail__full_name__rosidl_typesupport_introspection_c__FullName_service_type_support_handle = {
  0,
  &full_name_message__srv__detail__full_name__rosidl_typesupport_introspection_c__FullName_service_members,
  get_service_typesupport_handle_function,
  &full_name_message__srv__FullName_Request__rosidl_typesupport_introspection_c__FullName_Request_message_type_support_handle,
  &full_name_message__srv__FullName_Response__rosidl_typesupport_introspection_c__FullName_Response_message_type_support_handle,
  &full_name_message__srv__FullName_Event__rosidl_typesupport_introspection_c__FullName_Event_message_type_support_handle,
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_CREATE_EVENT_MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c,
    full_name_message,
    srv,
    FullName
  ),
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_DESTROY_EVENT_MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c,
    full_name_message,
    srv,
    FullName
  ),
  &full_name_message__srv__FullName__get_type_hash,
  &full_name_message__srv__FullName__get_type_description,
  &full_name_message__srv__FullName__get_type_description_sources,
};

// Forward declaration of message type support functions for service members
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, full_name_message, srv, FullName_Request)(void);

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, full_name_message, srv, FullName_Response)(void);

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, full_name_message, srv, FullName_Event)(void);

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_full_name_message
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, full_name_message, srv, FullName)(void) {
  if (!full_name_message__srv__detail__full_name__rosidl_typesupport_introspection_c__FullName_service_type_support_handle.typesupport_identifier) {
    full_name_message__srv__detail__full_name__rosidl_typesupport_introspection_c__FullName_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)full_name_message__srv__detail__full_name__rosidl_typesupport_introspection_c__FullName_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, full_name_message, srv, FullName_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, full_name_message, srv, FullName_Response)()->data;
  }
  if (!service_members->event_members_) {
    service_members->event_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, full_name_message, srv, FullName_Event)()->data;
  }

  return &full_name_message__srv__detail__full_name__rosidl_typesupport_introspection_c__FullName_service_type_support_handle;
}
