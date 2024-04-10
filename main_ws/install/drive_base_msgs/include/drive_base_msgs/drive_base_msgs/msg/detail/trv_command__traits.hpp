// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from drive_base_msgs:msg/TRVCommand.idl
// generated code does not contain a copyright notice

#ifndef DRIVE_BASE_MSGS__MSG__DETAIL__TRV_COMMAND__TRAITS_HPP_
#define DRIVE_BASE_MSGS__MSG__DETAIL__TRV_COMMAND__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "drive_base_msgs/msg/detail/trv_command__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "drive_base_msgs/msg/detail/command_header__traits.hpp"

namespace drive_base_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const TRVCommand & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: translational_velocity
  {
    out << "translational_velocity: ";
    rosidl_generator_traits::value_to_yaml(msg.translational_velocity, out);
    out << ", ";
  }

  // member: rotational_velocity
  {
    out << "rotational_velocity: ";
    rosidl_generator_traits::value_to_yaml(msg.rotational_velocity, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const TRVCommand & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: translational_velocity
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "translational_velocity: ";
    rosidl_generator_traits::value_to_yaml(msg.translational_velocity, out);
    out << "\n";
  }

  // member: rotational_velocity
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rotational_velocity: ";
    rosidl_generator_traits::value_to_yaml(msg.rotational_velocity, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const TRVCommand & msg, bool use_flow_style = false)
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
  const drive_base_msgs::msg::TRVCommand & msg,
  std::ostream & out, size_t indentation = 0)
{
  drive_base_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use drive_base_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const drive_base_msgs::msg::TRVCommand & msg)
{
  return drive_base_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<drive_base_msgs::msg::TRVCommand>()
{
  return "drive_base_msgs::msg::TRVCommand";
}

template<>
inline const char * name<drive_base_msgs::msg::TRVCommand>()
{
  return "drive_base_msgs/msg/TRVCommand";
}

template<>
struct has_fixed_size<drive_base_msgs::msg::TRVCommand>
  : std::integral_constant<bool, has_fixed_size<drive_base_msgs::msg::CommandHeader>::value> {};

template<>
struct has_bounded_size<drive_base_msgs::msg::TRVCommand>
  : std::integral_constant<bool, has_bounded_size<drive_base_msgs::msg::CommandHeader>::value> {};

template<>
struct is_message<drive_base_msgs::msg::TRVCommand>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // DRIVE_BASE_MSGS__MSG__DETAIL__TRV_COMMAND__TRAITS_HPP_
