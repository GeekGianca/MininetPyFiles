from mininet.topo import Topo


class MyTopo(Topo):
    "Creating user input topology example."

    def __init__(self):
        "Create custom topo."
        # Initialize topology
        Topo.__init__(self)
        # user input
        input_num = input("Enter your number hosts: ")
        conv_toint = int(input_num)
        "The number hosts is:" + str(conv_toint)
        hosts = []
        switches = []
        for i in range(conv_toint):
            hosts.append(self.addHost('h' + `i`))
            print "Hosts added " + hosts[i]

        input_swts = input("Enter number of Switches: ")
        swt_toint = int(input_swts)
        print "Switch added "+str(swt_toint)

        for j in range(swt_toint):
            switches.append(self.addSwitch('s' + `j`))
            print "Switch added" + switches[j]

        "Creating links by user"

        for k in range(swt_toint):
            print "Add the links to each switch."
            print "Example: 'h1 -> s1'"


topos = {'mytopo': (lambda: MyTopo())}
