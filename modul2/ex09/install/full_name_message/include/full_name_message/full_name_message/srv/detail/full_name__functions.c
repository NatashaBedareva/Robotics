// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from full_name_message:srv/FullName.idl
// generated code does not contain a copyright notice
#include "full_name_message/srv/detail/full_name__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `last_name`
// Member `name`
// Member `first_name`
#include "rosidl_runtime_c/string_functions.h"

bool
full_name_message__srv__FullName_Request__init(full_name_message__srv__FullName_Request * msg)
{
  if (!msg) {
    return false;
  }
  // last_name
  if (!rosidl_runtime_c__String__init(&msg->last_name)) {
    full_name_message__srv__FullName_Request__fini(msg);
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__init(&msg->name)) {
    full_name_message__srv__FullName_Request__fini(msg);
    return false;
  }
  // first_name
  if (!rosidl_runtime_c__String__init(&msg->first_name)) {
    full_name_message__srv__FullName_Request__fini(msg);
    return false;
  }
  return true;
}

void
full_name_message__srv__FullName_Request__fini(full_name_message__srv__FullName_Request * msg)
{
  if (!msg) {
    return;
  }
  // last_name
  rosidl_runtime_c__String__fini(&msg->last_name);
  // name
  rosidl_runtime_c__String__fini(&msg->name);
  // first_name
  rosidl_runtime_c__String__fini(&msg->first_name);
}

bool
full_name_message__srv__FullName_Request__are_equal(const full_name_message__srv__FullName_Request * lhs, const full_name_message__srv__FullName_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // last_name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->last_name), &(rhs->last_name)))
  {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->name), &(rhs->name)))
  {
    return false;
  }
  // first_name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->first_name), &(rhs->first_name)))
  {
    return false;
  }
  return true;
}

bool
full_name_message__srv__FullName_Request__copy(
  const full_name_message__srv__FullName_Request * input,
  full_name_message__srv__FullName_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // last_name
  if (!rosidl_runtime_c__String__copy(
      &(input->last_name), &(output->last_name)))
  {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__copy(
      &(input->name), &(output->name)))
  {
    return false;
  }
  // first_name
  if (!rosidl_runtime_c__String__copy(
      &(input->first_name), &(output->first_name)))
  {
    return false;
  }
  return true;
}

