
from qiskit_metal.qlibrary.terminations.launchpad_wb_coupled import LaunchpadWirebondCoupled

from qiskit_metal.qlibrary.qubits.transmon_pocket import TransmonPocket

from qiskit_metal.qlibrary.tlines.meandered import RouteMeander

from qiskit_metal import designs, MetalGUI

design = designs.DesignPlanar()

gui = MetalGUI(design)



            # WARNING
#options_connection_pads failed to have a value
Q1 = TransmonPocket(
design,
name='Q1',
options={'connection_pads': {'a': {'cpw_extend': '50um',
                           'cpw_gap': 'cpw_gap',
                           'cpw_width': 'cpw_width',
                           'loc_H': -1,
                           'loc_W': 1,
                           'pad_cpw_extent': '25um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15um',
                           'pad_height': '30um',
                           'pad_width': '70um',
                           'pocket_extent': '5um',
                           'pocket_rise': '65um'},
                     'b': {'cpw_extend': '50um',
                           'cpw_gap': 'cpw_gap',
                           'cpw_width': 'cpw_width',
                           'loc_H': -1,
                           'loc_W': -1,
                           'pad_cpw_extent': '25um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15um',
                           'pad_height': '30um',
                           'pad_width': '125um',
                           'pocket_extent': '5um',
                           'pocket_rise': '65um'},
                     'c': {'cpw_extend': '50um',
                           'cpw_gap': 'cpw_gap',
                           'cpw_width': 'cpw_width',
                           'loc_H': 1,
                           'loc_W': -1,
                           'pad_cpw_extent': '25um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15um',
                           'pad_height': '30um',
                           'pad_width': '110um',
                           'pocket_extent': '5um',
                           'pocket_rise': '65um'},
                     'd': {'cpw_extend': '50um',
                           'cpw_gap': 'cpw_gap',
                           'cpw_width': 'cpw_width',
                           'loc_H': 1,
                           'loc_W': 1,
                           'pad_cpw_extent': '25um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15um',
                           'pad_height': '30um',
                           'pad_width': '80um',
                           'pocket_extent': '5um',
                           'pocket_rise': '65um'}},
 'gds_cell_name': 'FakeJunction_01',
 'pos_x': '3000um',
 'pos_y': '0um'}
)





            # WARNING
#options_connection_pads failed to have a value
Q2 = TransmonPocket(
design,
name='Q2',
options={'connection_pads': {'a': {'cpw_extend': '50um',
                           'cpw_gap': 'cpw_gap',
                           'cpw_width': 'cpw_width',
                           'loc_H': -1,
                           'loc_W': 1,
                           'pad_cpw_extent': '25um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15um',
                           'pad_height': '30um',
                           'pad_width': '70um',
                           'pocket_extent': '5um',
                           'pocket_rise': '65um'},
                     'b': {'cpw_extend': '50um',
                           'cpw_gap': 'cpw_gap',
                           'cpw_width': 'cpw_width',
                           'loc_H': -1,
                           'loc_W': -1,
                           'pad_cpw_extent': '25um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15um',
                           'pad_height': '30um',
                           'pad_width': '125um',
                           'pocket_extent': '5um',
                           'pocket_rise': '65um'},
                     'c': {'cpw_extend': '50um',
                           'cpw_gap': 'cpw_gap',
                           'cpw_width': 'cpw_width',
                           'loc_H': 1,
                           'loc_W': -1,
                           'pad_cpw_extent': '25um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15um',
                           'pad_height': '30um',
                           'pad_width': '110um',
                           'pocket_extent': '5um',
                           'pocket_rise': '65um'},
                     'd': {'cpw_extend': '50um',
                           'cpw_gap': 'cpw_gap',
                           'cpw_width': 'cpw_width',
                           'loc_H': 1,
                           'loc_W': 1,
                           'pad_cpw_extent': '25um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15um',
                           'pad_height': '30um',
                           'pad_width': '80um',
                           'pocket_extent': '5um',
                           'pocket_rise': '65um'}},
 'gds_cell_name': 'FakeJunction_01',
 'orientation': '90',
 'pos_x': '1500um',
 'pos_y': '2000um'}
)





            # WARNING
