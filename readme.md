# httPY
[![progress-banner](https://backend.codecrafters.io/progress/http-server/1d701c87-bf62-433b-9c42-d59e3e1422d2)](https://app.codecrafters.io/users/codecrafters-bot?r=2qF)

This is a solution to the
["Build Your Own HTTP server" Challenge](https://app.codecrafters.io/courses/http-server/overview).

A simple HTTP server implemented in Python that handles basic HTTP requests and responds according to specified endpoints.

## Description

This Python script sets up a basic HTTP server that can handle incoming requests and respond accordingly. It currently supports several endpoints:

- `/`: Returns a 200 OK response.
- `/echo/{message}`: Echoes back the provided message.
- `/user-agent`: Retrieves and returns the User-Agent header value from the request.
- `/files/{filename}`: Serves a file from the specified directory.
- POST `/files/{filename}`: Accepts file uploads and stores them in the specified directory.

The server is implemented using Python's socket module, providing a foundational understanding of how HTTP servers can be built from scratch.

## Features

- Handles incoming HTTP GET and POST requests.
- Supports basic endpoints for various responses.
- Logs incoming requests and headers.
- Serves static files from a specified directory.
- Accepts file uploads and stores them in a specified directory.
- Error handling for common HTTP status codes (200, 400, 404, 500).

# Roadmap

This roadmap outlines the planned enhancements and features for the httPY project. My goal is to improve the coolness, uniqueness, employability, and code quality of the project.

- [ ] Add HTTPS support for secure communication.
- [ ] Implement request routing capabilities.
- [ ] Develop middleware functionality.
- [ ] Create a web-based interface for monitoring server activity.
- [ ] Integrate real-time data processing features.
- [ ] Provide examples integrating with modern web frameworks.
- [ ] Develop detailed use-case examples and tutorials.
- [ ] Enhance documentation with comprehensive guides.
- [ ] Showcase real-world applications or projects using httPY.
- [ ] Create a series of tutorial videos demonstrating usage and features.
- [ ] Improve code comments and documentation.
- [ ] Implement extensive error handling and logging.
- [ ] Write unit tests to ensure code reliability and maintainability.
- [ ] Refactor code for better readability and performance.

## Contribution
I welcome contributions from the community! Feel free to open issues, submit pull requests, or suggest features and improvements.

Together, let's make httPY a powerful and robust HTTP server implementation in Python!