full_name_message__srv__FullName_Request *
full_name_message__srv__FullName_Request__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  full_name_message__srv__FullName_Request * msg = (full_name_message__srv__FullName_Request *)allocator.allocate(sizeof(full_name_message__srv__FullName_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(full_name_message__srv__FullName_Request));
  bool success = full_name_message__srv__FullName_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
full_name_message__srv__FullName_Request__destroy(full_name_message__srv__FullName_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    full_name_message__srv__FullName_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
full_name_message__srv__FullName_Request__Sequence__init(full_name_message__srv__FullName_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  full_name_message__srv__FullName_Request * data = NULL;

  if (size) {
    data = (full_name_message__srv__FullName_Request *)allocator.zero_allocate(size, sizeof(full_name_message__srv__FullName_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = full_name_message__srv__FullName_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        full_name_message__srv__FullName_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
full_name_message__srv__FullName_Request__Sequence__fini(full_name_message__srv__FullName_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      full_name_message__srv__FullName_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

full_name_message__srv__FullName_Request__Sequence *
full_name_message__srv__FullName_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  full_name_message__srv__FullName_Request__Sequence * array = (full_name_message__srv__FullName_Request__Sequence *)allocator.allocate(sizeof(full_name_message__srv__FullName_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = full_name_message__srv__FullName_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
full_name_message__srv__FullName_Request__Sequence__destroy(full_name_message__srv__FullName_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    full_name_message__srv__FullName_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
full_name_message__srv__FullName_Request__Sequence__are_equal(const full_name_message__srv__FullName_Request__Sequence * lhs, const full_name_message__srv__FullName_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!full_name_message__srv__FullName_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
full_name_message__srv__FullName_Request__Sequence__copy(
  const full_name_message__srv__FullName_Request__Sequence * input,
  full_name_message__srv__FullName_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(full_name_message__srv__FullName_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    full_name_message__srv__FullName_Request * data =
      (full_name_message__srv__FullName_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!full_name_message__srv__FullName_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          full_name_message__srv__FullName_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!full_name_message__srv__FullName_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `full_name`
// already included above
// #include "rosidl_runtime_c/string_functions.h"

bool
full_name_message__srv__FullName_Response__init(full_name_message__srv__FullName_Response * msg)
{
  if (!msg) {
    return false;
  }
  // full_name
  if (!rosidl_runtime_c__String__init(&msg->full_name)) {
    full_name_message__srv__FullName_Response__fini(msg);
    return false;
  }
  return true;
}

void
full_name_message__srv__FullName_Response__fini(full_name_message__srv__FullName_Response * msg)
{
  if (!msg) {
    return;
  }
  // full_name
  rosidl_runtime_c__String__fini(&msg->full_name);
}

bool
full_name_message__srv__FullName_Response__are_equal(const full_name_message__srv__FullName_Response * lhs, const full_name_message__srv__FullName_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // full_name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->full_name), &(rhs->full_name)))
  {
    return false;
  }
  return true;
}

bool
full_name_message__srv__FullName_Response__copy(
  const full_name_message__srv__FullName_Response * input,
  full_name_message__srv__FullName_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // full_name
  if (!rosidl_runtime_c__String__copy(
      &(input->full_name), &(output->full_name)))
  {
    return false;
  }
  return true;
}

full_name_message__srv__FullName_Response *
full_name_message__srv__FullName_Response__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  full_name_message__srv__FullName_Response * msg = (full_name_message__srv__FullName_Response *)allocator.allocate(sizeof(full_name_message__srv__FullName_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(full_name_message__srv__FullName_Response));
  bool success = full_name_message__srv__FullName_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
full_name_message__srv__FullName_Response__destroy(full_name_message__srv__FullName_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    full_name_message__srv__FullName_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
full_name_message__srv__FullName_Response__Sequence__init(full_name_message__srv__FullName_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  full_name_message__srv__FullName_Response * data = NULL;

  if (size) {
    data = (full_name_message__srv__FullName_Response *)allocator.zero_allocate(size, sizeof(full_name_message__srv__FullName_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = full_name_message__srv__FullName_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        full_name_message__srv__FullName_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
full_name_message__srv__FullName_Response__Sequence__fini(full_name_message__srv__FullName_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      full_name_message__srv__FullName_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

full_name_message__srv__FullName_Response__Sequence *
full_name_message__srv__FullName_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  full_name_message__srv__FullName_Response__Sequence * array = (full_name_message__srv__FullName_Response__Sequence *)allocator.allocate(sizeof(full_name_message__srv__FullName_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = full_name_message__srv__FullName_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
full_name_message__srv__FullName_Response__Sequence__destroy(full_name_message__srv__FullName_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    full_name_message__srv__FullName_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
full_name_message__srv__FullName_Response__Sequence__are_equal(const full_name_message__srv__FullName_Response__Sequence * lhs, const full_name_message__srv__FullName_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!full_name_message__srv__FullName_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
full_name_message__srv__FullName_Response__Sequence__copy(
  const full_name_message__srv__FullName_Response__Sequence * input,
  full_name_message__srv__FullName_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(full_name_message__srv__FullName_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    full_name_message__srv__FullName_Response * data =
      (full_name_message__srv__FullName_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!full_name_message__srv__FullName_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          full_name_message__srv__FullName_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!full_name_message__srv__FullName_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `info`
#include "service_msgs/msg/detail/service_event_info__functions.h"
// Member `request`
// Member `response`
// already included above
// #include "full_name_message/srv/detail/full_name__functions.h"

bool
full_name_message__srv__FullName_Event__init(full_name_message__srv__FullName_Event * msg)
{
  if (!msg) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__init(&msg->info)) {
    full_name_message__srv__FullName_Event__fini(msg);
    return false;
  }
  // request
  if (!full_name_message__srv__FullName_Request__Sequence__init(&msg->request, 0)) {
    full_name_message__srv__FullName_Event__fini(msg);
    return false;
  }
  // response
  if (!full_name_message__srv__FullName_Response__Sequence__init(&msg->response, 0)) {
    full_name_message__srv__FullName_Event__fini(msg);
    return false;
  }
  return true;
}

void
full_name_message__srv__FullName_Event__fini(full_name_message__srv__FullName_Event * msg)
{
  if (!msg) {
    return;
  }
  // info
  service_msgs__msg__ServiceEventInfo__fini(&msg->info);
  // request
  full_name_message__srv__FullName_Request__Sequence__fini(&msg->request);
  // response
  full_name_message__srv__FullName_Response__Sequence__fini(&msg->response);
}

bool
full_name_message__srv__FullName_Event__are_equal(const full_name_message__srv__FullName_Event * lhs, const full_name_message__srv__FullName_Event * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__are_equal(
      &(lhs->info), &(rhs->info)))
  {
    return false;
  }
  // request
  if (!full_name_message__srv__FullName_Request__Sequence__are_equal(
      &(lhs->request), &(rhs->request)))
  {
    return false;
  }
  // response
  if (!full_name_message__srv__FullName_Response__Sequence__are_equal(
      &(lhs->response), &(rhs->response)))
  {
    return false;
  }
  return true;
}

bool
full_name_message__srv__FullName_Event__copy(
  const full_name_message__srv__FullName_Event * input,
  full_name_message__srv__FullName_Event * output)
{
  if (!input || !output) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__copy(
      &(input->info), &(output->info)))
  {
    return false;
  }
  // request
  if (!full_name_message__srv__FullName_Request__Sequence__copy(
      &(input->request), &(output->request)))
  {
    return false;
  }
  // response
  if (!full_name_message__srv__FullName_Response__Sequence__copy(
      &(input->response), &(output->response)))
  {
    return false;
  }
  return true;
}

full_name_message__srv__FullName_Event *
full_name_message__srv__FullName_Event__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  full_name_message__srv__FullName_Event * msg = (full_name_message__srv__FullName_Event *)allocator.allocate(sizeof(full_name_message__srv__FullName_Event), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(full_name_message__srv__FullName_Event));
  bool success = full_name_message__srv__FullName_Event__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
full_name_message__srv__FullName_Event__destroy(full_name_message__srv__FullName_Event * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    full_name_message__srv__FullName_Event__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
full_name_message__srv__FullName_Event__Sequence__init(full_name_message__srv__FullName_Event__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  full_name_message__srv__FullName_Event * data = NULL;

  if (size) {
    data = (full_name_message__srv__FullName_Event *)allocator.zero_allocate(size, sizeof(full_name_message__srv__FullName_Event), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = full_name_message__srv__FullName_Event__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        full_name_message__srv__FullName_Event__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
full_name_message__srv__FullName_Event__Sequence__fini(full_name_message__srv__FullName_Event__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      full_name_message__srv__FullName_Event__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

full_name_message__srv__FullName_Event__Sequence *
full_name_message__srv__FullName_Event__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  full_name_message__srv__FullName_Event__Sequence * array = (full_name_message__srv__FullName_Event__Sequence *)allocator.allocate(sizeof(full_name_message__srv__FullName_Event__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = full_name_message__srv__FullName_Event__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
full_name_message__srv__FullName_Event__Sequence__destroy(full_name_message__srv__FullName_Event__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    full_name_message__srv__FullName_Event__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
full_name_message__srv__FullName_Event__Sequence__are_equal(const full_name_message__srv__FullName_Event__Sequence * lhs, const full_name_message__srv__FullName_Event__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!full_name_message__srv__FullName_Event__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
full_name_message__srv__FullName_Event__Sequence__copy(
  const full_name_message__srv__FullName_Event__Sequence * input,
  full_name_message__srv__FullName_Event__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(full_name_message__srv__FullName_Event);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    full_name_message__srv__FullName_Event * data =
      (full_name_message__srv__FullName_Event *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!full_name_message__srv__FullName_Event__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          full_name_message__srv__FullName_Event__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!full_name_message__srv__FullName_Event__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
