// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from drive_base_msgs:msg/TRVCommand.idl
// generated code does not contain a copyright notice

#ifndef DRIVE_BASE_MSGS__MSG__DETAIL__TRV_COMMAND__BUILDER_HPP_
#define DRIVE_BASE_MSGS__MSG__DETAIL__TRV_COMMAND__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "drive_base_msgs/msg/detail/trv_command__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace drive_base_msgs
{

namespace msg
{

namespace builder
{

class Init_TRVCommand_rotational_velocity
{
public:
  explicit Init_TRVCommand_rotational_velocity(::drive_base_msgs::msg::TRVCommand & msg)
  : msg_(msg)
  {}
  ::drive_base_msgs::msg::TRVCommand rotational_velocity(::drive_base_msgs::msg::TRVCommand::_rotational_velocity_type arg)
  {
    msg_.rotational_velocity = std::move(arg);
    return std::move(msg_);
  }

private:
  ::drive_base_msgs::msg::TRVCommand msg_;
};

class Init_TRVCommand_translational_velocity
{
public:
  explicit Init_TRVCommand_translational_velocity(::drive_base_msgs::msg::TRVCommand & msg)
  : msg_(msg)
  {}
  Init_TRVCommand_rotational_velocity translational_velocity(::drive_base_msgs::msg::TRVCommand::_translational_velocity_type arg)
  {
    msg_.translational_velocity = std::move(arg);
    return Init_TRVCommand_rotational_velocity(msg_);
  }

private:
  ::drive_base_msgs::msg::TRVCommand msg_;
};

class Init_TRVCommand_header
{
public:
  Init_TRVCommand_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TRVCommand_translational_velocity header(::drive_base_msgs::msg::TRVCommand::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_TRVCommand_translational_velocity(msg_);
  }

private:
  ::drive_base_msgs::msg::TRVCommand msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::drive_base_msgs::msg::TRVCommand>()
{
  return drive_base_msgs::msg::builder::Init_TRVCommand_header();
}

}  // namespace drive_base_msgs

#endif  // DRIVE_BASE_MSGS__MSG__DETAIL__TRV_COMMAND__BUILDER_HPP_
