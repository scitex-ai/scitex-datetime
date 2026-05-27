#!/usr/bin/env python3
# Timestamp: "2026-05-18 00:00:00 (ywatanabe)"
# File: tests/scitex_datetime/test__linspace.py

"""Comprehensive tests for datetime._linspace module"""

import datetime
from datetime import timedelta, timezone

import numpy as np
import pytest


class TestLinspaceBasicNSamples:
    """linspace with n_samples — basic return shape and endpoints."""

    def test_linspace_returns_ndarray_when_n_samples_given(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0)
        end = datetime.datetime(2023, 1, 1, 0, 0, 10)
        # Act
        result = linspace(start, end, n_samples=11)
        # Assert
        assert isinstance(result, np.ndarray)

    def test_linspace_returns_requested_length_for_n_samples(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0)
        end = datetime.datetime(2023, 1, 1, 0, 0, 10)
        # Act
        result = linspace(start, end, n_samples=11)
        # Assert
        assert len(result) == 11

    def test_linspace_first_element_equals_start_for_n_samples(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0)
        end = datetime.datetime(2023, 1, 1, 0, 0, 10)
        # Act
        result = linspace(start, end, n_samples=11)
        # Assert
        assert result[0] == start

    def test_linspace_last_element_equals_end_for_n_samples(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0)
        end = datetime.datetime(2023, 1, 1, 0, 0, 10)
        # Act
        result = linspace(start, end, n_samples=11)
        # Assert
        assert result[-1] == end

    def test_linspace_yields_datetime_objects_for_n_samples(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0)
        end = datetime.datetime(2023, 1, 1, 0, 0, 10)
        # Act
        result = linspace(start, end, n_samples=11)
        # Assert
        assert all(isinstance(dt, datetime.datetime) for dt in result)


class TestLinspaceBasicSamplingRate:
    """linspace with sampling_rate — basic return shape and endpoints."""

    def test_linspace_returns_ndarray_when_sampling_rate_given(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0)
        end = datetime.datetime(2023, 1, 1, 0, 0, 1)
        # Act
        result = linspace(start, end, sampling_rate=10)
        # Assert
        assert isinstance(result, np.ndarray)

    def test_linspace_returns_n_plus_one_samples_for_sampling_rate(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0)
        end = datetime.datetime(2023, 1, 1, 0, 0, 1)
        # Act
        result = linspace(start, end, sampling_rate=10)
        # Assert
        assert len(result) == 11

    def test_linspace_first_element_equals_start_for_sampling_rate(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0)
        end = datetime.datetime(2023, 1, 1, 0, 0, 1)
        # Act
        result = linspace(start, end, sampling_rate=10)
        # Assert
        assert result[0] == start

    def test_linspace_last_element_equals_end_for_sampling_rate(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0)
        end = datetime.datetime(2023, 1, 1, 0, 0, 1)
        # Act
        result = linspace(start, end, sampling_rate=10)
        # Assert
        assert result[-1] == end


class TestLinspaceUniformSpacing:
    """linspace produces uniform spacing across the requested range."""

    def test_linspace_creates_uniform_spacing_across_range(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0)
        end = datetime.datetime(2023, 1, 1, 0, 1, 0)
        # Act
        result = linspace(start, end, n_samples=61)
        deltas = [
            (result[i + 1] - result[i]).total_seconds() for i in range(len(result) - 1)
        ]
        # Assert
        assert all(pytest.approx(delta, rel=1e-6) == 1.0 for delta in deltas)


class TestLinspaceParameterValidation:
    """linspace rejects invalid parameter combinations."""

    def test_linspace_raises_when_both_n_samples_and_sampling_rate_given(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1)
        end = datetime.datetime(2023, 1, 2)
        # Act
        # Assert
        with pytest.raises(
            ValueError, match="Provide either n_samples or sampling_rate, not both"
        ):
            linspace(start, end, n_samples=10, sampling_rate=1.0)

    def test_linspace_raises_when_neither_parameter_given(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1)
        end = datetime.datetime(2023, 1, 2)
        # Act
        # Assert
        with pytest.raises(
            ValueError, match="Either n_samples or sampling_rate must be provided"
        ):
            linspace(start, end)


