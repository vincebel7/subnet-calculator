class IpconfigObject: 
    def __init__(self, CIDR):
        self.CIDR = CIDR
        self.binaddr = ""
        self.binmask = ""
        self.binnetworkaddr = ""
        self.binbroadcast = ""
        self.num_hosts = ""

    def get_CIDR(self):
        return self.CIDR


    def set_binaddr(self, binaddr):
        self.binaddr = binaddr

    def get_binaddr(self):
        return self.binaddr


    def set_binmask(self, binmask):
        self.binmask = binmask

    def get_binmask(self):
        return self.binmask


    def set_binnetworkaddr(self, binnetworkaddr):
        self.binnetworkaddr = binnetworkaddr

    def get_binnetworkaddr(self):
        return self.binnetworkaddr


    def set_binbroadcast(self, binbroadcast):
        self.binbroadcast = binbroadcast

    def get_binbroadcast(self):
        return self.binbroadcast


    def set_num_hosts(self, num_hosts):
        self.num_hosts = num_hosts

    def get_num_hosts(self):
        return self.num_hosts

