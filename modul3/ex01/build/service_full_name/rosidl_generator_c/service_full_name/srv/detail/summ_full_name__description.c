// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from service_full_name:srv/SummFullName.idl
// generated code does not contain a copyright notice

#include "service_full_name/srv/detail/summ_full_name__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_service_full_name
const rosidl_type_hash_t *
service_full_name__srv__SummFullName__get_type_hash(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x85, 0xb1, 0xb3, 0x14, 0x55, 0x12, 0x76, 0x6b,
      0x6a, 0xea, 0x39, 0x2d, 0xb2, 0xf3, 0xd1, 0x6c,
      0xae, 0x26, 0x49, 0x28, 0xe7, 0xa9, 0xf2, 0xa3,
      0x20, 0x26, 0xd1, 0xa2, 0x4d, 0x69, 0x78, 0x3a,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_service_full_name
const rosidl_type_hash_t *
service_full_name__srv__SummFullName_Request__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xf9, 0x8b, 0xe6, 0x0a, 0x7f, 0x92, 0x0c, 0x40,
      0xd7, 0xc0, 0xc4, 0xf9, 0x7c, 0xc9, 0x8f, 0x36,
      0xf2, 0x61, 0x6f, 0x0d, 0x3d, 0x38, 0xe7, 0x53,
      0xb3, 0x92, 0x3a, 0x79, 0xc9, 0x36, 0x5a, 0x8f,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_service_full_name
const rosidl_type_hash_t *
service_full_name__srv__SummFullName_Response__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x2c, 0x94, 0x20, 0x5c, 0x95, 0x85, 0x39, 0x03,
      0x9d, 0x9d, 0x8d, 0x99, 0xb7, 0x0b, 0x9f, 0x0e,
      0xec, 0x0b, 0x88, 0xd0, 0x47, 0x9e, 0x04, 0x44,
      0x13, 0xa6, 0x2b, 0xcc, 0x58, 0xdf, 0xed, 0x2b,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_service_full_name
const rosidl_type_hash_t *
service_full_name__srv__SummFullName_Event__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xe8, 0x85, 0x40, 0xe4, 0x6f, 0xc0, 0xdb, 0x40,
      0x3f, 0x43, 0xbe, 0x27, 0xcb, 0x76, 0xab, 0xb3,
      0xb0, 0x3e, 0x65, 0x0c, 0x86, 0x01, 0xee, 0xec,
      0x2a, 0x89, 0xc7, 0x61, 0x68, 0xfa, 0x71, 0x3a,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "builtin_interfaces/msg/detail/time__functions.h"
#include "service_msgs/msg/detail/service_event_info__functions.h"

// Hashes for external referenced types
#ifndef NDEBUG
static const rosidl_type_hash_t builtin_interfaces__msg__Time__EXPECTED_HASH = {1, {
    0xb1, 0x06, 0x23, 0x5e, 0x25, 0xa4, 0xc5, 0xed,
    0x35, 0x09, 0x8a, 0xa0, 0xa6, 0x1a, 0x3e, 0xe9,
    0xc9, 0xb1, 0x8d, 0x19, 0x7f, 0x39, 0x8b, 0x0e,
    0x42, 0x06, 0xce, 0xa9, 0xac, 0xf9, 0xc1, 0x97,
  }};
static const rosidl_type_hash_t service_msgs__msg__ServiceEventInfo__EXPECTED_HASH = {1, {
    0x41, 0xbc, 0xbb, 0xe0, 0x7a, 0x75, 0xc9, 0xb5,
    0x2b, 0xc9, 0x6b, 0xfd, 0x5c, 0x24, 0xd7, 0xf0,
    0xfc, 0x0a, 0x08, 0xc0, 0xcb, 0x79, 0x21, 0xb3,
    0x37, 0x3c, 0x57, 0x32, 0x34, 0x5a, 0x6f, 0x45,
  }};
#endif

static char service_full_name__srv__SummFullName__TYPE_NAME[] = "service_full_name/srv/SummFullName";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";
static char service_full_name__srv__SummFullName_Event__TYPE_NAME[] = "service_full_name/srv/SummFullName_Event";
static char service_full_name__srv__SummFullName_Request__TYPE_NAME[] = "service_full_name/srv/SummFullName_Request";
static char service_full_name__srv__SummFullName_Response__TYPE_NAME[] = "service_full_name/srv/SummFullName_Response";
static char service_msgs__msg__ServiceEventInfo__TYPE_NAME[] = "service_msgs/msg/ServiceEventInfo";

// Define type names, field names, and default values
static char service_full_name__srv__SummFullName__FIELD_NAME__request_message[] = "request_message";
static char service_full_name__srv__SummFullName__FIELD_NAME__response_message[] = "response_message";
static char service_full_name__srv__SummFullName__FIELD_NAME__event_message[] = "event_message";

static rosidl_runtime_c__type_description__Field service_full_name__srv__SummFullName__FIELDS[] = {
  {
    {service_full_name__srv__SummFullName__FIELD_NAME__request_message, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {service_full_name__srv__SummFullName_Request__TYPE_NAME, 42, 42},
    },
    {NULL, 0, 0},
  },
  {
    {service_full_name__srv__SummFullName__FIELD_NAME__response_message, 16, 16},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {service_full_name__srv__SummFullName_Response__TYPE_NAME, 43, 43},
    },
    {NULL, 0, 0},
  },
  {
    {service_full_name__srv__SummFullName__FIELD_NAME__event_message, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {service_full_name__srv__SummFullName_Event__TYPE_NAME, 40, 40},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription service_full_name__srv__SummFullName__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {service_full_name__srv__SummFullName_Event__TYPE_NAME, 40, 40},
    {NULL, 0, 0},
  },
  {
    {service_full_name__srv__SummFullName_Request__TYPE_NAME, 42, 42},
    {NULL, 0, 0},
  },
  {
    {service_full_name__srv__SummFullName_Response__TYPE_NAME, 43, 43},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
service_full_name__srv__SummFullName__get_type_description(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {service_full_name__srv__SummFullName__TYPE_NAME, 34, 34},
      {service_full_name__srv__SummFullName__FIELDS, 3, 3},
    },
    {service_full_name__srv__SummFullName__REFERENCED_TYPE_DESCRIPTIONS, 5, 5},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[1].fields = service_full_name__srv__SummFullName_Event__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[2].fields = service_full_name__srv__SummFullName_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[3].fields = service_full_name__srv__SummFullName_Response__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[4].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char service_full_name__srv__SummFullName_Request__FIELD_NAME__last_name[] = "last_name";
static char service_full_name__srv__SummFullName_Request__FIELD_NAME__name[] = "name";
static char service_full_name__srv__SummFullName_Request__FIELD_NAME__first_name[] = "first_name";

static rosidl_runtime_c__type_description__Field service_full_name__srv__SummFullName_Request__FIELDS[] = {
  {
    {service_full_name__srv__SummFullName_Request__FIELD_NAME__last_name, 9, 9},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {service_full_name__srv__SummFullName_Request__FIELD_NAME__name, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {service_full_name__srv__SummFullName_Request__FIELD_NAME__first_name, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
service_full_name__srv__SummFullName_Request__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {service_full_name__srv__SummFullName_Request__TYPE_NAME, 42, 42},
      {service_full_name__srv__SummFullName_Request__FIELDS, 3, 3},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char service_full_name__srv__SummFullName_Response__FIELD_NAME__full_name[] = "full_name";

static rosidl_runtime_c__type_description__Field service_full_name__srv__SummFullName_Response__FIELDS[] = {
  {
    {service_full_name__srv__SummFullName_Response__FIELD_NAME__full_name, 9, 9},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
service_full_name__srv__SummFullName_Response__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {service_full_name__srv__SummFullName_Response__TYPE_NAME, 43, 43},
      {service_full_name__srv__SummFullName_Response__FIELDS, 1, 1},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char service_full_name__srv__SummFullName_Event__FIELD_NAME__info[] = "info";
static char service_full_name__srv__SummFullName_Event__FIELD_NAME__request[] = "request";
static char service_full_name__srv__SummFullName_Event__FIELD_NAME__response[] = "response";

static rosidl_runtime_c__type_description__Field service_full_name__srv__SummFullName_Event__FIELDS[] = {
  {
    {service_full_name__srv__SummFullName_Event__FIELD_NAME__info, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    },
    {NULL, 0, 0},
  },
  {
    {service_full_name__srv__SummFullName_Event__FIELD_NAME__request, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {service_full_name__srv__SummFullName_Request__TYPE_NAME, 42, 42},
    },
    {NULL, 0, 0},
  },
  {
    {service_full_name__srv__SummFullName_Event__FIELD_NAME__response, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {service_full_name__srv__SummFullName_Response__TYPE_NAME, 43, 43},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription service_full_name__srv__SummFullName_Event__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {service_full_name__srv__SummFullName_Request__TYPE_NAME, 42, 42},
    {NULL, 0, 0},
  },
  {
    {service_full_name__srv__SummFullName_Response__TYPE_NAME, 43, 43},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
service_full_name__srv__SummFullName_Event__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {service_full_name__srv__SummFullName_Event__TYPE_NAME, 40, 40},
      {service_full_name__srv__SummFullName_Event__FIELDS, 3, 3},
    },
    {service_full_name__srv__SummFullName_Event__REFERENCED_TYPE_DESCRIPTIONS, 4, 4},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[1].fields = service_full_name__srv__SummFullName_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[2].fields = service_full_name__srv__SummFullName_Response__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[3].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "string last_name\n"
  "string name\n"
  "string first_name\n"
  "---\n"
  "string full_name";

static char srv_encoding[] = "srv";
static char implicit_encoding[] = "implicit";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
service_full_name__srv__SummFullName__get_individual_type_description_source(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {service_full_name__srv__SummFullName__TYPE_NAME, 34, 34},
    {srv_encoding, 3, 3},
    {toplevel_type_raw_source, 67, 67},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
service_full_name__srv__SummFullName_Request__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {service_full_name__srv__SummFullName_Request__TYPE_NAME, 42, 42},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
service_full_name__srv__SummFullName_Response__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {service_full_name__srv__SummFullName_Response__TYPE_NAME, 43, 43},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
service_full_name__srv__SummFullName_Event__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {service_full_name__srv__SummFullName_Event__TYPE_NAME, 40, 40},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
service_full_name__srv__SummFullName__get_type_description_sources(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[6];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 6, 6};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *service_full_name__srv__SummFullName__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *service_full_name__srv__SummFullName_Event__get_individual_type_description_source(NULL);
    sources[3] = *service_full_name__srv__SummFullName_Request__get_individual_type_description_source(NULL);
    sources[4] = *service_full_name__srv__SummFullName_Response__get_individual_type_description_source(NULL);
    sources[5] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
service_full_name__srv__SummFullName_Request__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *service_full_name__srv__SummFullName_Request__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
service_full_name__srv__SummFullName_Response__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *service_full_name__srv__SummFullName_Response__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
service_full_name__srv__SummFullName_Event__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[5];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 5, 5};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *service_full_name__srv__SummFullName_Event__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *service_full_name__srv__SummFullName_Request__get_individual_type_description_source(NULL);
    sources[3] = *service_full_name__srv__SummFullName_Response__get_individual_type_description_source(NULL);
    sources[4] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
