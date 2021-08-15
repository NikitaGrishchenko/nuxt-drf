
from .common import *
from .environment import *

DEBUG = env('DEBUG', default=True)

if DEBUG:
    from .local import *
else:
    from .production import *
