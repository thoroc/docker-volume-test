from pathlib import Path


class DisplayablePath(object):
    # Generously donated from https://stackoverflow.com/a/49912639/2120421
    DISPLAY_FILENAME_PREFIX_MIDDLE = '├──'
    DISPLAY_FILENAME_PREFIX_LAST = '└──'
    DISPLAY_PARENT_PREFIX_MIDDLE = '    '
    DISPLAY_PARENT_PREFIX_LAST = '│   '

    def __init__(self, path, parent_path, is_last):
        self.path = Path(str(path))
        self.parent = parent_path
        self.is_last = is_last

        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0

    @property
    def displayname(self):
        if self.path.is_dir():
            return self.path.name + '/'

        return self.path.name

    @classmethod
    def make_tree(cls, root, parent=None, is_last=False, criteria=None):
        root = Path(str(root))
        criteria = criteria or cls._default_criteria
        displayable_root = cls(root, parent, is_last)

        yield displayable_root

        children = sorted(
            list(path for path in root.iterdir() if criteria(path)),
            key=lambda s: str(s).lower()
        )
        count = 1

        for path in children:
            is_last = count == len(children)

            if path.is_dir():
                yield from cls.make_tree(
                    path,
                    parent=displayable_root,
                    is_last=is_last,
                    criteria=criteria
                )
            else:
                yield cls(path, displayable_root, is_last)

            count += 1

    @classmethod
    def _default_criteria(cls, path):
        return True

    def displayable(self):
        if self.parent is None:
            return self.displayname

        _filename_prefix = (self.DISPLAY_FILENAME_PREFIX_LAST
                            if self.is_last
                            else self.DISPLAY_FILENAME_PREFIX_MIDDLE)

        parts = [f"{_filename_prefix} {self.displayname}"]
        parent = self.parent

        while parent and parent.parent is not None:
            parts.append(
                self.DISPLAY_PARENT_PREFIX_MIDDLE
                if parent.is_last
                else self.DISPLAY_PARENT_PREFIX_LAST
            )
            parent = parent.parent

        return ''.join(reversed(parts))
