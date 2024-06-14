import re
import uuid


def slugify(self, slug):
    slug = slug + str(uuid.uuid4())
    return slug
