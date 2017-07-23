from StructuralEngineering.FEM.system import SystemElements

"""
Test the primary force vector when applying a q_load at a hinged element.
"""

ss = SystemElements()
ss.add_element([[0, 0], [7, 0]], hinge=2)
ss.add_element([7.1, 0])
ss.add_support_fixed([1, 3])
ss.q_load(10, 1)
ss.solve()
ss.show_bending_moment()

