# generated from rosidl_generator_py/resource/_idl.py.em
# with input from action_cleaning_robot:action/CleaningTask.idl
# generated code does not contain a copyright notice

from __future__ import annotations

import collections.abc
from os import getenv
import typing

# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
ros_python_check_fields = getenv('ROS_PYTHON_CHECK_FIELDS', default='')


if typing.TYPE_CHECKING:
    from ctypes import Structure

    class PyCapsule(Structure):
        pass  # don't need to define the full structure


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_CleaningTask_Goal(type):
    """Metaclass of message 'CleaningTask_Goal'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class CleaningTask_GoalConstants(typing.TypedDict):
        pass

    __constants: CleaningTask_GoalConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('action_cleaning_robot')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'action_cleaning_robot.action.CleaningTask_Goal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__cleaning_task__goal
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__cleaning_task__goal
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__cleaning_task__goal
            cls._TYPE_SUPPORT = module.type_support_msg__action__cleaning_task__goal
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__cleaning_task__goal

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CleaningTask_Goal(metaclass=Metaclass_CleaningTask_Goal):
    """Message class 'CleaningTask_Goal'."""

    __slots__ = [
        '_task_type',
        '_area_size',
        '_target_x',
        '_target_y',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'task_type': 'string',
        'area_size': 'double',
        'target_x': 'double',
        'target_y': 'double',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, *,
                 task_type: typing.Optional[str] = None,  # noqa: E501
                 area_size: typing.Optional[float] = None,  # noqa: E501
                 target_x: typing.Optional[float] = None,  # noqa: E501
                 target_y: typing.Optional[float] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.task_type = task_type if task_type is not None else str()
        self.area_size = area_size if area_size is not None else float()
        self.target_x = target_x if target_x is not None else float()
        self.target_y = target_y if target_y is not None else float()

    def __repr__(self) -> str:
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args: list[str] = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CleaningTask_Goal):
            return False
        if self.task_type != other.task_type:
            return False
        if self.area_size != other.area_size:
            return False
        if self.target_x != other.target_x:
            return False
        if self.target_y != other.target_y:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def task_type(self) -> str:
        """Message field 'task_type'."""
        return self._task_type

    @task_type.setter
    def task_type(self, value: str) -> None:
        if self._check_fields:
            assert \
                isinstance(value, str), \
                "The 'task_type' field must be of type 'str'"
        self._task_type = value

    @builtins.property
    def area_size(self) -> float:
        """Message field 'area_size'."""
        return self._area_size

    @area_size.setter
    def area_size(self, value: float) -> None:
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'area_size' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'area_size' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._area_size = value

    @builtins.property
    def target_x(self) -> float:
        """Message field 'target_x'."""
        return self._target_x

    @target_x.setter
    def target_x(self, value: float) -> None:
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'target_x' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'target_x' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._target_x = value

    @builtins.property
    def target_y(self) -> float:
        """Message field 'target_y'."""
        return self._target_y

    @target_y.setter
    def target_y(self, value: float) -> None:
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'target_y' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'target_y' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._target_y = value


if typing.TYPE_CHECKING:
    pass


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import math

# already imported above
# import rosidl_parser.definition


class Metaclass_CleaningTask_Result(type):
    """Metaclass of message 'CleaningTask_Result'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class CleaningTask_ResultConstants(typing.TypedDict):
        pass

    __constants: CleaningTask_ResultConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('action_cleaning_robot')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'action_cleaning_robot.action.CleaningTask_Result')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__cleaning_task__result
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__cleaning_task__result
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__cleaning_task__result
            cls._TYPE_SUPPORT = module.type_support_msg__action__cleaning_task__result
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__cleaning_task__result

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CleaningTask_Result(metaclass=Metaclass_CleaningTask_Result):
    """Message class 'CleaningTask_Result'."""

    __slots__ = [
        '_success',
        '_cleaned_points',
        '_total_distance',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'success': 'boolean',
        'cleaned_points': 'int32',
        'total_distance': 'double',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, *,
                 success: typing.Optional[bool] = None,  # noqa: E501
                 cleaned_points: typing.Optional[int] = None,  # noqa: E501
                 total_distance: typing.Optional[float] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.success = success if success is not None else bool()
        self.cleaned_points = cleaned_points if cleaned_points is not None else int()
        self.total_distance = total_distance if total_distance is not None else float()

    def __repr__(self) -> str:
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args: list[str] = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CleaningTask_Result):
            return False
        if self.success != other.success:
            return False
        if self.cleaned_points != other.cleaned_points:
            return False
        if self.total_distance != other.total_distance:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def success(self) -> bool:
        """Message field 'success'."""
        return self._success

    @success.setter
    def success(self, value: bool) -> None:
        if self._check_fields:
            assert \
                isinstance(value, bool), \
                "The 'success' field must be of type 'bool'"
        self._success = value

    @builtins.property
    def cleaned_points(self) -> int:
        """Message field 'cleaned_points'."""
        return self._cleaned_points

    @cleaned_points.setter
    def cleaned_points(self, value: int) -> None:
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'cleaned_points' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'cleaned_points' field must be an integer in [-2147483648, 2147483647]"
        self._cleaned_points = value

    @builtins.property
    def total_distance(self) -> float:
        """Message field 'total_distance'."""
        return self._total_distance

    @total_distance.setter
    def total_distance(self, value: float) -> None:
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'total_distance' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'total_distance' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._total_distance = value


