from Blocks import *

class ReadBlockSim():
    def __init__(self, file):
        self.file = file
        self.nets = []
        self.blocks = []
        self.scopes = []


    def read(self):
        self.read_file = open(self.file, 'r')
        self.file_change = self.change_file2list()
        nets, blocks, scopes = self.get_net_blocks_scopes()
        self.nets = self.check_components(nets, nets=1)
        self.blocks = self.check_components(blocks, blocks=1)
        duration, Ts = self.get_times()
        return self.nets, self.blocks, scopes, duration, Ts


    def get_times(self):
        for line in self.file_change:
            if line.find("Duration = ") != -1:
                duration = float(line[10:].replace(";", "").strip())
            if line.find("Ts = ") != -1:
                Ts = float(line[4:].replace(";", "").strip())
        return duration, Ts


    def list_func(self, line):
        payload = line.replace(" ", "")
        payload = payload.split("{")[1]
        payload = payload.split("}")[0]
        list = payload.split(",")
        return list


    def get_net_blocks_scopes(self):
        for i in self.file_change:
            if i.find("nets = ") != -1:
                nets = self.list_func(i)
            # get blocks
            if i.find("blocks = ") != -1:
                blocks = self.list_func(i)
            if i.find("scopes = ") != -1:
                scopes = self.list_func(i)
        return nets, blocks, scopes


    def check_components(self, list_components, nets=0, blocks=0):
        list_output = []
        for component in list_components:
            flag = 0
            list = [component]
            for i in self.file_change:
                i = i.replace(" ", "")
                i = i.replace(";", "")
                if component == i[:len(component)]:
                    flag = 1
                    i = i[len(component)+2:]
                if flag == 1:
                    if i[0] == "}":
                        flag = 0
                        list_output.append(list)
                    else:
                        list.append(i)
        
        if nets == 1:
            list_output = self.generate_netlist(list_output)
        elif blocks == 1:
            list_output = self.generate_blocklist(list_output)
        return list_output


    def generate_netlist(self, net_list):
        net_output = []
        for net in net_list:
            if net[1].find("Input:") != -1:
                net[1] = net[1][len("Input:"):]
                if net[1].find(",") != -1:
                    net[1] = net[1].split(",")
            
            if net[2].find("Output:") != -1:
                net[2] = net[2][len("Output:"):]
                if net[2].find(",") != -1:
                    net[2] = net[2].split(",")

            if net[3].find("name:") != -1:
                net[3] = net[3][len("name:\""):-1]
            
            net_output.append(net)
        return net_output


    def generate_blocklist(self, block_list):
        lista = []
        for block in block_list:
            lista.append(self.search_type(block)[0])
        return lista


    def change_file2list(self):
        lines = self.read_file.readlines()
        lines_out = []
        for r in lines:
            lines_out.append(r.replace("\n", ""))
        return lines_out
    

    def search_type(self, block):
        output = []
        block_type = block[1][5:]
        id = block[0]
        num = []
        den = []
        values = []
        if block_type == "tfs":
            num.append(self.split_values(block[2][4:], floating=1))
            if len(num)==1:
                if type(num[0]) is list:
                    num = num[0]
            den.append(self.split_values(block[3][4:], floating=1))
            if len(den)==1:
                if type(den[0]) is list:
                    den = den[0]
            output.append([id, block_type, num, den])
        elif block_type == "step":
            value = float(block[2][6:])
            time = float(block[3][5:])
            output.append([id, block_type, value, time])
        elif block_type == "add":
            inputs = int(block[2][7:])
            values.append(self.split_values(block[3][6:]))
            output.append([id, block_type, inputs, values[0]])
            
        return output
    
    def split_values(self, value, floating=0):
        value_list = []
        if value.find(",") != -1:
            val_pre = value.split(",")
            for n in val_pre:
                if floating == 1:
                    value_list.append(float(n))
                else:
                    value_list.append(n)
            return value_list
        else:
            if floating == 1:
                value_list.append(float(value))
            else:
                value_list.append(value)
            return value_list[0]