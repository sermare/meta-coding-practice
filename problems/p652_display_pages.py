DESCRIPTION = """Display Pages

Given a list of search results where each result has a host_id, listing_id, score,
and city, display the results page by page with a given page size. Each page should
not contain more than one result from the same host_id. If there are no remaining
results that have a unique host_id for the current page, backfill with duplicate
host_ids. Pages are separated by an empty string.

This is a classic Airbnb interview question about pagination with deduplication.

Example:
    Input: results = [
        "1,28,300.1,SanFrancisco",
        "4,5,209.1,SanFrancisco",
        "1,7,208.0,SanFrancisco",
        "3,8,207.0,Oakland"
    ], page_size = 2
    Output: [
        "1,28,300.1,SanFrancisco",
        "4,5,209.1,SanFrancisco",
        "",
        "1,7,208.0,SanFrancisco",
        "3,8,207.0,Oakland"
    ]
"""


def solution(results, page_size):
    return None
