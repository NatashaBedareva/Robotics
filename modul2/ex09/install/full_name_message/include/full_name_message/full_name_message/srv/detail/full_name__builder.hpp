// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from full_name_message:srv/FullName.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "full_name_message/srv/full_name.hpp"


#ifndef FULL_NAME_MESSAGE__SRV__DETAIL__FULL_NAME__BUILDER_HPP_
#define FULL_NAME_MESSAGE__SRV__DETAIL__FULL_NAME__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "full_name_message/srv/detail/full_name__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace full_name_message
{

namespace srv
{

namespace builder
{

class Init_FullName_Request_first_name
{
public:
  explicit Init_FullName_Request_first_name(::full_name_message::srv::FullName_Request & msg)
  : msg_(msg)
  {}
  ::full_name_message::srv::FullName_Request first_name(::full_name_message::srv::FullName_Request::_first_name_type arg)
  {
    msg_.first_name = std::move(arg);
    return std::move(msg_);
  }

private:
  ::full_name_message::srv::FullName_Request msg_;
};

class Init_FullName_Request_name
{
public:
  explicit Init_FullName_Request_name(::full_name_message::srv::FullName_Request & msg)
  : msg_(msg)
  {}
  Init_FullName_Request_first_name name(::full_name_message::srv::FullName_Request::_name_type arg)
  {
    msg_.name = std::move(arg);
    return Init_FullName_Request_first_name(msg_);
  }

private:
  ::full_name_message::srv::FullName_Request msg_;
};

class Init_FullName_Request_last_name
{
public:
  Init_FullName_Request_last_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_FullName_Request_name last_name(::full_name_message::srv::FullName_Request::_last_name_type arg)
  {
    msg_.last_name = std::move(arg);
    return Init_FullName_Request_name(msg_);
  }

private:
  ::full_name_message::srv::FullName_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::full_name_message::srv::FullName_Request>()
{
  return full_name_message::srv::builder::Init_FullName_Request_last_name();
}

}  // namespace full_name_message


namespace full_name_message
{

namespace srv
{

namespace builder
{

class Init_FullName_Response_full_name
{
public:
  Init_FullName_Response_full_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::full_name_message::srv::FullName_Response full_name(::full_name_message::srv::FullName_Response::_full_name_type arg)
  {
    msg_.full_name = std::move(arg);
    return std::move(msg_);
  }

private:
  ::full_name_message::srv::FullName_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::full_name_message::srv::FullName_Response>()
{
  return full_name_message::srv::builder::Init_FullName_Response_full_name();
}

}  // namespace full_name_message


namespace full_name_message
{

namespace srv
{

namespace builder
{

class Init_FullName_Event_response
{
public:
  explicit Init_FullName_Event_response(::full_name_message::srv::FullName_Event & msg)
  : msg_(msg)
  {}
  ::full_name_message::srv::FullName_Event response(::full_name_message::srv::FullName_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::full_name_message::srv::FullName_Event msg_;
};

class Init_FullName_Event_request
{
public:
  explicit Init_FullName_Event_request(::full_name_message::srv::FullName_Event & msg)
  : msg_(msg)
  {}
  Init_FullName_Event_response request(::full_name_message::srv::FullName_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_FullName_Event_response(msg_);
  }

private:
  ::full_name_message::srv::FullName_Event msg_;
};

class Init_FullName_Event_info
{
public:
  Init_FullName_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_FullName_Event_request info(::full_name_message::srv::FullName_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_FullName_Event_request(msg_);
  }

private:
  ::full_name_message::srv::FullName_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::full_name_message::srv::FullName_Event>()
{
  return full_name_message::srv::builder::Init_FullName_Event_info();
}

}  // namespace full_name_message

#endif  // FULL_NAME_MESSAGE__SRV__DETAIL__FULL_NAME__BUILDER_HPP_
