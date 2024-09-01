import base64
import hashlib
from refactor.design import Object
from refactor.utils.assets.loaders import AssetLoaders


class Asset(Object):
  """
  Load asset as raw.

  :authors: Hieu Pham.
  :created: 22:42 Sun 1 Sep 2024.
  :updated: 22:42 Sun 1 Sep 2024.
  """

  @property
  def src(self) -> any:
    return self._src
  
  @property
  def data(self) -> bytes:
    return self._data
  
  @property
  def hash(self) -> str:
    return hashlib.md5(self.data).hexdigest()
  
  @property
  def base64(self) -> str:
    return str(base64.b64encode(self.data))

  def __init__(self, src: any, *args, **kwargs) -> None:
    self._src = src
    self._data = AssetLoaders().load(src, *args, **kwargs)