if typing.TYPE_CHECKING:
    pass


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import math

# already imported above
# import rosidl_parser.definition


class Metaclass_CleaningTask_Feedback(type):
    """Metaclass of message 'CleaningTask_Feedback'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class CleaningTask_FeedbackConstants(typing.TypedDict):
        pass

    __constants: CleaningTask_FeedbackConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('action_cleaning_robot')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'action_cleaning_robot.action.CleaningTask_Feedback')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__cleaning_task__feedback
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__cleaning_task__feedback
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__cleaning_task__feedback
            cls._TYPE_SUPPORT = module.type_support_msg__action__cleaning_task__feedback
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__cleaning_task__feedback

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CleaningTask_Feedback(metaclass=Metaclass_CleaningTask_Feedback):
    """Message class 'CleaningTask_Feedback'."""

    __slots__ = [
        '_progress_percent',
        '_current_cleaned_points',
        '_current_x',
        '_current_y',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'progress_percent': 'int32',
        'current_cleaned_points': 'int32',
        'current_x': 'double',
        'current_y': 'double',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, *,
                 progress_percent: typing.Optional[int] = None,  # noqa: E501
                 current_cleaned_points: typing.Optional[int] = None,  # noqa: E501
                 current_x: typing.Optional[float] = None,  # noqa: E501
                 current_y: typing.Optional[float] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.progress_percent = progress_percent if progress_percent is not None else int()
        self.current_cleaned_points = current_cleaned_points if current_cleaned_points is not None else int()
        self.current_x = current_x if current_x is not None else float()
        self.current_y = current_y if current_y is not None else float()

    def __repr__(self) -> str:
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args: list[str] = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CleaningTask_Feedback):
            return False
        if self.progress_percent != other.progress_percent:
            return False
        if self.current_cleaned_points != other.current_cleaned_points:
            return False
        if self.current_x != other.current_x:
            return False
        if self.current_y != other.current_y:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def progress_percent(self) -> int:
        """Message field 'progress_percent'."""
        return self._progress_percent

    @progress_percent.setter
    def progress_percent(self, value: int) -> None:
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'progress_percent' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'progress_percent' field must be an integer in [-2147483648, 2147483647]"
        self._progress_percent = value

    @builtins.property
    def current_cleaned_points(self) -> int:
        """Message field 'current_cleaned_points'."""
        return self._current_cleaned_points

    @current_cleaned_points.setter
    def current_cleaned_points(self, value: int) -> None:
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'current_cleaned_points' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'current_cleaned_points' field must be an integer in [-2147483648, 2147483647]"
        self._current_cleaned_points = value

    @builtins.property
    def current_x(self) -> float:
        """Message field 'current_x'."""
        return self._current_x

    @current_x.setter
    def current_x(self, value: float) -> None:
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'current_x' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'current_x' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._current_x = value

    @builtins.property
    def current_y(self) -> float:
        """Message field 'current_y'."""
        return self._current_y

    @current_y.setter
    def current_y(self, value: float) -> None:
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'current_y' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'current_y' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._current_y = value


if typing.TYPE_CHECKING:
    from unique_identifier_msgs.msg import UUID


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_CleaningTask_SendGoal_Request(type):
    """Metaclass of message 'CleaningTask_SendGoal_Request'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class CleaningTask_SendGoal_RequestConstants(typing.TypedDict):
        pass

    __constants: CleaningTask_SendGoal_RequestConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('action_cleaning_robot')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'action_cleaning_robot.action.CleaningTask_SendGoal_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__cleaning_task__send_goal__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__cleaning_task__send_goal__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__cleaning_task__send_goal__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__cleaning_task__send_goal__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__cleaning_task__send_goal__request

            from action_cleaning_robot.action import CleaningTask
            if CleaningTask.Goal._TYPE_SUPPORT is None:
                CleaningTask.Goal.__import_type_support__()

            from unique_identifier_msgs.msg import UUID
            if UUID._TYPE_SUPPORT is None:
                UUID.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CleaningTask_SendGoal_Request(metaclass=Metaclass_CleaningTask_SendGoal_Request):
    """Message class 'CleaningTask_SendGoal_Request'."""

    __slots__ = [
        '_goal_id',
        '_goal',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'goal': 'action_cleaning_robot/CleaningTask_Goal',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['action_cleaning_robot', 'action'], 'CleaningTask_Goal'),  # noqa: E501
    )

    def __init__(self, *,
                 goal_id: typing.Optional[UUID] = None,  # noqa: E501
                 goal: typing.Optional[CleaningTask_Goal] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from unique_identifier_msgs.msg import UUID
        self.goal_id = goal_id if goal_id is not None else UUID()
        from action_cleaning_robot.action._cleaning_task import CleaningTask_Goal
        self.goal = goal if goal is not None else CleaningTask_Goal()

    def __repr__(self) -> str:
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args: list[str] = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CleaningTask_SendGoal_Request):
            return False
        if self.goal_id != other.goal_id:
            return False
        if self.goal != other.goal:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self) -> UUID:
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value: UUID) -> None:
        if self._check_fields:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value

    @builtins.property
    def goal(self) -> CleaningTask_Goal:
        """Message field 'goal'."""
        return self._goal

    @goal.setter
    def goal(self, value: CleaningTask_Goal) -> None:
        if self._check_fields:
            from action_cleaning_robot.action._cleaning_task import CleaningTask_Goal
            assert \
                isinstance(value, CleaningTask_Goal), \
                "The 'goal' field must be a sub message of type 'CleaningTask_Goal'"
        self._goal = value


