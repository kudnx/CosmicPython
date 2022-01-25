import abc
from domain import model


class AbstractRepository(abc.ABC):
    def __init__(self):
        self.seen = set()

    def add(self, product: model.Product):
        self._add(product)
        self.seen.add(product)

    def get(self, sku) -> model.Product:
        product = self._get(sku)
        if product:
            self.seen.add(product)
        return product

    @abc.abstractmethod
    def _add(self, product: model.Product):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, sku) -> model.Product:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def _add(self, product):
        self.session.add(product)

    def _get(self, sku):
        return self.session.query(model.Product).filter_by(sku=sku).first()

    # def add(self, batch):
    #     self.session.add(batch)
    #
    # def get(self, reference):
    #     return self.session.query(model.Batch).filter_by(reference=reference).one()
    #
    # def list(self):
    #     return self.session.query(model.Batch).all()


# class AbstractProductRepository(abc.ABC):
#
#     def __init__(self):
#         self.seen = set()
#
#     def add(self, product: model.Product):
#         self.__add__(product)
#         self.seen.add(product)
#
#     def get(self, sku) -> model.Product:
#         product = self._get(sku)
#         if product:
#             self.seen.add(product)
#         return product
#
#     @abc.abstractmethod
#     def __add__(self, product: model.Product):
#         raise NotImplementedError
#
#     @abc.abstractmethod
#     def _get(self, sku) -> model.Product:
#         raise NotImplementedError
#
#     @abc.abstractmethod
#     def get(self, sku) -> model.Product:
#         return (
#             self.session.query(model.Product)
#                 .filter_by(sku=sku)
#                 .with_for_update()
#                 .first()
#         )

# class TrackingRepository:
#     seen: Set[model.Product]
#
#     def __init__(self, repo: AbstractRepository):
#         self.seen = set()
#         self._repo = repo
#
#     def add(self, product: model.Product):
#         self._repo.add(product)
#         self.seen.add(product)
#
#     def get(self, sku) -> model.Product:
#         product = self._repo.get(sku)
#         if product:
#             self.seen.add(product)
#         return product
