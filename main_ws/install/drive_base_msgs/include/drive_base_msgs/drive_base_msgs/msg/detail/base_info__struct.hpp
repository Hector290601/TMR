// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from drive_base_msgs:msg/BaseInfo.idl
// generated code does not contain a copyright notice

#ifndef DRIVE_BASE_MSGS__MSG__DETAIL__BASE_INFO__STRUCT_HPP_
#define DRIVE_BASE_MSGS__MSG__DETAIL__BASE_INFO__STRUCT_HPP_

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
# define DEPRECATED__drive_base_msgs__msg__BaseInfo __attribute__((deprecated))
#else
# define DEPRECATED__drive_base_msgs__msg__BaseInfo __declspec(deprecated)
#endif

namespace drive_base_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct BaseInfo_
{
  using Type = BaseInfo_<ContainerAllocator>;

  explicit BaseInfo_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->hw_id = 0ul;
      this->hw_timestamp = 0ul;
      this->x = 0.0f;
      this->y = 0.0f;
      this->orientation = 0.0f;
      this->forward_velocity = 0.0f;
      this->rotational_velocity = 0.0f;
      this->battery_voltage_pct = 0;
      this->power_supply = 0;
      this->overcurrent = false;
      this->blocked = false;
      this->in_collision = false;
      this->at_cliff = false;
      this->safety_state = 0;
    }
  }

  explicit BaseInfo_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->hw_id = 0ul;
      this->hw_timestamp = 0ul;
      this->x = 0.0f;
      this->y = 0.0f;
      this->orientation = 0.0f;
      this->forward_velocity = 0.0f;
      this->rotational_velocity = 0.0f;
      this->battery_voltage_pct = 0;
      this->power_supply = 0;
      this->overcurrent = false;
      this->blocked = false;
      this->in_collision = false;
      this->at_cliff = false;
      this->safety_state = 0;
    }
  }

  // field types and members
  using _hw_id_type =
    uint32_t;
  _hw_id_type hw_id;
  using _hw_timestamp_type =
    uint32_t;
  _hw_timestamp_type hw_timestamp;
  using _stamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _stamp_type stamp;
  using _x_type =
    float;
  _x_type x;
  using _y_type =
    float;
  _y_type y;
  using _orientation_type =
    float;
  _orientation_type orientation;
  using _forward_velocity_type =
    float;
  _forward_velocity_type forward_velocity;
  using _rotational_velocity_type =
    float;
  _rotational_velocity_type rotational_velocity;
  using _battery_voltage_pct_type =
    uint8_t;
  _battery_voltage_pct_type battery_voltage_pct;
  using _power_supply_type =
    uint8_t;
  _power_supply_type power_supply;
  using _overcurrent_type =
    bool;
  _overcurrent_type overcurrent;
  using _blocked_type =
    bool;
  _blocked_type blocked;
  using _in_collision_type =
    bool;
  _in_collision_type in_collision;
  using _at_cliff_type =
    bool;
  _at_cliff_type at_cliff;
  using _safety_state_type =
    uint16_t;
  _safety_state_type safety_state;

  // setters for named parameter idiom
  Type & set__hw_id(
    const uint32_t & _arg)
  {
    this->hw_id = _arg;
    return *this;
  }
  Type & set__hw_timestamp(
    const uint32_t & _arg)
  {
    this->hw_timestamp = _arg;
    return *this;
  }
  Type & set__stamp(
    const builtin_interfaces::msg::Time_<ContainerAllocator> & _arg)
  {
    this->stamp = _arg;
    return *this;
  }
  Type & set__x(
    const float & _arg)
  {
    this->x = _arg;
    return *this;
  }
  Type & set__y(
    const float & _arg)
  {
    this->y = _arg;
    return *this;
  }
  Type & set__orientation(
    const float & _arg)
  {
    this->orientation = _arg;
    return *this;
  }
  Type & set__forward_velocity(
    const float & _arg)
  {
    this->forward_velocity = _arg;
    return *this;
  }
  Type & set__rotational_velocity(
    const float & _arg)
  {
    this->rotational_velocity = _arg;
    return *this;
  }
  Type & set__battery_voltage_pct(
    const uint8_t & _arg)
  {
    this->battery_voltage_pct = _arg;
    return *this;
  }
  Type & set__power_supply(
    const uint8_t & _arg)
  {
    this->power_supply = _arg;
    return *this;
  }
  Type & set__overcurrent(
    const bool & _arg)
  {
    this->overcurrent = _arg;
    return *this;
  }
  Type & set__blocked(
    const bool & _arg)
  {
    this->blocked = _arg;
    return *this;
  }
  Type & set__in_collision(
    const bool & _arg)
  {
    this->in_collision = _arg;
    return *this;
  }
  Type & set__at_cliff(
    const bool & _arg)
  {
    this->at_cliff = _arg;
    return *this;
  }
  Type & set__safety_state(
    const uint16_t & _arg)
  {
    this->safety_state = _arg;
    return *this;
  }

  // constant declarations
  static constexpr uint8_t POWER_SUPPLY_STATUS_UNKNOWN =
    0u;
  static constexpr uint8_t POWER_SUPPLY_STATUS_CHARGING =
    1u;
  static constexpr uint8_t POWER_SUPPLY_STATUS_DISCHARGING =
    2u;
  static constexpr uint8_t POWER_SUPPLY_STATUS_NOT_CHARGING =
    3u;
  static constexpr uint8_t POWER_SUPPLY_STATUS_FULL =
    4u;
  static constexpr uint16_t SAFETY_STATE_OPERATIONAL =
    1u;
  static constexpr uint16_t SAFETY_STATE_LOW_SPEED =
    2u;
  static constexpr uint16_t SAFETY_STATE_NO_FORWARD =
    4u;
  static constexpr uint16_t SAFETY_STATE_NO_BACKWARD =
    8u;
  static constexpr uint16_t SAFETY_STATE_NO_ROTATE =
    16u;

  // pointer types
  using RawPtr =
    drive_base_msgs::msg::BaseInfo_<ContainerAllocator> *;
  using ConstRawPtr =
    const drive_base_msgs::msg::BaseInfo_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<drive_base_msgs::msg::BaseInfo_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<drive_base_msgs::msg::BaseInfo_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      drive_base_msgs::msg::BaseInfo_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<drive_base_msgs::msg::BaseInfo_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      drive_base_msgs::msg::BaseInfo_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<drive_base_msgs::msg::BaseInfo_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<drive_base_msgs::msg::BaseInfo_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<drive_base_msgs::msg::BaseInfo_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__drive_base_msgs__msg__BaseInfo
    std::shared_ptr<drive_base_msgs::msg::BaseInfo_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__drive_base_msgs__msg__BaseInfo
    std::shared_ptr<drive_base_msgs::msg::BaseInfo_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const BaseInfo_ & other) const
  {
    if (this->hw_id != other.hw_id) {
      return false;
    }
    if (this->hw_timestamp != other.hw_timestamp) {
      return false;
    }
    if (this->stamp != other.stamp) {
      return false;
    }
    if (this->x != other.x) {
      return false;
    }
    if (this->y != other.y) {
      return false;
    }
    if (this->orientation != other.orientation) {
      return false;
    }
    if (this->forward_velocity != other.forward_velocity) {
      return false;
    }
    if (this->rotational_velocity != other.rotational_velocity) {
      return false;
    }
    if (this->battery_voltage_pct != other.battery_voltage_pct) {
      return false;
    }
    if (this->power_supply != other.power_supply) {
      return false;
    }
    if (this->overcurrent != other.overcurrent) {
      return false;
    }
    if (this->blocked != other.blocked) {
      return false;
    }
    if (this->in_collision != other.in_collision) {
      return false;
    }
    if (this->at_cliff != other.at_cliff) {
      return false;
    }
    if (this->safety_state != other.safety_state) {
      return false;
    }
    return true;
  }
  bool operator!=(const BaseInfo_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct BaseInfo_

// alias to use template instance with default allocator
using BaseInfo =
  drive_base_msgs::msg::BaseInfo_<std::allocator<void>>;

// constant definitions
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t BaseInfo_<ContainerAllocator>::POWER_SUPPLY_STATUS_UNKNOWN;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t BaseInfo_<ContainerAllocator>::POWER_SUPPLY_STATUS_CHARGING;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t BaseInfo_<ContainerAllocator>::POWER_SUPPLY_STATUS_DISCHARGING;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t BaseInfo_<ContainerAllocator>::POWER_SUPPLY_STATUS_NOT_CHARGING;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t BaseInfo_<ContainerAllocator>::POWER_SUPPLY_STATUS_FULL;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint16_t BaseInfo_<ContainerAllocator>::SAFETY_STATE_OPERATIONAL;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint16_t BaseInfo_<ContainerAllocator>::SAFETY_STATE_LOW_SPEED;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint16_t BaseInfo_<ContainerAllocator>::SAFETY_STATE_NO_FORWARD;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint16_t BaseInfo_<ContainerAllocator>::SAFETY_STATE_NO_BACKWARD;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint16_t BaseInfo_<ContainerAllocator>::SAFETY_STATE_NO_ROTATE;
#endif  // __cplusplus < 201703L

}  // namespace msg

}  // namespace drive_base_msgs

#endif  // DRIVE_BASE_MSGS__MSG__DETAIL__BASE_INFO__STRUCT_HPP_
