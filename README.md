# indeed_scraper
> Micro-pipeline for scraping job data from Indeed.co.uk

### Setup

This code was written using Python 3.8.

In a virtual environment, install dependencies with:

```bash
python -m pip install -r requirements.txt
```

### Scraper demo

The code for scraping an individual job advert is stored in
`indeed_scraper.py`.  A demonstration of the output can be seen by calling the
file on the command line:

```bash
python indeed_scraper.py
```

### Micropipeline demo

The code for a micropipeline is stored in `micropipeline.py`.  It will download
job data from a queue and store to file and record exceptions.  It can be
called from the command line with:

```bash
python micropipeline.py
```

Look at the contents of `results.txt` and `failed_keys.txt` for details.  For
now it repeatedly calls the example job advert and a simulated failure.

### Tests

Unit and integration tests for the scraper can be run with:

```bash
export PYTHONPATH=.
pytest -vs test
```
