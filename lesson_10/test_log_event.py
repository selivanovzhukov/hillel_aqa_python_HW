import unittest
import os
from lesson_10.homework_10 import log_event
import logging

LOG_FILE = 'login_system.log'

class TestLogEvent(unittest.TestCase):

    def setUp(self):
        logger = logging.getLogger("log_event")
        if logger.hasHandlers():
            logger.handlers.clear()
        try:
            with open(LOG_FILE, 'w'):
                pass
        except FileNotFoundError:
            pass

    @staticmethod
    def read_log_file():
        with open(LOG_FILE, 'r') as file:
            return file.read()

    def test_log_event_success(self):
        log_event(username='username1', status='success')
        log_content = self.read_log_file()
        self.assertIn('INFO Login event - Username: username1, Status: success', log_content)
        self.assertNotIn('WARNING', log_content)
        self.assertNotIn('ERROR', log_content)

    def test_log_event_expired(self):
        log_event(username='username2', status='expired')
        log_content = self.read_log_file()
        self.assertIn('WARNING Login event - Username: username2, Status: expired', log_content)
        self.assertNotIn('INFO', log_content)
        self.assertNotIn('ERROR', log_content)

    def test_log_event_empty_username(self):
        log_event(username='', status='success')
        log_content = self.read_log_file()
        self.assertIn('INFO Login event - Username: , Status: success', log_content)
        self.assertNotIn('WARNING', log_content)
        self.assertNotIn('ERROR', log_content)

    def test_log_event_empty_status(self):
        log_event(username='username3', status='')
        log_content = self.read_log_file()
        self.assertIn('ERROR Login event - Username: username3, Status: ', log_content)
        self.assertNotIn('WARNING', log_content)
        self.assertNotIn('INFO', log_content)

    def test_log_event_empty_all(self):
        log_event(username='', status='')
        log_content = self.read_log_file()
        self.assertIn('ERROR Login event - Username: , Status: ', log_content)
        self.assertNotIn('WARNING', log_content)
        self.assertNotIn('INFO', log_content)

if __name__ == '__main__':
    unittest.main()