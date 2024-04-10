// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from drive_base_msgs:msg/BaseInfo.idl
// generated code does not contain a copyright notice

#ifndef DRIVE_BASE_MSGS__MSG__DETAIL__BASE_INFO__TRAITS_HPP_
#define DRIVE_BASE_MSGS__MSG__DETAIL__BASE_INFO__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "drive_base_msgs/msg/detail/base_info__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"

namespace drive_base_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const BaseInfo & msg,
  std::ostream & out)
{
  out << "{";
  // member: hw_id
  {
    out << "hw_id: ";
    rosidl_generator_traits::value_to_yaml(msg.hw_id, out);
    out << ", ";
  }

  // member: hw_timestamp
  {
    out << "hw_timestamp: ";
    rosidl_generator_traits::value_to_yaml(msg.hw_timestamp, out);
    out << ", ";
  }

  // member: stamp
  {
    out << "stamp: ";
    to_flow_style_yaml(msg.stamp, out);
    out << ", ";
  }

  // member: x
  {
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << ", ";
  }

  // member: y
  {
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
    out << ", ";
  }

  // member: orientation
  {
    out << "orientation: ";
    rosidl_generator_traits::value_to_yaml(msg.orientation, out);
    out << ", ";
  }

  // member: forward_velocity
  {
    out << "forward_velocity: ";
    rosidl_generator_traits::value_to_yaml(msg.forward_velocity, out);
    out << ", ";
  }

  // member: rotational_velocity
  {
    out << "rotational_velocity: ";
    rosidl_generator_traits::value_to_yaml(msg.rotational_velocity, out);
    out << ", ";
  }

  // member: battery_voltage_pct
  {
    out << "battery_voltage_pct: ";
    rosidl_generator_traits::value_to_yaml(msg.battery_voltage_pct, out);
    out << ", ";
  }

  // member: power_supply
  {
    out << "power_supply: ";
    rosidl_generator_traits::value_to_yaml(msg.power_supply, out);
    out << ", ";
  }

  // member: overcurrent
  {
    out << "overcurrent: ";
    rosidl_generator_traits::value_to_yaml(msg.overcurrent, out);
    out << ", ";
  }

  // member: blocked
  {
    out << "blocked: ";
    rosidl_generator_traits::value_to_yaml(msg.blocked, out);
    out << ", ";
  }

  // member: in_collision
  {
    out << "in_collision: ";
    rosidl_generator_traits::value_to_yaml(msg.in_collision, out);
    out << ", ";
  }

  // member: at_cliff
  {
    out << "at_cliff: ";
    rosidl_generator_traits::value_to_yaml(msg.at_cliff, out);
    out << ", ";
  }

  // member: safety_state
  {
    out << "safety_state: ";
    rosidl_generator_traits::value_to_yaml(msg.safety_state, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const BaseInfo & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: hw_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "hw_id: ";
    rosidl_generator_traits::value_to_yaml(msg.hw_id, out);
    out << "\n";
  }

  // member: hw_timestamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "hw_timestamp: ";
    rosidl_generator_traits::value_to_yaml(msg.hw_timestamp, out);
    out << "\n";
  }

  // member: stamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "stamp:\n";
    to_block_style_yaml(msg.stamp, out, indentation + 2);
  }

  // member: x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << "\n";
  }

  // member: y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
    out << "\n";
  }

  // member: orientation
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "orientation: ";
    rosidl_generator_traits::value_to_yaml(msg.orientation, out);
    out << "\n";
  }

  // member: forward_velocity
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "forward_velocity: ";
    rosidl_generator_traits::value_to_yaml(msg.forward_velocity, out);
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

  // member: battery_voltage_pct
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "battery_voltage_pct: ";
    rosidl_generator_traits::value_to_yaml(msg.battery_voltage_pct, out);
    out << "\n";
  }

  // member: power_supply
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "power_supply: ";
    rosidl_generator_traits::value_to_yaml(msg.power_supply, out);
    out << "\n";
  }

  // member: overcurrent
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "overcurrent: ";
    rosidl_generator_traits::value_to_yaml(msg.overcurrent, out);
    out << "\n";
  }

  // member: blocked
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "blocked: ";
    rosidl_generator_traits::value_to_yaml(msg.blocked, out);
    out << "\n";
  }

  // member: in_collision
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "in_collision: ";
    rosidl_generator_traits::value_to_yaml(msg.in_collision, out);
    out << "\n";
  }

  // member: at_cliff
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "at_cliff: ";
    rosidl_generator_traits::value_to_yaml(msg.at_cliff, out);
    out << "\n";
  }

  // member: safety_state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "safety_state: ";
    rosidl_generator_traits::value_to_yaml(msg.safety_state, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const BaseInfo & msg, bool use_flow_style = false)
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
  const drive_base_msgs::msg::BaseInfo & msg,
  std::ostream & out, size_t indentation = 0)
{
  drive_base_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use drive_base_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const drive_base_msgs::msg::BaseInfo & msg)
{
  return drive_base_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<drive_base_msgs::msg::BaseInfo>()
{
  return "drive_base_msgs::msg::BaseInfo";
}

template<>
inline const char * name<drive_base_msgs::msg::BaseInfo>()
{
  return "drive_base_msgs/msg/BaseInfo";
}

template<>
struct has_fixed_size<drive_base_msgs::msg::BaseInfo>
  : std::integral_constant<bool, has_fixed_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct has_bounded_size<drive_base_msgs::msg::BaseInfo>
  : std::integral_constant<bool, has_bounded_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct is_message<drive_base_msgs::msg::BaseInfo>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // DRIVE_BASE_MSGS__MSG__DETAIL__BASE_INFO__TRAITS_HPP_
