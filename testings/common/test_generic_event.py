import unittest

from common.generic_event import GenericEvent

class GenericEventTest(unittest.TestCase):

    def setUp(self) -> None:
        self.counter = 0

    def event_handler1(self, data):
        print(data)
        self.counter += 1

    def event_handler2(self, data):
        print(data)
        self.counter += 1

    def test_registration_and_invocation(self):
        self.my_event = GenericEvent()

        self.my_event.register(lambda data: print(data))
        self.assertEqual(self.my_event.handlers_count(), 1)

        self.my_event.register(self.event_handler1)
        self.my_event += self.event_handler2
        self.assertEqual(self.my_event.handlers_count(), 3)

        self.my_event.raise_event('some data')
        self.assertEqual(self.counter, 2)

        self.assertTrue(self.my_event.is_registered(self.event_handler1))
        self.my_event -= self.event_handler1
        self.assertFalse(self.my_event.is_registered(self.event_handler1))
        self.assertEqual(self.my_event.handlers_count(), 2)

        self.my_event.clear()
        self.assertEqual(self.my_event.handlers_count(), 0)
        self.assertFalse(self.my_event.is_registered(self.event_handler2))
