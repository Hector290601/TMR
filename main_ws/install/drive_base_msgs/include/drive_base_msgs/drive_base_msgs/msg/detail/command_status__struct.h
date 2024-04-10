// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from drive_base_msgs:msg/CommandStatus.idl
// generated code does not contain a copyright notice

#ifndef DRIVE_BASE_MSGS__MSG__DETAIL__COMMAND_STATUS__STRUCT_H_
#define DRIVE_BASE_MSGS__MSG__DETAIL__COMMAND_STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Constant 'OK'.
enum
{
  drive_base_msgs__msg__CommandStatus__OK = 0
};

/// Constant 'CAPABILITIES_EXCEEDED'.
/**
  * the command contained requests that exceed the capabilities of the system
  * e.g., the command speed was too high
  * NOTE: The system will still attempt to perform as best it can
 */
enum
{
  drive_base_msgs__msg__CommandStatus__CAPABILITIES_EXCEEDED = 1
};

/// Constant 'INVALID'.
/**
  * the command contained invalid values, and the system will not attempt
  * to perform it
 */
enum
{
  drive_base_msgs__msg__CommandStatus__INVALID = 2
};

/// Constant 'POWER_INSUFFICIENT'.
/**
  * the command cannot be executed because the system has insufficient power to operate
 */
enum
{
  drive_base_msgs__msg__CommandStatus__POWER_INSUFFICIENT = 3
};

/// Constant 'TEMPORARY_FAILURE'.
/**
  * the system is currently inoperational for an unspecified reason
  * it expects to be able to recover
 */
enum
{
  drive_base_msgs__msg__CommandStatus__TEMPORARY_FAILURE = 4
};

/// Constant 'SYSTEM_FAILURE'.
/**
  * the system is inoperational indefinitely
 */
enum
{
  drive_base_msgs__msg__CommandStatus__SYSTEM_FAILURE = 5
};

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"
// Member 'cmd_header'
#include "drive_base_msgs/msg/detail/command_header__struct.h"

/// Struct defined in msg/CommandStatus in the package drive_base_msgs.
/**
  * command has been accepted
 */
typedef struct drive_base_msgs__msg__CommandStatus
{
  /// timestamp of this message
  builtin_interfaces__msg__Time stamp;
  /// command this pertains to
  drive_base_msgs__msg__CommandHeader cmd_header;
  /// result of the command
  uint8_t status;
} drive_base_msgs__msg__CommandStatus;

// Struct for a sequence of drive_base_msgs__msg__CommandStatus.
typedef struct drive_base_msgs__msg__CommandStatus__Sequence
{
  drive_base_msgs__msg__CommandStatus * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} drive_base_msgs__msg__CommandStatus__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DRIVE_BASE_MSGS__MSG__DETAIL__COMMAND_STATUS__STRUCT_H_
