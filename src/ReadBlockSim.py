

class ReadBlockSim():
    def __init__(self, file):
        self.file = file
        self.nets = []
        self.blocks = []
        self.scopes = []


    def read(self):
        read_file = open(self.file, 'r')
        file_change = self.change_file2list()
        self.nets, self.blocks, self.scopes = self.get_net_blocks_scopes()
        




    def list_func(self, line):
        payload = line.replace(" ", "")
        payload = payload.split("{")[1]
        payload = payload.split("}")[0]
        list = payload.split(",")
        return list


    def get_net_blocks_scopes(self, file):
        for i in file:
            if i.find("nets = ") != -1:
                nets = list_func(i)
            # get blocks
            if i.find("blocks = ") != -1:
                blocks = list_func(i)
            if i.find("scopes = ") != -1:
                scopes = list_func(i)
        return nets, blocks, scopes


    def check_components(self, file, list_components, nets=0, blocks=0):
        list_output = []
        for component in list_components:
            flag = 0
            list = [component]
            for i in file:
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
            list_output = generate_netlist(list_output)
        elif blocks == 1:
            list_output = generate_blocklist(list_output)
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
        
        return


    def change_file2list(self):
        lines = self.file.readlines()
        lines_out = []
        for r in lines:
            lines_out.append(r.replace("\n", ""))
        return lines_out