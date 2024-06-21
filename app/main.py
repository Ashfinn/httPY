import socket
import sys


def handle_GET(path, header_lines):
    # Extract user agent header value
    user_agent = None
    for header in header_lines:
        if header.lower().startswith("user-agent: "):
            user_agent = header.split(":", 1)[1].strip()
            break
        
    # Log the User-Agent header value
    if user_agent:
        print(f"User-Agent: {user_agent}")
        
    # Determine the response based on the path
    if path == '/':
        response = "HTTP/1.1 200 OK\r\n\r\n"
        
    elif path.startswith('/echo/'):
        echo_message = path[len('/echo/'):]
        response = ("HTTP/1.1 200 OK\r\n"
                    "Content-Type: text/plain\r\n"
                    f"Content-Length: {len(echo_message)}\r\n\r\n"
                    f"{echo_message}")
        
    elif path.startswith("/user-agent"):
        if user_agent:    
            response = ("HTTP/1.1 200 OK\r\n"
                        "Content-Type: text/plain\r\n"
                        f"Content-Length: {len(user_agent)}\r\n\r\n"
                        f"{user_agent}")
        else:
            response = "HTTP/1.1 400 Bad Request\r\n\r\n"
            
    elif path.startswith('/files'):
        directory = sys.argv[2]
        filename = path[7:]
        print(directory, filename)
        try:
            with open (f"/{directory}/{filename}", "r") as f:
                body = f.read()
                response = "HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\n"f"Content-Length: {len(body)}\r\n\r\n"f"{body}"
        
        except:
            response = "HTTP/1.1 404 Not Found\r\n\r\n"

    else:
        response = "HTTP/1.1 404 Not Found\r\n\r\n"     
        
    return response 


def handle_POST(path, body):
    if path.startswith('/files/'):
        directory = sys.argv[2]
        filename = path[7:]
        print(directory, filename)
          
        try:
            with open(f"{directory}/{filename}", "w") as f:
                f.write(body)
            response = "HTTP/1.1 201 Created\r\n\r\n"
            
        except Exception as e:
            print(f"Error writing file: {e}")
        
    else:
        response = "HTTP/1.1 404 Not Found\r\n\r\n"
    
    return response


def handle_client(client_socket):
    try:
        # Recieve data from the client
        request_lines = client_socket.recv(1024).decode()   
        
        print(f"Recieved request: {request_lines}")
        
        # Extract the path and headers from the request
        request, *header_lines = request_lines.splitlines()
        method, path, version = request.split()
        body = request_lines.split("\r\n\r\n", 1)[1]
        
        if method.upper() == 'GET':
            response = handle_GET(path, header_lines)
            
        elif method.upper() == 'POST':
            response = handle_POST(path, body)

        # Send an error response back to the client
        client_socket.sendall(response.encode())                
        
    except Exception as e:
        print(f"Error handling client: {e}")
        # Send an error response back to the client

        client_socket.sendall(b"HTTP/1.1 500 Internal Server Error\r\n\r\n")

    finally:
        client_socket.close()


def main():

    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 4221))
    
    # Listen for incoming connections
    server_socket.listen()
    print("Server is listening for incoming connection...")

    while True:
        # Accept a connection from a client
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        # Handle the client connection in a separate thread or process
        handle_client(client_socket)


if __name__ == "__main__":
    main()
