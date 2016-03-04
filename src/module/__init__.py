__version__ = '0.0.1a'
__all__ = ['options', 'osimage']
__author__ = 'Dmitry Chirikov'

from luna.config import *
import pymongo
from options import Options
from osimage import OsImage
from ifcfg import IfCfg
from bmcsetup import BMCSetup
#from group import Group
from node import Node, Group
from switch import Switch, MacUpdater
from network import Network
from tracker import *
from manager import Manager


def list(collection):
    import logging
    logging.basicConfig(level=logging.INFO)
#    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    try:
        mongo_client = pymongo.MongoClient()
    except:
        logger.error("Unable to connect to MongoDB.")
        raise RuntimeError
    logger.debug("Connection to MongoDB was successful.")
    mongo_db = mongo_client[db_name]
    mongo_collection = mongo_db[collection]
    ret = []
    for doc in mongo_collection.find({}):
        try:
            ret.extend([doc['name']])
        except:
            ret.extend([doc['_id']])
    return ret

def set_mac_node(mac,node, mongodg = None):
    import logging
    logging.basicConfig(level=logging.INFO)
#    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    try:
        mongo_client = pymongo.MongoClient()
    except:
        logger.error("Unable to connect to MongoDB.")
        raise RuntimeError
    logger.debug("Connection to MongoDB was successful.")
    mongo_db = mongo_client[db_name]
    mongo_collection = mongo_db['mac']
    mongo_collection.remove({'mac': mac})
    mongo_collection.remove({'node': node})
    mongo_collection.insert({'mac': mac, 'node': node})