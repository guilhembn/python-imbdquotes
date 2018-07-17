IMBD Quotes
===========

Install
-------

Run `pip3 install imbd-quotes --user`

Usage
-----

In a python3 file/interpreter:
```python3
import imbd_quotes
quotes = imbd_quotes.quotes_from_page_id("tt0133093")
```

Features
--------
Retrieves quotes and their character for the **page id**, which has to be provided by the user from the IMBD web URL
 (e.g. https://www.imdb.com/title/tt0133093/ for _The Matrix_).
 
Todos
-----
* Retrieve quotes from movie title instead of page id.