// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from full_name_message:msg/FullName.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "full_name_message/msg/full_name.hpp"


#ifndef FULL_NAME_MESSAGE__MSG__DETAIL__FULL_NAME__STRUCT_HPP_
#define FULL_NAME_MESSAGE__MSG__DETAIL__FULL_NAME__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__full_name_message__msg__FullName __attribute__((deprecated))
#else
# define DEPRECATED__full_name_message__msg__FullName __declspec(deprecated)
#endif

namespace full_name_message
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct FullName_
{
  using Type = FullName_<ContainerAllocator>;

  explicit FullName_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->last_name = "";
      this->name = "";
      this->first_name = "";
    }
  }

  explicit FullName_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : last_name(_alloc),
    name(_alloc),
    first_name(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->last_name = "";
      this->name = "";
      this->first_name = "";
    }
  }

  // field types and members
  using _last_name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _last_name_type last_name;
  using _name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _name_type name;
  using _first_name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _first_name_type first_name;

  // setters for named parameter idiom
  Type & set__last_name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->last_name = _arg;
    return *this;
  }
  Type & set__name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->name = _arg;
    return *this;
  }
  Type & set__first_name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->first_name = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    full_name_message::msg::FullName_<ContainerAllocator> *;
  using ConstRawPtr =
    const full_name_message::msg::FullName_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<full_name_message::msg::FullName_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<full_name_message::msg::FullName_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      full_name_message::msg::FullName_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<full_name_message::msg::FullName_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      full_name_message::msg::FullName_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<full_name_message::msg::FullName_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<full_name_message::msg::FullName_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<full_name_message::msg::FullName_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__full_name_message__msg__FullName
    std::shared_ptr<full_name_message::msg::FullName_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__full_name_message__msg__FullName
    std::shared_ptr<full_name_message::msg::FullName_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const FullName_ & other) const
  {
    if (this->last_name != other.last_name) {
      return false;
    }
    if (this->name != other.name) {
      return false;
    }
    if (this->first_name != other.first_name) {
      return false;
    }
    return true;
  }
  bool operator!=(const FullName_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct FullName_

// alias to use template instance with default allocator
using FullName =
  full_name_message::msg::FullName_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace full_name_message

#endif  // FULL_NAME_MESSAGE__MSG__DETAIL__FULL_NAME__STRUCT_HPP_
