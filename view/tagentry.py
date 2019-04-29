"""Module that provides customizable tag entries for the GUI"""

from tkinter import Entry, Label


class TagEntry:
    """Class that display can music tags as entries in the GUI"""

    def __init__(self, tag, parent, gridmanager, row, width=20):
        self.tag = tag
        self.width = width
        self.gridmanager = gridmanager
        self.row = row
        self.parent = parent
        self.entries = []
        self.entries.append(Entry(parent, width=self.width))
        self.label = Label(parent, text=tag.name)
        self.currfiles = []

    def draw(self):
        self.gridmanager.add_element(self.label, self.row)

        for entry in self.entries:
            self.gridmanager.add_element(entry, self.row)

    def fill_entries(self, files):
        for entry in self.entries:
            entry.destroy()

        self.entries = []
        for file in files:
            value = file.get_tag_value(self.tag)
            newentry = Entry(self.parent, width=self.width)

            if value is not None:
                newentry.insert(0, value)

            self.entries.append(newentry)

        self.currfiles = files
        self.draw()

    def write_files(self):
        for file, entry in zip(self.currfiles, self.entries):
            if len(entry.get()) > 0:
                file.write_tag(self.tag, entry.get())


class SingleTagEntry:
    """Special version of the tag entry that displays
    one entry for a set of music files"""

    def __init__(self, tag, parent, gridmanager, row, width=20):
        self.tag = tag
        self.width = width
        self.gridmanager = gridmanager
        self.row = row
        self.parent = parent
        self.entry = Entry(parent, width=self.width)
        self.label = Label(parent, text=tag.name)
        self.currfiles = []
        self.oldentry = None

    def draw(self):
        self.gridmanager.add_element(self.label, self.row)
        self.gridmanager.add_element(self.entry, self.row)

    def fill_entries(self, files):
        if len(files) is 0:
            return

        file = files[0]
        value = file.get_tag_value(self.tag)

        if value is not None:
            self.entry.delete(0, 'end')
            self.entry.insert(0, value)
            self.oldentry = value
        else:
            self.entry.insert(0, "")

        self.currfiles = files
        self.draw()

    def write_files(self):
        for file in self.currfiles:
            newentry = self.entry.get()

            if len(newentry) > 0 and newentry != self.oldentry:
                file.write_tag(self.tag, self.entry.get())
                self.oldentry = None
