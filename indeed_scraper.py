"""Scrape job data from Indeed website"""
import datetime
import logging

import bs4
import requests

from schemas import IndeedJobSpec, IndeedJobSpecSchema

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
    logger.info("Scraping job_key: %s", job_key)

    # Fetch HTML from website
    try:
        html = fetch_html(job_key)
    except requests.exceptions.HTTPError as exc:
        msg = f"Download failed for {job_key}: {exc}"
        raise IndeedScraperException(msg)

    # Extract information into job spec
    job_spec = extract_job_spec(job_key, html)

    return job_spec


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
    logger.debug("Building model for %s", job_key)
    # Extract description from html
    soup = bs4.BeautifulSoup(html, features='lxml')
    description = soup.findAll("div", class_="jobsearch-jobDescriptionText")[0]

    # Extract attributes from description

    def text_that_follows(attribute):
        """Return text from tag following one containing named attribute."""
        return description.find('p', text=attribute).nextSibling.string

    def list_that_follows(attribute):
        """Return a pipe-separated string of items from list following
        attribute."""
        items = description.find('p', text=attribute).next_sibling.findAll('li')  # noqa
        return '|'.join(item.string for item in items)

    def text_that_starts_with(attribute):
        """Return trimmed text from tag that starts with named attribute."""
        full_text = description.find(
            'p', text=lambda x: x.startswith(attribute)).string
        return full_text.replace(attribute, '').strip()

    summary = description.find('b', text='Job Summary').parent.nextSibling.text
    duties = None  # Save this fiddly one for later
    job_types = text_that_starts_with('Job Types:')
    salary = text_that_starts_with('Salary:')
    benefits = list_that_follows('Benefits:')
    experience = list_that_follows('Experience:')
    licence = list_that_follows('Licence:')
    work_remotely = list_that_follows('Work remotely:')
    fetched_at = datetime.datetime.now()

    # Build model
    spec = IndeedJobSpec(job_key=job_key,
                         summary=summary,
                         duties=duties,
                         job_types=job_types,
                         salary=salary,
                         benefits=benefits,
                         experience=experience,
                         licence=licence,
                         work_remotely=work_remotely,
                         fetched_at=fetched_at
                         )

    return spec


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    schema = IndeedJobSpecSchema()
    harringtons_spec = scrape_indeed_job('9a2565f2b076b6f0')
    print(schema.dump(harringtons_spec))
