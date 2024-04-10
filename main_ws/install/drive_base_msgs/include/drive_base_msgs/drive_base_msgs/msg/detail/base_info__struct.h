// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from drive_base_msgs:msg/BaseInfo.idl
// generated code does not contain a copyright notice

#ifndef DRIVE_BASE_MSGS__MSG__DETAIL__BASE_INFO__STRUCT_H_
#define DRIVE_BASE_MSGS__MSG__DETAIL__BASE_INFO__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Constant 'POWER_SUPPLY_STATUS_UNKNOWN'.
enum
{
  drive_base_msgs__msg__BaseInfo__POWER_SUPPLY_STATUS_UNKNOWN = 0
};

/// Constant 'POWER_SUPPLY_STATUS_CHARGING'.
enum
{
  drive_base_msgs__msg__BaseInfo__POWER_SUPPLY_STATUS_CHARGING = 1
};

/// Constant 'POWER_SUPPLY_STATUS_DISCHARGING'.
enum
{
  drive_base_msgs__msg__BaseInfo__POWER_SUPPLY_STATUS_DISCHARGING = 2
};

/// Constant 'POWER_SUPPLY_STATUS_NOT_CHARGING'.
enum
{
  drive_base_msgs__msg__BaseInfo__POWER_SUPPLY_STATUS_NOT_CHARGING = 3
};

/// Constant 'POWER_SUPPLY_STATUS_FULL'.
enum
{
  drive_base_msgs__msg__BaseInfo__POWER_SUPPLY_STATUS_FULL = 4
};

/// Constant 'SAFETY_STATE_OPERATIONAL'.
/**
  * OR'able bits to communicate current safety state as determined by base sensors
 */
enum
{
  drive_base_msgs__msg__BaseInfo__SAFETY_STATE_OPERATIONAL = 1
};

/// Constant 'SAFETY_STATE_LOW_SPEED'.
enum
{
  drive_base_msgs__msg__BaseInfo__SAFETY_STATE_LOW_SPEED = 2
};

/// Constant 'SAFETY_STATE_NO_FORWARD'.
enum
{
  drive_base_msgs__msg__BaseInfo__SAFETY_STATE_NO_FORWARD = 4
};

/// Constant 'SAFETY_STATE_NO_BACKWARD'.
enum
{
  drive_base_msgs__msg__BaseInfo__SAFETY_STATE_NO_BACKWARD = 8
};

/// Constant 'SAFETY_STATE_NO_ROTATE'.
enum
{
  drive_base_msgs__msg__BaseInfo__SAFETY_STATE_NO_ROTATE = 16
};

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in msg/BaseInfo in the package drive_base_msgs.
typedef struct drive_base_msgs__msg__BaseInfo
{
  /// identifying information
  /// a, hopefully unique, id
  uint32_t hw_id;
  /// timestamp as returned by the hardware
  uint32_t hw_timestamp;
  /// wall clock timestamp
  builtin_interfaces__msg__Time stamp;
  /// position information (estimated, relative to starting pose)
  float x;
  float y;
  float orientation;
  /// should we add z?
  /// velocity information
  float forward_velocity;
  float rotational_velocity;
  /// battery state
  /// range: 0-100. current battery voltage as percent of nominal.
  uint8_t battery_voltage_pct;
  /// one of the constants above
  uint8_t power_supply;
  /// diagnostic information
  /// motor overcurrent detected
  bool overcurrent;
  /// True if forward direction is blocked by an obstacle
  bool blocked;
  /// True if the robot is in collision (usually detected via bumper)
  bool in_collision;
  /// True if the robot has detected a cliff in the forward direction
  bool at_cliff;
  uint16_t safety_state;
} drive_base_msgs__msg__BaseInfo;

// Struct for a sequence of drive_base_msgs__msg__BaseInfo.
typedef struct drive_base_msgs__msg__BaseInfo__Sequence
{
  drive_base_msgs__msg__BaseInfo * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} drive_base_msgs__msg__BaseInfo__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DRIVE_BASE_MSGS__MSG__DETAIL__BASE_INFO__STRUCT_H_