class TestLinspaceTypeChecking:
    """linspace enforces type contracts on its inputs."""

    def test_linspace_raises_typeerror_when_start_is_not_datetime(self):
        # Arrange
        from scitex_datetime import linspace

        end = datetime.datetime(2023, 1, 2)
        # Act
        # Assert
        with pytest.raises(TypeError, match="start_dt must be a datetime object"):
            linspace("2023-01-01", end, n_samples=10)

    def test_linspace_raises_typeerror_when_end_is_not_datetime(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1)
        # Act
        # Assert
        with pytest.raises(TypeError, match="end_dt must be a datetime object"):
            linspace(start, "2023-01-02", n_samples=10)

    def test_linspace_raises_typeerror_when_n_samples_is_string(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1)
        end = datetime.datetime(2023, 1, 2)
        # Act
        # Assert
        with pytest.raises(TypeError, match="n_samples must be a number"):
            linspace(start, end, n_samples="10")

    def test_linspace_raises_typeerror_when_sampling_rate_is_string(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1)
        end = datetime.datetime(2023, 1, 2)
        # Act
        # Assert
        with pytest.raises(TypeError, match="sampling_rate must be a number"):
            linspace(start, end, sampling_rate="10")


class TestLinspaceValueValidation:
    """linspace enforces value constraints on inputs."""

    def test_linspace_raises_when_start_after_end(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1)
        end = datetime.datetime(2023, 1, 2)
        # Act
        # Assert
        with pytest.raises(ValueError, match="start_dt must be earlier than end_dt"):
            linspace(end, start, n_samples=10)

    def test_linspace_raises_when_start_equals_end(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1)
        # Act
        # Assert
        with pytest.raises(ValueError, match="start_dt must be earlier than end_dt"):
            linspace(start, start, n_samples=10)

    def test_linspace_raises_when_n_samples_is_negative(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1)
        end = datetime.datetime(2023, 1, 2)
        # Act
        # Assert
        with pytest.raises(ValueError, match="n_samples must be positive"):
            linspace(start, end, n_samples=-1)

    def test_linspace_raises_when_n_samples_is_zero(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1)
        end = datetime.datetime(2023, 1, 2)
        # Act
        # Assert
        with pytest.raises(ValueError, match="n_samples must be positive"):
            linspace(start, end, n_samples=0)

    def test_linspace_raises_when_sampling_rate_is_negative(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1)
        end = datetime.datetime(2023, 1, 2)
        # Act
        # Assert
        with pytest.raises(ValueError, match="sampling_rate must be positive"):
            linspace(start, end, sampling_rate=-1.0)

    def test_linspace_raises_when_sampling_rate_is_zero(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1)
        end = datetime.datetime(2023, 1, 2)
        # Act
        # Assert
        with pytest.raises(ValueError, match="sampling_rate must be positive"):
            linspace(start, end, sampling_rate=0.0)


class TestLinspaceMicrosecondPrecision:
    """linspace preserves microsecond resolution."""

    def test_linspace_preserves_microsecond_precision_across_samples(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0, 0)
        end = datetime.datetime(2023, 1, 1, 0, 0, 0, 10000)
        # Act
        result = linspace(start, end, n_samples=11)
        observed = [result[i].microsecond for i in range(len(result))]
        expected = [i * 1000 for i in range(11)]
        # Assert
        assert observed == expected


class TestLinspaceLargeRange:
    """linspace behaves correctly with year-scale spans."""

    def test_linspace_returns_requested_length_for_year_scale_range(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2020, 1, 1)
        end = datetime.datetime(2025, 1, 1)
        # Act
        result = linspace(start, end, n_samples=6)
        # Assert
        assert len(result) == 6

    def test_linspace_preserves_endpoints_for_year_scale_range(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2020, 1, 1)
        end = datetime.datetime(2025, 1, 1)
        # Act
        result = linspace(start, end, n_samples=6)
        # Assert
        assert (result[0], result[-1]) == (start, end)

    def test_linspace_yearly_spacing_within_leap_year_tolerance(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2020, 1, 1)
        end = datetime.datetime(2025, 1, 1)
        # Act
        result = linspace(start, end, n_samples=6)
        deltas_days = [(result[i + 1] - result[i]).days for i in range(len(result) - 1)]
        # Assert
        assert all(364 <= d <= 366 for d in deltas_days)


