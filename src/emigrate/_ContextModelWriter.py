#

from __future__ import absolute_import

import xml.etree.ElementTree as ET

from ._ContextModel import ContextModel


class ContextModelWriter(object):

    def write(self, path, cm_model):
        """ Write model on disk

        @param str path:
        @param ContextModel cm_model:
        """
        root = ET.Element("emigrate", attrib={"version": "0.5"})
        connections = ET.SubElement(root, "connections")
        for c in cm_model.connections:
            node_conn = ET.SubElement(connections, "connection", name=c.name)
            ET.SubElement(node_conn, "param", name="host", value=str(c.host))
            ET.SubElement(node_conn, "param", name="port", value=str(c.port))
            ET.SubElement(node_conn, "param", name="username", value=str(c.username))
            ET.SubElement(node_conn, "param", name="password", value=str(c.password))
        tree = ET.ElementTree(root)
        tree.write(path)
