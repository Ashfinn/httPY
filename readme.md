# Simple Python HTTP Server

A simple HTTP server implemented in Python that handles basic HTTP requests and responds according to specified endpoints.

## Description

This Python script sets up a basic HTTP server that can handle incoming requests and respond accordingly. It currently supports three endpoints:

- `/`: Returns a 200 OK response.
- `/echo/{message}`: Echoes back the provided message.
- `/user-agent`: Retrieves and returns the User-Agent header value from the request.

The server is implemented using Python's socket module, providing a foundational understanding of how HTTP servers can be built from scratch.

## Features

- Handles incoming HTTP GET requests.
- Supports basic endpoints for various responses.
- Logs incoming requests and headers.
- Error handling for common HTTP status codes (200, 400, 404, 500).

[![progress-banner](https://backend.codecrafters.io/progress/http-server/1d701c87-bf62-433b-9c42-d59e3e1422d2)](https://app.codecrafters.io/users/codecrafters-bot?r=2qF)

This is a starting point for Python solutions to the
["Build Your Own HTTP server" Challenge](https://app.codecrafters.io/courses/http-server/overview).

[HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) is the
protocol that powers the web. In this challenge, you'll build a HTTP/1.1 server
that is capable of serving multiple clients.

Along the way you'll learn about TCP servers,
[HTTP request syntax](https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html),
and more.

**Note**: If you're viewing this repo on GitHub, head over to
[codecrafters.io](https://codecrafters.io) to try the challenge.

# Passing the first stage

The entry point for your HTTP server implementation is in `app/main.py`. Study
and uncomment the relevant code, and push your changes to pass the first stage:

```sh
git add .
git commit -m "pass 1st stage" # any msg
git push origin master
```

Time to move on to the next stage!

# Stage 2 & beyond

Note: This section is for stages 2 and beyond.

1. Ensure you have `python (3.11)` installed locally
1. Run `./your_server.sh` to run your program, which is implemented in
   `app/main.py`.
1. Commit your changes and run `git push origin master` to submit your solution
   to CodeCrafters. Test output will be streamed to your terminal.