if typing.TYPE_CHECKING:
    from builtin_interfaces.msg import Time


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_CleaningTask_SendGoal_Response(type):
    """Metaclass of message 'CleaningTask_SendGoal_Response'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class CleaningTask_SendGoal_ResponseConstants(typing.TypedDict):
        pass

    __constants: CleaningTask_SendGoal_ResponseConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('action_cleaning_robot')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'action_cleaning_robot.action.CleaningTask_SendGoal_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__cleaning_task__send_goal__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__cleaning_task__send_goal__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__cleaning_task__send_goal__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__cleaning_task__send_goal__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__cleaning_task__send_goal__response

            from builtin_interfaces.msg import Time
            if Time._TYPE_SUPPORT is None:
                Time.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CleaningTask_SendGoal_Response(metaclass=Metaclass_CleaningTask_SendGoal_Response):
    """Message class 'CleaningTask_SendGoal_Response'."""

    __slots__ = [
        '_accepted',
        '_stamp',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'accepted': 'boolean',
        'stamp': 'builtin_interfaces/Time',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
    )

    def __init__(self, *,
                 accepted: typing.Optional[bool] = None,  # noqa: E501
                 stamp: typing.Optional[Time] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.accepted = accepted if accepted is not None else bool()
        from builtin_interfaces.msg import Time
        self.stamp = stamp if stamp is not None else Time()

    def __repr__(self) -> str:
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args: list[str] = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CleaningTask_SendGoal_Response):
            return False
        if self.accepted != other.accepted:
            return False
        if self.stamp != other.stamp:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def accepted(self) -> bool:
        """Message field 'accepted'."""
        return self._accepted

    @accepted.setter
    def accepted(self, value: bool) -> None:
        if self._check_fields:
            assert \
                isinstance(value, bool), \
                "The 'accepted' field must be of type 'bool'"
        self._accepted = value

    @builtins.property
    def stamp(self) -> Time:
        """Message field 'stamp'."""
        return self._stamp

    @stamp.setter
    def stamp(self, value: Time) -> None:
        if self._check_fields:
            from builtin_interfaces.msg import Time
            assert \
                isinstance(value, Time), \
                "The 'stamp' field must be a sub message of type 'Time'"
        self._stamp = value


if typing.TYPE_CHECKING:
    from service_msgs.msg import ServiceEventInfo
    import collections


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_CleaningTask_SendGoal_Event(type):
    """Metaclass of message 'CleaningTask_SendGoal_Event'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class CleaningTask_SendGoal_EventConstants(typing.TypedDict):
        pass

    __constants: CleaningTask_SendGoal_EventConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('action_cleaning_robot')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'action_cleaning_robot.action.CleaningTask_SendGoal_Event')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__cleaning_task__send_goal__event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__cleaning_task__send_goal__event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__cleaning_task__send_goal__event
            cls._TYPE_SUPPORT = module.type_support_msg__action__cleaning_task__send_goal__event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__cleaning_task__send_goal__event

            from service_msgs.msg import ServiceEventInfo
            if ServiceEventInfo._TYPE_SUPPORT is None:
                ServiceEventInfo.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CleaningTask_SendGoal_Event(metaclass=Metaclass_CleaningTask_SendGoal_Event):
    """Message class 'CleaningTask_SendGoal_Event'."""

    __slots__ = [
        '_info',
        '_request',
        '_response',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'info': 'service_msgs/ServiceEventInfo',
        'request': 'sequence<action_cleaning_robot/CleaningTask_SendGoal_Request, 1>',
        'response': 'sequence<action_cleaning_robot/CleaningTask_SendGoal_Response, 1>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['service_msgs', 'msg'], 'ServiceEventInfo'),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['action_cleaning_robot', 'action'], 'CleaningTask_SendGoal_Request'), 1),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['action_cleaning_robot', 'action'], 'CleaningTask_SendGoal_Response'), 1),  # noqa: E501
    )

    def __init__(self, *,
                 info: typing.Optional[ServiceEventInfo] = None,  # noqa: E501
                 request: typing.Optional[typing.Union[collections.abc.Sequence[CleaningTask_SendGoal_Request], collections.abc.Set[CleaningTask_SendGoal_Request], collections.UserList[CleaningTask_SendGoal_Request]]] = None,  # noqa: E501
                 response: typing.Optional[typing.Union[collections.abc.Sequence[CleaningTask_SendGoal_Response], collections.abc.Set[CleaningTask_SendGoal_Response], collections.UserList[CleaningTask_SendGoal_Response]]] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from service_msgs.msg import ServiceEventInfo
        self.info = info if info is not None else ServiceEventInfo()
        self.request = request if request is not None else []
        self.response = response if response is not None else []

    def __repr__(self) -> str:
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args: list[str] = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CleaningTask_SendGoal_Event):
            return False
        if self.info != other.info:
            return False
        if self.request != other.request:
            return False
        if self.response != other.response:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def info(self) -> ServiceEventInfo:
        """Message field 'info'."""
        return self._info

    @info.setter
    def info(self, value: ServiceEventInfo) -> None:
        if self._check_fields:
            from service_msgs.msg import ServiceEventInfo
            assert \
                isinstance(value, ServiceEventInfo), \
                "The 'info' field must be a sub message of type 'ServiceEventInfo'"
        self._info = value

    @builtins.property
    def request(self) -> typing.Union[collections.abc.Sequence[CleaningTask_SendGoal_Request], collections.abc.Set[CleaningTask_SendGoal_Request], collections.UserList[CleaningTask_SendGoal_Request]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'request'."""
        return self._request

    @request.setter
    def request(self, value: typing.Union[collections.abc.Sequence[CleaningTask_SendGoal_Request], collections.abc.Set[CleaningTask_SendGoal_Request], collections.UserList[CleaningTask_SendGoal_Request]]) -> None:
        if self._check_fields:
            from action_cleaning_robot.action import CleaningTask_SendGoal_Request
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) <= 1 and
                 all(isinstance(v, CleaningTask_SendGoal_Request) for v in value) and
                 True), \
                "The 'request' field must be a set or sequence with length <= 1 and each value of type 'CleaningTask_SendGoal_Request'"
        self._request = value

    @builtins.property
    def response(self) -> typing.Union[collections.abc.Sequence[CleaningTask_SendGoal_Response], collections.abc.Set[CleaningTask_SendGoal_Response], collections.UserList[CleaningTask_SendGoal_Response]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value: typing.Union[collections.abc.Sequence[CleaningTask_SendGoal_Response], collections.abc.Set[CleaningTask_SendGoal_Response], collections.UserList[CleaningTask_SendGoal_Response]]) -> None:
        if self._check_fields:
            from action_cleaning_robot.action import CleaningTask_SendGoal_Response
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) <= 1 and
                 all(isinstance(v, CleaningTask_SendGoal_Response) for v in value) and
                 True), \
                "The 'response' field must be a set or sequence with length <= 1 and each value of type 'CleaningTask_SendGoal_Response'"
        self._response = value


class Metaclass_CleaningTask_SendGoal(type):
    """Metaclass of service 'CleaningTask_SendGoal'."""

    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('action_cleaning_robot')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'action_cleaning_robot.action.CleaningTask_SendGoal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__cleaning_task__send_goal

            from action_cleaning_robot.action import _cleaning_task
            if _cleaning_task.Metaclass_CleaningTask_SendGoal_Request._TYPE_SUPPORT is None:
                _cleaning_task.Metaclass_CleaningTask_SendGoal_Request.__import_type_support__()
            if _cleaning_task.Metaclass_CleaningTask_SendGoal_Response._TYPE_SUPPORT is None:
                _cleaning_task.Metaclass_CleaningTask_SendGoal_Response.__import_type_support__()
            if _cleaning_task.Metaclass_CleaningTask_SendGoal_Event._TYPE_SUPPORT is None:
                _cleaning_task.Metaclass_CleaningTask_SendGoal_Event.__import_type_support__()


class CleaningTask_SendGoal(metaclass=Metaclass_CleaningTask_SendGoal):
    from action_cleaning_robot.action._cleaning_task import CleaningTask_SendGoal_Request as Request
    from action_cleaning_robot.action._cleaning_task import CleaningTask_SendGoal_Response as Response
    from action_cleaning_robot.action._cleaning_task import CleaningTask_SendGoal_Event as Event

    # type ignore below fixed in mypy 1.0+ see mypy#10342
    def __init__(self) -> typing.NoReturn:  # type: ignore
        raise NotImplementedError('Service classes can not be instantiated')


if typing.TYPE_CHECKING:
    pass


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_CleaningTask_GetResult_Request(type):
    """Metaclass of message 'CleaningTask_GetResult_Request'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class CleaningTask_GetResult_RequestConstants(typing.TypedDict):
        pass

    __constants: CleaningTask_GetResult_RequestConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('action_cleaning_robot')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'action_cleaning_robot.action.CleaningTask_GetResult_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__cleaning_task__get_result__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__cleaning_task__get_result__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__cleaning_task__get_result__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__cleaning_task__get_result__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__cleaning_task__get_result__request

            from unique_identifier_msgs.msg import UUID
            if UUID._TYPE_SUPPORT is None:
                UUID.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CleaningTask_GetResult_Request(metaclass=Metaclass_CleaningTask_GetResult_Request):
    """Message class 'CleaningTask_GetResult_Request'."""

    __slots__ = [
        '_goal_id',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'goal_id': 'unique_identifier_msgs/UUID',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
    )

    def __init__(self, *,
                 goal_id: typing.Optional[UUID] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from unique_identifier_msgs.msg import UUID
        self.goal_id = goal_id if goal_id is not None else UUID()

    def __repr__(self) -> str:
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args: list[str] = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CleaningTask_GetResult_Request):
            return False
        if self.goal_id != other.goal_id:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self) -> UUID:
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value: UUID) -> None:
        if self._check_fields:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value


