import asynchat
import asyncore

PORT = 6666


class EndSession(Exception):
    pass

class ChatServer(asyncore.dispatcher):
    """
     chat server
     """

    def __init__(self,port):
        asyncore.dispatcher.__init__(self)
        self.create_socket()
        self.set_reuse_addr()
        self.bind(('',port))
        self.listen(5)
        self.users = {}
        self.main_room = ChatRoom(self)

    def handle_accept(self):
        conn,addr = self.accept()
        ChatSession(self,conn)




class ChatSession(asynchat.async_chat):
    """
    the duty of chat for client
    """
    def __init__(self,server,sock):
        asynchat.async_chat.__init__(self,sock)
        self.server = server
        self.set_terminator(b'\n')
        self.data = []
        self.name = None
        self.enter(LoginRoom(server))

    def enter(self,room):
        try:
            cur = self.room
        except AttributeError:
            pass
        else:
            cur.remove(self)
        self.room = room
        room.add(self)

    def collect_incoming_data(self,data):
        self.data.append(data.decode("utf-8"))

    def found_terminator(self):
        line = ''.join(self.data)
        self.data = []
        try:
            self.room.handle(self,line.encode("utf-8"))
        except EndSession:
            self.handle_close()

    def handle_close(self):
        asynchat.async_chat.handle_close(self)
        self.enter(LogouRoom(self.server)

class CommandHandler:
"""
process command
"""
    def unkonw(self,session,cmd):
        session.push(('Unknown command [] \n'.format(cmd)).encode("utf-8"))
    def handle(self,session,line):
        line = line.decode()
        if not line.strip():
            return
        parts = line.split(' ',1)
        cmd = parts[0]
        try:
            line = parts[1].strip()
        except IndexError:
            line = ''
        method = getattr(self,'do_' + cmd, None)
        try:
            method(session,line)
        except TypeError:
            self.unknown(session,cmd)

class LoginRoom(Room):
    """
    ??????
    """

    def add(self, session):
        # ?????????
        Room.add(self, session)
        # ?? asynchat.asyn_chat.push ??????
        session.push(b'Connect Success')

    def do_login(self, session, line):
        # ??????
        name = line.strip()
        # ??????
        if not name:
            session.push(b'UserName Empty')
        # ?????????
        elif name in self.server.users:
            session.push(b'UserName Exist')
        # ???????????????
        else:
            session.name = name
            session.enter(self.server.main_room)


class LogoutRoom(Room):
    """
    ??????
    """
    def add(self, session):
        # ???????
        try:
            del self.server.users[session.name]
        except KeyError:
            pass
class ChatRoom(Room):
    """
    ??????
    """

    def add(self, session):
        # ???????
        session.push(b'Login Success')
        self.broadcast((session.name + ' has entered the room.\n').encode("utf-8"))
        self.server.users[session.name] = session
        Room.add(self, session)

    def remove(self, session):
        # ??????
        Room.remove(self, session)
        self.broadcast((session.name + ' has left the room.\n').encode("utf-8"))

    def do_say(self, session, line):
        # ???????
        self.broadcast((session.name + ': ' + line + '\n').encode("utf-8"))

    def do_look(self, session, line):
        # ??????
        session.push(b'Online Users:\n')
        for other in self.sessions:
            session.push((other.name + '\n').encode("utf-8"))

if __name__ == '__main__':

    s = ChatServer(PORT)
    try:
        print("chat server run at '0.0.0.0:{0}'".format(PORT))
        asyncore.loop()
    except KeyboardInterrupt:
        print("chat server exit")
