"""Unit tests for indeed_scraper"""
import datetime

from freezegun import freeze_time
from indeed_scraper import extract_job_spec
from schemas import IndeedJobSpec, IndeedJobSpecSchema


@freeze_time(datetime.datetime(2020, 6, 30, 12, 0, 0))
def test_extract_job_spec(harringtons_job_key, harringtons_html):
    # Arrange

    # At this point we just pick out the easy ones, can add normalised
    # fields later
    expected_spec = IndeedJobSpec(
        job_key=harringtons_job_key,
        summary="We are currently recruiting for an experienced accounts assistant who has knowledge of Sage Line 50 accounts. The ideal candidate should have initiative to both work alone and as part of a team.",  # noqa
        duties=None,
        job_types="Full-time, Permanent",
        salary="£25,000.00 /year",
        benefits="On-site Parking",
        experience="Accounting: 5 years (Required)|Sage Line 50: 5 years (Required)",  # noqa
        licence="Driving (Required)",
        work_remotely="Temporarily due to COVID-19",
        fetched_at=datetime.datetime(2020, 6, 30, 12, 0, 0)
    )
    schema = IndeedJobSpecSchema()

    # Act
    spec = extract_job_spec(harringtons_job_key, harringtons_html)

    # Assert
    assert schema.dump(spec) == schema.dump(expected_spec)
