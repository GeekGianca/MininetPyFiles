from mininet.topo import Topo


class MyTopo(Topo):
    "Simple topology example."

    def __init__(self):
        "Create custom topo."

        # Initialize topology
        Topo.__init__(self)
        # Add Host and Switches
        Host0 = self.addHost('h0')
        Host1 = self.addHost('h1')
        Host2 = self.addHost('h2')
        Host3 = self.addHost('h3')
        Host4 = self.addHost('h4')
        Host5 = self.addHost('h5')
        Switch0 = self.addSwitch('s0')
        Switch1 = self.addSwitch('s1')
        Switch2 = self.addSwitch('s2')
        # Add Links
        self.addLink(Host0, Switch0)
        self.addLink(Host1, Switch0)
        self.addLink(Host2, Switch0)
        self.addLink(Host3, Switch1)
        self.addLink(Host4, Switch1)
        self.addLink(Host5, Switch1)
        self.addLink(Switch0, Switch2)
        self.addLink(Switch2, Switch1)

topos = {'mytopo': (lambda: MyTopo())}