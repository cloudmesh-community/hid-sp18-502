import connexion
import six

from swagger_server.models.resourcegroup import Resourcegroup  # noqa: E501
from swagger_server.models.resourcegroup_properties import ResourcegroupProperties  #
# noqa: E501
from swagger_server.models.vm import VM  # noqa: E501
from swagger_server.models.vm_hardware_profile import VMHardwareProfile  # noqa: E501
from swagger_server.models.vm_network_profile import VMNetworkProfile  # noqa:
# E501
from swagger_server.models.vm_os_profile import VMOsProfile  # noqa: E501
from swagger_server.models.vm_storage_profile import VMStorageProfile  # noqa:
# E501
from swagger_server.models.vm_storage_profile_image_ref import VMStorageProfileImageRef
# noqa: E501
from swagger_server import util

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import DiskCreateOption

# Azure Datacenter
LOCATION = 'westus'

# Network
VNET_NAME = 'azure-sample-vnet'
SUBNET_NAME = 'azure-sample-subnet'

IP_CONFIG_NAME = 'azure-sample-ip-config'
NIC_NAME = 'azure-sample-nic'
USERNAME = 'userlogin'
PASSWORD = 'Pa$$w0rd91'
VM_NAME = 'VmName'

# VM References
VM_REFERENCE = {
    'linux': {
        'publisher': 'Canonical',
        'offer': 'UbuntuServer',
        'sku': '16.04.0-LTS',
        'version': 'latest'
    },
    'windows': {
        'publisher': 'MicrosoftWindowsServerEssentials',
        'offer': 'WindowsServerEssentials',
        'sku': 'WindowsServerEssentials',
        'version': 'latest'
    }
}

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

def create_resource_group_by_id(id):  # noqa: E501
    """create_resource_group_by_id

    Creates new resource group with given name # noqa: E501

    :param id: name of the resource group
    :type id: str

    :rtype: str
    """
    # Create Resource group
    print('\nCreate Resource Group')
    resource_client.resource_groups.create_or_update(id,
                                                     {'location': LOCATION})
    return 'Resource created'


def create_virtual_machine_by_id(id):  # noqa: E501
    """create_virtual_machine_by_id

    Creates new vitual machine with given name # noqa: E501

    :param id: name of the virtual machine
    :type id: str

    :rtype: str
    """
    nic = create_nic(network_client)

    # Create Linux VM
    print('\nCreating Linux Virtual Machine')
    vm_parameters = create_vm_parameters(nic.id, VM_REFERENCE['linux'])
    async_vm_creation = compute_client.virtual_machines.create_or_update(
        GROUP_NAME, id, vm_parameters)
    async_vm_creation.wait()

    return 'Virtual Machine Created'


def get_resource_group_by_id(id):  # noqa: E501
    """get_resource_group_by_id

    Returns details of resource group with given name # noqa: E501

    :param id: name of the resource group
    :type id: str

    :rtype: Resourcegroup
    """
    print('\nGet Resource Group')
    for group in resource_client.resource_groups.list():
        if (group.name == id):
            return Resourcegroup(group.name, group.tags, group.id,
                                 group.managed_by, group.location,
                                 ResourcegroupProperties(group.properties.provisioning_state))



def get_virtual_machine_by_id(id):  # noqa: E501
    """get_virtual_machine_by_id

    Returns details of virtual machine with given name # noqa: E501

    :param id: name of the virtual machine
    :type id: str

    :rtype: VM
    """
    # Get the virtual machine by name
    print('\nGet Virtual Machine by Name')
    vm = compute_client.virtual_machines.get(GROUP_NAME, id)
    nic = vm.network_profile.network_interfaces
    return VM(vm.identity, VMOsProfile(vm.os_profile.computer_name,
                                       vm.os_profile.admin_username,
                                       vm.os_profile.admin_password),
              VMStorageProfile(VMStorageProfileImageRef(
                  vm.storage_profile.image_reference.publisher,
                  vm.storage_profile.image_reference.offer,
                  vm.storage_profile.image_reference.sku,
                  vm.storage_profile.image_reference.version)), vm.name,
              vm.tags, vm.vm_id, VMHardwareProfile(
            vm.hardware_profile.vm_size), vm.provisioning_state,
              VMNetworkProfile(nic[0].id),
              vm.type, vm.id, vm.location)


def start_virtual_machine_by_id(id):  # noqa: E501
    """start_virtual_machine_by_id

    Start vitual machine with given name # noqa: E501

    :param id: name of the virtual machine
    :type id: str

    :rtype: str
    """
    # Start the VM
    print('\nStart VM')
    async_vm_start = compute_client.virtual_machines.start(GROUP_NAME, id)
    async_vm_start.wait()
    return 'Virtual Machine Started'


def stop_virtual_machine_by_id(id):  # noqa: E501
    """stop_virtual_machine_by_id

    Stop vitual machine with given name # noqa: E501

    :param id: name of the virtual machine
    :type id: str

    :rtype: str
    """
    # Stop the VM
    print('\nStop VM')
    async_vm_stop = compute_client.virtual_machines.power_off(GROUP_NAME, id)
    async_vm_stop.wait()
    return 'Virtual Machine Stopped'


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
