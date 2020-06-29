"""Unit tests for indeed_scraper"""
from indeed_scraper import extract_job_spec
from schemas import IndeedJobSpec


def test_extract_job_spec(harringtons_job_key, harringtons_html):
    # Arrange
    expected_spec = IndeedJobSpec(job_key=harringtons_job_key,
                                  description='blah')

    # Act
    spec = extract_job_spec(harringtons_job_key, harringtons_html)

    # Assert
    assert spec == expected_spec
