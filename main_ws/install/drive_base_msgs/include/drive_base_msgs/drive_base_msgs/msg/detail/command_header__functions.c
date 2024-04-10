// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from drive_base_msgs:msg/CommandHeader.idl
// generated code does not contain a copyright notice
#include "drive_base_msgs/msg/detail/command_header__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__functions.h"

bool
drive_base_msgs__msg__CommandHeader__init(drive_base_msgs__msg__CommandHeader * msg)
{
  if (!msg) {
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__init(&msg->stamp)) {
    drive_base_msgs__msg__CommandHeader__fini(msg);
    return false;
  }
  // command_id
  // expected_period
  return true;
}

void
drive_base_msgs__msg__CommandHeader__fini(drive_base_msgs__msg__CommandHeader * msg)
{
  if (!msg) {
    return;
  }
  // stamp
  builtin_interfaces__msg__Time__fini(&msg->stamp);
  // command_id
  // expected_period
}

bool
drive_base_msgs__msg__CommandHeader__are_equal(const drive_base_msgs__msg__CommandHeader * lhs, const drive_base_msgs__msg__CommandHeader * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__are_equal(
      &(lhs->stamp), &(rhs->stamp)))
  {
    return false;
  }
  // command_id
  if (lhs->command_id != rhs->command_id) {
    return false;
  }
  // expected_period
  if (lhs->expected_period != rhs->expected_period) {
    return false;
  }
  return true;
}

bool
drive_base_msgs__msg__CommandHeader__copy(
  const drive_base_msgs__msg__CommandHeader * input,
  drive_base_msgs__msg__CommandHeader * output)
{
  if (!input || !output) {
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__copy(
      &(input->stamp), &(output->stamp)))
  {
    return false;
  }
  // command_id
  output->command_id = input->command_id;
  // expected_period
  output->expected_period = input->expected_period;
  return true;
}

drive_base_msgs__msg__CommandHeader *
drive_base_msgs__msg__CommandHeader__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  drive_base_msgs__msg__CommandHeader * msg = (drive_base_msgs__msg__CommandHeader *)allocator.allocate(sizeof(drive_base_msgs__msg__CommandHeader), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(drive_base_msgs__msg__CommandHeader));
  bool success = drive_base_msgs__msg__CommandHeader__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
drive_base_msgs__msg__CommandHeader__destroy(drive_base_msgs__msg__CommandHeader * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    drive_base_msgs__msg__CommandHeader__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
drive_base_msgs__msg__CommandHeader__Sequence__init(drive_base_msgs__msg__CommandHeader__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  drive_base_msgs__msg__CommandHeader * data = NULL;

  if (size) {
    data = (drive_base_msgs__msg__CommandHeader *)allocator.zero_allocate(size, sizeof(drive_base_msgs__msg__CommandHeader), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = drive_base_msgs__msg__CommandHeader__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        drive_base_msgs__msg__CommandHeader__fini(&data[i - 1]);
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
drive_base_msgs__msg__CommandHeader__Sequence__fini(drive_base_msgs__msg__CommandHeader__Sequence * array)
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
      drive_base_msgs__msg__CommandHeader__fini(&array->data[i]);
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

drive_base_msgs__msg__CommandHeader__Sequence *
drive_base_msgs__msg__CommandHeader__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  drive_base_msgs__msg__CommandHeader__Sequence * array = (drive_base_msgs__msg__CommandHeader__Sequence *)allocator.allocate(sizeof(drive_base_msgs__msg__CommandHeader__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = drive_base_msgs__msg__CommandHeader__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
drive_base_msgs__msg__CommandHeader__Sequence__destroy(drive_base_msgs__msg__CommandHeader__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    drive_base_msgs__msg__CommandHeader__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
drive_base_msgs__msg__CommandHeader__Sequence__are_equal(const drive_base_msgs__msg__CommandHeader__Sequence * lhs, const drive_base_msgs__msg__CommandHeader__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!drive_base_msgs__msg__CommandHeader__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
drive_base_msgs__msg__CommandHeader__Sequence__copy(
  const drive_base_msgs__msg__CommandHeader__Sequence * input,
  drive_base_msgs__msg__CommandHeader__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(drive_base_msgs__msg__CommandHeader);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    drive_base_msgs__msg__CommandHeader * data =
      (drive_base_msgs__msg__CommandHeader *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!drive_base_msgs__msg__CommandHeader__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          drive_base_msgs__msg__CommandHeader__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!drive_base_msgs__msg__CommandHeader__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
