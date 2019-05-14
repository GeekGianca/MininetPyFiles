from mininet.topo import Topo
import array

class MyTopo( Topo ):
	"Creating user input topology example."
	def __init__( self ):
		"Create custom topo."
		#Initialize topology
		Topo.__init__( self )
		#user input
		input_num = input("Enter your number hosts.")
		conv_toint = int(input_num)
		"The number hosts is:"+conv_toint
		hosts = []
                switches = []
		for i in range(0, conv_toint):
			hosts.append(self.addHost( 'h'+`i` ))
			"Hosts added "+hosts[i]
                input_swts = input("Enter number of Switches")
                swt_toint = int(input_swts)
                for j in range(1, swt_toint):
                        switches.append(self.addSwitch('s'+`j`))
                        "Switch added"+switches[j]

                "Creating links by user"
topos = { 'mytopo': (lambda: MyTopo() ) }
