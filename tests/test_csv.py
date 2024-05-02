import pytest
from patterns.csv_utils import parse_file, Ride
from unittest.mock import patch, mock_open
from datetime import datetime

@pytest.fixture
def mock_csv_file():
    csv_content = """TaxiID,lpep_pickup_datetime,lpep_dropoff_datetime,passenger_count,trip_distance,total_amount
7339,2018-01-01 00:56:29,2018-01-01 01:04:44,2,1.22,8.3
353,2018-01-01 00:11:48,2018-01-01 00:30:13,1,4.67,18.3
"""
    with patch('builtins.open', mock_open(read_data=csv_content)) as mock_file:
        yield mock_file

def test_parse_file(mock_csv_file):
    rides = parse_file("taxi_data.csv")
    assert len(rides) == 2
    assert isinstance(rides[0], Ride)
    assert rides[0].pick_up_time == datetime(2018, 1, 1, 0, 56, 29)
    assert rides[0].tolls_amount == 8.3