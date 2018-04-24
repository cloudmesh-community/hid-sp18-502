from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import DiskCreateOption

# Azure Datacenter
LOCATION = 'westus'

# Resource Group
GROUP_NAME = 'Cloudmesh'
NEW_GROUP_NAME = 'azure_group'
VM_NAME = 'Ubuntu'
subscription_id = '00efbb10-0564-4235-9a6d-256b4b94070b'
credentials = ServicePrincipalCredentials(
                                            client_id='9ab22f0a-37be-48a5-bc58-cf6303a845d9',
                                            secret='UmnVkEyZkEEvP/bRPa679DPl0lEG1o+YKvQBU+BpGj4=',
                                            tenant='d751dd0d-32c1-4886-b132-9f56e676c2b9'
                                            )
resource_client = ResourceManagementClient(credentials, subscription_id)
compute_client = ComputeManagementClient(credentials, subscription_id)
network_client = NetworkManagementClient(credentials, subscription_id)

# Get the virtual machine by name
print('\nGet Virtual Machine by Name')
virtual_machine = compute_client.virtual_machines.get(GROUP_NAME,VM_NAME)
print(virtual_machine)

# Create Resource group
print('\nCreate Resource Group')
resource_client.resource_groups.create_or_update(NEW_GROUP_NAME, {'location': LOCATION})

# get list of all the resource group
for item in resource_client.resource_groups.list():
    print(item)

# get list resources under given resource group
# List VM in resource group
print('\nList VMs in resource group')
for vm in compute_client.virtual_machines.list(GROUP_NAME):
    print("\tVM: {}".format(vm.name))

# create new NIC
nic = create_nic(network_client)

# create new VM
print('\nCreating Linux Virtual Machine')
    vm_parameters = create_vm_parameters(nic.id, VM_REFERENCE['linux'])
    async_vm_creation = compute_client.virtual_machines.create_or_update(
                                                                         GROUP_NAME, VM_NAME, vm_parameters)
        async_vm_creation.wait()


# create new disk
print('\nCreate (empty) managed Data Disk')
async_disk_creation = compute_client.disks.create_or_update(
                                                            GROUP_NAME,
                                                            'mydatadisk1',
                                                            {
                                                            'location': LOCATION,
                                                            'disk_size_gb': 1,
                                                            'creation_data': {
                                                            'create_option': DiskCreateOption.empty
                                                            }
                                                            }
                                                            )
data_disk = async_disk_creation.result()

# Deallocating the VM (in preparation for a disk resize)
print('\nDeallocating the VM (to prepare for a disk resize)')
    async_vm_deallocate = compute_client.virtual_machines.deallocate(GROUP_NAME, VM_NAME)
    async_vm_deallocate.wait()

# Start the VM
print('\nStart VM')
async_vm_start = compute_client.virtual_machines.start(GROUP_NAME, VM_NAME)
async_vm_start.wait()

# Stop the VM
print('\nStop VM')
async_vm_stop = compute_client.virtual_machines.power_off(GROUP_NAME, VM_NAME)
async_vm_stop.wait()

# function to create NIC
def create_nic(network_client):
    """Create a Network Interface for a VM.
        """
    # Create VNet
    print('\nCreate Vnet')
    async_vnet_creation = network_client.virtual_networks.create_or_update(
                                                                           GROUP_NAME,
                                                                           VNET_NAME,
                                                                           {
                                                                                'location': LOCATION,
                                                                                'address_space': {
                                                                                'address_prefixes': ['10.0.0.0/16']
                                                                                }
                                                                           }
                                                                           )
    async_vnet_creation.wait()
                                                                           
    # Create Subnet
    print('\nCreate Subnet')
    async_subnet_creation = network_client.subnets.create_or_update(
                                                                    GROUP_NAME,
                                                                    VNET_NAME,
                                                                    SUBNET_NAME,
                                                                    {'address_prefix': '10.0.0.0/24'}
                                                                    )
    subnet_info = async_subnet_creation.result()
                                                                           
    # Create NIC
    print('\nCreate NIC')
    async_nic_creation = network_client.network_interfaces.create_or_update(
                                                                            GROUP_NAME,
                                                                            NIC_NAME,
                                                                            {
                                                                                'location': LOCATION,
                                                                                'ip_configurations': [{
                                                                                    'name': IP_CONFIG_NAME,
                                                                                    'subnet': {
                                                                                        'id': subnet_info.id
                                                                                    }
                                                                                }]
                                                                            }
                                                                            )
return async_nic_creation.result()


def create_vm_parameters(nic_id, vm_reference):
    """Create the VM parameters structure.
        """
    return {
        'location': LOCATION,
        'os_profile': {
            'computer_name': VM_NAME,
            'admin_username': USERNAME,
            'admin_password': PASSWORD
        },
        'hardware_profile': {
            'vm_size': 'Standard_DS1_v2'
        },
        'storage_profile': {
            'image_reference': {
                'publisher': vm_reference['publisher'],
                'offer': vm_reference['offer'],
                'sku': vm_reference['sku'],
                'version': vm_reference['version']
            },
        },
        'network_profile': {
            'network_interfaces': [{
                                   'id': nic_id,
                                   }]
        },
}

  '/vms/{id}':
    get:
      description: "Returns list of all available virtual machines
      present in resource group given as input"
      operationId: getVMList
      produces:
        - 'application/json'
      parameters:
        - name: id
          in: path
          description: 'name of the resource group'
          required: true
          type: string
      responses:
        '200':
          desciption: 'A list of all virtual machines available in resource
          group'
          schema:
            type: "array"
            items:
              $ref: '#/definitions/VM'

'/resourcegroups':
    get:
      description: "Returns list of all available resource groups"
      operationId: getResourceGroupList
      produces:
        - 'application/json'
      responses:
        '200':
          desciption: 'A list of all the resource groups available'
          schema:
            type: 'array'
            items:
              $ref: '#/definitions/Resourcegroup'

