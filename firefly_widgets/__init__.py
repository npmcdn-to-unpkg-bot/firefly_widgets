from ._version import version_info, __version__

from .image import *
from .table import *

def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'jupyter-firefly',
        'require': 'jupyter-firefly/extension'
    }]
