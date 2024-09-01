import urllib
import base64
from typing import Any
from pathlib import Path
from refactor.design import Object
from abc import ABC, abstractmethod
from refactor.design.creational import Singleton


class AssetLoaderInterface(ABC, Object, metaclass=Singleton):
  """
  Base interface for all inherited asset loaders.

  :authors: Hieu Pham.
  :created: 22:00 Sun 1 Sep 2024.
  :updated: 22:32 Sun 1 Sep 2024.
  """

  @abstractmethod
  def load(self, src: Any, *args: Any, **kwds: Any) -> bytes:
    raise NotImplemented()
  


class AssetLoader(AssetLoaderInterface):
  """
  Basic asset loader which can load asset from file, url, base64 string and bytes.

  :authors: Hieu Pham.
  :created: 22:00 Sun 1 Sep 2024.
  :updated: 22:32 Sun 1 Sep 2024.
  """

  def load(self, src: Any, *args: Any, **kwds: Any) -> bytes:
    try:
      return Path(src).expanduser().resolve().read_bytes()
    except:
      self.logger.debug(f'cannot load asset {str(src)} as file.')
    try:
      return urllib.request.urlopen(src).read()
    except:
      self.logger.debug(f'cannot load asset {str(src)} as http.')
    try:
      return base64.b64decode(src, validate=True)
    except:
      self.logger.debug(f'cannot load asset {str(src)} as base64.')
    try:
      return bytes(src)
    except:
      self.logger.debug(f'cannot load asset {str(src)} as bytes.')
    raise TypeError(f'cannot load asset {str(src)}.')


class AssetLoaders(AssetLoaderInterface, Object, metaclass=Singleton):
  """
  Manage all asset loaders.

  :authors: Hieu Pham.
  :created: 22:00 Sun 1 Sep 2024.
  :updated: 22:32 Sun 1 Sep 2024.
  """

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)
    self._loaders = list()

  def register(self, loader: AssetLoaderInterface):
    if loader not in self._loaders:
      self._loaders.append(loader)
    return self
  
  def unregister(self, loader: AssetLoaderInterface):
    if loader in self._loaders:
      self._loaders.remove(loader)
    return self
  
  def load(self, src: Any, *args: Any, **kwds: Any) -> bytes:
    for loader in self._loaders:
      try:
        return loader.load(src, *args, **kwds)
      except:
        continue
    raise AssertionError(f'Cannot load asset {str(src):20s}.')
