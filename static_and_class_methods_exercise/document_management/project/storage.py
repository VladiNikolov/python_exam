from project.category import Category
from project.document import Document
from project.topic import Topic


# class Storage:
#
#     def __init__(self):
#         self.categories = []
#         self.topics = []
#         self.documents = []
#
#     def add_category(self, category: Category):
#         storage_category = self.__find_category_by_id(category.id)
#
#         if storage_category is None:
#             self.categories.append(category)
#
#     def add_topic(self, topic: Topic):
#         storage_topic = self.__find_topic_by_id(topic.id)
#
#         if storage_topic is None:
#             self.topics.append(topic)
#
#     def add_document(self, document: Document):
#         storage_document = self.__find_document_by_id(document.id)
#
#         if storage_document is None:
#             self.documents.append(document)
#
#     def edit_category(self, category_id: int, new_name:str):
#         category = self.__find_category_by_id(category_id)
#         category.edit(new_name)
#
#     def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
#         topic = self.__find_topic_by_id(topic_id)
#         topic.edit(new_topic, new_storage_folder)
#
#     def edit_document(self, document_id: int, new_file_name: str):
#         document = self.__find_document_by_id(document_id)
#         document.edit(new_file_name)
#
#     def delete_category(self, category_id):
#         del_category = self.__find_category_by_id(category_id)
#         self.categories.remove(del_category)
#
#     def delete_topic(self, topic_id):
#         del_topic = self.__find_topic_by_id(topic_id)
#         self.topics.remove(del_topic)
#
#     def delete_document(self, document_id):
#         del_document = self.__find_document_by_id(document_id)
#         self.documents.remove(del_document)
#
#     def get_document(self, document_id):
#         get_doc = self.__find_document_by_id(document_id)
#         return get_doc
#
#     def __repr__(self):
#         return '\n'.join([str(x) for x in self.documents])
#
#     def __find_category_by_id(self, category_id):
#         for category in self.categories:
#             if category.id == category_id:
#                 return category
#
#     def __find_topic_by_id(self, topic_id):
#         for topic in self.topics:
#             if topic.id == topic_id:
#                 return topic
#
#     def __find_document_by_id(self, document_id):
#         for document in self.documents:
#             if document.id == document_id:
#                 return document
class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name:str):
        for category in self.categories:
            if category.id == category_id:
                category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for topic in self.topics:
            if topic.id == topic_id:
                topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        for document in self.documents:
            if document.id == document_id:
                document.edit(new_file_name)

    def delete_category(self, category_id):
        for category in self.categories:
            if category.id == category_id:
                self.categories.remove(category)

    def delete_topic(self, topic_id):
        for topic in self.topics:
            if topic.id == topic_id:
                self.topics.remove(topic)

    def delete_document(self, document_id):
        for document in self.documents:
            if document.id == document_id:
                self.documents.remove(document)

    def get_document(self, document_id):
        for document in self.documents:
            if document.id == document_id:
                return document

    def __repr__(self):
        return '\n'.join([str(x) for x in self.documents])
