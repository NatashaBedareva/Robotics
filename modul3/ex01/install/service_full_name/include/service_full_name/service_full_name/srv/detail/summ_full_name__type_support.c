// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from service_full_name:srv/SummFullName.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "service_full_name/srv/detail/summ_full_name__rosidl_typesupport_introspection_c.h"
#include "service_full_name/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "service_full_name/srv/detail/summ_full_name__functions.h"
#include "service_full_name/srv/detail/summ_full_name__struct.h"


// Include directives for member types
// Member `last_name`
// Member `name`
// Member `first_name`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void service_full_name__srv__SummFullName_Request__rosidl_typesupport_introspection_c__SummFullName_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  service_full_name__srv__SummFullName_Request__init(message_memory);
}

void service_full_name__srv__SummFullName_Request__rosidl_typesupport_introspection_c__SummFullName_Request_fini_function(void * message_memory)
{
  service_full_name__srv__SummFullName_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember service_full_name__srv__SummFullName_Request__rosidl_typesupport_introspection_c__SummFullName_Request_message_member_array[3] = {
  {
    "last_name",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(service_full_name__srv__SummFullName_Request, last_name),  // bytes offset in struct
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
    offsetof(service_full_name__srv__SummFullName_Request, name),  // bytes offset in struct
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
    offsetof(service_full_name__srv__SummFullName_Request, first_name),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers service_full_name__srv__SummFullName_Request__rosidl_typesupport_introspection_c__SummFullName_Request_message_members = {
  "service_full_name__srv",  // message namespace
  "SummFullName_Request",  // message name
  3,  // number of fields
  sizeof(service_full_name__srv__SummFullName_Request),
  false,  // has_any_key_member_
  service_full_name__srv__SummFullName_Request__rosidl_typesupport_introspection_c__SummFullName_Request_message_member_array,  // message members
  service_full_name__srv__SummFullName_Request__rosidl_typesupport_introspection_c__SummFullName_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  service_full_name__srv__SummFullName_Request__rosidl_typesupport_introspection_c__SummFullName_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t service_full_name__srv__SummFullName_Request__rosidl_typesupport_introspection_c__SummFullName_Request_message_type_support_handle = {
  0,
  &service_full_name__srv__SummFullName_Request__rosidl_typesupport_introspection_c__SummFullName_Request_message_members,
  get_message_typesupport_handle_function,
  &service_full_name__srv__SummFullName_Request__get_type_hash,
  &service_full_name__srv__SummFullName_Request__get_type_description,
  &service_full_name__srv__SummFullName_Request__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_service_full_name
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_full_name, srv, SummFullName_Request)() {
  if (!service_full_name__srv__SummFullName_Request__rosidl_typesupport_introspection_c__SummFullName_Request_message_type_support_handle.typesupport_identifier) {
    service_full_name__srv__SummFullName_Request__rosidl_typesupport_introspection_c__SummFullName_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &service_full_name__srv__SummFullName_Request__rosidl_typesupport_introspection_c__SummFullName_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "service_full_name/srv/detail/summ_full_name__rosidl_typesupport_introspection_c.h"
// already included above
// #include "service_full_name/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "service_full_name/srv/detail/summ_full_name__functions.h"
// already included above
// #include "service_full_name/srv/detail/summ_full_name__struct.h"


// Include directives for member types
// Member `full_name`
// already included above
// #include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void service_full_name__srv__SummFullName_Response__rosidl_typesupport_introspection_c__SummFullName_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  service_full_name__srv__SummFullName_Response__init(message_memory);
}

void service_full_name__srv__SummFullName_Response__rosidl_typesupport_introspection_c__SummFullName_Response_fini_function(void * message_memory)
{
  service_full_name__srv__SummFullName_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember service_full_name__srv__SummFullName_Response__rosidl_typesupport_introspection_c__SummFullName_Response_message_member_array[1] = {
  {
    "full_name",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(service_full_name__srv__SummFullName_Response, full_name),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers service_full_name__srv__SummFullName_Response__rosidl_typesupport_introspection_c__SummFullName_Response_message_members = {
  "service_full_name__srv",  // message namespace
  "SummFullName_Response",  // message name
  1,  // number of fields
  sizeof(service_full_name__srv__SummFullName_Response),
  false,  // has_any_key_member_
  service_full_name__srv__SummFullName_Response__rosidl_typesupport_introspection_c__SummFullName_Response_message_member_array,  // message members
  service_full_name__srv__SummFullName_Response__rosidl_typesupport_introspection_c__SummFullName_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  service_full_name__srv__SummFullName_Response__rosidl_typesupport_introspection_c__SummFullName_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t service_full_name__srv__SummFullName_Response__rosidl_typesupport_introspection_c__SummFullName_Response_message_type_support_handle = {
  0,
  &service_full_name__srv__SummFullName_Response__rosidl_typesupport_introspection_c__SummFullName_Response_message_members,
  get_message_typesupport_handle_function,
  &service_full_name__srv__SummFullName_Response__get_type_hash,
  &service_full_name__srv__SummFullName_Response__get_type_description,
  &service_full_name__srv__SummFullName_Response__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_service_full_name
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_full_name, srv, SummFullName_Response)() {
  if (!service_full_name__srv__SummFullName_Response__rosidl_typesupport_introspection_c__SummFullName_Response_message_type_support_handle.typesupport_identifier) {
    service_full_name__srv__SummFullName_Response__rosidl_typesupport_introspection_c__SummFullName_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &service_full_name__srv__SummFullName_Response__rosidl_typesupport_introspection_c__SummFullName_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "service_full_name/srv/detail/summ_full_name__rosidl_typesupport_introspection_c.h"
// already included above
// #include "service_full_name/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "service_full_name/srv/detail/summ_full_name__functions.h"
// already included above
// #include "service_full_name/srv/detail/summ_full_name__struct.h"


// Include directives for member types
// Member `info`
#include "service_msgs/msg/service_event_info.h"
// Member `info`
#include "service_msgs/msg/detail/service_event_info__rosidl_typesupport_introspection_c.h"
// Member `request`
// Member `response`
#include "service_full_name/srv/summ_full_name.h"
// Member `request`
// Member `response`
// already included above
// #include "service_full_name/srv/detail/summ_full_name__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__SummFullName_Event_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  service_full_name__srv__SummFullName_Event__init(message_memory);
}

void service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__SummFullName_Event_fini_function(void * message_memory)
{
  service_full_name__srv__SummFullName_Event__fini(message_memory);
}

size_t service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__size_function__SummFullName_Event__request(
  const void * untyped_member)
{
  const service_full_name__srv__SummFullName_Request__Sequence * member =
    (const service_full_name__srv__SummFullName_Request__Sequence *)(untyped_member);
  return member->size;
}

const void * service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__get_const_function__SummFullName_Event__request(
  const void * untyped_member, size_t index)
{
  const service_full_name__srv__SummFullName_Request__Sequence * member =
    (const service_full_name__srv__SummFullName_Request__Sequence *)(untyped_member);
  return &member->data[index];
}

void * service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__get_function__SummFullName_Event__request(
  void * untyped_member, size_t index)
{
  service_full_name__srv__SummFullName_Request__Sequence * member =
    (service_full_name__srv__SummFullName_Request__Sequence *)(untyped_member);
  return &member->data[index];
}

void service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__fetch_function__SummFullName_Event__request(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const service_full_name__srv__SummFullName_Request * item =
    ((const service_full_name__srv__SummFullName_Request *)
    service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__get_const_function__SummFullName_Event__request(untyped_member, index));
  service_full_name__srv__SummFullName_Request * value =
    (service_full_name__srv__SummFullName_Request *)(untyped_value);
  *value = *item;
}

void service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__assign_function__SummFullName_Event__request(
  void * untyped_member, size_t index, const void * untyped_value)
{
  service_full_name__srv__SummFullName_Request * item =
    ((service_full_name__srv__SummFullName_Request *)
    service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__get_function__SummFullName_Event__request(untyped_member, index));
  const service_full_name__srv__SummFullName_Request * value =
    (const service_full_name__srv__SummFullName_Request *)(untyped_value);
  *item = *value;
}

bool service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__resize_function__SummFullName_Event__request(
  void * untyped_member, size_t size)
{
  service_full_name__srv__SummFullName_Request__Sequence * member =
    (service_full_name__srv__SummFullName_Request__Sequence *)(untyped_member);
  service_full_name__srv__SummFullName_Request__Sequence__fini(member);
  return service_full_name__srv__SummFullName_Request__Sequence__init(member, size);
}

size_t service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__size_function__SummFullName_Event__response(
  const void * untyped_member)
{
  const service_full_name__srv__SummFullName_Response__Sequence * member =
    (const service_full_name__srv__SummFullName_Response__Sequence *)(untyped_member);
  return member->size;
}

const void * service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__get_const_function__SummFullName_Event__response(
  const void * untyped_member, size_t index)
{
  const service_full_name__srv__SummFullName_Response__Sequence * member =
    (const service_full_name__srv__SummFullName_Response__Sequence *)(untyped_member);
  return &member->data[index];
}

void * service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__get_function__SummFullName_Event__response(
  void * untyped_member, size_t index)
{
  service_full_name__srv__SummFullName_Response__Sequence * member =
    (service_full_name__srv__SummFullName_Response__Sequence *)(untyped_member);
  return &member->data[index];
}

void service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__fetch_function__SummFullName_Event__response(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const service_full_name__srv__SummFullName_Response * item =
    ((const service_full_name__srv__SummFullName_Response *)
    service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__get_const_function__SummFullName_Event__response(untyped_member, index));
  service_full_name__srv__SummFullName_Response * value =
    (service_full_name__srv__SummFullName_Response *)(untyped_value);
  *value = *item;
}

void service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__assign_function__SummFullName_Event__response(
  void * untyped_member, size_t index, const void * untyped_value)
{
  service_full_name__srv__SummFullName_Response * item =
    ((service_full_name__srv__SummFullName_Response *)
    service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__get_function__SummFullName_Event__response(untyped_member, index));
  const service_full_name__srv__SummFullName_Response * value =
    (const service_full_name__srv__SummFullName_Response *)(untyped_value);
  *item = *value;
}

bool service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__resize_function__SummFullName_Event__response(
  void * untyped_member, size_t size)
{
  service_full_name__srv__SummFullName_Response__Sequence * member =
    (service_full_name__srv__SummFullName_Response__Sequence *)(untyped_member);
  service_full_name__srv__SummFullName_Response__Sequence__fini(member);
  return service_full_name__srv__SummFullName_Response__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__SummFullName_Event_message_member_array[3] = {
  {
    "info",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(service_full_name__srv__SummFullName_Event, info),  // bytes offset in struct
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
    offsetof(service_full_name__srv__SummFullName_Event, request),  // bytes offset in struct
    NULL,  // default value
    service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__size_function__SummFullName_Event__request,  // size() function pointer
    service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__get_const_function__SummFullName_Event__request,  // get_const(index) function pointer
    service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__get_function__SummFullName_Event__request,  // get(index) function pointer
    service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__fetch_function__SummFullName_Event__request,  // fetch(index, &value) function pointer
    service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__assign_function__SummFullName_Event__request,  // assign(index, value) function pointer
    service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__resize_function__SummFullName_Event__request  // resize(index) function pointer
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
    offsetof(service_full_name__srv__SummFullName_Event, response),  // bytes offset in struct
    NULL,  // default value
    service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__size_function__SummFullName_Event__response,  // size() function pointer
    service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__get_const_function__SummFullName_Event__response,  // get_const(index) function pointer
    service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__get_function__SummFullName_Event__response,  // get(index) function pointer
    service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__fetch_function__SummFullName_Event__response,  // fetch(index, &value) function pointer
    service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__assign_function__SummFullName_Event__response,  // assign(index, value) function pointer
    service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__resize_function__SummFullName_Event__response  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__SummFullName_Event_message_members = {
  "service_full_name__srv",  // message namespace
  "SummFullName_Event",  // message name
  3,  // number of fields
  sizeof(service_full_name__srv__SummFullName_Event),
  false,  // has_any_key_member_
  service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__SummFullName_Event_message_member_array,  // message members
  service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__SummFullName_Event_init_function,  // function to initialize message memory (memory has to be allocated)
  service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__SummFullName_Event_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__SummFullName_Event_message_type_support_handle = {
  0,
  &service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__SummFullName_Event_message_members,
  get_message_typesupport_handle_function,
  &service_full_name__srv__SummFullName_Event__get_type_hash,
  &service_full_name__srv__SummFullName_Event__get_type_description,
  &service_full_name__srv__SummFullName_Event__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_service_full_name
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_full_name, srv, SummFullName_Event)() {
  service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__SummFullName_Event_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_msgs, msg, ServiceEventInfo)();
  service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__SummFullName_Event_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_full_name, srv, SummFullName_Request)();
  service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__SummFullName_Event_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_full_name, srv, SummFullName_Response)();
  if (!service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__SummFullName_Event_message_type_support_handle.typesupport_identifier) {
    service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__SummFullName_Event_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__SummFullName_Event_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "service_full_name/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "service_full_name/srv/detail/summ_full_name__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers service_full_name__srv__detail__summ_full_name__rosidl_typesupport_introspection_c__SummFullName_service_members = {
  "service_full_name__srv",  // service namespace
  "SummFullName",  // service name
  // the following fields are initialized below on first access
  NULL,  // request message
  // service_full_name__srv__detail__summ_full_name__rosidl_typesupport_introspection_c__SummFullName_Request_message_type_support_handle,
  NULL,  // response message
  // service_full_name__srv__detail__summ_full_name__rosidl_typesupport_introspection_c__SummFullName_Response_message_type_support_handle
  NULL  // event_message
  // service_full_name__srv__detail__summ_full_name__rosidl_typesupport_introspection_c__SummFullName_Response_message_type_support_handle
};


static rosidl_service_type_support_t service_full_name__srv__detail__summ_full_name__rosidl_typesupport_introspection_c__SummFullName_service_type_support_handle = {
  0,
  &service_full_name__srv__detail__summ_full_name__rosidl_typesupport_introspection_c__SummFullName_service_members,
  get_service_typesupport_handle_function,
  &service_full_name__srv__SummFullName_Request__rosidl_typesupport_introspection_c__SummFullName_Request_message_type_support_handle,
  &service_full_name__srv__SummFullName_Response__rosidl_typesupport_introspection_c__SummFullName_Response_message_type_support_handle,
  &service_full_name__srv__SummFullName_Event__rosidl_typesupport_introspection_c__SummFullName_Event_message_type_support_handle,
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_CREATE_EVENT_MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c,
    service_full_name,
    srv,
    SummFullName
  ),
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_DESTROY_EVENT_MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c,
    service_full_name,
    srv,
    SummFullName
  ),
  &service_full_name__srv__SummFullName__get_type_hash,
  &service_full_name__srv__SummFullName__get_type_description,
  &service_full_name__srv__SummFullName__get_type_description_sources,
};

// Forward declaration of message type support functions for service members
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_full_name, srv, SummFullName_Request)(void);

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_full_name, srv, SummFullName_Response)(void);

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_full_name, srv, SummFullName_Event)(void);

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_service_full_name
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_full_name, srv, SummFullName)(void) {
  if (!service_full_name__srv__detail__summ_full_name__rosidl_typesupport_introspection_c__SummFullName_service_type_support_handle.typesupport_identifier) {
    service_full_name__srv__detail__summ_full_name__rosidl_typesupport_introspection_c__SummFullName_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)service_full_name__srv__detail__summ_full_name__rosidl_typesupport_introspection_c__SummFullName_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_full_name, srv, SummFullName_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_full_name, srv, SummFullName_Response)()->data;
  }
  if (!service_members->event_members_) {
    service_members->event_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_full_name, srv, SummFullName_Event)()->data;
  }

  return &service_full_name__srv__detail__summ_full_name__rosidl_typesupport_introspection_c__SummFullName_service_type_support_handle;
}
