// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from drive_base_msgs:msg/TRVCommand.idl
// generated code does not contain a copyright notice

#ifndef DRIVE_BASE_MSGS__MSG__DETAIL__TRV_COMMAND__STRUCT_HPP_
#define DRIVE_BASE_MSGS__MSG__DETAIL__TRV_COMMAND__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "drive_base_msgs/msg/detail/command_header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__drive_base_msgs__msg__TRVCommand __attribute__((deprecated))
#else
# define DEPRECATED__drive_base_msgs__msg__TRVCommand __declspec(deprecated)
#endif

namespace drive_base_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TRVCommand_
{
  using Type = TRVCommand_<ContainerAllocator>;

  explicit TRVCommand_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->translational_velocity = 0.0f;
      this->rotational_velocity = 0.0f;
    }
  }

  explicit TRVCommand_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->translational_velocity = 0.0f;
      this->rotational_velocity = 0.0f;
    }
  }

  // field types and members
  using _header_type =
    drive_base_msgs::msg::CommandHeader_<ContainerAllocator>;
  _header_type header;
  using _translational_velocity_type =
    float;
  _translational_velocity_type translational_velocity;
  using _rotational_velocity_type =
    float;
  _rotational_velocity_type rotational_velocity;

  // setters for named parameter idiom
  Type & set__header(
    const drive_base_msgs::msg::CommandHeader_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__translational_velocity(
    const float & _arg)
  {
    this->translational_velocity = _arg;
    return *this;
  }
  Type & set__rotational_velocity(
    const float & _arg)
  {
    this->rotational_velocity = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    drive_base_msgs::msg::TRVCommand_<ContainerAllocator> *;
  using ConstRawPtr =
    const drive_base_msgs::msg::TRVCommand_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<drive_base_msgs::msg::TRVCommand_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<drive_base_msgs::msg::TRVCommand_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      drive_base_msgs::msg::TRVCommand_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<drive_base_msgs::msg::TRVCommand_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      drive_base_msgs::msg::TRVCommand_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<drive_base_msgs::msg::TRVCommand_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<drive_base_msgs::msg::TRVCommand_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<drive_base_msgs::msg::TRVCommand_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__drive_base_msgs__msg__TRVCommand
    std::shared_ptr<drive_base_msgs::msg::TRVCommand_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__drive_base_msgs__msg__TRVCommand
    std::shared_ptr<drive_base_msgs::msg::TRVCommand_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TRVCommand_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->translational_velocity != other.translational_velocity) {
      return false;
    }
    if (this->rotational_velocity != other.rotational_velocity) {
      return false;
    }
    return true;
  }
  bool operator!=(const TRVCommand_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TRVCommand_

// alias to use template instance with default allocator
using TRVCommand =
  drive_base_msgs::msg::TRVCommand_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace drive_base_msgs

#endif  // DRIVE_BASE_MSGS__MSG__DETAIL__TRV_COMMAND__STRUCT_HPP_
