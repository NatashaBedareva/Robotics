// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from service_full_name:srv/SummFullName.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "service_full_name/srv/summ_full_name.hpp"


#ifndef SERVICE_FULL_NAME__SRV__DETAIL__SUMM_FULL_NAME__BUILDER_HPP_
#define SERVICE_FULL_NAME__SRV__DETAIL__SUMM_FULL_NAME__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "service_full_name/srv/detail/summ_full_name__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace service_full_name
{

namespace srv
{

namespace builder
{

class Init_SummFullName_Request_first_name
{
public:
  explicit Init_SummFullName_Request_first_name(::service_full_name::srv::SummFullName_Request & msg)
  : msg_(msg)
  {}
  ::service_full_name::srv::SummFullName_Request first_name(::service_full_name::srv::SummFullName_Request::_first_name_type arg)
  {
    msg_.first_name = std::move(arg);
    return std::move(msg_);
  }

private:
  ::service_full_name::srv::SummFullName_Request msg_;
};

class Init_SummFullName_Request_name
{
public:
  explicit Init_SummFullName_Request_name(::service_full_name::srv::SummFullName_Request & msg)
  : msg_(msg)
  {}
  Init_SummFullName_Request_first_name name(::service_full_name::srv::SummFullName_Request::_name_type arg)
  {
    msg_.name = std::move(arg);
    return Init_SummFullName_Request_first_name(msg_);
  }

private:
  ::service_full_name::srv::SummFullName_Request msg_;
};

class Init_SummFullName_Request_last_name
{
public:
  Init_SummFullName_Request_last_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SummFullName_Request_name last_name(::service_full_name::srv::SummFullName_Request::_last_name_type arg)
  {
    msg_.last_name = std::move(arg);
    return Init_SummFullName_Request_name(msg_);
  }

private:
  ::service_full_name::srv::SummFullName_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::service_full_name::srv::SummFullName_Request>()
{
  return service_full_name::srv::builder::Init_SummFullName_Request_last_name();
}

}  // namespace service_full_name


namespace service_full_name
{

namespace srv
{

namespace builder
{

class Init_SummFullName_Response_full_name
{
public:
  Init_SummFullName_Response_full_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::service_full_name::srv::SummFullName_Response full_name(::service_full_name::srv::SummFullName_Response::_full_name_type arg)
  {
    msg_.full_name = std::move(arg);
    return std::move(msg_);
  }

private:
  ::service_full_name::srv::SummFullName_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::service_full_name::srv::SummFullName_Response>()
{
  return service_full_name::srv::builder::Init_SummFullName_Response_full_name();
}

}  // namespace service_full_name


namespace service_full_name
{

namespace srv
{

namespace builder
{

class Init_SummFullName_Event_response
{
public:
  explicit Init_SummFullName_Event_response(::service_full_name::srv::SummFullName_Event & msg)
  : msg_(msg)
  {}
  ::service_full_name::srv::SummFullName_Event response(::service_full_name::srv::SummFullName_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::service_full_name::srv::SummFullName_Event msg_;
};

class Init_SummFullName_Event_request
{
public:
  explicit Init_SummFullName_Event_request(::service_full_name::srv::SummFullName_Event & msg)
  : msg_(msg)
  {}
  Init_SummFullName_Event_response request(::service_full_name::srv::SummFullName_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_SummFullName_Event_response(msg_);
  }

private:
  ::service_full_name::srv::SummFullName_Event msg_;
};

class Init_SummFullName_Event_info
{
public:
  Init_SummFullName_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SummFullName_Event_request info(::service_full_name::srv::SummFullName_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_SummFullName_Event_request(msg_);
  }

private:
  ::service_full_name::srv::SummFullName_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::service_full_name::srv::SummFullName_Event>()
{
  return service_full_name::srv::builder::Init_SummFullName_Event_info();
}

}  // namespace service_full_name

#endif  // SERVICE_FULL_NAME__SRV__DETAIL__SUMM_FULL_NAME__BUILDER_HPP_
