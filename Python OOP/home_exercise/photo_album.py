import math


class PhotoAlbum:
    PAGE_CAPACITY = 4
    IDX = 0

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = []
        for p in range(self.pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count):
        new_pages = math.ceil(photos_count / cls.PAGE_CAPACITY)
        return cls(new_pages)

    def add_photo(self, label):
        for row_idx in range(len(self.photos)):
            row = self.photos[row_idx]
            if len(row) < 4:
                self.photos[row_idx].append(label)
                return f"{label} photo added successfully on page {row_idx + 1} slot {len(self.photos[row_idx])}"
        return 'No more free slots'

    def display(self):
        result = '-' * 11 + '\n'
        for page in self.photos:
            new_result = []
            for _ in page:
                new_result.append('[]')
            result += ' '.join(new_result)
            result += '\n'
            result += '-' * 11 + '\n'
        return result.rstrip()