if typing.TYPE_CHECKING:
    pass


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_CleaningTask_GetResult_Response(type):
    """Metaclass of message 'CleaningTask_GetResult_Response'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class CleaningTask_GetResult_ResponseConstants(typing.TypedDict):
        pass

    __constants: CleaningTask_GetResult_ResponseConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('action_cleaning_robot')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'action_cleaning_robot.action.CleaningTask_GetResult_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__cleaning_task__get_result__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__cleaning_task__get_result__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__cleaning_task__get_result__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__cleaning_task__get_result__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__cleaning_task__get_result__response

            from action_cleaning_robot.action import CleaningTask
            if CleaningTask.Result._TYPE_SUPPORT is None:
                CleaningTask.Result.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CleaningTask_GetResult_Response(metaclass=Metaclass_CleaningTask_GetResult_Response):
    """Message class 'CleaningTask_GetResult_Response'."""

    __slots__ = [
        '_status',
        '_result',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'status': 'int8',
        'result': 'action_cleaning_robot/CleaningTask_Result',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['action_cleaning_robot', 'action'], 'CleaningTask_Result'),  # noqa: E501
    )

    def __init__(self, *,
                 status: typing.Optional[int] = None,  # noqa: E501
                 result: typing.Optional[CleaningTask_Result] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.status = status if status is not None else int()
        from action_cleaning_robot.action._cleaning_task import CleaningTask_Result
        self.result = result if result is not None else CleaningTask_Result()

    def __repr__(self) -> str:
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args: list[str] = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CleaningTask_GetResult_Response):
            return False
        if self.status != other.status:
            return False
        if self.result != other.result:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def status(self) -> int:
        """Message field 'status'."""
        return self._status

    @status.setter
    def status(self, value: int) -> None:
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'status' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'status' field must be an integer in [-128, 127]"
        self._status = value

    @builtins.property
    def result(self) -> CleaningTask_Result:
        """Message field 'result'."""
        return self._result

    @result.setter
    def result(self, value: CleaningTask_Result) -> None:
        if self._check_fields:
            from action_cleaning_robot.action._cleaning_task import CleaningTask_Result
            assert \
                isinstance(value, CleaningTask_Result), \
                "The 'result' field must be a sub message of type 'CleaningTask_Result'"
        self._result = value


if typing.TYPE_CHECKING:
    pass


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_CleaningTask_GetResult_Event(type):
    """Metaclass of message 'CleaningTask_GetResult_Event'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class CleaningTask_GetResult_EventConstants(typing.TypedDict):
        pass

    __constants: CleaningTask_GetResult_EventConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('action_cleaning_robot')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'action_cleaning_robot.action.CleaningTask_GetResult_Event')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__cleaning_task__get_result__event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__cleaning_task__get_result__event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__cleaning_task__get_result__event
            cls._TYPE_SUPPORT = module.type_support_msg__action__cleaning_task__get_result__event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__cleaning_task__get_result__event

            from service_msgs.msg import ServiceEventInfo
            if ServiceEventInfo._TYPE_SUPPORT is None:
                ServiceEventInfo.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CleaningTask_GetResult_Event(metaclass=Metaclass_CleaningTask_GetResult_Event):
    """Message class 'CleaningTask_GetResult_Event'."""

    __slots__ = [
        '_info',
        '_request',
        '_response',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'info': 'service_msgs/ServiceEventInfo',
        'request': 'sequence<action_cleaning_robot/CleaningTask_GetResult_Request, 1>',
        'response': 'sequence<action_cleaning_robot/CleaningTask_GetResult_Response, 1>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['service_msgs', 'msg'], 'ServiceEventInfo'),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['action_cleaning_robot', 'action'], 'CleaningTask_GetResult_Request'), 1),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['action_cleaning_robot', 'action'], 'CleaningTask_GetResult_Response'), 1),  # noqa: E501
    )

    def __init__(self, *,
                 info: typing.Optional[ServiceEventInfo] = None,  # noqa: E501
                 request: typing.Optional[typing.Union[collections.abc.Sequence[CleaningTask_GetResult_Request], collections.abc.Set[CleaningTask_GetResult_Request], collections.UserList[CleaningTask_GetResult_Request]]] = None,  # noqa: E501
                 response: typing.Optional[typing.Union[collections.abc.Sequence[CleaningTask_GetResult_Response], collections.abc.Set[CleaningTask_GetResult_Response], collections.UserList[CleaningTask_GetResult_Response]]] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from service_msgs.msg import ServiceEventInfo
        self.info = info if info is not None else ServiceEventInfo()
        self.request = request if request is not None else []
        self.response = response if response is not None else []

    def __repr__(self) -> str:
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args: list[str] = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CleaningTask_GetResult_Event):
            return False
        if self.info != other.info:
            return False
        if self.request != other.request:
            return False
        if self.response != other.response:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def info(self) -> ServiceEventInfo:
        """Message field 'info'."""
        return self._info

    @info.setter
    def info(self, value: ServiceEventInfo) -> None:
        if self._check_fields:
            from service_msgs.msg import ServiceEventInfo
            assert \
                isinstance(value, ServiceEventInfo), \
                "The 'info' field must be a sub message of type 'ServiceEventInfo'"
        self._info = value

    @builtins.property
    def request(self) -> typing.Union[collections.abc.Sequence[CleaningTask_GetResult_Request], collections.abc.Set[CleaningTask_GetResult_Request], collections.UserList[CleaningTask_GetResult_Request]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'request'."""
        return self._request

    @request.setter
    def request(self, value: typing.Union[collections.abc.Sequence[CleaningTask_GetResult_Request], collections.abc.Set[CleaningTask_GetResult_Request], collections.UserList[CleaningTask_GetResult_Request]]) -> None:
        if self._check_fields:
            from action_cleaning_robot.action import CleaningTask_GetResult_Request
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) <= 1 and
                 all(isinstance(v, CleaningTask_GetResult_Request) for v in value) and
                 True), \
                "The 'request' field must be a set or sequence with length <= 1 and each value of type 'CleaningTask_GetResult_Request'"
        self._request = value

    @builtins.property
    def response(self) -> typing.Union[collections.abc.Sequence[CleaningTask_GetResult_Response], collections.abc.Set[CleaningTask_GetResult_Response], collections.UserList[CleaningTask_GetResult_Response]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value: typing.Union[collections.abc.Sequence[CleaningTask_GetResult_Response], collections.abc.Set[CleaningTask_GetResult_Response], collections.UserList[CleaningTask_GetResult_Response]]) -> None:
        if self._check_fields:
            from action_cleaning_robot.action import CleaningTask_GetResult_Response
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) <= 1 and
                 all(isinstance(v, CleaningTask_GetResult_Response) for v in value) and
                 True), \
                "The 'response' field must be a set or sequence with length <= 1 and each value of type 'CleaningTask_GetResult_Response'"
        self._response = value


class Metaclass_CleaningTask_GetResult(type):
    """Metaclass of service 'CleaningTask_GetResult'."""

    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('action_cleaning_robot')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'action_cleaning_robot.action.CleaningTask_GetResult')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__cleaning_task__get_result

            from action_cleaning_robot.action import _cleaning_task
            if _cleaning_task.Metaclass_CleaningTask_GetResult_Request._TYPE_SUPPORT is None:
                _cleaning_task.Metaclass_CleaningTask_GetResult_Request.__import_type_support__()
            if _cleaning_task.Metaclass_CleaningTask_GetResult_Response._TYPE_SUPPORT is None:
                _cleaning_task.Metaclass_CleaningTask_GetResult_Response.__import_type_support__()
            if _cleaning_task.Metaclass_CleaningTask_GetResult_Event._TYPE_SUPPORT is None:
                _cleaning_task.Metaclass_CleaningTask_GetResult_Event.__import_type_support__()


class CleaningTask_GetResult(metaclass=Metaclass_CleaningTask_GetResult):
    from action_cleaning_robot.action._cleaning_task import CleaningTask_GetResult_Request as Request
    from action_cleaning_robot.action._cleaning_task import CleaningTask_GetResult_Response as Response
    from action_cleaning_robot.action._cleaning_task import CleaningTask_GetResult_Event as Event

    # type ignore below fixed in mypy 1.0+ see mypy#10342
    def __init__(self) -> typing.NoReturn:  # type: ignore
        raise NotImplementedError('Service classes can not be instantiated')


if typing.TYPE_CHECKING:
    pass


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_CleaningTask_FeedbackMessage(type):
    """Metaclass of message 'CleaningTask_FeedbackMessage'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class CleaningTask_FeedbackMessageConstants(typing.TypedDict):
        pass

    __constants: CleaningTask_FeedbackMessageConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('action_cleaning_robot')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'action_cleaning_robot.action.CleaningTask_FeedbackMessage')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__cleaning_task__feedback_message
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__cleaning_task__feedback_message
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__cleaning_task__feedback_message
            cls._TYPE_SUPPORT = module.type_support_msg__action__cleaning_task__feedback_message
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__cleaning_task__feedback_message

            from action_cleaning_robot.action import CleaningTask
            if CleaningTask.Feedback._TYPE_SUPPORT is None:
                CleaningTask.Feedback.__import_type_support__()

            from unique_identifier_msgs.msg import UUID
            if UUID._TYPE_SUPPORT is None:
                UUID.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CleaningTask_FeedbackMessage(metaclass=Metaclass_CleaningTask_FeedbackMessage):
    """Message class 'CleaningTask_FeedbackMessage'."""

    __slots__ = [
        '_goal_id',
        '_feedback',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'feedback': 'action_cleaning_robot/CleaningTask_Feedback',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['action_cleaning_robot', 'action'], 'CleaningTask_Feedback'),  # noqa: E501
    )

    def __init__(self, *,
                 goal_id: typing.Optional[UUID] = None,  # noqa: E501
                 feedback: typing.Optional[CleaningTask_Feedback] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from unique_identifier_msgs.msg import UUID
        self.goal_id = goal_id if goal_id is not None else UUID()
        from action_cleaning_robot.action._cleaning_task import CleaningTask_Feedback
        self.feedback = feedback if feedback is not None else CleaningTask_Feedback()

    def __repr__(self) -> str:
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args: list[str] = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CleaningTask_FeedbackMessage):
            return False
        if self.goal_id != other.goal_id:
            return False
        if self.feedback != other.feedback:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self) -> UUID:
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value: UUID) -> None:
        if self._check_fields:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value

    @builtins.property
    def feedback(self) -> CleaningTask_Feedback:
        """Message field 'feedback'."""
        return self._feedback

    @feedback.setter
    def feedback(self, value: CleaningTask_Feedback) -> None:
        if self._check_fields:
            from action_cleaning_robot.action._cleaning_task import CleaningTask_Feedback
            assert \
                isinstance(value, CleaningTask_Feedback), \
                "The 'feedback' field must be a sub message of type 'CleaningTask_Feedback'"
        self._feedback = value


