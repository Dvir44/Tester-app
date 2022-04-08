import json
import socket, threading

class Server:
    def __init__(self,ip,port):
        self.socket = socket.socket()
        self.socket.bind((ip,port))
        self.socket.listen(5)
        self.clients = {} # dictionary of connected users
        print("Server is up and running")
    
    def get_connection(self):
        client, address = self.socket.accept()
        thread = threading.Thread(target=Server.handle_client , args=(self,client,client_id,))
        client_id = len(self.clients)
        self.clients.update({client_id:client})

    def handle_client(self,client,client_id):
        data = client.recv(1024).decode()
        request = json.loads(data)
        
        action = request["action"]
        if action == 'login': # signup or login
            username = request["username"]
            password = request["password"]
            db.login(username, password)
            
        elif action == 'signup':
            username = request["username"]
            password = request["password"]
            email = request["email"]
            user_type = request["user_type"] # teacher or student
            db.newUser(username, password, email, user_type)

        # if(action=="Login"):
        #     username = Server.login(self, client,client_id)
        # if(action=="Signup"):
        #     Server.signup(self,client)

        status = client.recv(1024).decode() # is the user an uploader / signer
        if(status=="uploader"):
            Server.uploader(self, client, username)
        if(status=="signer"):
            Server.signer(self, client, username) ####


    def login(self, client,client_id):
        pass

    def signup(self, client):
        pass

    def uploader(self,client,username):
        pass
    
def main():
    server = Server("127.0.0.1",12345)
    
main()