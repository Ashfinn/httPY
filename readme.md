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