// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from drive_base_msgs:msg/CommandHeader.idl
// generated code does not contain a copyright notice

#ifndef DRIVE_BASE_MSGS__MSG__DETAIL__COMMAND_HEADER__BUILDER_HPP_
#define DRIVE_BASE_MSGS__MSG__DETAIL__COMMAND_HEADER__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "drive_base_msgs/msg/detail/command_header__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace drive_base_msgs
{

namespace msg
{

namespace builder
{

class Init_CommandHeader_expected_period
{
public:
  explicit Init_CommandHeader_expected_period(::drive_base_msgs::msg::CommandHeader & msg)
  : msg_(msg)
  {}
  ::drive_base_msgs::msg::CommandHeader expected_period(::drive_base_msgs::msg::CommandHeader::_expected_period_type arg)
  {
    msg_.expected_period = std::move(arg);
    return std::move(msg_);
  }

private:
  ::drive_base_msgs::msg::CommandHeader msg_;
};

class Init_CommandHeader_command_id
{
public:
  explicit Init_CommandHeader_command_id(::drive_base_msgs::msg::CommandHeader & msg)
  : msg_(msg)
  {}
  Init_CommandHeader_expected_period command_id(::drive_base_msgs::msg::CommandHeader::_command_id_type arg)
  {
    msg_.command_id = std::move(arg);
    return Init_CommandHeader_expected_period(msg_);
  }

private:
  ::drive_base_msgs::msg::CommandHeader msg_;
};

class Init_CommandHeader_stamp
{
public:
  Init_CommandHeader_stamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CommandHeader_command_id stamp(::drive_base_msgs::msg::CommandHeader::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return Init_CommandHeader_command_id(msg_);
  }

private:
  ::drive_base_msgs::msg::CommandHeader msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::drive_base_msgs::msg::CommandHeader>()
{
  return drive_base_msgs::msg::builder::Init_CommandHeader_stamp();
}

}  // namespace drive_base_msgs

#endif  // DRIVE_BASE_MSGS__MSG__DETAIL__COMMAND_HEADER__BUILDER_HPP_
