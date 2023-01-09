from google.cloud import firestore
from google.api_core.exceptions import (
    FailedPrecondition,
    PermissionDenied,
    ServiceUnavailable
)
from google.oauth2 import service_account


class FireStore:

    def __init__(self, collection_name=None,
                 project=None,
                 data_record=None,
                 service_account_json=None):
        if type(self).__name__ == 'FireStore':
            self.connect(collection_name=collection_name,
                         project=project,
                         service_account_json=service_account_json)
        self.key = None
        self.items = {}
        self.update_stack = {}
        self.model_object = None
        self.new_items = []

    def connect(self, collection_name,
                project=None,
                service_account_json=None):
        self.project = project
        self.collection_name = collection_name
        self.service_account_json = service_account_json
        self.client = None
        if self.service_account_json is not None:
            credentials = \
                service_account.Credentials.from_service_account_file(
                    self.service_account_json,
                    scopes=(
                        "https://www.googleapis.com/auth/cloud-platform",
                        "https://www.googleapis.com/auth/datastore",
                    ),
                )

            self.client = firestore.Client(project=project,
                                           credentials=credentials)
        else:
            self.client = firestore.Client(project=project)

        self.collection = self.client.collection(collection_name)

    @property
    def kind(self):
        return self.collection_name

    def read(self, key, model=None):
        self.key = key
        try:
            doc_ref = self.collection.document(key)
            doc = doc_ref.get()
        except (FailedPrecondition, PermissionDenied):
            # TODO - handle exeception
            raise
        except Exception:
            raise
        if type(self).__name__ == 'FireStore':
            if model:
                self.model_object = model.from_dict(doc.to_dict())
                self.model_object.route_paths()
                return self.model_object
            return doc.to_dict()
        else:
            # TODO - convert doc to type lazy loading
            self.from_dict(doc.to_dict())
            self.key = doc.id

    def get_docs(self):
        return [d.to_dict() for d in self.collection.stream()]

    def set(self, key, data=None):
        if not key:
            key = self.key
        if type(self).__name__ != 'FireStore' and not data:
            data = self.to_json()
        try:
            doc_ref = self.collection.document(self.key)
            doc_ref.set(data, merge=False)
        except (FailedPrecondition, PermissionDenied):
            # TODO - handle exeception
            raise
        except ServiceUnavailable:
            # TODO - handle exeception
            raise

    def __setitem__(self, key, model):
        self.new_items.append(key)
        self.items[key] = model

    # TODO - Rename to commit
    def update(self):
        if self.items:
            for key in self.items:
                # logger.info(('update', key, self.items[key].update_stack))
                if self.items[key].update_stack:
                    db = self.collection.document(key)
                    db.update(self.items[key].update_stack)
                    self.items[key].update_stack = {}
                elif key in self.new_items:
                    db = self.collection.document(key)
                    db.set(self.items[key].to_dict())
                    self.new_items.remove(key)
        else:
            if self.model_object and self.model_object.update_stack:
                db = self.collection.document(self.key)
                db.update(self.model_object.update_stack)
                self.model_object.update_stack = {}

    def query(self, *filters):
        query = self.collection
        for filter_ in filters:
            query = query.where(*filter_)
        return map(lambda x: (x.id, x.to_dict()), query.stream())

    def read_all(self, model):
        """
        Get all models from firestore
        """
        self.items = {}
        for item in self.collection.stream():
            self.items[item.id] = model.from_dict(item.to_dict())
            self.items[item.id].key = item.id
            self.items[item.id].route_paths()
        return self.items

    def delete(self, key):
        doc_ref = self.collection.document(key)
        doc_ref.delete()
