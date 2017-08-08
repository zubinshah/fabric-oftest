
# Copyright 2017-present Open Networking Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# Copyright (c) 2008 The Board of Trustees of The Leland Stanford Junior University
# Copyright (c) 2011, 2012 Open Networking Foundation
# Copyright (c) 2012, 2013 Big Switch Networks, Inc.
# See the file LICENSE.pyloxi which should have been included in the source distribution

# Automatically generated by LOXI from template module.py
# Do not modify

import struct
import loxi
import util
import loxi.generic_util

import sys
ofp = sys.modules['loxi.of10']

class action(loxi.OFObject):
    subtypes = {}


    def __init__(self, type=None):
        if type != None:
            self.type = type
        else:
            self.type = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append('\x00' * 4)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        subtype, = reader.peek('!H', 0)
        subclass = action.subtypes.get(subtype)
        if subclass:
            return subclass.unpack(reader)

        obj = action()
        obj.type = reader.read("!H")[0]
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        reader.skip(4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.type != other.type: return False
        return True

    def pretty_print(self, q):
        q.text("action {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')


class experimenter(action):
    subtypes = {}

    type = 65535

    def __init__(self, experimenter=None, data=None):
        if experimenter != None:
            self.experimenter = experimenter
        else:
            self.experimenter = 0
        if data != None:
            self.data = data
        else:
            self.data = ''
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(self.data)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        subtype, = reader.peek('!L', 4)
        subclass = experimenter.subtypes.get(subtype)
        if subclass:
            return subclass.unpack(reader)

        obj = experimenter()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        obj.experimenter = reader.read("!L")[0]
        obj.data = str(reader.read_all())
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.experimenter != other.experimenter: return False
        if self.data != other.data: return False
        return True

    def pretty_print(self, q):
        q.text("experimenter {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("data = ");
                q.pp(self.data)
            q.breakable()
        q.text('}')

action.subtypes[65535] = experimenter

class bsn(experimenter):
    subtypes = {}

    type = 65535
    experimenter = 6035143

    def __init__(self, subtype=None):
        if subtype != None:
            self.subtype = subtype
        else:
            self.subtype = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.subtype))
        packed.append('\x00' * 4)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        subtype, = reader.peek('!L', 8)
        subclass = bsn.subtypes.get(subtype)
        if subclass:
            return subclass.unpack(reader)

        obj = bsn()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        obj.subtype = reader.read("!L")[0]
        reader.skip(4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.subtype != other.subtype: return False
        return True

    def pretty_print(self, q):
        q.text("bsn {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

experimenter.subtypes[6035143] = bsn

class bsn_checksum(bsn):
    type = 65535
    experimenter = 6035143
    subtype = 4

    def __init__(self, checksum=None):
        if checksum != None:
            self.checksum = checksum
        else:
            self.checksum = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.subtype))
        packed.append(util.pack_checksum_128(self.checksum))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = bsn_checksum()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        _subtype = reader.read("!L")[0]
        assert(_subtype == 4)
        obj.checksum = util.unpack_checksum_128(reader)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.checksum != other.checksum: return False
        return True

    def pretty_print(self, q):
        q.text("bsn_checksum {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("checksum = ");
                q.pp(self.checksum)
            q.breakable()
        q.text('}')

bsn.subtypes[4] = bsn_checksum

class bsn_mirror(bsn):
    type = 65535
    experimenter = 6035143
    subtype = 1

    def __init__(self, dest_port=None, vlan_tag=None, copy_stage=None):
        if dest_port != None:
            self.dest_port = dest_port
        else:
            self.dest_port = 0
        if vlan_tag != None:
            self.vlan_tag = vlan_tag
        else:
            self.vlan_tag = 0
        if copy_stage != None:
            self.copy_stage = copy_stage
        else:
            self.copy_stage = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.subtype))
        packed.append(struct.pack("!L", self.dest_port))
        packed.append(struct.pack("!L", self.vlan_tag))
        packed.append(struct.pack("!B", self.copy_stage))
        packed.append('\x00' * 3)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = bsn_mirror()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        _subtype = reader.read("!L")[0]
        assert(_subtype == 1)
        obj.dest_port = reader.read("!L")[0]
        obj.vlan_tag = reader.read("!L")[0]
        obj.copy_stage = reader.read("!B")[0]
        reader.skip(3)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.dest_port != other.dest_port: return False
        if self.vlan_tag != other.vlan_tag: return False
        if self.copy_stage != other.copy_stage: return False
        return True

    def pretty_print(self, q):
        q.text("bsn_mirror {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("dest_port = ");
                q.text("%#x" % self.dest_port)
                q.text(","); q.breakable()
                q.text("vlan_tag = ");
                q.text("%#x" % self.vlan_tag)
                q.text(","); q.breakable()
                q.text("copy_stage = ");
                q.text("%#x" % self.copy_stage)
            q.breakable()
        q.text('}')

bsn.subtypes[1] = bsn_mirror

class bsn_set_tunnel_dst(bsn):
    type = 65535
    experimenter = 6035143
    subtype = 2

    def __init__(self, dst=None):
        if dst != None:
            self.dst = dst
        else:
            self.dst = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.subtype))
        packed.append(struct.pack("!L", self.dst))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = bsn_set_tunnel_dst()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        _subtype = reader.read("!L")[0]
        assert(_subtype == 2)
        obj.dst = reader.read("!L")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.dst != other.dst: return False
        return True

    def pretty_print(self, q):
        q.text("bsn_set_tunnel_dst {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("dst = ");
                q.text("%#x" % self.dst)
            q.breakable()
        q.text('}')

bsn.subtypes[2] = bsn_set_tunnel_dst

class enqueue(action):
    type = 11

    def __init__(self, port=None, queue_id=None):
        if port != None:
            self.port = port
        else:
            self.port = 0
        if queue_id != None:
            self.queue_id = queue_id
        else:
            self.queue_id = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(util.pack_port_no(self.port))
        packed.append('\x00' * 6)
        packed.append(struct.pack("!L", self.queue_id))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = enqueue()
        _type = reader.read("!H")[0]
        assert(_type == 11)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        obj.port = util.unpack_port_no(reader)
        reader.skip(6)
        obj.queue_id = reader.read("!L")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.port != other.port: return False
        if self.queue_id != other.queue_id: return False
        return True

    def pretty_print(self, q):
        q.text("enqueue {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("port = ");
                q.text(util.pretty_port(self.port))
                q.text(","); q.breakable()
                q.text("queue_id = ");
                q.text("%#x" % self.queue_id)
            q.breakable()
        q.text('}')

action.subtypes[11] = enqueue

class nicira(experimenter):
    subtypes = {}

    type = 65535
    experimenter = 8992

    def __init__(self, subtype=None):
        if subtype != None:
            self.subtype = subtype
        else:
            self.subtype = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!H", self.subtype))
        packed.append('\x00' * 2)
        packed.append('\x00' * 4)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        subtype, = reader.peek('!H', 8)
        subclass = nicira.subtypes.get(subtype)
        if subclass:
            return subclass.unpack(reader)

        obj = nicira()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 8992)
        obj.subtype = reader.read("!H")[0]
        reader.skip(2)
        reader.skip(4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.subtype != other.subtype: return False
        return True

    def pretty_print(self, q):
        q.text("nicira {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

experimenter.subtypes[8992] = nicira

class nicira_dec_ttl(nicira):
    type = 65535
    experimenter = 8992
    subtype = 18

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!H", self.subtype))
        packed.append('\x00' * 2)
        packed.append('\x00' * 4)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = nicira_dec_ttl()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 8992)
        _subtype = reader.read("!H")[0]
        assert(_subtype == 18)
        reader.skip(2)
        reader.skip(4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("nicira_dec_ttl {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

nicira.subtypes[18] = nicira_dec_ttl

class output(action):
    type = 0

    def __init__(self, port=None, max_len=None):
        if port != None:
            self.port = port
        else:
            self.port = 0
        if max_len != None:
            self.max_len = max_len
        else:
            self.max_len = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(util.pack_port_no(self.port))
        packed.append(struct.pack("!H", self.max_len))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = output()
        _type = reader.read("!H")[0]
        assert(_type == 0)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        obj.port = util.unpack_port_no(reader)
        obj.max_len = reader.read("!H")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.port != other.port: return False
        if self.max_len != other.max_len: return False
        return True

    def pretty_print(self, q):
        q.text("output {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("port = ");
                q.text(util.pretty_port(self.port))
                q.text(","); q.breakable()
                q.text("max_len = ");
                q.text("%#x" % self.max_len)
            q.breakable()
        q.text('}')

action.subtypes[0] = output

class set_dl_dst(action):
    type = 5

    def __init__(self, dl_addr=None):
        if dl_addr != None:
            self.dl_addr = dl_addr
        else:
            self.dl_addr = [0,0,0,0,0,0]
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!6B", *self.dl_addr))
        packed.append('\x00' * 6)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = set_dl_dst()
        _type = reader.read("!H")[0]
        assert(_type == 5)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        obj.dl_addr = list(reader.read('!6B'))
        reader.skip(6)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.dl_addr != other.dl_addr: return False
        return True

    def pretty_print(self, q):
        q.text("set_dl_dst {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("dl_addr = ");
                q.text(util.pretty_mac(self.dl_addr))
            q.breakable()
        q.text('}')

action.subtypes[5] = set_dl_dst

class set_dl_src(action):
    type = 4

    def __init__(self, dl_addr=None):
        if dl_addr != None:
            self.dl_addr = dl_addr
        else:
            self.dl_addr = [0,0,0,0,0,0]
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!6B", *self.dl_addr))
        packed.append('\x00' * 6)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = set_dl_src()
        _type = reader.read("!H")[0]
        assert(_type == 4)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        obj.dl_addr = list(reader.read('!6B'))
        reader.skip(6)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.dl_addr != other.dl_addr: return False
        return True

    def pretty_print(self, q):
        q.text("set_dl_src {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("dl_addr = ");
                q.text(util.pretty_mac(self.dl_addr))
            q.breakable()
        q.text('}')

action.subtypes[4] = set_dl_src

class set_nw_dst(action):
    type = 7

    def __init__(self, nw_addr=None):
        if nw_addr != None:
            self.nw_addr = nw_addr
        else:
            self.nw_addr = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.nw_addr))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = set_nw_dst()
        _type = reader.read("!H")[0]
        assert(_type == 7)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        obj.nw_addr = reader.read("!L")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.nw_addr != other.nw_addr: return False
        return True

    def pretty_print(self, q):
        q.text("set_nw_dst {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("nw_addr = ");
                q.text("%#x" % self.nw_addr)
            q.breakable()
        q.text('}')

action.subtypes[7] = set_nw_dst

class set_nw_src(action):
    type = 6

    def __init__(self, nw_addr=None):
        if nw_addr != None:
            self.nw_addr = nw_addr
        else:
            self.nw_addr = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.nw_addr))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = set_nw_src()
        _type = reader.read("!H")[0]
        assert(_type == 6)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        obj.nw_addr = reader.read("!L")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.nw_addr != other.nw_addr: return False
        return True

    def pretty_print(self, q):
        q.text("set_nw_src {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("nw_addr = ");
                q.text("%#x" % self.nw_addr)
            q.breakable()
        q.text('}')

action.subtypes[6] = set_nw_src

class set_nw_tos(action):
    type = 8

    def __init__(self, nw_tos=None):
        if nw_tos != None:
            self.nw_tos = nw_tos
        else:
            self.nw_tos = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!B", self.nw_tos))
        packed.append('\x00' * 3)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = set_nw_tos()
        _type = reader.read("!H")[0]
        assert(_type == 8)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        obj.nw_tos = reader.read("!B")[0]
        reader.skip(3)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.nw_tos != other.nw_tos: return False
        return True

    def pretty_print(self, q):
        q.text("set_nw_tos {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("nw_tos = ");
                q.text("%#x" % self.nw_tos)
            q.breakable()
        q.text('}')

action.subtypes[8] = set_nw_tos

class set_tp_dst(action):
    type = 10

    def __init__(self, tp_port=None):
        if tp_port != None:
            self.tp_port = tp_port
        else:
            self.tp_port = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!H", self.tp_port))
        packed.append('\x00' * 2)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = set_tp_dst()
        _type = reader.read("!H")[0]
        assert(_type == 10)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        obj.tp_port = reader.read("!H")[0]
        reader.skip(2)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.tp_port != other.tp_port: return False
        return True

    def pretty_print(self, q):
        q.text("set_tp_dst {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("tp_port = ");
                q.text("%#x" % self.tp_port)
            q.breakable()
        q.text('}')

action.subtypes[10] = set_tp_dst

class set_tp_src(action):
    type = 9

    def __init__(self, tp_port=None):
        if tp_port != None:
            self.tp_port = tp_port
        else:
            self.tp_port = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!H", self.tp_port))
        packed.append('\x00' * 2)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = set_tp_src()
        _type = reader.read("!H")[0]
        assert(_type == 9)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        obj.tp_port = reader.read("!H")[0]
        reader.skip(2)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.tp_port != other.tp_port: return False
        return True

    def pretty_print(self, q):
        q.text("set_tp_src {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("tp_port = ");
                q.text("%#x" % self.tp_port)
            q.breakable()
        q.text('}')

action.subtypes[9] = set_tp_src

class set_vlan_pcp(action):
    type = 2

    def __init__(self, vlan_pcp=None):
        if vlan_pcp != None:
            self.vlan_pcp = vlan_pcp
        else:
            self.vlan_pcp = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!B", self.vlan_pcp))
        packed.append('\x00' * 3)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = set_vlan_pcp()
        _type = reader.read("!H")[0]
        assert(_type == 2)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        obj.vlan_pcp = reader.read("!B")[0]
        reader.skip(3)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.vlan_pcp != other.vlan_pcp: return False
        return True

    def pretty_print(self, q):
        q.text("set_vlan_pcp {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("vlan_pcp = ");
                q.text("%#x" % self.vlan_pcp)
            q.breakable()
        q.text('}')

action.subtypes[2] = set_vlan_pcp

class set_vlan_vid(action):
    type = 1

    def __init__(self, vlan_vid=None):
        if vlan_vid != None:
            self.vlan_vid = vlan_vid
        else:
            self.vlan_vid = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!H", self.vlan_vid))
        packed.append('\x00' * 2)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = set_vlan_vid()
        _type = reader.read("!H")[0]
        assert(_type == 1)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        obj.vlan_vid = reader.read("!H")[0]
        reader.skip(2)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.vlan_vid != other.vlan_vid: return False
        return True

    def pretty_print(self, q):
        q.text("set_vlan_vid {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("vlan_vid = ");
                q.text("%#x" % self.vlan_vid)
            q.breakable()
        q.text('}')

action.subtypes[1] = set_vlan_vid

class strip_vlan(action):
    type = 3

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append('\x00' * 4)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = strip_vlan()
        _type = reader.read("!H")[0]
        assert(_type == 3)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        reader.skip(4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("strip_vlan {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

action.subtypes[3] = strip_vlan


