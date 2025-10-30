# college.py
class College:
    def __init__(self, ccode, cname):
        self._ccode = ccode
        self._cname = cname

    @property
    def ccode(self):
        return self._ccode

    @property
    def cname(self):
        return self._cname

    @property
    def display(self):
        """Return (ccode, cname) tuple for convenience."""
        return self._ccode, self._cname

