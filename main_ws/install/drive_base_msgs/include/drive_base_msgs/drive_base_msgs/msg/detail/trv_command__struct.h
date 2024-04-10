// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from drive_base_msgs:msg/TRVCommand.idl
// generated code does not contain a copyright notice

#ifndef DRIVE_BASE_MSGS__MSG__DETAIL__TRV_COMMAND__STRUCT_H_
#define DRIVE_BASE_MSGS__MSG__DETAIL__TRV_COMMAND__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "drive_base_msgs/msg/detail/command_header__struct.h"

/// Struct defined in msg/TRVCommand in the package drive_base_msgs.
/**
  * Command a mobile base by Translational and Rotational Velocity
  * Primarily intended for differential drive bases.
 */
typedef struct drive_base_msgs__msg__TRVCommand
{
  drive_base_msgs__msg__CommandHeader header;
  float translational_velocity;
  float rotational_velocity;
} drive_base_msgs__msg__TRVCommand;

// Struct for a sequence of drive_base_msgs__msg__TRVCommand.
typedef struct drive_base_msgs__msg__TRVCommand__Sequence
{
  drive_base_msgs__msg__TRVCommand * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} drive_base_msgs__msg__TRVCommand__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DRIVE_BASE_MSGS__MSG__DETAIL__TRV_COMMAND__STRUCT_H_