class Metaclass_CleaningTask(type):
    """Metaclass of action 'CleaningTask'."""

    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('action_cleaning_robot')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'action_cleaning_robot.action.CleaningTask')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_action__action__cleaning_task

            from action_msgs.msg import _goal_status_array
            if _goal_status_array.Metaclass_GoalStatusArray._TYPE_SUPPORT is None:
                _goal_status_array.Metaclass_GoalStatusArray.__import_type_support__()
            from action_msgs.srv import _cancel_goal
            if _cancel_goal.Metaclass_CancelGoal._TYPE_SUPPORT is None:
                _cancel_goal.Metaclass_CancelGoal.__import_type_support__()

            from action_cleaning_robot.action import _cleaning_task
            if _cleaning_task.Metaclass_CleaningTask_SendGoal._TYPE_SUPPORT is None:
                _cleaning_task.Metaclass_CleaningTask_SendGoal.__import_type_support__()
            if _cleaning_task.Metaclass_CleaningTask_GetResult._TYPE_SUPPORT is None:
                _cleaning_task.Metaclass_CleaningTask_GetResult.__import_type_support__()
            if _cleaning_task.Metaclass_CleaningTask_FeedbackMessage._TYPE_SUPPORT is None:
                _cleaning_task.Metaclass_CleaningTask_FeedbackMessage.__import_type_support__()


