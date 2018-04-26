import connexion
import six
import yaml
import os.path import expanduser

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
from swagger_server.models.detail import Detail
from swagger_server import util

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import DiskCreateOption

HOME = expanduser("~")
CREDFILE = HOME+"/hid-sp18-502/project-code/cred.yaml"
cred = yaml.load(open(CREADFILE))
subscription_id = cred['azure']['subscript']
credentials = ServicePrincipalCredentials(
                                            client_id=cred['azure']['clientId'],
                                            secret=cred['azure']['clentSecret'],
                                            tenant=cred['azure']['tenantId']
                                            )
resource_client = ResourceManagementClient(credentials, subscription_id)
compute_client = ComputeManagementClient(credentials, subscription_id)
network_client = NetworkManagementClient(credentials, subscription_id)

def create_disk_by_id(detail):  # noqa: E501
    """create_disk_by_id

    Creates new data disk of given size # noqa: E501

    :param detail: size of new data disk
    :type detail: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        detail = connexion.request.get_json()  # noqa: E501

    disk_creation = compute_client.disks.create_or_update(
        detail['group_name'],
        'myDataDisk1',
        {
            'location': detail['location'],
            'disk_size_gb': int(detail['disk_size']),
            'creation_data': {
                'create_option': DiskCreateOption.empty
            }
        }
    )
    return "Disk created"


def create_ip_by_location(detail):  # noqa: E501
    """create_ip_by_location

    Creates new IP address with given location # noqa: E501

    :param detail: name of IP adress and the location
    :type detail: dict | bytes

    :rtype: str
    """
    detail = {}
    if connexion.request.is_json:
        detail = connexion.request.get_json()  # noqa: E501

    public_ip_addess_params = {
        'location': detail['location'],
        'public_ip_allocation_method': 'Dynamic'
    }
    creation_result = network_client.public_ip_addresses.create_or_update(
        detail['group_name'],
        detail['ip_name'],
        public_ip_addess_params
    )

    return "ip created"


def create_nic_by_id(detail):  # noqa: E501
    """create_nic_by_id

    Creates new network interface card with given name # noqa: E501

    :param detail: name of the network interface card
    :type detail: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        detail = connexion.request.get_json()  # noqa: E501

    subnet_info = network_client.subnets.get(
        detail['group_name'],
        detail['vnet_name'],
        detail['subnet_name']
    )
    publicIPAddress = network_client.public_ip_addresses.get(
        detail['group_name'],
        detail['ip_name']
    )
    nic_params = {
        'location': detail['location'],
        'ip_configurations': [{
            'name': 'myIPConfig',
            'public_ip_address': publicIPAddress,
            'subnet': {
                'id': subnet_info.id
            }
        }]
    }
    creation_result = network_client.network_interfaces.create_or_update(
        detail['group_name'],
        detail['nic_name'],
        nic_params
    )
    return "Network Interface Card created"


def create_resource_group_by_id(id):  # noqa: E501
    """create_resource_group_by_id

    Creates new resource group with given name # noqa: E501

    :param id: name of the resource group
    :type id: str

    :rtype: str
    """
    print('\nCreate Resource Group')
    resource_client.resource_groups.create_or_update(id,
                                                     {'location': LOCATION})
    return 'Resource group created'


def create_subnet_by_id(detail):  # noqa: E501
    """create_subnet_by_id

    Creates new subnet with given name # noqa: E501

    :param detail: name of the sub network
    :type detail: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        detail = connexion.request.get_json()  # noqa: E501

    subnet_params = {
        'address_prefix': '10.0.0.0/24'
    }
    creation_result = network_client.subnets.create_or_update(
        detail['group_name'],
        detail['vnet_name'],
        detail['subnet_name'],
        subnet_params
    )

    return "Subnet created"


def create_virtual_machine_by_id(detail):  # noqa: E501
    """create_virtual_machine_by_id

    Creates new vitual machine with given name # noqa: E501

    :param detail: parameters to create VM like nic, IP Address, Image reference
    :type detail: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        detail = connexion.request.get_json()  # noqa: E501

    nic = network_client.network_interfaces.get(
        detail['group_name'],
        detail['nic_name']
    )

    vm_parameters = {
        'location': detail['location'],
        'os_profile': {
            'computer_name': detail['vm_name'],
            'admin_username': detail['username'],
            'admin_password': detail['password']
        },
        'hardware_profile': {
            'vm_size': detail['vm_size']
        },
        'storage_profile': {
            'image_reference': {
                'publisher': detail['publisher'],
                'offer': detail['offer'],
                'sku': detail['sku'],
                'version': detail['version']
            }
        },
        'network_profile': {
            'network_interfaces': [{
                'id': nic.id
            }]
        }
    }
    creation_result = compute_client.virtual_machines.create_or_update(
        detail['group_name'],
        detail['vm_name'],
        vm_parameters
    )

    return "Virtual Machine created"


