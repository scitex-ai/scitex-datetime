#!/usr/bin/env python3
# Timestamp: "2026-05-18 00:00:00 (ywatanabe)"
# File: tests/scitex_datetime/test__normalize_timestamp.py

"""Comprehensive tests for datetime._normalize_timestamp module"""

from datetime import datetime, timedelta, timezone

import pytest


class TestNormalizeTimestampDatetimeToStr:
    """normalize_timestamp(datetime, return_as='str')."""

    def test_normalize_datetime_to_str_returns_str_type(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        dt = datetime(2010, 6, 18, 10, 15, 0)
        # Act
        result = normalize_timestamp(dt, return_as="str", normalize_utc=False)
        # Assert
        assert isinstance(result, str)

    def test_normalize_datetime_to_str_contains_date_portion(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        dt = datetime(2010, 6, 18, 10, 15, 0)
        # Act
        result = normalize_timestamp(dt, return_as="str", normalize_utc=False)
        # Assert
        assert "2010-06-18" in result

    def test_normalize_datetime_to_str_contains_time_portion(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        dt = datetime(2010, 6, 18, 10, 15, 0)
        # Act
        result = normalize_timestamp(dt, return_as="str", normalize_utc=False)
        # Assert
        assert "10:15:00" in result


class TestNormalizeTimestampDatetimeToDatetime:
    """normalize_timestamp(datetime, return_as='datetime')."""

    def test_normalize_datetime_to_datetime_returns_datetime_type(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        dt = datetime(2010, 6, 18, 10, 15, 0)
        # Act
        result = normalize_timestamp(dt, return_as="datetime", normalize_utc=True)
        # Assert
        assert isinstance(result, datetime)

    def test_normalize_datetime_to_datetime_attaches_utc_tzinfo(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        dt = datetime(2010, 6, 18, 10, 15, 0)
        # Act
        result = normalize_timestamp(dt, return_as="datetime", normalize_utc=True)
        # Assert
        assert result.tzinfo == timezone.utc


class TestNormalizeTimestampDatetimeToTimestamp:
    """normalize_timestamp(datetime, return_as='timestamp')."""

    def test_normalize_datetime_to_timestamp_returns_float_type(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        dt = datetime(2010, 6, 18, 10, 15, 0, tzinfo=timezone.utc)
        # Act
        result = normalize_timestamp(dt, return_as="timestamp")
        # Assert
        assert isinstance(result, float)

    def test_normalize_datetime_to_timestamp_returns_positive_value(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        dt = datetime(2010, 6, 18, 10, 15, 0, tzinfo=timezone.utc)
        # Act
        result = normalize_timestamp(dt, return_as="timestamp")
        # Assert
        assert result > 0


class TestNormalizeTimestampUnixInput:
    """normalize_timestamp accepts Unix timestamps."""

    def test_normalize_unix_timestamp_returns_datetime_type(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        unix_ts = 1276856100.0
        # Act
        result = normalize_timestamp(unix_ts, return_as="datetime")
        # Assert
        assert isinstance(result, datetime)

    def test_normalize_unix_timestamp_attaches_utc_tzinfo(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        unix_ts = 1276856100.0
        # Act
        result = normalize_timestamp(unix_ts, return_as="datetime")
        # Assert
        assert result.tzinfo == timezone.utc

    def test_normalize_int_timestamp_returns_datetime_type(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        unix_ts = 1276856100
        # Act
        result = normalize_timestamp(unix_ts, return_as="datetime")
        # Assert
        assert isinstance(result, datetime)


class TestNormalizeTimestampStringIsoFormat:
    """normalize_timestamp handles ISO-format strings."""

    def test_normalize_iso_string_returns_datetime_type(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        ts_str = "2010-06-18T10:15:00"
        # Act
        result = normalize_timestamp(ts_str, return_as="datetime", normalize_utc=False)
        # Assert
        assert isinstance(result, datetime)

    def test_normalize_iso_string_parses_year_component(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        ts_str = "2010-06-18T10:15:00"
        # Act
        result = normalize_timestamp(ts_str, return_as="datetime", normalize_utc=False)
        # Assert
        assert result.year == 2010

    def test_normalize_iso_string_parses_month_component(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        ts_str = "2010-06-18T10:15:00"
        # Act
        result = normalize_timestamp(ts_str, return_as="datetime", normalize_utc=False)
        # Assert
        assert result.month == 6

    def test_normalize_iso_string_parses_day_component(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        ts_str = "2010-06-18T10:15:00"
        # Act
        result = normalize_timestamp(ts_str, return_as="datetime", normalize_utc=False)
        # Assert
        assert result.day == 18


class TestNormalizeTimestampMicroseconds:
    """normalize_timestamp preserves microseconds from strings."""

    def test_normalize_string_with_microseconds_returns_datetime_type(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        ts_str = "2010-06-18 10:15:00.123456"
        # Act
        result = normalize_timestamp(ts_str, return_as="datetime", normalize_utc=False)
        # Assert
        assert isinstance(result, datetime)

    def test_normalize_string_with_microseconds_preserves_microsecond_value(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        ts_str = "2010-06-18 10:15:00.123456"
        # Act
        result = normalize_timestamp(ts_str, return_as="datetime", normalize_utc=False)
        # Assert
        assert result.microsecond == 123456


class TestNormalizeTimestampVariousFormats:
    """normalize_timestamp parses several common formats."""

    @pytest.mark.parametrize(
        "ts_str",
        [
            "2010-06-18 10:15:00",
            "2010/06/18 10:15:00",
            "18-06-2010 10:15:00",
            "18/06/2010 10:15:00",
        ],
    )
    def test_normalize_various_string_formats_returns_datetime_type(self, ts_str):
        # Arrange
        from scitex_datetime import normalize_timestamp

        # Act
        result = normalize_timestamp(ts_str, return_as="datetime", normalize_utc=False)
        # Assert
        assert isinstance(result, datetime)


class TestNormalizeTimestampUtcHandling:
    """normalize_timestamp UTC normalization behaviour."""

    def test_normalize_without_utc_preserves_naive_datetime(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        dt = datetime(2010, 6, 18, 10, 15, 0)
        # Act
        result = normalize_timestamp(dt, return_as="datetime", normalize_utc=False)
        # Assert
        assert result.tzinfo is None

    def test_normalize_aware_input_to_utc_returns_utc_tzinfo(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        dt = datetime(2010, 6, 18, 10, 15, 0, tzinfo=timezone(timedelta(hours=5)))
        # Act
        result = normalize_timestamp(dt, return_as="datetime", normalize_utc=True)
        # Assert
        assert result.tzinfo == timezone.utc

    def test_normalize_aware_input_to_utc_shifts_hour_by_offset(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        dt = datetime(2010, 6, 18, 10, 15, 0, tzinfo=timezone(timedelta(hours=5)))
        # Act
        result = normalize_timestamp(dt, return_as="datetime", normalize_utc=True)
        # Assert
        assert result.hour == 5


class TestNormalizeTimestampInvalidReturnAs:
    """normalize_timestamp rejects invalid return_as."""

    def test_normalize_invalid_return_as_raises_valueerror(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        dt = datetime(2010, 6, 18, 10, 15, 0)
        # Act
        # Assert
        with pytest.raises(ValueError, match="return_as must be"):
            normalize_timestamp(dt, return_as="invalid")


class TestToDatetimeFromDatetime:
    """to_datetime returns the input datetime unchanged."""

    def test_to_datetime_from_datetime_returns_same_object(self):
        # Arrange
        from scitex_datetime import to_datetime

        dt = datetime(2010, 6, 18, 10, 15, 0)
        # Act
        result = to_datetime(dt)
        # Assert
        assert result is dt


class TestToDatetimeFromInt:
    """to_datetime converts integer Unix timestamps."""

    def test_to_datetime_from_int_returns_datetime_type(self):
        # Arrange
        from scitex_datetime import to_datetime

        unix_ts = 1276856100
        # Act
        result = to_datetime(unix_ts)
        # Assert
        assert isinstance(result, datetime)

    def test_to_datetime_from_int_attaches_utc_tzinfo(self):
        # Arrange
        from scitex_datetime import to_datetime

        unix_ts = 1276856100
        # Act
        result = to_datetime(unix_ts)
        # Assert
        assert result.tzinfo == timezone.utc


class TestToDatetimeFromFloat:
    """to_datetime converts floating-point Unix timestamps."""

    def test_to_datetime_from_float_returns_datetime_type(self):
        # Arrange
        from scitex_datetime import to_datetime

        unix_ts = 1276856100.123456
        # Act
        result = to_datetime(unix_ts)
        # Assert
        assert isinstance(result, datetime)

    def test_to_datetime_from_float_attaches_utc_tzinfo(self):
        # Arrange
        from scitex_datetime import to_datetime

        unix_ts = 1276856100.123456
        # Act
        result = to_datetime(unix_ts)
        # Assert
        assert result.tzinfo == timezone.utc


class TestToDatetimeFromStringIso:
    """to_datetime parses ISO-format strings into components."""

    def test_to_datetime_from_iso_string_parses_year_component(self):
        # Arrange
        from scitex_datetime import to_datetime

        ts_str = "2010-06-18T10:15:00"
        # Act
        result = to_datetime(ts_str)
        # Assert
        assert result.year == 2010

    def test_to_datetime_from_iso_string_parses_month_component(self):
        # Arrange
        from scitex_datetime import to_datetime

        ts_str = "2010-06-18T10:15:00"
        # Act
        result = to_datetime(ts_str)
        # Assert
        assert result.month == 6

    def test_to_datetime_from_iso_string_parses_day_component(self):
        # Arrange
        from scitex_datetime import to_datetime

        ts_str = "2010-06-18T10:15:00"
        # Act
        result = to_datetime(ts_str)
        # Assert
        assert result.day == 18

    def test_to_datetime_from_iso_string_parses_hour_component(self):
        # Arrange
        from scitex_datetime import to_datetime

        ts_str = "2010-06-18T10:15:00"
        # Act
        result = to_datetime(ts_str)
        # Assert
        assert result.hour == 10

    def test_to_datetime_from_iso_string_parses_minute_component(self):
        # Arrange
        from scitex_datetime import to_datetime

        ts_str = "2010-06-18T10:15:00"
        # Act
        result = to_datetime(ts_str)
        # Assert
        assert result.minute == 15


class TestToDatetimeFromStringStandard:
    """to_datetime parses standard-format strings."""

    def test_to_datetime_from_standard_string_parses_year_component(self):
        # Arrange
        from scitex_datetime import to_datetime

        ts_str = "2010-06-18 10:15:00"
        # Act
        result = to_datetime(ts_str)
        # Assert
        assert result.year == 2010

    def test_to_datetime_from_standard_string_parses_month_component(self):
        # Arrange
        from scitex_datetime import to_datetime

        ts_str = "2010-06-18 10:15:00"
        # Act
        result = to_datetime(ts_str)
        # Assert
        assert result.month == 6

    def test_to_datetime_from_standard_string_parses_day_component(self):
        # Arrange
        from scitex_datetime import to_datetime

        ts_str = "2010-06-18 10:15:00"
        # Act
        result = to_datetime(ts_str)
        # Assert
        assert result.day == 18


class TestToDatetimeNanosecondTruncation:
    """to_datetime truncates nanosecond input to microseconds."""

    def test_to_datetime_nanosecond_input_truncates_to_six_digit_microseconds(self):
        # Arrange
        from scitex_datetime import to_datetime

        ts_str = "2010-06-18 10:15:00.123456789"
        # Act
        result = to_datetime(ts_str)
        # Assert
        assert result.microsecond == 123456


class TestToDatetimeInvalidInputs:
    """to_datetime rejects unparseable / unsupported inputs."""

    def test_to_datetime_invalid_string_raises_valueerror(self):
        # Arrange
        from scitex_datetime import to_datetime

        # Act
        # Assert
        with pytest.raises(ValueError, match="Could not parse timestamp string"):
            to_datetime("not-a-valid-timestamp")

    def test_to_datetime_invalid_type_raises_typeerror(self):
        # Arrange
        from scitex_datetime import to_datetime

        # Act
        # Assert
        with pytest.raises(TypeError, match="timestamp must be"):
            to_datetime([2010, 6, 18])


class TestToDatetimeAlternativeFormats:
    """to_datetime parses every documented alternative format."""

    @pytest.mark.parametrize(
        "ts_str,year,month,day",
        [
            ("2010-06-18T10:15:00.123456", 2010, 6, 18),
            ("2010/06/18 10:15:00", 2010, 6, 18),
            ("18-06-2010 10:15:00", 2010, 6, 18),
            ("18/06/2010 10:15:00", 2010, 6, 18),
            ("18/06/2010, 10:15:00", 2010, 6, 18),
            ("20100618 10:15:00", 2010, 6, 18),
            ("2010-06-18_10:15:00", 2010, 6, 18),
        ],
    )
    def test_to_datetime_alternative_format_parses_year_component(
        self, ts_str, year, month, day
    ):
        # Arrange
        from scitex_datetime import to_datetime

        # Act
        result = to_datetime(ts_str)
        # Assert
        assert result.year == year, f"Failed for {ts_str}"

    @pytest.mark.parametrize(
        "ts_str,year,month,day",
        [
            ("2010-06-18T10:15:00.123456", 2010, 6, 18),
            ("2010/06/18 10:15:00", 2010, 6, 18),
            ("18-06-2010 10:15:00", 2010, 6, 18),
            ("18/06/2010 10:15:00", 2010, 6, 18),
            ("18/06/2010, 10:15:00", 2010, 6, 18),
            ("20100618 10:15:00", 2010, 6, 18),
            ("2010-06-18_10:15:00", 2010, 6, 18),
        ],
    )
    def test_to_datetime_alternative_format_parses_month_component(
        self, ts_str, year, month, day
    ):
        # Arrange
        from scitex_datetime import to_datetime

        # Act
        result = to_datetime(ts_str)
        # Assert
        assert result.month == month, f"Failed for {ts_str}"

    @pytest.mark.parametrize(
        "ts_str,year,month,day",
        [
            ("2010-06-18T10:15:00.123456", 2010, 6, 18),
            ("2010/06/18 10:15:00", 2010, 6, 18),
            ("18-06-2010 10:15:00", 2010, 6, 18),
            ("18/06/2010 10:15:00", 2010, 6, 18),
            ("18/06/2010, 10:15:00", 2010, 6, 18),
            ("20100618 10:15:00", 2010, 6, 18),
            ("2010-06-18_10:15:00", 2010, 6, 18),
        ],
    )
    def test_to_datetime_alternative_format_parses_day_component(
        self, ts_str, year, month, day
    ):
        # Arrange
        from scitex_datetime import to_datetime

        # Act
        result = to_datetime(ts_str)
        # Assert
        assert result.day == day, f"Failed for {ts_str}"


class TestValidateTimestampFormat:
    """validate_timestamp_format checks the standard format."""

    def test_validate_valid_format_returns_true(self):
        # Arrange
        from scitex_datetime import STANDARD_FORMAT, validate_timestamp_format

        dt = datetime(2010, 6, 18, 10, 15, 0)
        ts_str = dt.strftime(STANDARD_FORMAT)
        # Act
        result = validate_timestamp_format(ts_str)
        # Assert
        assert result is True

    def test_validate_invalid_format_returns_false(self):
        # Arrange
        from scitex_datetime import validate_timestamp_format

        # Act
        result = validate_timestamp_format("not-a-timestamp")
        # Assert
        assert result is False

    def test_validate_iso_format_returns_false(self):
        # Arrange
        from scitex_datetime import validate_timestamp_format

        # Act
        result = validate_timestamp_format("2010-06-18T10:15:00")
        # Assert
        assert result is False

    def test_validate_none_input_returns_false(self):
        # Arrange
        from scitex_datetime import validate_timestamp_format

        # Act
        result = validate_timestamp_format(None)
        # Assert
        assert result is False


class TestFormatForFilename:
    """format_for_filename produces filename-safe timestamps."""

    def test_format_datetime_for_filename_returns_expected_string(self):
        # Arrange
        from scitex_datetime import format_for_filename

        dt = datetime(2010, 6, 18, 10, 15, 0)
        # Act
        result = format_for_filename(dt)
        # Assert
        assert result == "20100618_101500"

    def test_format_datetime_for_filename_contains_no_spaces(self):
        # Arrange
        from scitex_datetime import format_for_filename

        dt = datetime(2010, 6, 18, 10, 15, 0)
        # Act
        result = format_for_filename(dt)
        # Assert
        assert " " not in result

    def test_format_datetime_for_filename_contains_no_colons(self):
        # Arrange
        from scitex_datetime import format_for_filename

        dt = datetime(2010, 6, 18, 10, 15, 0)
        # Act
        result = format_for_filename(dt)
        # Assert
        assert ":" not in result

    def test_format_string_for_filename_returns_expected_string(self):
        # Arrange
        from scitex_datetime import format_for_filename

        ts_str = "2010-06-18 10:15:00"
        # Act
        result = format_for_filename(ts_str)
        # Assert
        assert result == "20100618_101500"

    def test_format_for_filename_contains_only_digits_and_underscore(self):
        # Arrange
        from scitex_datetime import format_for_filename

        dt = datetime(2010, 6, 18, 10, 15, 30)
        # Act
        result = format_for_filename(dt)
        # Assert
        assert all(c.isdigit() or c == "_" for c in result)


class TestFormatForDisplay:
    """format_for_display produces human-readable strings."""

    def test_format_datetime_for_display_returns_expected_string(self):
        # Arrange
        from scitex_datetime import format_for_display

        dt = datetime(2010, 6, 18, 10, 15, 0)
        # Act
        result = format_for_display(dt)
        # Assert
        assert result == "2010-06-18 10:15:00"

    def test_format_string_for_display_normalises_separator(self):
        # Arrange
        from scitex_datetime import format_for_display

        ts_str = "2010/06/18 10:15:00"
        # Act
        result = format_for_display(ts_str)
        # Assert
        assert result == "2010-06-18 10:15:00"

    def test_format_for_display_contains_space_between_date_and_time(self):
        # Arrange
        from scitex_datetime import format_for_display

        dt = datetime(2010, 6, 18, 10, 15, 30)
        # Act
        result = format_for_display(dt)
        # Assert
        assert " " in result

    def test_format_for_display_contains_date_separator(self):
        # Arrange
        from scitex_datetime import format_for_display

        dt = datetime(2010, 6, 18, 10, 15, 30)
        # Act
        result = format_for_display(dt)
        # Assert
        assert "-" in result

    def test_format_for_display_contains_time_separator(self):
        # Arrange
        from scitex_datetime import format_for_display

        dt = datetime(2010, 6, 18, 10, 15, 30)
        # Act
        result = format_for_display(dt)
        # Assert
        assert ":" in result


class TestParsePatientRecordingStartFormat:
    """parse_patient_recording_start_format handles REC_START format."""

    def test_parse_rec_start_format_parses_year(self):
        # Arrange
        from scitex_datetime import parse_patient_recording_start_format

        ts_str = "10/06/2010, 07:40:34"
        # Act
        result = parse_patient_recording_start_format(ts_str)
        # Assert
        assert result.year == 2010

    def test_parse_rec_start_format_parses_month(self):
        # Arrange
        from scitex_datetime import parse_patient_recording_start_format

        ts_str = "10/06/2010, 07:40:34"
        # Act
        result = parse_patient_recording_start_format(ts_str)
        # Assert
        assert result.month == 6

    def test_parse_rec_start_format_parses_day(self):
        # Arrange
        from scitex_datetime import parse_patient_recording_start_format

        ts_str = "10/06/2010, 07:40:34"
        # Act
        result = parse_patient_recording_start_format(ts_str)
        # Assert
        assert result.day == 10

    def test_parse_rec_start_format_parses_hour(self):
        # Arrange
        from scitex_datetime import parse_patient_recording_start_format

        ts_str = "10/06/2010, 07:40:34"
        # Act
        result = parse_patient_recording_start_format(ts_str)
        # Assert
        assert result.hour == 7

    def test_parse_rec_start_format_parses_minute(self):
        # Arrange
        from scitex_datetime import parse_patient_recording_start_format

        ts_str = "10/06/2010, 07:40:34"
        # Act
        result = parse_patient_recording_start_format(ts_str)
        # Assert
        assert result.minute == 40

    def test_parse_rec_start_format_parses_second(self):
        # Arrange
        from scitex_datetime import parse_patient_recording_start_format

        ts_str = "10/06/2010, 07:40:34"
        # Act
        result = parse_patient_recording_start_format(ts_str)
        # Assert
        assert result.second == 34

    def test_parse_rec_start_invalid_format_raises_valueerror(self):
        # Arrange
        from scitex_datetime import parse_patient_recording_start_format

        # Act
        # Assert
        with pytest.raises(ValueError):
            parse_patient_recording_start_format("2010-06-10 07:40:34")


class TestGetTimeDeltaSeconds:
    """get_time_delta_seconds returns elapsed seconds between timestamps."""

    def test_get_delta_returns_positive_for_forward_range(self):
        # Arrange
        from scitex_datetime import get_time_delta_seconds

        start = datetime(2010, 6, 18, 10, 0, 0)
        end = datetime(2010, 6, 18, 10, 1, 0)
        # Act
        result = get_time_delta_seconds(start, end)
        # Assert
        assert result == 60.0

    def test_get_delta_returns_negative_when_end_before_start(self):
        # Arrange
        from scitex_datetime import get_time_delta_seconds

        start = datetime(2010, 6, 18, 10, 1, 0)
        end = datetime(2010, 6, 18, 10, 0, 0)
        # Act
        result = get_time_delta_seconds(start, end)
        # Assert
        assert result == -60.0

    def test_get_delta_with_string_inputs_returns_expected_seconds(self):
        # Arrange
        from scitex_datetime import get_time_delta_seconds

        start = "2010-06-18 10:00:00"
        end = "2010-06-18 10:01:00"
        # Act
        result = get_time_delta_seconds(start, end)
        # Assert
        assert result == 60.0

    def test_get_delta_with_mixed_inputs_returns_expected_seconds(self):
        # Arrange
        from scitex_datetime import get_time_delta_seconds

        start = datetime(2010, 6, 18, 10, 0, 0)
        end = "2010-06-18 11:00:00"
        # Act
        result = get_time_delta_seconds(start, end)
        # Assert
        assert result == 3600.0

    def test_get_delta_returns_zero_when_start_equals_end(self):
        # Arrange
        from scitex_datetime import get_time_delta_seconds

        dt = datetime(2010, 6, 18, 10, 0, 0)
        # Act
        result = get_time_delta_seconds(dt, dt)
        # Assert
        assert result == 0.0

    def test_get_delta_returns_seconds_for_one_year_span(self):
        # Arrange
        from scitex_datetime import get_time_delta_seconds

        start = datetime(2010, 1, 1, 0, 0, 0)
        end = datetime(2011, 1, 1, 0, 0, 0)
        expected = 365 * 24 * 60 * 60
        # Act
        result = get_time_delta_seconds(start, end)
        # Assert
        assert result == pytest.approx(expected, rel=0.01)

    def test_get_delta_with_microsecond_inputs_returns_half_second(self):
        # Arrange
        from scitex_datetime import get_time_delta_seconds

        start = datetime(2010, 6, 18, 10, 0, 0, 0)
        end = datetime(2010, 6, 18, 10, 0, 0, 500000)
        # Act
        result = get_time_delta_seconds(start, end)
        # Assert
        assert result == 0.5


class TestConstants:
    """STANDARD_FORMAT and ALTERNATIVE_FORMATS module constants."""

    def test_standard_format_is_defined(self):
        # Arrange
        from scitex_datetime import STANDARD_FORMAT

        # Act
        value = STANDARD_FORMAT
        # Assert
        assert value is not None

    def test_standard_format_is_str_type(self):
        # Arrange
        from scitex_datetime import STANDARD_FORMAT

        # Act
        value = STANDARD_FORMAT
        # Assert
        assert isinstance(value, str)

    def test_standard_format_contains_strftime_directive(self):
        # Arrange
        from scitex_datetime import STANDARD_FORMAT

        # Act
        value = STANDARD_FORMAT
        # Assert
        assert "%" in value

    def test_alternative_formats_is_defined(self):
        # Arrange
        from scitex_datetime import ALTERNATIVE_FORMATS

        # Act
        value = ALTERNATIVE_FORMATS
        # Assert
        assert value is not None

    def test_alternative_formats_is_list_type(self):
        # Arrange
        from scitex_datetime import ALTERNATIVE_FORMATS

        # Act
        value = ALTERNATIVE_FORMATS
        # Assert
        assert isinstance(value, list)

    def test_alternative_formats_is_non_empty(self):
        # Arrange
        from scitex_datetime import ALTERNATIVE_FORMATS

        # Act
        value = ALTERNATIVE_FORMATS
        # Assert
        assert len(value) > 0

    def test_alternative_formats_contains_only_strings(self):
        # Arrange
        from scitex_datetime import ALTERNATIVE_FORMATS

        # Act
        value = ALTERNATIVE_FORMATS
        # Assert
        assert all(isinstance(fmt, str) for fmt in value)


class TestEdgeCasesEpoch:
    """Edge cases at the Unix epoch boundary."""

    def test_epoch_timestamp_zero_parses_to_year_1970(self):
        # Arrange
        from scitex_datetime import to_datetime

        # Act
        result = to_datetime(0)
        # Assert
        assert result.year == 1970

    def test_epoch_timestamp_zero_parses_to_january(self):
        # Arrange
        from scitex_datetime import to_datetime

        # Act
        result = to_datetime(0)
        # Assert
        assert result.month == 1

    def test_epoch_timestamp_zero_parses_to_first_day(self):
        # Arrange
        from scitex_datetime import to_datetime

        # Act
        result = to_datetime(0)
        # Assert
        assert result.day == 1


class TestEdgeCasesLargeAndNegativeTimestamps:
    """Edge cases at extreme Unix timestamp values."""

    def test_large_timestamp_for_year_2100_parses_to_correct_year(self):
        # Arrange
        from scitex_datetime import to_datetime

        large_ts = 4102444800
        # Act
        result = to_datetime(large_ts)
        # Assert
        assert result.year == 2100

    def test_negative_timestamp_for_year_1969_parses_to_correct_year(self):
        # Arrange
        from scitex_datetime import to_datetime

        neg_ts = -31536000
        # Act
        result = to_datetime(neg_ts)
        # Assert
        assert result.year == 1969


class TestEdgeCasesMicrosecondPreservation:
    """normalize_timestamp preserves microsecond precision on datetime input."""

    def test_microsecond_precision_preserved_through_normalize(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        dt = datetime(2010, 6, 18, 10, 15, 0, 123456)
        # Act
        result = normalize_timestamp(dt, return_as="datetime", normalize_utc=False)
        # Assert
        assert result.microsecond == 123456


class TestEdgeCasesRoundtrip:
    """normalize_timestamp roundtrip datetime -> timestamp -> datetime."""

    def test_roundtrip_datetime_timestamp_datetime_preserves_year(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        original = datetime(2010, 6, 18, 10, 15, 0, tzinfo=timezone.utc)
        ts = normalize_timestamp(original, return_as="timestamp")
        # Act
        result = normalize_timestamp(ts, return_as="datetime")
        # Assert
        assert result.year == original.year

    def test_roundtrip_datetime_timestamp_datetime_preserves_month(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        original = datetime(2010, 6, 18, 10, 15, 0, tzinfo=timezone.utc)
        ts = normalize_timestamp(original, return_as="timestamp")
        # Act
        result = normalize_timestamp(ts, return_as="datetime")
        # Assert
        assert result.month == original.month

    def test_roundtrip_datetime_timestamp_datetime_preserves_day(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        original = datetime(2010, 6, 18, 10, 15, 0, tzinfo=timezone.utc)
        ts = normalize_timestamp(original, return_as="timestamp")
        # Act
        result = normalize_timestamp(ts, return_as="datetime")
        # Assert
        assert result.day == original.day

    def test_roundtrip_datetime_timestamp_datetime_preserves_hour(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        original = datetime(2010, 6, 18, 10, 15, 0, tzinfo=timezone.utc)
        ts = normalize_timestamp(original, return_as="timestamp")
        # Act
        result = normalize_timestamp(ts, return_as="datetime")
        # Assert
        assert result.hour == original.hour

    def test_roundtrip_datetime_timestamp_datetime_preserves_minute(self):
        # Arrange
        from scitex_datetime import normalize_timestamp

        original = datetime(2010, 6, 18, 10, 15, 0, tzinfo=timezone.utc)
        ts = normalize_timestamp(original, return_as="timestamp")
        # Act
        result = normalize_timestamp(ts, return_as="datetime")
        # Assert
        assert result.minute == original.minute


# --------------------------------------------------------------------------------

if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.abspath(__file__)])

# --------------------------------------------------------------------------------
# Start of Source Code from: /home/ywatanabe/proj/scitex-code/src/scitex/datetime/_normalize_timestamp.py
# --------------------------------------------------------------------------------
# #!/usr/bin/env python3
# # Timestamp: "2026-01-05 14:30:00 (ywatanabe)"
# # File: /home/ywatanabe/proj/scitex-code/src/scitex/datetime/_normalize_timestamp.py
#
# # EOF

# --------------------------------------------------------------------------------
# End of Source Code from: /home/ywatanabe/proj/scitex-code/src/scitex/datetime/_normalize_timestamp.py
# --------------------------------------------------------------------------------
