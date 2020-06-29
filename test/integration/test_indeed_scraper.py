"""Integration tests for indeed_scraper module"""
import bs4
import pytest

from indeed_scraper import (
    scrape_indeed_job, fetch_html, IndeedScraperException
)


def test_fetch_html_happy_path():
    # Arrange
    job_key = "9a2565f2b076b6f0"

    # Act
    html = fetch_html(job_key)
    soup = bs4.BeautifulSoup(html, features='lxml')

    # Assert resulting HTML contains job description data
    assert soup.findAll("div", class_="jobsearch-jobDescriptionText")


def test_scrape_indeed_job_bad_job_key():
    # Arrange
    job_key = "not_a_real_job"

    # Act
    with pytest.raises(IndeedScraperException):
        scrape_indeed_job(job_key)
