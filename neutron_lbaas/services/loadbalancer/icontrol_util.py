import json
import requests
from oslo_log import log as logging

BIGIP_ADDRESS = '172.28.9.89'
BIGIP_USER = 'admin'
BIGIP_PASS = 'admin'

LOG = logging.getLogger(__name__)

def get_lb_member(ip=BIGIP_ADDRESS, name=None, folder='Common'):
    bigip = requests.session()
    bigip.auth = (BIGIP_USER, BIGIP_PASS)
    bigip.verify = False
    bigip.headers.update({'Content-Type': 'application/json'})
    BASE_URL = 'https://%s/mgmt/tm' % ip
    folder = str(folder).replace('/', '')
    request_url = BASE_URL + '/ltm/pool/'
    request_url += '~Project_' + folder + '~Project_' + name
    request_url += '/members'
    print(request_url)
    result = bigip.get(request_url)
    members = []
    if result.status_code < 400:
        LOG.info("success, result is %s.", result.text)
        return_obj = json.loads(result.text)
        if 'items' in return_obj:
            for member in return_obj['items']:
                (addr, port) = split_addr_port(member['name'])
                members.append(
                    {'addr': addr,
                     'port': int(port),
                     'state': member['state']})
    else:
        LOG.error("operation fail, cause %s", result.text)
    return members

def split_addr_port(dest):
    if len(dest.split(':')) > 2:
        # ipv6: bigip syntax is addr.port
        parts = dest.split('.')
    else:
        # ipv4: bigip syntax is addr:port
        parts = dest.split(':')
    if len(parts[0].split('%')) > 1:
        addr_parts = parts[0].split('%')
        parts[0] = addr_parts[0]
        print(addr_parts)
        print(parts[0])
    return (parts[0], parts[1])


def main():
    print("this message is from main function")
    members = get_lb_member('dbebcbdf-0a85-4793-a348-b2f1031ef6f5','61a7756e94e749e28e56ca407a533259')
    print(members)

if __name__ == '__main__':
    main()