import packet

manager = packet.Manager(auth_token="tokengoeshere")
#create_op_sys = manager.operating_system

device = manager.create_device(project_id='project-id',
                               hostname='node-name-of-your-choice',
                               plan='baremetal_1', facility='ewr1',
                               operating_system='ubuntu_14_04')

#print(create_op_sys)
print(device)