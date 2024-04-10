// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from drive_base_msgs:msg/CommandStatus.idl
// generated code does not contain a copyright notice

#ifndef DRIVE_BASE_MSGS__MSG__DETAIL__COMMAND_STATUS__BUILDER_HPP_
#define DRIVE_BASE_MSGS__MSG__DETAIL__COMMAND_STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "drive_base_msgs/msg/detail/command_status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace drive_base_msgs
{

namespace msg
{

namespace builder
{

class Init_CommandStatus_status
{
public:
  explicit Init_CommandStatus_status(::drive_base_msgs::msg::CommandStatus & msg)
  : msg_(msg)
  {}
  ::drive_base_msgs::msg::CommandStatus status(::drive_base_msgs::msg::CommandStatus::_status_type arg)
  {
    msg_.status = std::move(arg);
    return std::move(msg_);
  }

private:
  ::drive_base_msgs::msg::CommandStatus msg_;
};

class Init_CommandStatus_cmd_header
{
public:
  explicit Init_CommandStatus_cmd_header(::drive_base_msgs::msg::CommandStatus & msg)
  : msg_(msg)
  {}
  Init_CommandStatus_status cmd_header(::drive_base_msgs::msg::CommandStatus::_cmd_header_type arg)
  {
    msg_.cmd_header = std::move(arg);
    return Init_CommandStatus_status(msg_);
  }

private:
  ::drive_base_msgs::msg::CommandStatus msg_;
};

class Init_CommandStatus_stamp
{
public:
  Init_CommandStatus_stamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CommandStatus_cmd_header stamp(::drive_base_msgs::msg::CommandStatus::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return Init_CommandStatus_cmd_header(msg_);
  }

private:
  ::drive_base_msgs::msg::CommandStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::drive_base_msgs::msg::CommandStatus>()
{
  return drive_base_msgs::msg::builder::Init_CommandStatus_stamp();
}

}  // namespace drive_base_msgs

#endif  // DRIVE_BASE_MSGS__MSG__DETAIL__COMMAND_STATUS__BUILDER_HPP_