#options_connection_pads failed to have a value
Q3 = TransmonPocket(
design,
name='Q3',
options={'connection_pads': {'a': {'cpw_extend': '50um',
                           'cpw_gap': 'cpw_gap',
                           'cpw_width': 'cpw_width',
                           'loc_H': -1,
                           'loc_W': 1,
                           'pad_cpw_extent': '25um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15um',
                           'pad_height': '30um',
                           'pad_width': '70um',
                           'pocket_extent': '5um',
                           'pocket_rise': '65um'},
                     'b': {'cpw_extend': '50um',
                           'cpw_gap': 'cpw_gap',
                           'cpw_width': 'cpw_width',
                           'loc_H': -1,
                           'loc_W': -1,
                           'pad_cpw_extent': '25um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15um',
                           'pad_height': '30um',
                           'pad_width': '125um',
                           'pocket_extent': '5um',
                           'pocket_rise': '65um'},
                     'c': {'cpw_extend': '50um',
                           'cpw_gap': 'cpw_gap',
                           'cpw_width': 'cpw_width',
                           'loc_H': 1,
                           'loc_W': -1,
                           'pad_cpw_extent': '25um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15um',
                           'pad_height': '30um',
                           'pad_width': '110um',
                           'pocket_extent': '5um',
                           'pocket_rise': '65um'},
                     'd': {'cpw_extend': '50um',
                           'cpw_gap': 'cpw_gap',
                           'cpw_width': 'cpw_width',
                           'loc_H': 1,
                           'loc_W': 1,
                           'pad_cpw_extent': '25um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15um',
                           'pad_height': '30um',
                           'pad_width': '80um',
                           'pocket_extent': '5um',
                           'pocket_rise': '65um'}},
 'gds_cell_name': 'FakeJunction_01',
 'orientation': '90',
 'pos_x': '-1500um',
 'pos_y': '2000um'}
)





            # WARNING
#options_connection_pads failed to have a value
Q4 = TransmonPocket(
design,
name='Q4',
options={'connection_pads': {'a': {'cpw_extend': '50um',
                           'cpw_gap': 'cpw_gap',
                           'cpw_width': 'cpw_width',
                           'loc_H': -1,
                           'loc_W': 1,
                           'pad_cpw_extent': '25um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15um',
                           'pad_height': '30um',
                           'pad_width': '70um',
                           'pocket_extent': '5um',
                           'pocket_rise': '65um'},
                     'b': {'cpw_extend': '50um',
                           'cpw_gap': 'cpw_gap',
                           'cpw_width': 'cpw_width',
                           'loc_H': -1,
                           'loc_W': -1,
                           'pad_cpw_extent': '25um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15um',
                           'pad_height': '30um',
                           'pad_width': '125um',
                           'pocket_extent': '5um',
                           'pocket_rise': '65um'},
                     'c': {'cpw_extend': '50um',
                           'cpw_gap': 'cpw_gap',
                           'cpw_width': 'cpw_width',
                           'loc_H': 1,
                           'loc_W': -1,
                           'pad_cpw_extent': '25um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15um',
                           'pad_height': '30um',
                           'pad_width': '110um',
                           'pocket_extent': '5um',
                           'pocket_rise': '65um'},
                     'd': {'cpw_extend': '50um',
                           'cpw_gap': 'cpw_gap',
                           'cpw_width': 'cpw_width',
                           'loc_H': 1,
                           'loc_W': 1,
                           'pad_cpw_extent': '25um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15um',
                           'pad_height': '30um',
                           'pad_width': '80um',
                           'pocket_extent': '5um',
                           'pocket_rise': '65um'}},
 'gds_cell_name': 'FakeJunction_01',
 'orientation': '180',
 'pos_x': '-3000um',
 'pos_y': '0um'}
)





            # WARNING
#options_connection_pads failed to have a value
Q5 = TransmonPocket(
design,
name='Q5',
options={'connection_pads': {'a': {'cpw_extend': '50um',
                           'cpw_gap': 'cpw_gap',
                           'cpw_width': 'cpw_width',
                           'loc_H': -1,
                           'loc_W': 1,
                           'pad_cpw_extent': '25um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15um',
                           'pad_height': '30um',
                           'pad_width': '70um',
                           'pocket_extent': '5um',
                           'pocket_rise': '65um'},
                     'b': {'cpw_extend': '50um',
                           'cpw_gap': 'cpw_gap',
                           'cpw_width': 'cpw_width',
                           'loc_H': -1,
                           'loc_W': -1,
                           'pad_cpw_extent': '25um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15um',
                           'pad_height': '30um',
                           'pad_width': '125um',
                           'pocket_extent': '5um',
                           'pocket_rise': '65um'},
                     'c': {'cpw_extend': '50um',
                           'cpw_gap': 'cpw_gap',
                           'cpw_width': 'cpw_width',
                           'loc_H': 1,
                           'loc_W': -1,
                           'pad_cpw_extent': '25um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15um',
                           'pad_height': '30um',
                           'pad_width': '110um',
                           'pocket_extent': '5um',
                           'pocket_rise': '65um'},
                     'd': {'cpw_extend': '50um',
                           'cpw_gap': 'cpw_gap',
                           'cpw_width': 'cpw_width',
                           'loc_H': 1,
                           'loc_W': 1,
                           'pad_cpw_extent': '25um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15um',
                           'pad_height': '30um',
                           'pad_width': '80um',
                           'pocket_extent': '5um',
                           'pocket_rise': '65um'}},
 'gds_cell_name': 'FakeJunction_01',
 'orientation': '270',
 'pos_x': '-1500um',
 'pos_y': '-2000um'}
)





            # WARNING
