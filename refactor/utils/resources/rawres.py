import base64
import hashlib
from typing import Any
from refactor.objects import Object
from refactor.utils.resources import ResourceLoaders



class Resource(Object):
  """
  Raw bytes resource.
  """
  @property
  def data(self) -> bytes:
    return self._data
  
  @property
  def hash(self) -> str:
    return hashlib.md5(self.data).hexdigest()
  
  @property
  def base64(self) -> str:
    return str(base64.b64encode(self.data))
  
  @property
  def size(self) -> int:
    return len(self.data)

  def __init__(self, source: Any, *args, **kwds) -> None:
    super().__init__(*args, **kwds)
    self._data = ResourceLoaders().load(source, *args, **kwds)
