from .base import AssetLoaderInterface, AssetLoader, AssetLoaders


manager = AssetLoaders()
manager.register(AssetLoader())
