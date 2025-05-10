import pytest
from lesson_10.homework_10 import log_event

LOG_FILE = 'login_system.log'

class TestLogEvent:

    def test_log_event_success(self):
        log_event(username='username1', status='success')
        with open(LOG_FILE, 'r') as f:
            log_content = f.read()
        assert 'INFO - Login event - Username: username1, Status: success' in log_content
        assert 'WARNING - Login event - Username: username1, Status: success' not in log_content
        assert 'ERROR - Login event - Username: username1, Status: success' not in log_content
        assert 'username1' in log_content
        assert 'success' in log_content

    def test_log_event_expired(self):
        log_event(username='username2', status='expired')
        with open(LOG_FILE, 'r') as f:
            log_content = f.read()
        assert 'WARNING - Login event - Username: username2, Status: expired' in log_content
        assert 'INFO - Login event - Username: username2, Status: expired' not in log_content
        assert 'ERROR - Login event - Username: username2, Status: expired' not in log_content
        assert 'username2' in log_content
        assert 'expired' in log_content

    def test_log_event_empty_username(self):
        log_event(username='', status='success')
        with open(LOG_FILE, 'r') as f:
            log_content = f.read()
        assert 'INFO - Login event - Username: , Status: success' in log_content
        assert 'WARNING- Login event - Username: , Status: success' not in log_content
        assert 'ERROR - Login event - Username: , Status: success' not in log_content
        assert 'Username: ' in log_content
        assert 'success' in log_content

    def test_log_event_empty_status(self):
        log_event(username='username3', status='')
        with open(LOG_FILE, 'r') as f:
            log_content = f.read()
        assert 'ERROR - Login event - Username: username3, Status: ' in log_content
        assert 'WARNING - Login event - Username: username3, Status: ' not in log_content
        assert 'INFO - Login event - Username: username3, Status: ' not in log_content
        assert 'username3' in log_content
        assert 'Status: ' in log_content

    def test_log_event_empty_all(self):
        log_event(username='', status='')
        with open(LOG_FILE, 'r') as f:
            log_content = f.read()
        assert 'ERROR - Login event - Username: , Status: ' in log_content
        assert 'WARNING - Login event - Username: , Status: ' not in log_content
        assert 'Username: ' in log_content
        assert 'Status: ' in log_content


if __name__ == '__main__':
    pytest.main()