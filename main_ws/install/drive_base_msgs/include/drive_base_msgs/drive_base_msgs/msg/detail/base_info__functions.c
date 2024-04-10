// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from drive_base_msgs:msg/BaseInfo.idl
// generated code does not contain a copyright notice
#include "drive_base_msgs/msg/detail/base_info__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__functions.h"

bool
drive_base_msgs__msg__BaseInfo__init(drive_base_msgs__msg__BaseInfo * msg)
{
  if (!msg) {
    return false;
  }
  // hw_id
  // hw_timestamp
  // stamp
  if (!builtin_interfaces__msg__Time__init(&msg->stamp)) {
    drive_base_msgs__msg__BaseInfo__fini(msg);
    return false;
  }
  // x
  // y
  // orientation
  // forward_velocity
  // rotational_velocity
  // battery_voltage_pct
  // power_supply
  // overcurrent
  // blocked
  // in_collision
  // at_cliff
  // safety_state
  return true;
}

void
drive_base_msgs__msg__BaseInfo__fini(drive_base_msgs__msg__BaseInfo * msg)
{
  if (!msg) {
    return;
  }
  // hw_id
  // hw_timestamp
  // stamp
  builtin_interfaces__msg__Time__fini(&msg->stamp);
  // x
  // y
  // orientation
  // forward_velocity
  // rotational_velocity
  // battery_voltage_pct
  // power_supply
  // overcurrent
  // blocked
  // in_collision
  // at_cliff
  // safety_state
}

bool
drive_base_msgs__msg__BaseInfo__are_equal(const drive_base_msgs__msg__BaseInfo * lhs, const drive_base_msgs__msg__BaseInfo * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // hw_id
  if (lhs->hw_id != rhs->hw_id) {
    return false;
  }
  // hw_timestamp
  if (lhs->hw_timestamp != rhs->hw_timestamp) {
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__are_equal(
      &(lhs->stamp), &(rhs->stamp)))
  {
    return false;
  }
  // x
  if (lhs->x != rhs->x) {
    return false;
  }
  // y
  if (lhs->y != rhs->y) {
    return false;
  }
  // orientation
  if (lhs->orientation != rhs->orientation) {
    return false;
  }
  // forward_velocity
  if (lhs->forward_velocity != rhs->forward_velocity) {
    return false;
  }
  // rotational_velocity
  if (lhs->rotational_velocity != rhs->rotational_velocity) {
    return false;
  }
  // battery_voltage_pct
  if (lhs->battery_voltage_pct != rhs->battery_voltage_pct) {
    return false;
  }
  // power_supply
  if (lhs->power_supply != rhs->power_supply) {
    return false;
  }
  // overcurrent
  if (lhs->overcurrent != rhs->overcurrent) {
    return false;
  }
  // blocked
  if (lhs->blocked != rhs->blocked) {
    return false;
  }
  // in_collision
  if (lhs->in_collision != rhs->in_collision) {
    return false;
  }
  // at_cliff
  if (lhs->at_cliff != rhs->at_cliff) {
    return false;
  }
  // safety_state
  if (lhs->safety_state != rhs->safety_state) {
    return false;
  }
  return true;
}

bool
drive_base_msgs__msg__BaseInfo__copy(
  const drive_base_msgs__msg__BaseInfo * input,
  drive_base_msgs__msg__BaseInfo * output)
{
  if (!input || !output) {
    return false;
  }
  // hw_id
  output->hw_id = input->hw_id;
  // hw_timestamp
  output->hw_timestamp = input->hw_timestamp;
  // stamp
  if (!builtin_interfaces__msg__Time__copy(
      &(input->stamp), &(output->stamp)))
  {
    return false;
  }
  // x
  output->x = input->x;
  // y
  output->y = input->y;
  // orientation
  output->orientation = input->orientation;
  // forward_velocity
  output->forward_velocity = input->forward_velocity;
  // rotational_velocity
  output->rotational_velocity = input->rotational_velocity;
  // battery_voltage_pct
  output->battery_voltage_pct = input->battery_voltage_pct;
  // power_supply
  output->power_supply = input->power_supply;
  // overcurrent
  output->overcurrent = input->overcurrent;
  // blocked
  output->blocked = input->blocked;
  // in_collision
  output->in_collision = input->in_collision;
  // at_cliff
  output->at_cliff = input->at_cliff;
  // safety_state
  output->safety_state = input->safety_state;
  return true;
}

drive_base_msgs__msg__BaseInfo *
drive_base_msgs__msg__BaseInfo__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  drive_base_msgs__msg__BaseInfo * msg = (drive_base_msgs__msg__BaseInfo *)allocator.allocate(sizeof(drive_base_msgs__msg__BaseInfo), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(drive_base_msgs__msg__BaseInfo));
  bool success = drive_base_msgs__msg__BaseInfo__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
drive_base_msgs__msg__BaseInfo__destroy(drive_base_msgs__msg__BaseInfo * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    drive_base_msgs__msg__BaseInfo__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
drive_base_msgs__msg__BaseInfo__Sequence__init(drive_base_msgs__msg__BaseInfo__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  drive_base_msgs__msg__BaseInfo * data = NULL;

  if (size) {
    data = (drive_base_msgs__msg__BaseInfo *)allocator.zero_allocate(size, sizeof(drive_base_msgs__msg__BaseInfo), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = drive_base_msgs__msg__BaseInfo__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        drive_base_msgs__msg__BaseInfo__fini(&data[i - 1]);
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
drive_base_msgs__msg__BaseInfo__Sequence__fini(drive_base_msgs__msg__BaseInfo__Sequence * array)
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
      drive_base_msgs__msg__BaseInfo__fini(&array->data[i]);
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

drive_base_msgs__msg__BaseInfo__Sequence *
drive_base_msgs__msg__BaseInfo__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  drive_base_msgs__msg__BaseInfo__Sequence * array = (drive_base_msgs__msg__BaseInfo__Sequence *)allocator.allocate(sizeof(drive_base_msgs__msg__BaseInfo__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = drive_base_msgs__msg__BaseInfo__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
drive_base_msgs__msg__BaseInfo__Sequence__destroy(drive_base_msgs__msg__BaseInfo__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    drive_base_msgs__msg__BaseInfo__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
drive_base_msgs__msg__BaseInfo__Sequence__are_equal(const drive_base_msgs__msg__BaseInfo__Sequence * lhs, const drive_base_msgs__msg__BaseInfo__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!drive_base_msgs__msg__BaseInfo__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
drive_base_msgs__msg__BaseInfo__Sequence__copy(
  const drive_base_msgs__msg__BaseInfo__Sequence * input,
  drive_base_msgs__msg__BaseInfo__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(drive_base_msgs__msg__BaseInfo);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    drive_base_msgs__msg__BaseInfo * data =
      (drive_base_msgs__msg__BaseInfo *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!drive_base_msgs__msg__BaseInfo__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          drive_base_msgs__msg__BaseInfo__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!drive_base_msgs__msg__BaseInfo__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