#options_connection_pads failed to have a value
Q6 = TransmonPocket(
design,
name='Q6',
options={'connection_pads': {'a': {'cpw_extend': '50um',
                           'cpw_gap': 'cpw_gap',
                           'cpw_width': 'cpw_width',
                           'loc_H': -1,
                           'loc_W': 1,
                           'pad_cpw_extent': '25um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15um',
                           'pad_height': '30um',
                           'pad_width': '70um',
                           'pocket_extent': '5um',
                           'pocket_rise': '65um'},
                     'b': {'cpw_extend': '50um',
                           'cpw_gap': 'cpw_gap',
                           'cpw_width': 'cpw_width',
                           'loc_H': -1,
                           'loc_W': -1,
                           'pad_cpw_extent': '25um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15um',
                           'pad_height': '30um',
                           'pad_width': '125um',
                           'pocket_extent': '5um',
                           'pocket_rise': '65um'},
                     'c': {'cpw_extend': '50um',
                           'cpw_gap': 'cpw_gap',
                           'cpw_width': 'cpw_width',
                           'loc_H': 1,
                           'loc_W': -1,
                           'pad_cpw_extent': '25um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15um',
                           'pad_height': '30um',
                           'pad_width': '110um',
                           'pocket_extent': '5um',
                           'pocket_rise': '65um'},
                     'd': {'cpw_extend': '50um',
                           'cpw_gap': 'cpw_gap',
                           'cpw_width': 'cpw_width',
                           'loc_H': 1,
                           'loc_W': 1,
                           'pad_cpw_extent': '25um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15um',
                           'pad_height': '30um',
                           'pad_width': '80um',
                           'pocket_extent': '5um',
                           'pocket_rise': '65um'}},
 'gds_cell_name': 'FakeJunction_01',
 'orientation': '270',
 'pos_x': '1500um',
 'pos_y': '-2000um'}
)




cpw1 = RouteMeander(
design,
name='cpw1',
options={'_actual_length': '7.0 mm',
 'fillet': '99.99um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '250um',
          'start_jogged_extension': '',
          'start_straight': '100um'},
 'meander': {'asymmetry': '-237.5um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'Q2',
                            'pin': 'b'},
                'start_pin': {'component': 'Q1',
                              'pin': 'c'}},
 'total_length': '7000um',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




cpw2 = RouteMeander(
design,
name='cpw2',
options={'_actual_length': '7.000000000000001 '
                   'mm',
 'fillet': '99.99um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '250um',
          'start_jogged_extension': '',
          'start_straight': '100um'},
 'meander': {'asymmetry': '+237.5um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'Q2',
                            'pin': 'c'},
                'start_pin': {'component': 'Q3',
                              'pin': 'b'}},
 'total_length': '7000um',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




cpw3 = RouteMeander(
design,
name='cpw3',
options={'_actual_length': '7.0 mm',
 'fillet': '99.99um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '250um',
          'start_jogged_extension': '',
          'start_straight': '100um'},
 'meander': {'asymmetry': '-337.5um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'Q3',
                            'pin': 'c'},
                'start_pin': {'component': 'Q4',
                              'pin': 'b'}},
 'total_length': '7000um',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




cpw4 = RouteMeander(
design,
name='cpw4',
options={'_actual_length': '7.0 mm',
 'fillet': '99.99um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '250um',
          'start_jogged_extension': '',
          'start_straight': '100um'},
 'meander': {'asymmetry': '+337.5um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'Q5',
                            'pin': 'b'},
                'start_pin': {'component': 'Q4',
                              'pin': 'c'}},
 'total_length': '7000um',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




cpw5 = RouteMeander(
design,
name='cpw5',
options={'_actual_length': '7.000000000000003 '
                   'mm',
 'fillet': '99.99um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '250um',
          'start_jogged_extension': '',
          'start_straight': '100um'},
 'meander': {'asymmetry': '-320.0um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'Q6',
                            'pin': 'b'},
                'start_pin': {'component': 'Q5',
                              'pin': 'c'}},
 'total_length': '7000um',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




