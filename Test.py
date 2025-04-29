import requests
from collections import Counter
import pytest
from unittest.mock import patch, Mock

class APIError(Exception):
    pass

class CatFactProcessor:
    def __init__(self):
        self.last_fact = ""

    def get_fact(self):
        try:
            response = requests.get("https://catfact.ninja/fact")
            response.raise_for_status()
            self.last_fact = response.json()["fact"]
            return self.last_fact
        except requests.exceptions.RequestException as e:
            raise APIError(f"Ошибка при запросе к API: {e}") from e

    def get_fact_analysis(self):
        fact_length = len(self.last_fact)
        letter_frequencies = dict(Counter(self.last_fact.lower()))
        return {"length": fact_length, "letter_frequencies": letter_frequencies}

@patch("requests.get")
def test_get_fact_success(mock_get):
    mock_get.return_value = Mock(status_code=200, json=lambda: {"fact": "Cats sleep 70% of their lives."})
    processor = CatFactProcessor()
    fact = processor.get_fact()
    assert fact == "Cats sleep 70% of their lives."
    assert processor.last_fact == fact

@patch("requests.get")
def test_get_fact_api_error(mock_get):
    mock_get.side_effect = requests.exceptions.RequestException("Connection failed")
    processor = CatFactProcessor()
    with pytest.raises(APIError, match="Ошибка при запросе к API"):
        processor.get_fact()

def test_get_fact_analysis():
    processor = CatFactProcessor()
    processor.last_fact = "Cat"
    result = processor.get_fact_analysis()
    assert result == {"length": 3, "letter_frequencies": {'c': 1, 'a': 1, 't': 1}}

def test_get_fact_analysis_empty():
    processor = CatFactProcessor()
    processor.last_fact = ""
    result = processor.get_fact_analysis()
    assert result == {"length": 0, "letter_frequencies": {}}