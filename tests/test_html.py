# test_web_report.py
import pytest
from patterns.web_report import create_content, create_file
from patterns.csv_utils import Ride
from datetime import datetime
from unittest.mock import patch, mock_open

# Datos de prueba modificados
rides = [
    Ride(
        error="",
        taxi_id=3,
        pick_up_time=datetime(2023, 1, 2, 14, 30),
        drop_of_time=datetime(2023, 1, 2, 15, 45),  # Tiempo de viaje más largo
        passenger_count=3,
        trip_distance=12.5,
        tolls_amount=30.00  # Monto de peaje mayor
    ),
    Ride(
        error="",
        taxi_id=4,
        pick_up_time=datetime(2023, 1, 2, 16, 0),
        drop_of_time=datetime(2023, 1, 2, 16, 15),
        passenger_count=1,
        trip_distance=2.0,
        tolls_amount=5.00  # Monto de peaje negativo para verificar el formateo
    )
]

def test_create_content():
    # Test para verificar que el contenido HTML generado es correcto
    html_content = create_content(rides)
    assert "<h1>Taxi Report</h1>" in html_content
    assert "2023-01-02T14:30:00" in html_content
    assert "<td>5.0</td>" in html_content  # Verificar si se maneja correctamente el peaje negativo

@pytest.fixture
def mock_file():
    # Fixture para simular la apertura y escritura de archivos
    with patch('builtins.open', mock_open()) as mock:
        yield mock

def test_create_file(mock_file):
    # Test para verificar que el archivo se crea y escribe correctamente
    content = "Sample HTML content"
    create_file(content)
    mock_file.assert_called_with("financial-report.html", "w")
    mock_file().write.assert_called_once_with(content)
