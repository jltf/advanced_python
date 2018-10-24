To benchmark this task I used serving of image usign nginx server.

Image of cat was placed to /var/www/html/ directory and there were some
rules added to prevent caching and to limit speed of downloading.
Image of cat can be downloaded by providing an arbitrary name of file.

location /download/ {
    limit_rate 500k;
    rewrite ^/download/.*\.jpg$ /cat.jpg break;
}
