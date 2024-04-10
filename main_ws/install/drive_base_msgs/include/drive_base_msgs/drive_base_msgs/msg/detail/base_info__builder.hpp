// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from drive_base_msgs:msg/BaseInfo.idl
// generated code does not contain a copyright notice

#ifndef DRIVE_BASE_MSGS__MSG__DETAIL__BASE_INFO__BUILDER_HPP_
#define DRIVE_BASE_MSGS__MSG__DETAIL__BASE_INFO__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "drive_base_msgs/msg/detail/base_info__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace drive_base_msgs
{

namespace msg
{

namespace builder
{

class Init_BaseInfo_safety_state
{
public:
  explicit Init_BaseInfo_safety_state(::drive_base_msgs::msg::BaseInfo & msg)
  : msg_(msg)
  {}
  ::drive_base_msgs::msg::BaseInfo safety_state(::drive_base_msgs::msg::BaseInfo::_safety_state_type arg)
  {
    msg_.safety_state = std::move(arg);
    return std::move(msg_);
  }

private:
  ::drive_base_msgs::msg::BaseInfo msg_;
};

class Init_BaseInfo_at_cliff
{
public:
  explicit Init_BaseInfo_at_cliff(::drive_base_msgs::msg::BaseInfo & msg)
  : msg_(msg)
  {}
  Init_BaseInfo_safety_state at_cliff(::drive_base_msgs::msg::BaseInfo::_at_cliff_type arg)
  {
    msg_.at_cliff = std::move(arg);
    return Init_BaseInfo_safety_state(msg_);
  }

private:
  ::drive_base_msgs::msg::BaseInfo msg_;
};

class Init_BaseInfo_in_collision
{
public:
  explicit Init_BaseInfo_in_collision(::drive_base_msgs::msg::BaseInfo & msg)
  : msg_(msg)
  {}
  Init_BaseInfo_at_cliff in_collision(::drive_base_msgs::msg::BaseInfo::_in_collision_type arg)
  {
    msg_.in_collision = std::move(arg);
    return Init_BaseInfo_at_cliff(msg_);
  }

private:
  ::drive_base_msgs::msg::BaseInfo msg_;
};

class Init_BaseInfo_blocked
{
public:
  explicit Init_BaseInfo_blocked(::drive_base_msgs::msg::BaseInfo & msg)
  : msg_(msg)
  {}
  Init_BaseInfo_in_collision blocked(::drive_base_msgs::msg::BaseInfo::_blocked_type arg)
  {
    msg_.blocked = std::move(arg);
    return Init_BaseInfo_in_collision(msg_);
  }

private:
  ::drive_base_msgs::msg::BaseInfo msg_;
};

class Init_BaseInfo_overcurrent
{
public:
  explicit Init_BaseInfo_overcurrent(::drive_base_msgs::msg::BaseInfo & msg)
  : msg_(msg)
  {}
  Init_BaseInfo_blocked overcurrent(::drive_base_msgs::msg::BaseInfo::_overcurrent_type arg)
  {
    msg_.overcurrent = std::move(arg);
    return Init_BaseInfo_blocked(msg_);
  }

private:
  ::drive_base_msgs::msg::BaseInfo msg_;
};

class Init_BaseInfo_power_supply
{
public:
  explicit Init_BaseInfo_power_supply(::drive_base_msgs::msg::BaseInfo & msg)
  : msg_(msg)
  {}
  Init_BaseInfo_overcurrent power_supply(::drive_base_msgs::msg::BaseInfo::_power_supply_type arg)
  {
    msg_.power_supply = std::move(arg);
    return Init_BaseInfo_overcurrent(msg_);
  }

private:
  ::drive_base_msgs::msg::BaseInfo msg_;
};

class Init_BaseInfo_battery_voltage_pct
{
public:
  explicit Init_BaseInfo_battery_voltage_pct(::drive_base_msgs::msg::BaseInfo & msg)
  : msg_(msg)
  {}
  Init_BaseInfo_power_supply battery_voltage_pct(::drive_base_msgs::msg::BaseInfo::_battery_voltage_pct_type arg)
  {
    msg_.battery_voltage_pct = std::move(arg);
    return Init_BaseInfo_power_supply(msg_);
  }

private:
  ::drive_base_msgs::msg::BaseInfo msg_;
};

class Init_BaseInfo_rotational_velocity
{
public:
  explicit Init_BaseInfo_rotational_velocity(::drive_base_msgs::msg::BaseInfo & msg)
  : msg_(msg)
  {}
  Init_BaseInfo_battery_voltage_pct rotational_velocity(::drive_base_msgs::msg::BaseInfo::_rotational_velocity_type arg)
  {
    msg_.rotational_velocity = std::move(arg);
    return Init_BaseInfo_battery_voltage_pct(msg_);
  }

private:
  ::drive_base_msgs::msg::BaseInfo msg_;
};

class Init_BaseInfo_forward_velocity
{
public:
  explicit Init_BaseInfo_forward_velocity(::drive_base_msgs::msg::BaseInfo & msg)
  : msg_(msg)
  {}
  Init_BaseInfo_rotational_velocity forward_velocity(::drive_base_msgs::msg::BaseInfo::_forward_velocity_type arg)
  {
    msg_.forward_velocity = std::move(arg);
    return Init_BaseInfo_rotational_velocity(msg_);
  }

private:
  ::drive_base_msgs::msg::BaseInfo msg_;
};

class Init_BaseInfo_orientation
{
public:
  explicit Init_BaseInfo_orientation(::drive_base_msgs::msg::BaseInfo & msg)
  : msg_(msg)
  {}
  Init_BaseInfo_forward_velocity orientation(::drive_base_msgs::msg::BaseInfo::_orientation_type arg)
  {
    msg_.orientation = std::move(arg);
    return Init_BaseInfo_forward_velocity(msg_);
  }

private:
  ::drive_base_msgs::msg::BaseInfo msg_;
};

class Init_BaseInfo_y
{
public:
  explicit Init_BaseInfo_y(::drive_base_msgs::msg::BaseInfo & msg)
  : msg_(msg)
  {}
  Init_BaseInfo_orientation y(::drive_base_msgs::msg::BaseInfo::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_BaseInfo_orientation(msg_);
  }

private:
  ::drive_base_msgs::msg::BaseInfo msg_;
};

class Init_BaseInfo_x
{
public:
  explicit Init_BaseInfo_x(::drive_base_msgs::msg::BaseInfo & msg)
  : msg_(msg)
  {}
  Init_BaseInfo_y x(::drive_base_msgs::msg::BaseInfo::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_BaseInfo_y(msg_);
  }

private:
  ::drive_base_msgs::msg::BaseInfo msg_;
};

class Init_BaseInfo_stamp
{
public:
  explicit Init_BaseInfo_stamp(::drive_base_msgs::msg::BaseInfo & msg)
  : msg_(msg)
  {}
  Init_BaseInfo_x stamp(::drive_base_msgs::msg::BaseInfo::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return Init_BaseInfo_x(msg_);
  }

private:
  ::drive_base_msgs::msg::BaseInfo msg_;
};

class Init_BaseInfo_hw_timestamp
{
public:
  explicit Init_BaseInfo_hw_timestamp(::drive_base_msgs::msg::BaseInfo & msg)
  : msg_(msg)
  {}
  Init_BaseInfo_stamp hw_timestamp(::drive_base_msgs::msg::BaseInfo::_hw_timestamp_type arg)
  {
    msg_.hw_timestamp = std::move(arg);
    return Init_BaseInfo_stamp(msg_);
  }

private:
  ::drive_base_msgs::msg::BaseInfo msg_;
};

class Init_BaseInfo_hw_id
{
public:
  Init_BaseInfo_hw_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_BaseInfo_hw_timestamp hw_id(::drive_base_msgs::msg::BaseInfo::_hw_id_type arg)
  {
    msg_.hw_id = std::move(arg);
    return Init_BaseInfo_hw_timestamp(msg_);
  }

private:
  ::drive_base_msgs::msg::BaseInfo msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::drive_base_msgs::msg::BaseInfo>()
{
  return drive_base_msgs::msg::builder::Init_BaseInfo_hw_id();
}

}  // namespace drive_base_msgs

#endif  // DRIVE_BASE_MSGS__MSG__DETAIL__BASE_INFO__BUILDER_HPP_
