// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from drive_base_msgs:msg/TRVCommand.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "drive_base_msgs/msg/detail/trv_command__functions.h"
#include "drive_base_msgs/msg/detail/trv_command__struct.hpp"
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

void TRVCommand_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) drive_base_msgs::msg::TRVCommand(_init);
}

void TRVCommand_fini_function(void * message_memory)
{
  auto typed_message = static_cast<drive_base_msgs::msg::TRVCommand *>(message_memory);
  typed_message->~TRVCommand();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember TRVCommand_message_member_array[3] = {
  {
    "header",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<drive_base_msgs::msg::CommandHeader>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drive_base_msgs::msg::TRVCommand, header),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "translational_velocity",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drive_base_msgs::msg::TRVCommand, translational_velocity),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "rotational_velocity",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drive_base_msgs::msg::TRVCommand, rotational_velocity),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers TRVCommand_message_members = {
  "drive_base_msgs::msg",  // message namespace
  "TRVCommand",  // message name
  3,  // number of fields
  sizeof(drive_base_msgs::msg::TRVCommand),
  TRVCommand_message_member_array,  // message members
  TRVCommand_init_function,  // function to initialize message memory (memory has to be allocated)
  TRVCommand_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t TRVCommand_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &TRVCommand_message_members,
  get_message_typesupport_handle_function,
  &drive_base_msgs__msg__TRVCommand__get_type_hash,
  &drive_base_msgs__msg__TRVCommand__get_type_description,
  &drive_base_msgs__msg__TRVCommand__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace drive_base_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<drive_base_msgs::msg::TRVCommand>()
{
  return &::drive_base_msgs::msg::rosidl_typesupport_introspection_cpp::TRVCommand_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, drive_base_msgs, msg, TRVCommand)() {
  return &::drive_base_msgs::msg::rosidl_typesupport_introspection_cpp::TRVCommand_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
