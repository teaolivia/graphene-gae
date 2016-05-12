from graphene.core.classtypes.objecttype import ObjectTypeOptions
from graphene.relay.types import Node
from graphene.relay.utils import is_node


class NdbOptions(ObjectTypeOptions):
    VALID_ATTRS = ('model', 'only_fields', 'exclude_fields')

    def __init__(self, *args, **kwargs):
        super(NdbOptions, self).__init__(*args, **kwargs)
        self.model = None
        self.valid_attrs += self.VALID_ATTRS
        self.only_fields = None
        self.exclude_fields = []

    def contribute_to_class(self, cls, name):
        super(NdbOptions, self).contribute_to_class(cls, name)
        if is_node(cls):
            self.exclude_fields = list(self.exclude_fields) + ['id']
            self.interfaces.append(Node)
