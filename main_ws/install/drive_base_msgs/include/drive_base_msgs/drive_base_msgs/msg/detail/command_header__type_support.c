// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from drive_base_msgs:msg/CommandHeader.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "drive_base_msgs/msg/detail/command_header__rosidl_typesupport_introspection_c.h"
#include "drive_base_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "drive_base_msgs/msg/detail/command_header__functions.h"
#include "drive_base_msgs/msg/detail/command_header__struct.h"


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/time.h"
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void drive_base_msgs__msg__CommandHeader__rosidl_typesupport_introspection_c__CommandHeader_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  drive_base_msgs__msg__CommandHeader__init(message_memory);
}

void drive_base_msgs__msg__CommandHeader__rosidl_typesupport_introspection_c__CommandHeader_fini_function(void * message_memory)
{
  drive_base_msgs__msg__CommandHeader__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember drive_base_msgs__msg__CommandHeader__rosidl_typesupport_introspection_c__CommandHeader_message_member_array[3] = {
  {
    "stamp",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drive_base_msgs__msg__CommandHeader, stamp),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "command_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drive_base_msgs__msg__CommandHeader, command_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "expected_period",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drive_base_msgs__msg__CommandHeader, expected_period),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers drive_base_msgs__msg__CommandHeader__rosidl_typesupport_introspection_c__CommandHeader_message_members = {
  "drive_base_msgs__msg",  // message namespace
  "CommandHeader",  // message name
  3,  // number of fields
  sizeof(drive_base_msgs__msg__CommandHeader),
  drive_base_msgs__msg__CommandHeader__rosidl_typesupport_introspection_c__CommandHeader_message_member_array,  // message members
  drive_base_msgs__msg__CommandHeader__rosidl_typesupport_introspection_c__CommandHeader_init_function,  // function to initialize message memory (memory has to be allocated)
  drive_base_msgs__msg__CommandHeader__rosidl_typesupport_introspection_c__CommandHeader_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t drive_base_msgs__msg__CommandHeader__rosidl_typesupport_introspection_c__CommandHeader_message_type_support_handle = {
  0,
  &drive_base_msgs__msg__CommandHeader__rosidl_typesupport_introspection_c__CommandHeader_message_members,
  get_message_typesupport_handle_function,
  &drive_base_msgs__msg__CommandHeader__get_type_hash,
  &drive_base_msgs__msg__CommandHeader__get_type_description,
  &drive_base_msgs__msg__CommandHeader__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_drive_base_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, drive_base_msgs, msg, CommandHeader)() {
  drive_base_msgs__msg__CommandHeader__rosidl_typesupport_introspection_c__CommandHeader_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, builtin_interfaces, msg, Time)();
  if (!drive_base_msgs__msg__CommandHeader__rosidl_typesupport_introspection_c__CommandHeader_message_type_support_handle.typesupport_identifier) {
    drive_base_msgs__msg__CommandHeader__rosidl_typesupport_introspection_c__CommandHeader_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &drive_base_msgs__msg__CommandHeader__rosidl_typesupport_introspection_c__CommandHeader_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
