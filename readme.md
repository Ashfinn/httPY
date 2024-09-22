<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<br />
<div align="center">
   <h3 align="center">httPY</h3>

  <p align="center">
    A simple HTTP server implementation in Python.
    <br />
    <br />
    <a href="https://github.com/Ashfinn/httPY/issues">Report Bug</a>
    ·
    <a href="https://github.com/Ashfinn/httPY/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

httPY is a solution to the [**"Build Your Own HTTP Server" Challenge**](https://app.codecrafters.io/courses/http-server/overview). It is a simple HTTP server implemented in Python that handles basic HTTP requests and responds according to specified endpoints.

### Features

- Handles incoming HTTP GET and POST requests.
- Supports various endpoints:
  - `/`: Returns a 200 OK response.
  - `/echo/{message}`: Echoes back the provided message.
  - `/user-agent`: Retrieves and returns the User-Agent header from the request.
  - `/files/{filename}`: Serves a file from the specified directory.
  - POST `/files/{filename}`: Accepts file uploads and stores them in the specified directory.
- Logs incoming requests and headers.
- Serves static files from a specified directory.
- Accepts file uploads and stores them appropriately.
- Error handling for common HTTP status codes (200, 400, 404, 500).
- Implemented using Python's `socket` module for foundational understanding.

### Built With

[![Python][Python.svg]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Follow these instructions to set up httPY locally.

### Prerequisites

Ensure you have Python installed on your machine. httPY is compatible with Python 3.6 and above.

### Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/Ashfinn/httPY.git
   ```
2. **Navigate to the project directory**
   ```sh
   cd httPY
   ```
3. **(Optional) Create and activate a virtual environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
5. **Run the server**
   ```sh
   python server.py
   ```
6. **Access the server**
   Open your browser and navigate to `http://localhost:8080`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE -->
## Usage

httPY provides several endpoints to interact with. Below are some examples of how to use them:

- **Root Endpoint**
  ```sh
  GET /
  ```
  **Response:**
  ```
  HTTP/1.1 200 OK
  ```

- **Echo Message**
  ```sh
  GET /echo/HelloWorld
  ```
  **Response:**
  ```
  HTTP/1.1 200 OK
  HelloWorld
  ```

- **User-Agent**
  ```sh
  GET /user-agent
  ```
  **Response:**
  ```
  HTTP/1.1 200 OK
  [Your User-Agent]
  ```

- **Serve a File**
  ```sh
  GET /files/example.txt
  ```
  **Response:**
  ```
  HTTP/1.1 200 OK
  [Contents of example.txt]
  ```

- **Upload a File**
  ```sh
  POST /files/upload.txt
  [File data]
  ```
  **Response:**
  ```
  HTTP/1.1 201 Created
  ```

For more detailed usage examples and advanced configurations, please refer to the [Documentation](https://github.com/Ashfinn/httPY/docs).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

This roadmap outlines the planned enhancements and features for the httPY project. The goal is to improve the functionality, security, and usability of the server.

- [x] Implement basic HTTP GET and POST request handling
- [x] Support multiple endpoints (`/`, `/echo/{message}`, `/user-agent`, `/files/{filename}`)
- [x] Serve static files from a specified directory
- [x] Accept and store file uploads
- [x] Log incoming requests and headers
- [x] Handle common HTTP status codes (200, 400, 404, 500)
- [ ] Add HTTPS support for secure communication
- [ ] Implement request routing capabilities
- [ ] Develop middleware functionality
- [ ] Create a web-based interface for monitoring server activity
- [ ] Integrate real-time data processing features
- [ ] Provide examples integrating with modern web frameworks
- [ ] Develop detailed use-case examples and tutorials
- [ ] Enhance documentation with comprehensive guides
- [ ] Showcase real-world applications or projects using httPY
- [ ] Create a series of tutorial videos demonstrating usage and features
- [ ] Improve code comments and documentation
- [ ] Implement extensive error handling and logging
- [ ] Write unit tests to ensure code reliability and maintainability
- [ ] Refactor code for better readability and performance

See the [open issues](https://github.com/Ashfinn/httPY/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. **Fork the Project**
   ```sh
   git clone https://github.com/Ashfinn/httPY.git
   ```
2. **Create your Feature Branch**
   ```sh
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your Changes**
   ```sh
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the Branch**
   ```sh
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

Feel free to open issues for bug reports or feature requests. Don't forget to give the project a star! Thanks again!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Obidur Rahman - [@linkedIn](https://linkedin.com/in/obidur-rahman-shawal) - obidur.shawal@gmail.com

Project Link: [https://github.com/Ashfinn/httPY](https://github.com/Ashfinn/httPY)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

- [Codecrafters.io](https://codecrafters.io) for the HTTP Server Challenge
- [Python Documentation](https://docs.python.org/3/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/Ashfinn/httPY.svg?style=for-the-badge
[contributors-url]: https://github.com/Ashfinn/httPY/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Ashfinn/httPY.svg?style=for-the-badge
[forks-url]: https://github.com/Ashfinn/httPY/network/members
[stars-shield]: https://img.shields.io/github/stars/Ashfinn/httPY.svg?style=for-the-badge
[stars-url]: https://github.com/Ashfinn/httPY/stargazers
[issues-shield]: https://img.shields.io/github/issues/Ashfinn/httPY.svg?style=for-the-badge
[issues-url]: https://github.com/Ashfinn/httPY/issues
[license-shield]: https://img.shields.io/github/license/Ashfinn/httPY.svg?style=for-the-badge
[license-url]: https://github.com/Ashfinn/httPY/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/obidur-rahman-shawal

[Python.svg]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[product-screenshot]: images/screenshot.png