class TestLinspaceSmallRange:
    """linspace handles microsecond-scale spans."""

    def test_linspace_returns_two_samples_for_one_microsecond_range(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0, 0)
        end = datetime.datetime(2023, 1, 1, 0, 0, 0, 1)
        # Act
        result = linspace(start, end, n_samples=2)
        # Assert
        assert len(result) == 2

    def test_linspace_preserves_endpoints_for_one_microsecond_range(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0, 0)
        end = datetime.datetime(2023, 1, 1, 0, 0, 0, 1)
        # Act
        result = linspace(start, end, n_samples=2)
        # Assert
        assert (result[0], result[-1]) == (start, end)


class TestLinspaceHighFrequencySampling:
    """linspace produces correct sample counts at high sampling rates."""

    @pytest.mark.parametrize("rate", [100, 256, 512, 1000])
    def test_linspace_high_frequency_returns_expected_sample_count(self, rate):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0)
        end = datetime.datetime(2023, 1, 1, 0, 0, 1)
        expected_samples = int(1.0 * rate) + 1
        # Act
        result = linspace(start, end, sampling_rate=rate)
        # Assert
        assert len(result) == expected_samples

    @pytest.mark.parametrize("rate", [100, 256, 512, 1000])
    def test_linspace_high_frequency_first_sample_equals_start(self, rate):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0)
        end = datetime.datetime(2023, 1, 1, 0, 0, 1)
        # Act
        result = linspace(start, end, sampling_rate=rate)
        # Assert
        assert result[0] == start

    @pytest.mark.parametrize("rate", [100, 256, 512, 1000])
    def test_linspace_high_frequency_last_sample_equals_end(self, rate):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0)
        end = datetime.datetime(2023, 1, 1, 0, 0, 1)
        # Act
        result = linspace(start, end, sampling_rate=rate)
        # Assert
        assert result[-1] == end

    @pytest.mark.parametrize("rate", [100, 256, 512, 1000])
    def test_linspace_high_frequency_sample_spacing_matches_one_over_rate(self, rate):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0)
        end = datetime.datetime(2023, 1, 1, 0, 0, 1)
        expected_delta = 1.0 / rate
        # Act
        result = linspace(start, end, sampling_rate=rate)
        delta = (result[1] - result[0]).total_seconds()
        # Assert
        assert pytest.approx(expected_delta, rel=1e-4) == delta