def create_vnet_by_id(detail):  # noqa: E501
    """create_vnet_by_id

    Creates new Vnet with given name # noqa: E501

    :param detail: name of the virtual network
    :type detail: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        detail = connexion.request.get_json()  # noqa: E501

    vnet_params = {
        'location': detail['location'],
        'address_space': {
            'address_prefixes': ['10.0.0.0/16']
        }
    }
    creation_result = network_client.virtual_networks.create_or_update(
        detail['group_name'],
        detail['vnet_name'],
        vnet_params
    )
    return "Vnet created"

def delete_resource_group_by_id(id):  # noqa: E501
    """delete_resource_group_by_id

    Delete resource group with given name # noqa: E501

    :param id: name of the resource group
    :type id: str

    :rtype: str
    """
    delete_async_operation = resource_client.resource_groups.delete(id)
    delete_async_operation.wait()
    return "Resource group" + id + " Deleted"

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
                                 ResourcegroupProperties(
                                     group.properties.provisioning_state))


def get_virtual_machine_by_id(detail):  # noqa: E501
    """get_virtual_machine_by_id

    Returns details of virtual machine with given name # noqa: E501

    :param detail: name of the virtual machine and resource group
    :type detail: dict | bytes

    :rtype: VM
    """
    if connexion.request.is_json:
        detail = connexion.request.get_json()  # noqa: E501

    print('\nGet Virtual Machine by Name')
    print(detail['group_name'], detail['vm_name'])
    vm = compute_client.virtual_machines.get(detail['group_name'],
                                             detail['vm_name'])
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

def resourcegroups_get():  # noqa: E501
    """resourcegroups_get

    Returns list of resource group present # noqa: E501


    :rtype: Resourcegroup
    """
    print('\nGet Resource Group List')
    listofgroups = []
    for group in resource_client.resource_groups.list():
        listofgroups.append(Resourcegroup(group.name, group.tags, group.id,
                                 group.managed_by, group.location,
                                 ResourcegroupProperties(
                                     group.properties.provisioning_state)))
    return listofgroups

def start_virtual_machine_by_id(detail):  # noqa: E501
    """start_virtual_machine_by_id

    Start virtual machine with given name # noqa: E501

    :param detail: name of the virtual machine and resource group
    :type detail: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        detail = connexion.request.get_json()  # noqa: E501

    print('\nStart VM')
    async_vm_start = compute_client.virtual_machines.start(detail[
                                                               'group_name'],
                                                           detail['vm_name'])
    async_vm_start.wait()
    return 'Virtual Machine Started'


def stop_virtual_machine_by_id(detail):  # noqa: E501
    """stop_virtual_machine_by_id

    Stop virtual machine with given name # noqa: E501

    :param detail: name of the virtual machine and resource group
    :type detail: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        detail = connexion.request.get_json()  # noqa: E501

    print('\nStop VM')
    async_vm_stop = compute_client.virtual_machines.power_off(detail[
                                                                  'group_name'], detail['vm_name'])
    async_vm_stop.wait()
    return 'Virtual Machine Stopped'


def vms_id_get(id):  # noqa: E501
    """vms_id_get

    Returns list of virtual machines present in given resource group # noqa: E501

    :param id: name of the resource group
    :type id: str

    :rtype: VM
    """
    print('\nList VMs in resource group')
    listofvm = []
    for vm in compute_client.virtual_machines.list(id):
        nic = vm.network_profile.network_interfaces
        listofvm.append(VM(vm.identity, VMOsProfile(vm.os_profile.computer_name,
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
                  vm.type, vm.id, vm.location))
    return listofvm
