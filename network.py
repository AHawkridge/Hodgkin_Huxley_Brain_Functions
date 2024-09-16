"""
Filename: network.py    
Description: Models the action potential travelling
through n neurons in series
"""
import matplotlib.pyplot as plt
from neuron import h
from neuron.units import ms, mV ,µm
h.load_file('stdrun.hoc')

class Cell:
    def __init__(self, gid):
        self._gid = gid
        self._setup_morphology()
        self.all = self.soma.wholetree()
        self._setup_biophysics()

    def __repr__(self):
        return "{}[{}]".format(self.name, self._gid)

    
class Neuron(Cell):
    name = "Neuron"

    def _setup_morphology(self):
        self.soma = h.Section(name="soma", cell=self)
        self.dend = h.Section(name="dend", cell=self)
        self.dend.connect(self.soma)
        self.soma.L = self.soma.diam = 10
        self.dend.L = 200
        self.dend.diam = 1

    def _setup_biophysics(self):
        for sec in self.all:
            sec.Ra = 100   
            sec.cm = 1  
        self.soma.insert("hh") # Hodgkin Huxley model of neuron
        #soma and axon parameters.
        for seg in self.soma:
            seg.hh.gnabar = 0.24   
            seg.hh.gkbar = 0.036   
            seg.hh.gl = 0.0003  
            seg.hh.el = -54.3  
        # Insert passive current in the dendrite
        self.dend.insert("pas")
        # dendrite paramaters 
        for seg in self.dend:
            seg.pas.g = 0.001   
            seg.pas.e = -65   

def create_n_Neuron(n):
    #where n is the number of cells 
    cells = []
    for i in range(n):
        cells.append(Neuron(i))
    return cells
#creates 10 idententical cells.
my_cells = create_n_Neuron(10)  

stim = h.NetStim() 
syn_ = h.ExpSyn(my_cells[0].dend(0.5))

stim.number = 1
stim.start = 0
ncstim = h.NetCon(stim, syn_)
ncstim.delay = 1 * ms
ncstim.weight[0] = 0.04 
syn_.tau = 2 * ms

syns = []
netcons = []

for source, target in zip(my_cells, my_cells[1:]):
    syn = h.ExpSyn(target.dend(0.5))
    nc = h.NetCon(source.soma(0.5)._ref_v, syn, sec=source.soma)
    nc.weight[0] = 1
    nc.delay = 10
    netcons.append(nc)
    syns.append(syn)

lstcell = []
for i in range(len(my_cells)):
    recording_cell = my_cells[i]
    soma_v = h.Vector().record(recording_cell.soma(0.5)._ref_v)
    t = h.Vector().record(h._ref_t)
    lstcell.append(soma_v)

h.topology()
h.finitialize(-65 * mV)
h.continuerun(100 * ms)

for i in range(len(lstcell)):
    lbl = "AP " + str([i])
    plt.plot(t, lstcell[i], label=lbl)


plt.legend()
plt.savefig('Images/network.png', dpi = 300)

plt.show()