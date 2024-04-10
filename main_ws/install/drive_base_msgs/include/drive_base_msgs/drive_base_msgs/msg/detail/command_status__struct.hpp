// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from drive_base_msgs:msg/CommandStatus.idl
// generated code does not contain a copyright notice

#ifndef DRIVE_BASE_MSGS__MSG__DETAIL__COMMAND_STATUS__STRUCT_HPP_
#define DRIVE_BASE_MSGS__MSG__DETAIL__COMMAND_STATUS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.hpp"
// Member 'cmd_header'
#include "drive_base_msgs/msg/detail/command_header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__drive_base_msgs__msg__CommandStatus __attribute__((deprecated))
#else
# define DEPRECATED__drive_base_msgs__msg__CommandStatus __declspec(deprecated)
#endif

namespace drive_base_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct CommandStatus_
{
  using Type = CommandStatus_<ContainerAllocator>;

  explicit CommandStatus_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_init),
    cmd_header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = 0;
    }
  }

  explicit CommandStatus_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_alloc, _init),
    cmd_header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = 0;
    }
  }

  // field types and members
  using _stamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _stamp_type stamp;
  using _cmd_header_type =
    drive_base_msgs::msg::CommandHeader_<ContainerAllocator>;
  _cmd_header_type cmd_header;
  using _status_type =
    uint8_t;
  _status_type status;

  // setters for named parameter idiom
  Type & set__stamp(
    const builtin_interfaces::msg::Time_<ContainerAllocator> & _arg)
  {
    this->stamp = _arg;
    return *this;
  }
  Type & set__cmd_header(
    const drive_base_msgs::msg::CommandHeader_<ContainerAllocator> & _arg)
  {
    this->cmd_header = _arg;
    return *this;
  }
  Type & set__status(
    const uint8_t & _arg)
  {
    this->status = _arg;
    return *this;
  }

  // constant declarations
  static constexpr uint8_t OK =
    0u;
  static constexpr uint8_t CAPABILITIES_EXCEEDED =
    1u;
  static constexpr uint8_t INVALID =
    2u;
  static constexpr uint8_t POWER_INSUFFICIENT =
    3u;
  static constexpr uint8_t TEMPORARY_FAILURE =
    4u;
  static constexpr uint8_t SYSTEM_FAILURE =
    5u;

  // pointer types
  using RawPtr =
    drive_base_msgs::msg::CommandStatus_<ContainerAllocator> *;
  using ConstRawPtr =
    const drive_base_msgs::msg::CommandStatus_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<drive_base_msgs::msg::CommandStatus_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<drive_base_msgs::msg::CommandStatus_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      drive_base_msgs::msg::CommandStatus_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<drive_base_msgs::msg::CommandStatus_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      drive_base_msgs::msg::CommandStatus_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<drive_base_msgs::msg::CommandStatus_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<drive_base_msgs::msg::CommandStatus_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<drive_base_msgs::msg::CommandStatus_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__drive_base_msgs__msg__CommandStatus
    std::shared_ptr<drive_base_msgs::msg::CommandStatus_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__drive_base_msgs__msg__CommandStatus
    std::shared_ptr<drive_base_msgs::msg::CommandStatus_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const CommandStatus_ & other) const
  {
    if (this->stamp != other.stamp) {
      return false;
    }
    if (this->cmd_header != other.cmd_header) {
      return false;
    }
    if (this->status != other.status) {
      return false;
    }
    return true;
  }
  bool operator!=(const CommandStatus_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct CommandStatus_

// alias to use template instance with default allocator
using CommandStatus =
  drive_base_msgs::msg::CommandStatus_<std::allocator<void>>;

// constant definitions
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t CommandStatus_<ContainerAllocator>::OK;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t CommandStatus_<ContainerAllocator>::CAPABILITIES_EXCEEDED;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t CommandStatus_<ContainerAllocator>::INVALID;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t CommandStatus_<ContainerAllocator>::POWER_INSUFFICIENT;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t CommandStatus_<ContainerAllocator>::TEMPORARY_FAILURE;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t CommandStatus_<ContainerAllocator>::SYSTEM_FAILURE;
#endif  // __cplusplus < 201703L

}  // namespace msg

}  // namespace drive_base_msgs

#endif  // DRIVE_BASE_MSGS__MSG__DETAIL__COMMAND_STATUS__STRUCT_HPP_
