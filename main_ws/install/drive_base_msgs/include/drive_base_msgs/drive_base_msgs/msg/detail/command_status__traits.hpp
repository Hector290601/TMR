// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from drive_base_msgs:msg/CommandStatus.idl
// generated code does not contain a copyright notice

#ifndef DRIVE_BASE_MSGS__MSG__DETAIL__COMMAND_STATUS__TRAITS_HPP_
#define DRIVE_BASE_MSGS__MSG__DETAIL__COMMAND_STATUS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "drive_base_msgs/msg/detail/command_status__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"
// Member 'cmd_header'
#include "drive_base_msgs/msg/detail/command_header__traits.hpp"

namespace drive_base_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const CommandStatus & msg,
  std::ostream & out)
{
  out << "{";
  // member: stamp
  {
    out << "stamp: ";
    to_flow_style_yaml(msg.stamp, out);
    out << ", ";
  }

  // member: cmd_header
  {
    out << "cmd_header: ";
    to_flow_style_yaml(msg.cmd_header, out);
    out << ", ";
  }

  // member: status
  {
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const CommandStatus & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: stamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "stamp:\n";
    to_block_style_yaml(msg.stamp, out, indentation + 2);
  }

  // member: cmd_header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "cmd_header:\n";
    to_block_style_yaml(msg.cmd_header, out, indentation + 2);
  }

  // member: status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const CommandStatus & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace drive_base_msgs

namespace rosidl_generator_traits
{

[[deprecated("use drive_base_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const drive_base_msgs::msg::CommandStatus & msg,
  std::ostream & out, size_t indentation = 0)
{
  drive_base_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use drive_base_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const drive_base_msgs::msg::CommandStatus & msg)
{
  return drive_base_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<drive_base_msgs::msg::CommandStatus>()
{
  return "drive_base_msgs::msg::CommandStatus";
}

template<>
inline const char * name<drive_base_msgs::msg::CommandStatus>()
{
  return "drive_base_msgs/msg/CommandStatus";
}

template<>
struct has_fixed_size<drive_base_msgs::msg::CommandStatus>
  : std::integral_constant<bool, has_fixed_size<builtin_interfaces::msg::Time>::value && has_fixed_size<drive_base_msgs::msg::CommandHeader>::value> {};

template<>
struct has_bounded_size<drive_base_msgs::msg::CommandStatus>
  : std::integral_constant<bool, has_bounded_size<builtin_interfaces::msg::Time>::value && has_bounded_size<drive_base_msgs::msg::CommandHeader>::value> {};

template<>
struct is_message<drive_base_msgs::msg::CommandStatus>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // DRIVE_BASE_MSGS__MSG__DETAIL__COMMAND_STATUS__TRAITS_HPP_
