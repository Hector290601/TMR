// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from drive_base_msgs:msg/CommandStatus.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "drive_base_msgs/msg/detail/command_status__functions.h"
#include "drive_base_msgs/msg/detail/command_status__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace drive_base_msgs
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void CommandStatus_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) drive_base_msgs::msg::CommandStatus(_init);
}

void CommandStatus_fini_function(void * message_memory)
{
  auto typed_message = static_cast<drive_base_msgs::msg::CommandStatus *>(message_memory);
  typed_message->~CommandStatus();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember CommandStatus_message_member_array[3] = {
  {
    "stamp",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<builtin_interfaces::msg::Time>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drive_base_msgs::msg::CommandStatus, stamp),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "cmd_header",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<drive_base_msgs::msg::CommandHeader>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drive_base_msgs::msg::CommandStatus, cmd_header),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "status",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drive_base_msgs::msg::CommandStatus, status),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers CommandStatus_message_members = {
  "drive_base_msgs::msg",  // message namespace
  "CommandStatus",  // message name
  3,  // number of fields
  sizeof(drive_base_msgs::msg::CommandStatus),
  CommandStatus_message_member_array,  // message members
  CommandStatus_init_function,  // function to initialize message memory (memory has to be allocated)
  CommandStatus_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t CommandStatus_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &CommandStatus_message_members,
  get_message_typesupport_handle_function,
  &drive_base_msgs__msg__CommandStatus__get_type_hash,
  &drive_base_msgs__msg__CommandStatus__get_type_description,
  &drive_base_msgs__msg__CommandStatus__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace drive_base_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<drive_base_msgs::msg::CommandStatus>()
{
  return &::drive_base_msgs::msg::rosidl_typesupport_introspection_cpp::CommandStatus_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, drive_base_msgs, msg, CommandStatus)() {
  return &::drive_base_msgs::msg::rosidl_typesupport_introspection_cpp::CommandStatus_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
