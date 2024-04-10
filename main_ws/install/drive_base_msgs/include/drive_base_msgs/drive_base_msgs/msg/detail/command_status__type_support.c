// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from drive_base_msgs:msg/CommandStatus.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "drive_base_msgs/msg/detail/command_status__rosidl_typesupport_introspection_c.h"
#include "drive_base_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "drive_base_msgs/msg/detail/command_status__functions.h"
#include "drive_base_msgs/msg/detail/command_status__struct.h"


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/time.h"
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__rosidl_typesupport_introspection_c.h"
// Member `cmd_header`
#include "drive_base_msgs/msg/command_header.h"
// Member `cmd_header`
#include "drive_base_msgs/msg/detail/command_header__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void drive_base_msgs__msg__CommandStatus__rosidl_typesupport_introspection_c__CommandStatus_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  drive_base_msgs__msg__CommandStatus__init(message_memory);
}

void drive_base_msgs__msg__CommandStatus__rosidl_typesupport_introspection_c__CommandStatus_fini_function(void * message_memory)
{
  drive_base_msgs__msg__CommandStatus__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember drive_base_msgs__msg__CommandStatus__rosidl_typesupport_introspection_c__CommandStatus_message_member_array[3] = {
  {
    "stamp",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drive_base_msgs__msg__CommandStatus, stamp),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "cmd_header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drive_base_msgs__msg__CommandStatus, cmd_header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "status",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drive_base_msgs__msg__CommandStatus, status),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers drive_base_msgs__msg__CommandStatus__rosidl_typesupport_introspection_c__CommandStatus_message_members = {
  "drive_base_msgs__msg",  // message namespace
  "CommandStatus",  // message name
  3,  // number of fields
  sizeof(drive_base_msgs__msg__CommandStatus),
  drive_base_msgs__msg__CommandStatus__rosidl_typesupport_introspection_c__CommandStatus_message_member_array,  // message members
  drive_base_msgs__msg__CommandStatus__rosidl_typesupport_introspection_c__CommandStatus_init_function,  // function to initialize message memory (memory has to be allocated)
  drive_base_msgs__msg__CommandStatus__rosidl_typesupport_introspection_c__CommandStatus_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t drive_base_msgs__msg__CommandStatus__rosidl_typesupport_introspection_c__CommandStatus_message_type_support_handle = {
  0,
  &drive_base_msgs__msg__CommandStatus__rosidl_typesupport_introspection_c__CommandStatus_message_members,
  get_message_typesupport_handle_function,
  &drive_base_msgs__msg__CommandStatus__get_type_hash,
  &drive_base_msgs__msg__CommandStatus__get_type_description,
  &drive_base_msgs__msg__CommandStatus__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_drive_base_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, drive_base_msgs, msg, CommandStatus)() {
  drive_base_msgs__msg__CommandStatus__rosidl_typesupport_introspection_c__CommandStatus_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, builtin_interfaces, msg, Time)();
  drive_base_msgs__msg__CommandStatus__rosidl_typesupport_introspection_c__CommandStatus_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, drive_base_msgs, msg, CommandHeader)();
  if (!drive_base_msgs__msg__CommandStatus__rosidl_typesupport_introspection_c__CommandStatus_message_type_support_handle.typesupport_identifier) {
    drive_base_msgs__msg__CommandStatus__rosidl_typesupport_introspection_c__CommandStatus_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &drive_base_msgs__msg__CommandStatus__rosidl_typesupport_introspection_c__CommandStatus_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
