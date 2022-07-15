from project.category import Category
from project.topic import Topic


class Document:
    def __init__(self, id, category_id, topic_id, file_name):
        self.id = id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = []

    @classmethod
    def from_instances(cls, id, category: Category, topic: Topic, file_name):
        return cls(id, category.id, topic.id, file_name)

    def add_tag(self, tag_content):
        for tag in self.tags:
            if tag == tag_content:
                return
        self.tags.append(tag_content)

    def remove_tag(self, tag_content):
        for tag in self.tags:
            if tag == tag_content:
                self.tags.remove(tag)

    def edit(self, file_name):
        self.file_name = file_name

    def __repr__(self):
        result = f"Document {self.id}: {self.file_name}; " \
               f"category {self.category_id}, topic {self.topic_id}, tags: {', '.join(self.tags)}"
        return result
