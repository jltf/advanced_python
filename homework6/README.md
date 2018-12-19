# Homework 6

Download a bunch  of files (e.g., from https://www.python.org/downloads/source/):
- using aiohttp, syncio
- using common threads

Benchmark performance in both cases time and put results into the PR description.

---

To benchmark this task I used serving of image usign nginx server.

Image of cat was placed to /var/www/html/ directory and there were some
rules added to prevent caching and to limit speed of downloading.
Image of cat can be downloaded by providing an arbitrary name of file.

location /download/ {
    limit_rate 500k;
    rewrite ^/download/.*\.jpg$ /cat.jpg break;
}
