Verify how IPs are handled in Heroku
====================================


This is a simple Pyramid app to see how IPs are handled in Heroku and how to
get an IP we can trust without adversaries being able to spoof their IP with
headers.

It goes a little something like this:


App deployed, let's do a request:

```bash
$ curl https://polar-forest-10391.herokuapp.com/

Request info:
    request.client_addr: <MY REAL IP>
    request.remote_addr: 10.157.148.138  # Heroku internal IP
    request.headers['X-Forwarded-For']: <MY REAL IP>

```

All good, pyramid thinks my IP is what it really is. Now, let's try to spoof
the real IP:

```bash
$ curl -H "X-Forwarded-For: 6.6.6.6" https://polar-forest-10391.herokuapp.com/

Request info:
    request.client_addr: 6.6.6.6
    request.remote_addr: 10.157.148.138
    request.headers['X-Forwarded-For']: 8.8.8.8, <MY REAL IP>

```

Aha! Pyramid now thinks that my real IP is 6.6.6.6, a spoofed one!

Does `guniron` setting `forwarded_allow_ips = '*'` help?

```bash
$ curl -H"X-Forwarded-For: 6.6.6.6" https://polar-forest-10391.herokuapp.com/

Request info:
    request.client_addr: 6.6.6.6
    request.remote_addr: 10.150.135.91
    request.headers['X-Forwarded-For']: 6.6.6.6, <MY REAL IP>
```

No, not really.

Conclusion: When running Pyramid with guniorn on Heroku, you should set
*the last IP* in `request.client_addr` as `request.client_addr` so that all code
that relies on having user's IP works.

## We're hiring!

At Niteo we regularly contribute back to the Open Source community. If you do too, we'd like to invite you to [join our team](https://niteo.co/careers)!
¸
