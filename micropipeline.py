"""
Code for the Fetch Job Details part of the pipeline.  This could be configured
with queues for incoming job_keys and outgoing data and error messages.
"""
from concurrent.futures import ThreadPoolExecutor
import json
import logging
from pathlib import Path

from indeed_scraper import (
    scrape_indeed_job, IndeedScraperException, IndeedJobSpecSchema
)


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def fetch_job_details():
    """
    Fetch details for jobs on queue and store results or mark
    as failed.
    """
    logger.info('Fetching job_keys')
    job_keys = read_job_keys_from_queue()

    for job_key in job_keys:
        fetch_and_register(job_key)


def read_job_keys_from_queue():
    return ['9a2565f2b076b6f0', '9a2565f2b076b6f0', 'not-a-job']


def fetch_and_register(job_key):
    """
    Scrape job_key details and pass to outbound queue or register failure.
    """
    try:
        job_details = scrape_indeed_job(job_key)
        export_result(job_details)
    except IndeedScraperException as exc:
        mark_as_failed(job_key, exc)


def export_result(job_details):
    """Append result details to file."""
    job_details_dict = IndeedJobSpecSchema().dump(job_details)
    job_details_json = json.dumps(job_details_dict, indent=2, sort_keys=True)
    results_queue = Path('results.txt')
    with open(results_queue, 'at') as outfile:
        outfile.write(job_details_json + '\n')


def mark_as_failed(job_key, exc):
    """Append failure details to file."""
    message = f"{job_key}|{exc.args[0]}\n"
    failures_queue = Path('failed_keys.txt')
    with open(failures_queue, 'at') as outfile:
        outfile.write(message)


if __name__ == "__main__":
    fetch_job_details()
