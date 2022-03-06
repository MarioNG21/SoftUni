class PhotoAlbum:
    PAGE_CAP = 4
    SLOT_COUNTER = 1
    PAGE_COUNTER = 1

    def __init__(self, pages):
        self.pages = pages
        self.photos = []
        for row in range(pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(photos_count)

    @classmethod
    def set_new_counters(cls, page_counter, slot_counter):
        cls.PAGE_COUNTER += page_counter
        cls.SLOT_COUNTER += slot_counter
    def add_photo(self, label):

        if self.PAGE_CAP:
            self.photos.append(label)
            result =  f"{label} photo added successfully on page {self.PAGE_COUNTER} slot {self.SLOT_COUNTER}"
        if self.PAGE_COUNTER < self.pages and self.SLOT_COUNTER < self.PAGE_CAP:
            PhotoAlbum.set_new_counters(1, 1)

        else:
            result =  'No more free slots'

        return result


    def display(self):
        pass


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