class TestLinspaceTimezoneAware:
    """linspace preserves tzinfo on timezone-aware inputs."""

    def test_linspace_returns_requested_length_for_utc_inputs(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        end = datetime.datetime(2023, 1, 1, 1, 0, 0, tzinfo=timezone.utc)
        # Act
        result = linspace(start, end, n_samples=5)
        # Assert
        assert len(result) == 5

    def test_linspace_propagates_utc_tzinfo_to_all_samples(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        end = datetime.datetime(2023, 1, 1, 1, 0, 0, tzinfo=timezone.utc)
        # Act
        result = linspace(start, end, n_samples=5)
        # Assert
        assert all(dt.tzinfo == timezone.utc for dt in result)

    def test_linspace_preserves_endpoints_for_utc_inputs(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        end = datetime.datetime(2023, 1, 1, 1, 0, 0, tzinfo=timezone.utc)
        # Act
        result = linspace(start, end, n_samples=5)
        # Assert
        assert (result[0], result[-1]) == (start, end)


class TestLinspaceFloatNSamples:
    """linspace handles int n_samples value."""

    def test_linspace_int_n_samples_returns_requested_length(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1)
        end = datetime.datetime(2023, 1, 2)
        # Act
        result = linspace(start, end, n_samples=10)
        # Assert
        assert len(result) == 10


class TestLinspaceEdgeCaseSingleSample:
    """linspace edge case: n_samples=1."""

    def test_linspace_single_sample_returns_one_element(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1)
        end = datetime.datetime(2023, 1, 2)
        # Act
        result = linspace(start, end, n_samples=1)
        # Assert
        assert len(result) == 1

    def test_linspace_single_sample_returns_start_value(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1)
        end = datetime.datetime(2023, 1, 2)
        # Act
        result = linspace(start, end, n_samples=1)
        # Assert
        assert result[0] == start


class TestLinspaceNumericalStability:
    """linspace numerical stability with very small intervals."""

    def test_linspace_microsecond_step_preserves_each_microsecond(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0, 0)
        end = datetime.datetime(2023, 1, 1, 0, 0, 0, 100)
        # Act
        result = linspace(start, end, n_samples=101)
        observed = [result[i].microsecond for i in range(101)]
        expected = list(range(101))
        # Assert
        assert observed == expected


class TestLinspaceSamplingRateCalculation:
    """linspace produces correct sample counts across durations and rates."""

    @pytest.mark.parametrize(
        "duration,rate",
        [(1, 256), (10, 100), (0.5, 1000), (60, 1)],
    )
    def test_linspace_sample_count_matches_duration_times_rate_plus_one(
        self, duration, rate
    ):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0)
        end = start + timedelta(seconds=duration)
        expected_samples = int(duration * rate) + 1
        # Act
        result = linspace(start, end, sampling_rate=rate)
        # Assert
        assert len(result) == expected_samples


class TestLinspaceReturnType:
    """linspace return type is numpy ndarray of datetime objects."""

    def test_linspace_returns_ndarray_for_n_samples_request(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1)
        end = datetime.datetime(2023, 1, 2)
        # Act
        result = linspace(start, end, n_samples=10)
        # Assert
        assert isinstance(result, np.ndarray)

    def test_linspace_returns_object_dtype_for_n_samples_request(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1)
        end = datetime.datetime(2023, 1, 2)
        # Act
        result = linspace(start, end, n_samples=10)
        # Assert
        assert result.dtype == object

    def test_linspace_yields_datetime_objects_for_n_samples_request(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1)
        end = datetime.datetime(2023, 1, 2)
        # Act
        result = linspace(start, end, n_samples=10)
        # Assert
        assert all(isinstance(dt, datetime.datetime) for dt in result)

    def test_linspace_returns_ndarray_for_sampling_rate_request(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1)
        end = datetime.datetime(2023, 1, 2)
        # Act
        result = linspace(start, end, sampling_rate=1.0)
        # Assert
        assert isinstance(result, np.ndarray)

    def test_linspace_returns_object_dtype_for_sampling_rate_request(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1)
        end = datetime.datetime(2023, 1, 2)
        # Act
        result = linspace(start, end, sampling_rate=1.0)
        # Assert
        assert result.dtype == object

    def test_linspace_yields_datetime_objects_for_sampling_rate_request(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1)
        end = datetime.datetime(2023, 1, 2)
        # Act
        result = linspace(start, end, sampling_rate=1.0)
        # Assert
        assert all(isinstance(dt, datetime.datetime) for dt in result)


class TestLinspacePracticalEegTimestamps:
    """linspace practical use case: EEG timestamp generation."""

    @pytest.mark.parametrize("rate", [256, 512])
    def test_linspace_eeg_sample_count_equals_duration_times_rate_plus_one(self, rate):
        # Arrange
        from scitex_datetime import linspace

        duration = 10
        start = datetime.datetime(2023, 1, 1, 12, 0, 0)
        end = start + timedelta(seconds=duration)
        expected_samples = duration * rate + 1
        # Act
        timestamps = linspace(start, end, sampling_rate=rate)
        # Assert
        assert len(timestamps) == expected_samples

    @pytest.mark.parametrize("rate", [256, 512])
    def test_linspace_eeg_sample_intervals_match_one_over_rate(self, rate):
        # Arrange
        from scitex_datetime import linspace

        duration = 10
        start = datetime.datetime(2023, 1, 1, 12, 0, 0)
        end = start + timedelta(seconds=duration)
        expected_interval = 1.0 / rate
        # Act
        timestamps = linspace(start, end, sampling_rate=rate)
        intervals = [
            (timestamps[i + 1] - timestamps[i]).total_seconds() for i in range(10)
        ]
        # Assert
        assert all(pytest.approx(expected_interval, rel=1e-3) == iv for iv in intervals)


class TestLinspaceHourlyDailySchedules:
    """linspace practical use case: hourly/daily schedule generation."""

    def test_linspace_hourly_schedule_returns_24_samples(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0)
        end = datetime.datetime(2023, 1, 1, 23, 0, 0)
        # Act
        hourly = linspace(start, end, n_samples=24)
        # Assert
        assert len(hourly) == 24

    def test_linspace_hourly_schedule_hour_component_matches_index(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0)
        end = datetime.datetime(2023, 1, 1, 23, 0, 0)
        # Act
        hourly = linspace(start, end, n_samples=24)
        observed_hours = [ts.hour for ts in hourly]
        # Assert
        assert observed_hours == list(range(24))

    def test_linspace_hourly_schedule_minute_component_is_zero(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0)
        end = datetime.datetime(2023, 1, 1, 23, 0, 0)
        # Act
        hourly = linspace(start, end, n_samples=24)
        # Assert
        assert all(ts.minute == 0 for ts in hourly)

    def test_linspace_hourly_schedule_second_component_is_zero(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 0, 0, 0)
        end = datetime.datetime(2023, 1, 1, 23, 0, 0)
        # Act
        hourly = linspace(start, end, n_samples=24)
        # Assert
        assert all(ts.second == 0 for ts in hourly)


class TestLinspaceDataLoggingScenario:
    """linspace practical use case: periodic logging timestamps."""

    def test_linspace_data_logging_returns_13_samples(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 9, 0, 0)
        end = datetime.datetime(2023, 1, 1, 10, 0, 0)
        # Act
        timestamps = linspace(start, end, n_samples=13)
        # Assert
        assert len(timestamps) == 13

    def test_linspace_data_logging_intervals_are_five_minutes(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1, 9, 0, 0)
        end = datetime.datetime(2023, 1, 1, 10, 0, 0)
        # Act
        timestamps = linspace(start, end, n_samples=13)
        deltas_minutes = [
            (timestamps[i + 1] - timestamps[i]).total_seconds() / 60
            for i in range(len(timestamps) - 1)
        ]
        # Assert
        assert all(pytest.approx(d, rel=1e-6) == 5.0 for d in deltas_minutes)


class TestLinspacePerformance:
    """linspace performance characteristics with one million samples."""

    def test_linspace_performance_returns_one_million_samples(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1)
        end = datetime.datetime(2023, 12, 31)
        # Act
        result = linspace(start, end, n_samples=1_000_000)
        # Assert
        assert len(result) == 1_000_000

    def test_linspace_performance_completes_within_five_seconds(self):
        # Arrange
        import time

        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1)
        end = datetime.datetime(2023, 12, 31)
        # Act
        t0 = time.time()
        linspace(start, end, n_samples=1_000_000)
        elapsed = time.time() - t0
        # Assert
        assert elapsed < 5.0

    def test_linspace_performance_first_sample_equals_start(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1)
        end = datetime.datetime(2023, 12, 31)
        # Act
        result = linspace(start, end, n_samples=1_000_000)
        # Assert
        assert result[0] == start

    def test_linspace_performance_last_sample_equals_end(self):
        # Arrange
        from scitex_datetime import linspace

        start = datetime.datetime(2023, 1, 1)
        end = datetime.datetime(2023, 12, 31)
        # Act
        result = linspace(start, end, n_samples=1_000_000)
        # Assert
        assert result[-1] == end


# --------------------------------------------------------------------------------

if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.abspath(__file__)])

# --------------------------------------------------------------------------------
# Start of Source Code from: /home/ywatanabe/proj/scitex-code/src/scitex/datetime/_linspace.py
# --------------------------------------------------------------------------------
# #!/usr/bin/env python3
# # Timestamp: "2026-01-05 14:30:00 (ywatanabe)"
# # File: /home/ywatanabe/proj/scitex-code/src/scitex/datetime/_linspace.py
#
# """
# Datetime linspace utility for creating evenly spaced datetime arrays.
# """
#
# # EOF

# --------------------------------------------------------------------------------
# End of Source Code from: /home/ywatanabe/proj/scitex-code/src/scitex/datetime/_linspace.py
# --------------------------------------------------------------------------------