class CleaningTask(metaclass=Metaclass_CleaningTask):

    # The goal message defined in the action definition.
    from action_cleaning_robot.action._cleaning_task import CleaningTask_Goal as Goal
    # The result message defined in the action definition.
    from action_cleaning_robot.action._cleaning_task import CleaningTask_Result as Result
    # The feedback message defined in the action definition.
    from action_cleaning_robot.action._cleaning_task import CleaningTask_Feedback as Feedback

    class Impl:

        # The send_goal service using a wrapped version of the goal message as a request.
        from action_cleaning_robot.action._cleaning_task import CleaningTask_SendGoal as SendGoalService
        # The get_result service using a wrapped version of the result message as a response.
        from action_cleaning_robot.action._cleaning_task import CleaningTask_GetResult as GetResultService
        # The feedback message with generic fields which wraps the feedback message.
        from action_cleaning_robot.action._cleaning_task import CleaningTask_FeedbackMessage as FeedbackMessage

        # The generic service to cancel a goal.
        from action_msgs.srv._cancel_goal import CancelGoal as CancelGoalService
        # The generic message for get the status of a goal.
        from action_msgs.msg._goal_status_array import GoalStatusArray as GoalStatusMessage

    # type ignore below fixed in mypy 1.0+ see mypy#10342
    def __init__(self) -> typing.NoReturn:  # type: ignore
        raise NotImplementedError('Action classes can not be instantiated')
