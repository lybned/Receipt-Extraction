import socket
import unittest

def is_port_open(port, host="127.0.0.1"):

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex((host,port))
	print("result",result)
	sock.close()	
	if result == 0:
	   return True
	else:
	   return False

		
		
class Test_Connect(unittest.TestCase):
	def test_connect(self):
		self.assertTrue( is_port_open(7777), "Port 7777 is NOT opened.")
	
if __name__ == "__main__":
    unittest.main()