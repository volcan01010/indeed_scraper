"""Scrape job data from Indeed website"""
import logging

import requests

logger = logging.getLogger(__name__)

BASE_URL = "https://www.indeed.co.uk/viewjob?jk={job_key}"


class IndeedScraperException(Exception):
    """Exception from indeed_scraper module"""
    pass


def scrape_indeed_job(job_key):
    """
    Scrape job details from Indeed.co.uk.

    :param job_key: str, job key
    :return IndeedJob: SQLAlchemy model for Indeed job
    """
    # Fetch HTML from website
    try:
        html = fetch_html(job_key)
    except requests.exceptions.HTTPError as exc:
        msg = f"Download failed for {job_key}: {exc}"
        raise IndeedScraperException(msg)

    # Extract information into job spec
    job_spec = extract_job_spec(job_key, html)
    return html


def fetch_html(job_key):
    """
    Pull raw HTML for job_key.

    :param job_key: str, job key
    :return IndeedJobSpec: SQLAlchemy model for Indeed job
    """
    path = BASE_URL.format(job_key=job_key)
    logger.debug("Fetching %s", path)
    response = requests.get(path)
    response.raise_for_status()  # Raise exception if not 200
    return response.text


def extract_job_spec(job_key, html):
    """
    Extract details from HTML for job_key.

    :param job_key: str, job_key
    :param html: str, html from web page
    :return IndeedJobSpec: SQLAlchemy model for Indeed job
    """
    pass
