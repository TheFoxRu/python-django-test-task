from abc import ABC, abstractmethod

from django.db.models import QuerySet

from ..models import Shop
from ..types import URL


class IShopRepository(ABC):

    @abstractmethod
    def get_all(self) -> QuerySet[Shop | None]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Shop | None:
        pass

    @abstractmethod
    def search_by_title(self, title: str) -> QuerySet[Shop | None]:
        pass

    @abstractmethod
    def create_shop(self, title: str, description: str, image_url: URL) -> Shop:
        pass

    @abstractmethod
    def update_shop(self, id: int, data: dict) -> None:
        pass

    @abstractmethod
    def delete_shop(self, id: int) -> None:
        pass
