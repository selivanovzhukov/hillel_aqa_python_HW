import pytest
from lesson_16.homework_16_teamlead import TeamLead



class TestTeamLead:

    def test_team_lead_attributes(self):
        team_lead = TeamLead('John', 100000, 'Software Engineering', 'Python', 5)
        assert hasattr(team_lead, 'department')
        assert hasattr(team_lead, 'programming_language')

if __name__ == '__main__':
    pytest.main()