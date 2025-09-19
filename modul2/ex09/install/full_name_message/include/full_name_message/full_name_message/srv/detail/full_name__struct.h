// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from full_name_message:srv/FullName.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "full_name_message/srv/full_name.h"


#ifndef FULL_NAME_MESSAGE__SRV__DETAIL__FULL_NAME__STRUCT_H_
#define FULL_NAME_MESSAGE__SRV__DETAIL__FULL_NAME__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'last_name'
// Member 'name'
// Member 'first_name'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/FullName in the package full_name_message.
typedef struct full_name_message__srv__FullName_Request
{
  rosidl_runtime_c__String last_name;
  rosidl_runtime_c__String name;
  rosidl_runtime_c__String first_name;
} full_name_message__srv__FullName_Request;

// Struct for a sequence of full_name_message__srv__FullName_Request.
typedef struct full_name_message__srv__FullName_Request__Sequence
{
  full_name_message__srv__FullName_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} full_name_message__srv__FullName_Request__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'full_name'
// already included above
// #include "rosidl_runtime_c/string.h"

/// Struct defined in srv/FullName in the package full_name_message.
typedef struct full_name_message__srv__FullName_Response
{
  rosidl_runtime_c__String full_name;
} full_name_message__srv__FullName_Response;

// Struct for a sequence of full_name_message__srv__FullName_Response.
typedef struct full_name_message__srv__FullName_Response__Sequence
{
  full_name_message__srv__FullName_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} full_name_message__srv__FullName_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  full_name_message__srv__FullName_Event__request__MAX_SIZE = 1
};
// response
enum
{
  full_name_message__srv__FullName_Event__response__MAX_SIZE = 1
};

/// Struct defined in srv/FullName in the package full_name_message.
typedef struct full_name_message__srv__FullName_Event
{
  service_msgs__msg__ServiceEventInfo info;
  full_name_message__srv__FullName_Request__Sequence request;
  full_name_message__srv__FullName_Response__Sequence response;
} full_name_message__srv__FullName_Event;

// Struct for a sequence of full_name_message__srv__FullName_Event.
typedef struct full_name_message__srv__FullName_Event__Sequence
{
  full_name_message__srv__FullName_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} full_name_message__srv__FullName_Event__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // FULL_NAME_MESSAGE__SRV__DETAIL__FULL_NAME__STRUCT_H_
