import unittest
from unittest.mock import Mock, patch
import datetime
from typing import Any
from requests.exceptions import Timeout
from calander import (
    is_weekday as calander_is_weekday,
    get_holidays as calander_get_holidays,
)

mock = Mock()
# <Mock id='4394778696'>

# >>> mock.some_attribute
# <Mock name='mock.some_attribute' id='4394778696'>

# >>> mock.do_something()
# <Mock name='mock.do_something()' id='4394778920'>

# >>> mock.dumps()
# <Mock name='mock.dumps()' id='4392249776'>
# * Mocked method requires no arguments. In fact, it will accept any arguments that you pass to it.
# * The return value of dumps() is also a Mock.

# >>> mock.loads('{"k": "v"}').get('k')
# <Mock name='mock.loads().get()' id='4379599424'>


# Assertions and Inspection
mock_json = '{"key": "value"}'
mock.loads(mock_json)

mock.loads.assert_called()
mock.loads.assert_called_once()
mock.loads.assert_called_with(mock_json)
mock.loads.assert_called_once_with(mock_json)
# mock.loads.assert_not_called() # AssertionError: Expected 'loads' to not have been called. Called 1 times
assert mock.loads.call_count == 1


# Managing a Mock’s Return Value
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

# mock datetime package
datetime = Mock()


def is_weekday():
    today = datetime.datetime.today()
    return 0 <= today.weekday() < 5


# mock .today() to return Tuesday
datetime.datetime.today.return_value = tuesday
assert is_weekday() is True

# mock .today() to return Saturday
datetime.datetime.today.return_value = saturday
assert not is_weekday()


# Managing a Mock’s Side Effects
# You can control your code’s behavior by specifying a mocked function’s side effects.
# A .side_effect defines what happens when you call the mocked function.
requests = Mock()


def get_holidays() -> dict[str, Any] | None:
    # print(4)
    req = requests.get("http://localhost:8081/api/holidays")
    # print(5)
    if req.status_code == 200:
        # print(6)
        return req.json()
    # print(7)


class TestGetHolidayInSameFile(unittest.TestCase):
    def test_get_holidays_timeout(self):
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()

    def log_request(self, url: str) -> Mock:
        # logging a fake request for testing output purpose
        # print("Starting log_request ...")
        # print(f"Making a request to a {url=}")

        # Creating a new Mock to immitate a Response
        response_mock = Mock()
        # print("Creating a mock response.")
        response_mock.status_code = 200
        # print("Assigning a status code of 200")
        response_mock.json.return_value = {"12/25": "Remember", "17/04": "Ignore"}
        # print("Assigning a json return response.")
        return response_mock

    def test_get_holidays_successful_with_logging(self):
        # print(1)
        requests.get.side_effect = self.log_request
        # print(2)
        return_value = get_holidays()
        # print(3)
        assert return_value == {"12/25": "Remember", "17/04": "Ignore"}

    def test_get_holidays_retry(self):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {"message": "Holiday!"}

        requests.get.side_effect = [Timeout, response_mock]
        with self.assertRaises(Timeout):
            get_holidays()

        return_value = get_holidays()
        assert return_value == {"message": "Holiday!"}
        assert requests.get.call_count == 2


# Configuring Your Mock
# You can configure a Mock to set up some of the object’s behaviors.
# Some configurable members include .side_effect, .return_value, and .name.
mock = Mock(side_effect=Exception)
# mock()

mock = Mock(name="todo mocker")
# mock.name

mock = Mock(return_value=True)
# mock()


# patch()
# unittest.mock provides a powerful mechanism for mocking objects, called patch(),
# which looks up an object in a given module and replaces that object with a Mock.
# If you want to mock an object for the duration of your entire test function, you
# can use patch() as a function decorator.

# Up to this point, you’ve monkey patched objects in the file in which they exist.
# Monkey patching is the replacement of one object with another at runtime.
# Now, you’ll use patch() to replace your objects in calendar.py:


class TestGetHolidayInModule(unittest.TestCase):
    @patch("calander.requests")
    def test_calander_timeout(self, mock_requests):

        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            calander_get_holidays()

        mock_requests.get.assert_called_once()


# Technical Detail: patch() returns an instance of MagicMock, which is a Mock subclass.
# MagicMock is useful because it implements most magic methods for you, such as
# .__len__(), .__str__(), and .__iter__(), with reasonable defaults.


# Patching an Object’s Attributes
# Let’s say you only want to mock one method of an object instead of the entire object.
# You can do so by using patch.object().
# class TestGetHolidayInModuleWithPatchingObjects(unittest.TestCase):
#     @patch.object(requests, attribute="get", side_effect=Timeout)
#     def test_calander_timeout(self, mock_requests):
#         with self.assertRaises(Timeout):
#             calander_get_holidays()


# Avoiding Common Problems Using Specifications
# When configuring a Mock, you can pass an object specification to the spec parameter.
# If you attempt to access an attribute that does not belong to the specification,
# Mock will raise an AttributeError:
calender = Mock(spec=["is_weekday", "get_holidays"])
# >>> calendar.is_weekday()
# <Mock name='mock.is_weekday()' id='4569015856'>

# >>> calendar.create_event()
# AttributeError: Mock object has no attribute 'create_event'
if __name__ == "__main__":
    unittest.main()


# References:
# - https://realpython.com/python-mock-library/
