from typing import List

from document_management.category import Category
from document_management.document import Document
from document_management.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = next(filter(lambda c: c.id == category_id, self.categories))
        category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = next(filter(lambda t: t.id == topic_id, self.topics))
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, file_name):
        document = next(filter(lambda d: d.id == document_id, self.documents))
        document.edit(file_name)

    def delete_category(self, category_id):
        self.categories.remove(next(filter(lambda c: c.id == category_id, self.categories)))

    def delete_topic(self, topic_id):
        self.topics.remove(next(filter(lambda t: t.id == topic_id, self.topics)))

    def delete_document(self, document_id):
        self.documents.remove(next(filter(lambda d: d.id == document_id, self.documents)))

    def get_document(self, document_id):
        return next(filter(lambda d: d.id == document_id, self.documents))

    def __repr__(self):
        return  "\n".join(str(d) for d in self.documents)