cpw6 = RouteMeander(
design,
name='cpw6',
options={'_actual_length': '7.000000000000001 '
                   'mm',
 'fillet': '99.99um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '250um',
          'start_jogged_extension': '',
          'start_straight': '100um'},
 'meander': {'asymmetry': '+320.0um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'Q6',
                            'pin': 'c'},
                'start_pin': {'component': 'Q1',
                              'pin': 'b'}},
 'total_length': '7000um',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




ol1 = RouteMeander(
design,
name='ol1',
options={'_actual_length': '8.6 mm',
 'fillet': '99.99um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '0um',
          'start_jogged_extension': '',
          'start_straight': '430um'},
 'meander': {'asymmetry': '+150um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'P1_Q',
                            'pin': 'tie'},
                'start_pin': {'component': 'Q1',
                              'pin': 'a'}},
 'total_length': '8.6 mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




ol3 = RouteMeander(
design,
name='ol3',
options={'_actual_length': '8.600000000000001 '
                   'mm',
 'fillet': '99.99um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '0um',
          'start_jogged_extension': '',
          'start_straight': '430um'},
 'meander': {'asymmetry': '+150um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'P3_Q',
                            'pin': 'tie'},
                'start_pin': {'component': 'Q3',
                              'pin': 'a'}},
 'total_length': '8.6 mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




ol2 = RouteMeander(
design,
name='ol2',
options={'_actual_length': '8.600000000000001 '
                   'mm',
 'fillet': '99.99um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '0um',
          'start_jogged_extension': '',
          'start_straight': '535um'},
 'meander': {'asymmetry': '+200um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'P2_Q',
                            'pin': 'tie'},
                'start_pin': {'component': 'Q2',
                              'pin': 'a'}},
 'total_length': '8.6 mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




ol4 = RouteMeander(
design,
name='ol4',
options={'_actual_length': '8.600000000000001 '
                   'mm',
 'fillet': '99.99um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '0um',
          'start_jogged_extension': '',
          'start_straight': '535um'},
 'meander': {'asymmetry': '+200um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'P4_Q',
                            'pin': 'tie'},
                'start_pin': {'component': 'Q4',
                              'pin': 'a'}},
 'total_length': '8.6 mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




ol5 = RouteMeander(
design,
name='ol5',
options={'_actual_length': '8.599999999999998 '
                   'mm',
 'fillet': '99.99um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '0um',
          'start_jogged_extension': '',
          'start_straight': '640um'},
 'meander': {'asymmetry': '+250um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'P5_Q',
                            'pin': 'tie'},
                'start_pin': {'component': 'Q5',
                              'pin': 'a'}},
 'total_length': '8.6 mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




ol6 = RouteMeander(
design,
name='ol6',
options={'_actual_length': '8.6 mm',
 'fillet': '99.99um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '0um',
          'start_jogged_extension': '',
          'start_straight': '640um'},
 'meander': {'asymmetry': '+250um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'P6_Q',
                            'pin': 'tie'},
                'start_pin': {'component': 'Q6',
                              'pin': 'a'}},
 'total_length': '8.6 mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




P1_Q = LaunchpadWirebondCoupled(
design,
name='P1_Q',
options={'lead_length': '30um',
 'orientation': '180',
 'pos_x': '5000um',
 'pos_y': '0um'},

component_template=None,
)




P2_Q = LaunchpadWirebondCoupled(
design,
name='P2_Q',
options={'lead_length': '30um',
 'orientation': '270',
 'pos_x': '1500um',
 'pos_y': '4000um'},

component_template=None,
)




P3_Q = LaunchpadWirebondCoupled(
design,
name='P3_Q',
options={'lead_length': '30um',
 'orientation': '270',
 'pos_x': '-1500um',
 'pos_y': '4000um'},

component_template=None,
)




P4_Q = LaunchpadWirebondCoupled(
design,
name='P4_Q',
options={'lead_length': '30um',
 'orientation': '0',
 'pos_x': '-5000um',
 'pos_y': '0um'},

component_template=None,
)




P5_Q = LaunchpadWirebondCoupled(
design,
name='P5_Q',
options={'lead_length': '30um',
 'orientation': '90',
 'pos_x': '-1500um',
 'pos_y': '-4000um'},

component_template=None,
)




P6_Q = LaunchpadWirebondCoupled(
design,
name='P6_Q',
options={'lead_length': '30um',
 'orientation': '90',
 'pos_x': '1500um',
 'pos_y': '-4000um'},

component_template=None,
)



gui.rebuild()
gui.autoscale()
        