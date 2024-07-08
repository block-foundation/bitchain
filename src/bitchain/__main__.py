#!/usr/bin/env python


# =============================================================================
# Docstring
# =============================================================================

"""
Provides a Bitchain entry point.
"""


# =============================================================================
# Import
# =============================================================================

# Import | Futures
from __future__ import print_function

# Import | Standard Library
import platform
try:
    import pkg_resources
except ImportError:
    pkg_resources = None

# Import | Libraries
import bitchain

# Import | Local Modules


# =============================================================================
# Main
# =============================================================================

def main() -> None:
    """
    Main function to.
    """
    print()
    print("bitchain is set!")
    print()
    print("bitchain: {}".format(bitchain.__version__))
    print(
        "Python: {} ({})".format(platform.python_version(),
        platform.python_implementation())
    )

    if pkg_resources:
        working_set = pkg_resources.working_set
        packages = set(
            [p.project_name for p in working_set]) - set(["bitchain"]
        )
        bitchain_pkgs = [
            p for p in packages if p.lower().startswith("bitchain")
        ]

        if bitchain_pkgs:
            print("Extensions: {}".format([p for p in bitchain_pkgs]))


if __name__ == "__main__":
    main()
