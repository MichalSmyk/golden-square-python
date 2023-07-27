from lib.report_length import report_length

def test_for_one_letter():
    result = report_length("a")
    assert result == "This string was 1 characters long."