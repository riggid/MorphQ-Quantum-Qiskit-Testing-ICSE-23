from importlib import import_module

from .base import MetamorphicTransformation

_CLASS_MODULES = {
    "ChangeQubitOrder": ".change_qubit_order",
    "ChangeOptLevel": ".change_opt_level",
    "ChangeCouplingMap": ".change_coupling_map",
    "RunIndependentPartitions": ".run_independent_partitions",
    "ChangeBackend": ".change_backend",
    "ChangeTargetBasis": ".change_target_basis",
    "InjectNullEffect": ".inject_null_effect",
    "AddUnusedRegister": ".add_unused_register",
    "InjectParameters": ".inject_parameters",
    "ToQasmAndBack": ".to_qasm_and_back",
    "QdiffG1SwapToCnot": ".qdiff_g1_swap_to_cnot",
    "QdiffG2TwoHToId": ".qdiff_g2_two_h_to_id",
    "QdiffG3XToHSSH": ".qdiff_g3_x_to_hssh",
    "QdiffG4ZtoSS": ".qdiff_g4_z_to_ss",
    "QdiffG6TwoCzToId": ".qdiff_g6_two_cz_to_id",
    "QdiffG7CCNOTDecomposition": ".qdiff_g7_ccnot_decomposition",
    "QdiffG5CZtoHCnotH": ".qdiff_g5_cz_to_h_cnot_h",
}

__all__ = ["MetamorphicTransformation", *_CLASS_MODULES]


def __getattr__(name):
    module_name = _CLASS_MODULES.get(name)
    if module_name is None:
        raise AttributeError(name)
    value = getattr(import_module(module_name, __name__), name)
    globals()[name] = value
    return value
