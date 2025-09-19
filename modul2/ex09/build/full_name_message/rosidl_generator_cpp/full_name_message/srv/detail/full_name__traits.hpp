// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from full_name_message:srv/FullName.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "full_name_message/srv/full_name.hpp"


#ifndef FULL_NAME_MESSAGE__SRV__DETAIL__FULL_NAME__TRAITS_HPP_
#define FULL_NAME_MESSAGE__SRV__DETAIL__FULL_NAME__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "full_name_message/srv/detail/full_name__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace full_name_message
{

namespace srv
{

inline void to_flow_style_yaml(
  const FullName_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: last_name
  {
    out << "last_name: ";
    rosidl_generator_traits::value_to_yaml(msg.last_name, out);
    out << ", ";
  }

  // member: name
  {
    out << "name: ";
    rosidl_generator_traits::value_to_yaml(msg.name, out);
    out << ", ";
  }

  // member: first_name
  {
    out << "first_name: ";
    rosidl_generator_traits::value_to_yaml(msg.first_name, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const FullName_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: last_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "last_name: ";
    rosidl_generator_traits::value_to_yaml(msg.last_name, out);
    out << "\n";
  }

  // member: name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "name: ";
    rosidl_generator_traits::value_to_yaml(msg.name, out);
    out << "\n";
  }

  // member: first_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "first_name: ";
    rosidl_generator_traits::value_to_yaml(msg.first_name, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const FullName_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace full_name_message

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<full_name_message::srv::FullName_Request>()
{
  return "full_name_message::srv::FullName_Request";
}

template<>
inline const char * name<full_name_message::srv::FullName_Request>()
{
  return "full_name_message/srv/FullName_Request";
}

template<>
struct has_fixed_size<full_name_message::srv::FullName_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<full_name_message::srv::FullName_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<full_name_message::srv::FullName_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace full_name_message
{

namespace srv
{

inline void to_flow_style_yaml(
  const FullName_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: full_name
  {
    out << "full_name: ";
    rosidl_generator_traits::value_to_yaml(msg.full_name, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const FullName_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: full_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "full_name: ";
    rosidl_generator_traits::value_to_yaml(msg.full_name, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const FullName_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace full_name_message

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<full_name_message::srv::FullName_Response>()
{
  return "full_name_message::srv::FullName_Response";
}

template<>
inline const char * name<full_name_message::srv::FullName_Response>()
{
  return "full_name_message/srv/FullName_Response";
}

template<>
struct has_fixed_size<full_name_message::srv::FullName_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<full_name_message::srv::FullName_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<full_name_message::srv::FullName_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__traits.hpp"

namespace full_name_message
{

namespace srv
{

inline void to_flow_style_yaml(
  const FullName_Event & msg,
  std::ostream & out)
{
  out << "{";
  // member: info
  {
    out << "info: ";
    to_flow_style_yaml(msg.info, out);
    out << ", ";
  }

  // member: request
  {
    if (msg.request.size() == 0) {
      out << "request: []";
    } else {
      out << "request: [";
      size_t pending_items = msg.request.size();
      for (auto item : msg.request) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: response
  {
    if (msg.response.size() == 0) {
      out << "response: []";
    } else {
      out << "response: [";
      size_t pending_items = msg.response.size();
      for (auto item : msg.response) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const FullName_Event & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: info
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "info:\n";
    to_block_style_yaml(msg.info, out, indentation + 2);
  }

  // member: request
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.request.size() == 0) {
      out << "request: []\n";
    } else {
      out << "request:\n";
      for (auto item : msg.request) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: response
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.response.size() == 0) {
      out << "response: []\n";
    } else {
      out << "response:\n";
      for (auto item : msg.response) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const FullName_Event & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace full_name_message

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<full_name_message::srv::FullName_Event>()
{
  return "full_name_message::srv::FullName_Event";
}

template<>
inline const char * name<full_name_message::srv::FullName_Event>()
{
  return "full_name_message/srv/FullName_Event";
}

template<>
struct has_fixed_size<full_name_message::srv::FullName_Event>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<full_name_message::srv::FullName_Event>
  : std::integral_constant<bool, has_bounded_size<full_name_message::srv::FullName_Request>::value && has_bounded_size<full_name_message::srv::FullName_Response>::value && has_bounded_size<service_msgs::msg::ServiceEventInfo>::value> {};

template<>
struct is_message<full_name_message::srv::FullName_Event>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<full_name_message::srv::FullName>()
{
  return "full_name_message::srv::FullName";
}

template<>
inline const char * name<full_name_message::srv::FullName>()
{
  return "full_name_message/srv/FullName";
}

template<>
struct has_fixed_size<full_name_message::srv::FullName>
  : std::integral_constant<
    bool,
    has_fixed_size<full_name_message::srv::FullName_Request>::value &&
    has_fixed_size<full_name_message::srv::FullName_Response>::value
  >
{
};

template<>
struct has_bounded_size<full_name_message::srv::FullName>
  : std::integral_constant<
    bool,
    has_bounded_size<full_name_message::srv::FullName_Request>::value &&
    has_bounded_size<full_name_message::srv::FullName_Response>::value
  >
{
};

template<>
struct is_service<full_name_message::srv::FullName>
  : std::true_type
{
};

template<>
struct is_service_request<full_name_message::srv::FullName_Request>
  : std::true_type
{
};

template<>
struct is_service_response<full_name_message::srv::FullName_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // FULL_NAME_MESSAGE__SRV__DETAIL__FULL_NAME__TRAITS_HPP_
