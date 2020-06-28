# Indeed.com API

Indeed.co.uk is related to Indeed.com, which has a Job Search API that is
available to publishers of job data.  It may or may not be within the terms of
the licence agreement to use this.  For the purposes of this exercise, I am
assuming not.  Even so, the API site provides useful information about the job
data that is served.

https://opensource.indeedeng.io/api-documentation/docs/job-search/

This is an example JSON response from a job search:

```
{  
    "version":2,
    "query":"java",
    "location":"austin, tx",
    "dupefilter":true,
    "highlight":false,
    "radius":25,
    "start":1,
    "end":10,
    "totalResults":547,
    "pageNumber":0,
    "results":[  
        {  
            "jobtitle":"Java Developer",
            "company":"XYZ Corp.,",
            "city":"Austin",
            "state":"TX",
            "country":"US",
            "formattedLocation":"Austin, TX",
            "source":"Dice",
            "date":"Mon, 02 Aug 2017 16:21:00 GMT",
            "snippet":"looking for an object-oriented Java Developer... Java
Servlets,
              HTML, JavaScript, AJAX, Struts, Struts2, JSF) desirable.
Familiarity with
              Tomcat and the Java...",
            "url":"https://www.indeed.com/viewjob?jk=12345&indpubnum=8343699265155203",
            "onmousedown":"indeed_clk(this, '0000');",
            "latitude":30.27127,
            "longitude":-97.74103,
            "jobkey":"12345",
            "sponsored":false,
            "expired":false,
            "indeedApply":true,
            "formattedLocationFull":"Austin, TX",
            "formattedRelativeTime":"11 hours ago"
        }
    ]
}
```



# Meld comparison of adverts

Comparing adverts via Meld shows that most of the data comes within a single
line of the page.  The line was too long for this to be of use.

# Beautiful Soup

Searching HTML found a `div` with the class `jobsearch-jobDescriptionText`.
This contains most of the job details.  There may be others to check for.
