// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from drive_base_msgs:msg/CommandHeader.idl
// generated code does not contain a copyright notice

#ifndef DRIVE_BASE_MSGS__MSG__DETAIL__COMMAND_HEADER__STRUCT_HPP_
#define DRIVE_BASE_MSGS__MSG__DETAIL__COMMAND_HEADER__STRUCT_HPP_

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

#ifndef _WIN32
# define DEPRECATED__drive_base_msgs__msg__CommandHeader __attribute__((deprecated))
#else
# define DEPRECATED__drive_base_msgs__msg__CommandHeader __declspec(deprecated)
#endif

namespace drive_base_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct CommandHeader_
{
  using Type = CommandHeader_<ContainerAllocator>;

  explicit CommandHeader_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->command_id = 0ul;
      this->expected_period = 0;
    }
  }

  explicit CommandHeader_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->command_id = 0ul;
      this->expected_period = 0;
    }
  }

  // field types and members
  using _stamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _stamp_type stamp;
  using _command_id_type =
    uint32_t;
  _command_id_type command_id;
  using _expected_period_type =
    uint16_t;
  _expected_period_type expected_period;

  // setters for named parameter idiom
  Type & set__stamp(
    const builtin_interfaces::msg::Time_<ContainerAllocator> & _arg)
  {
    this->stamp = _arg;
    return *this;
  }
  Type & set__command_id(
    const uint32_t & _arg)
  {
    this->command_id = _arg;
    return *this;
  }
  Type & set__expected_period(
    const uint16_t & _arg)
  {
    this->expected_period = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    drive_base_msgs::msg::CommandHeader_<ContainerAllocator> *;
  using ConstRawPtr =
    const drive_base_msgs::msg::CommandHeader_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<drive_base_msgs::msg::CommandHeader_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<drive_base_msgs::msg::CommandHeader_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      drive_base_msgs::msg::CommandHeader_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<drive_base_msgs::msg::CommandHeader_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      drive_base_msgs::msg::CommandHeader_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<drive_base_msgs::msg::CommandHeader_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<drive_base_msgs::msg::CommandHeader_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<drive_base_msgs::msg::CommandHeader_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__drive_base_msgs__msg__CommandHeader
    std::shared_ptr<drive_base_msgs::msg::CommandHeader_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__drive_base_msgs__msg__CommandHeader
    std::shared_ptr<drive_base_msgs::msg::CommandHeader_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const CommandHeader_ & other) const
  {
    if (this->stamp != other.stamp) {
      return false;
    }
    if (this->command_id != other.command_id) {
      return false;
    }
    if (this->expected_period != other.expected_period) {
      return false;
    }
    return true;
  }
  bool operator!=(const CommandHeader_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct CommandHeader_

// alias to use template instance with default allocator
using CommandHeader =
  drive_base_msgs::msg::CommandHeader_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace drive_base_msgs

#endif  // DRIVE_BASE_MSGS__MSG__DETAIL__COMMAND_HEADER__STRUCT_HPP_
