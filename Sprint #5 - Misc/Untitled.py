#!/usr/bin/env python
# coding: utf-8

# In[4]:


import paramiko
from getpass import getpass

# Set the hostname, username, and password for the Raspberry Pi
HOSTNAME = "dex.local"
USERNAME = "pi"
PASSWORD=getpass("Enter password:")  # robot password
# Create an SSH client
ssh = paramiko.SSHClient()

# Add your Raspberry Pi's hostname to the known hosts file
ssh.load_system_host_keys()

# Connect to the Raspberry Pi
ssh.connect(HOSTNAME, username=USERNAME, password=PASSWORD)

# Execute a command on the Raspberry Pi
stdin, stdout, stderr = ssh.exec_command("python3 python/blah.py")

# Print the output of the command
print(stdout.read())

# Close the connection
ssh.close()


# In[7]:


import paramiko
import xmlrpc.client

# Set the hostname, username, and password for the remote machine
HOSTNAME = "dex.local"
USERNAME = "pi"
PASSWORD=getpass("Enter password:")  # robot password

# Create an SSH client
ssh = paramiko.SSHClient()

# Add the remote host's hostname to the known hosts file
ssh.load_system_host_keys()

# Connect to the remote host
ssh.connect(HOSTNAME, username=USERNAME, password=PASSWORD)

# Create an XML-RPC client using the SSH transport
transport = ssh.get_transport()
xmlrpc_client = xmlrpc.client.ServerProxy("http://dex.local:8002/", transport=transport)

# Call an XML-RPC method on the remote host
result = xmlrpc_client.your_method_name()

# Print the result of the XML-RPC call
print(result)

# Close the connection
ssh.close()




# In[ ]:





# In[ ]:


import paramiko
import xmlrpc.client

# Set the hostname, username, and password for the remote machine
HOSTNAME = "your_hostname"
USERNAME = "username"
PASSWORD=getpass("Enter password:")  # robot password
port="someport"

# Create an SSH client
ssh = paramiko.SSHClient()

# Add the remote host's hostname to the known hosts file
ssh.load_system_host_keys()

# Connect to the remote host
ssh.connect(HOSTNAME, username=USERNAME, password=PASSWORD)

# Create an XML-RPC client using the SSH transport
transport = ssh.get_transport()
xmlrpc_client = xmlrpc.client.ServerProxy(f"http://{hostname}:{port}", transport=transport)

# Call an XML-RPC method on the remote host
result = xmlrpc_client.your_method_name()

# Print the result of the XML-RPC call
print(result)

# Close the connection
ssh.close()




# In[11]:


import paramiko
from getpass import getpass

# Set the hostname, username, and password for the Raspberry Pi
HOSTNAME = "dex.local"
USERNAME = "pi"
PASSWORD=getpass("Enter password:")  # robot password
# Create an SSH client
ssh = paramiko.SSHClient()

# Add your Raspberry Pi's hostname to the known hosts file
ssh.load_system_host_keys()

# Connect to the Raspberry Pi
ssh.connect(HOSTNAME, username=USERNAME, password=PASSWORD)

# Execute a command on the Raspberry Pi
stdin, stdout, stderr = ssh.exec_command("python3 python/test_paramiko_stream.py")

# Print the output of the command
stdin.write("forward 5"+"\n")
x=input("pausing")
stdin.write("exit"+"\n")

# Close the connection
ssh.close()


# In[12]:


import paramiko
from getpass import getpass

# Set the hostname, username, and password for the Raspberry Pi
HOSTNAME = "dex.local"
USERNAME = "pi"
PASSWORD=getpass("Enter password:")  # robot password
# Create an SSH client
ssh = paramiko.SSHClient()


# In[10]:





# In[ ]:




