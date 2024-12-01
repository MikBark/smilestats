import networkx as nx

from molstats.helper import add_aromatic_atoms

# Aromating ring must contain 6 "C" elements
AROMATIC_RING_MOL_COUNT = 6


def aromatic_ring_count(molecule: nx.Graph, safety: bool = True) -> int:
    """
    Parameters
    ----------
    molecule : networkx.Graph
        The networkx.Graph created using pysmiles from a molecule containing (or
        not containing) an aromatic ring.
    safety : bool (default=True)
        If the checkbox is set to True, the calculations do not affect the transferred
        object - molecule. If the check box is set to False, it is assumed that the
        transmitted graph contains marked aromatic atoms supported by pysmiles. Disabling
        safety mode can increase the speed of operation, but lead to errors if the data
        is not properly prepared.

    Returns
    -------
    aromatic_ring_count : int
        The number of aromatic rings in the molecule.
    """
    if safety:
        molecule = add_aromatic_atoms(molecule)

    aromatic_atom_count = sum(
        dict(molecule.nodes(data='aromatic')).values(),
    )
    if aromatic_atom_count % AROMATIC_RING_MOL_COUNT != 0:
        raise ValueError(
            f'The number of aromatic atoms is not a multiple of {AROMATIC_RING_MOL_COUNT}',
        )
    return aromatic_atom_count // AROMATIC_RING_MOL_COUNT
