import collections.abc
import re

import pandas as pd

PATTERNS = {
    "unit_no": [r"G?(\d{4})-?(\d{5})", r"G?(\d{4})-(\d{1,5})"],
    "dh_no": [r"(\d{1,6})"],
    "obs_no": [r"([a-zA-Z]{3})[ -]?(\d{1,3})"],
}


class UnitNo:
    """Parse a well unit number.

    Arguments:
        *args (str or int): either the complete unit number or the map sheet and
            drillhole sequence numbers

    Example::

        >>> u1 = UnitNo("6628-123")
        >>> u2 = UnitNo("662800123")
        >>> u3 = UnitNo(662800123)
        >>> u4 = UnitNo("6628-00123")
        >>> u5 = UnitNo(6628, 123)
        >>> u6 = UnitNo("6628", "00123")
        >>> u7 = UnitNo("G662800123")
        >>> u1 == u2 == u3 == u4 == u5 == u6 == u7
        True

    Attributes:
        map (int): 10K map sheet
        seq (int): sequence number
        hyphen (str): hyphenated format e.g. "6628-123"
        long (str): zero-filled format e.g. "662800123"
        long_int (int/None): zero-filled format as integer e.g. 662800123 or
            None if missing
        wilma (str): WILMA style e.g. "6628-00123"
        hydstra (str): Hydstra style e.g. "G662800123"

    """

    def __init__(self, *args):
        self.map = None
        self.seq = None
        self._attributes = [
            "map",
            "seq",
            "hyphen",
            "long",
            "long_int",
            "wilma",
            "hydstra",
        ]
        self.set(*args)

    def set(self, *args):
        """See :class:`UnitNo` constructor for details of arguments."""
        if len(args) == 1:
            if args[0] == "nan":
                args[0] = None
            if args[0]:
                if isinstance(args[0], list) or isinstance(args[0], tuple):
                    return self.set(*args[0])
                for pattern in PATTERNS["unit_no"]:
                    match = re.match(pattern, str(args[0]))
                    if match:
                        self.map = int(match.group(1))
                        self.seq = int(match.group(2))
                        return
                raise ValueError(
                    "no identifier found in {}, "
                    "check docs for accepted formats".format(args[0])
                )
        elif len(args) == 2:
            self.map = int(args[0])
            self.seq = int(args[1])

    @property
    def hyphen(self):
        try:
            return "{:d}-{:d}".format(self.map, self.seq)
        except TypeError:
            return ""

    @property
    def long(self):
        try:
            return "{:d}{:05d}".format(self.map, self.seq)
        except TypeError:
            return ""

    @property
    def long_int(self):
        if self.long:
            return int(self.long)
        else:
            return None

    @property
    def wilma(self):
        try:
            return "{:d}-{:05d}".format(self.map, self.seq)
        except TypeError:
            return ""

    @property
    def hydstra(self):
        try:
            return "G{:d}{:05d}".format(self.map, self.seq)
        except TypeError:
            return ""

    def __str__(self):
        return self.hyphen

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash((self.map, self.seq))

    def __iter__(self):
        return iter((self.map, self.seq))

    def __bool__(self):
        return bool(self.map) and bool(self.seq)

    def to_scalar_dict(self):
        return {attr: getattr(self, attr) for attr in self._attributes}


class ObsNo:
    """Parse an observation well identifier.

    Arguments:
        *args (str or int): either one string, which can be either in the format
            'YAT017' or 'YAT-17', etc.; or two values, either int or str, for
            the plan prefix (three letters referring to the hundred) and
            the sequence number. e.g. 'YAT', 17

    Example::

        >>> from sa_gwdata import ObsNo
        >>> o1 = ObsNo("YAT017")
        >>> o2 = ObsNo("YAT17")
        >>> o3 = ObsNo("YAT 17")
        >>> o4 = ObsNo("YAT", 17)
        >>> o1 == o2 == o3 == o4
        True

    Attributes:
        plan (str): hundred prefix
        seq (int): sequence number
        id (str): consistent zero-padded identifier e.g. "YAT017"
        egis (str): ENVGIS style e.g. "YAT 17"

    """

    def __init__(self, *args):
        self.plan = ""
        self.seq = None
        self._attributes = ["plan", "seq", "id", "egis"]
        self.set(*args)

    @classmethod
    def parse(cls, *args, **kwargs):
        """Parse an obs identifier, ignoring all parsing errors.

        Arguments are the same as those for the class constructor,
        but all exceptions are ignored.

        Returns: ObsNo.id if successful, a blank string if not.

        """
        try:
            obs_no = cls(*args, **kwargs)
        except:
            return ""
        else:
            return obs_no.id

    def set(self, *args):
        """See :class:`ObsNo` constructor for details of arguments."""
        if len(args) == 1:
            if args[0] == "nan":
                args[0] = None
            if args[0]:
                if isinstance(args[0], list) or isinstance(args[0], tuple):
                    return self.set(*args[0])
                for pattern in PATTERNS["obs_no"]:
                    match = re.match(pattern, args[0])
                    if match:
                        self.plan = match.group(1)
                        self.seq = int(match.group(2))
                        return
                raise ValueError(
                    "no identifier found in {}, "
                    "check docs for accepted formats".format(args[0])
                )
        elif len(args) == 2:
            if isinstance(args[0], str):
                self.plan = args[0]
                self.seq = int(args[1])
            else:
                raise ValueError(
                    "first argument should be a str e.g. 'YAT', 'ADE', etc."
                )

    @property
    def id(self):
        try:
            return "{}{:03d}".format(self.plan.upper(), self.seq)
        except TypeError:
            return ""

    @property
    def egis(self):
        try:
            return "{} {:.0f}".format(self.plan.upper(), self.seq)
        except TypeError:
            return ""

    def __str__(self):
        return self.id

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash((self.plan, self.seq))

    def __iter__(self):
        return iter((self.plan, self.seq))

    def __bool__(self):
        return bool(self.plan) and bool(self.seq)

    def to_scalar_dict(self):
        return {attr: getattr(self, attr) for attr in self._attributes}


class Well:
    """Represents a well.

    Args:
            dh_no (int): drillhole number (required)
            unit_no (str/int): unit number (optional)
            obs_no (str/int): obs number (optional)

    Other keyword arguments will be set as attributes.

    Attributes:

        id (str): obs number if it exists, e.g. "NOA002", if not,
            unit number e.g. "6628-123", and in the rare case that
            a unit number does not exist, then drillhole no. e.g.
            "200135".
        title (str): available attributes including name, e.g.
            "7025-3985 / WRG038 / WESTERN LAGOON".
        obs_no (ObsNo): obs number
        unit_no (UnitNo): unit number

    """

    def __init__(self, *args, **kwargs):
        self._attributes = []
        self.unit_no = UnitNo()
        self.obs_no = ObsNo()
        self.name = ""
        self.set(*args, **kwargs)

    def set(self, dh_no, unit_no="", obs_no="", **kwargs):
        """See :class:`Well` constructor for docstring."""
        self.dh_no = dh_no
        self.set_unit_no(unit_no)
        self.set_obs_no(obs_no)
        for key, value in kwargs.items():
            if not key in ("unit_long", "unit_hyphen", "id", "title"):
                try:
                    self.set_well_attribute(key, value)
                except AttributeError:
                    print(f"Error setting {key} to {value}")

    def set_well_attribute(self, key, value):
        key = key.lower()
        self._attributes.append(key)
        setattr(self, key, value)

    def set_obs_no(self, *args):
        """Set obswell number.

        Args are passed to :class:`ObsNo` constructor.

        """
        self.obs_no.set(*args)

    def set_unit_no(self, *args):
        """Set unit number.

        Args are passed to :class:`UnitNo` constructor.

        """
        self.unit_no.set(*args)

    @property
    def unit_hyphen(self):
        return self.unit_no.hyphen

    @property
    def unit_long(self):
        return self.unit_no.long

    def __eq__(self, other):
        if hasattr(other, "dh_no"):
            return self.dh_no == other.dh_no
        else:
            return False

    def __hash__(self):
        return hash(self.dh_no)

    def __bool__(self):
        return bool(self.dh_no)

    @property
    def id(self):
        if self.obs_no:
            return self.obs_no
        elif self.unit_no:
            return self.unit_no
        else:
            return str(self.dh_no)

    @property
    def title(self):
        names = [self.unit_no.hyphen]
        if not names[0]:
            names[0] = "[dh_no={:d}]".format(self.dh_no)
        if self.obs_no:
            names.append(self.obs_no.id)
        if self.name:
            names.append(self.name)
        return " / ".join(names)

    def __repr__(self):
        if self.obs_no:
            return f"'{str(self.obs_no)}'"
        elif self.unit_hyphen:
            return f"'{str(self.unit_hyphen)}'"
        else:
            return str(self.dh_no)

    def to_scalar_dict(self):
        """Convert Well to a dictionary containing scalar values.

        Returns: dict.

        Guaranteed keys are "dh_no", "id", "title" and "name".

        The keys present in `well.unit_no.to_scalar_dict()` will
        be added with the prefix "unit_no.". Same for `obs_no`.

        Any additional attributes will also be present.

        """
        d = {"dh_no": self.dh_no, "id": self.id, "title": self.title, "name": self.name}
        d.update(
            {("unit_no." + k): v for k, v in self.unit_no.to_scalar_dict().items()}
        )
        d.update({("obs_no." + k): v for k, v in self.obs_no.to_scalar_dict().items()})
        d.update({attr: getattr(self, attr) for attr in self._attributes})
        return d

    def path_safe_repr(self, remove_prefix=True):
        """Return title containing only characters which are allowed in
        Windows path names."""
        r = str(self)
        for char in ["\\", "/", "?", ":", "*", '"', "<", ">", "|"]:
            r = r.replace(char, "")

        # This keyword argument now has no function.
        # if remove_prefix:
        #     parts = r.split(")")
        #     r = " ".join(parts[1:])[1:]
        return r


class Wells(collections.abc.MutableSequence):
    """Represents a set of wells.

    This is not meant to be instantiated here, but can be
    accessed from methods of other objects, such as
    :meth:`sa_gwdata.WaterConnectSession.find_wells`.

    Attributes:
        wells (list): list of :class:`sa_gwdata.Well` objects.

    All attributes of the contained Well objects will also be
    present as attributes on this object, returning lists of the
    values from the Well objects contained here. It sounds more
    complex than it is! Tab completion is enabled, so try it out
    in IPython and you will quickly see how it works.

    """

    def __init__(self, wells=None):
        if wells is None:
            wells = []
        self.wells = wells
        self._refresh()

    def __repr__(self):
        return repr(self.wells)

    def __len__(self):
        return len(self.wells)

    def __getitem__(self, ix):
        if isinstance(ix, int):
            if ix < len(self):
                return self.wells[ix]
        key = ix
        if not key in self._map:
            for id_type, value in parse_well_ids_plaintext(str(key)):
                if value in self._map:
                    key = value
                    break
        return self._map[key]

    def __delitem__(self, ix):
        del self.wells[ix]
        self._refresh()

    def __setitem__(self, ix, value):
        self.wells[ix] = value

    def insert(self, ix, value):
        self.wells.insert(ix, value)
        self._refresh()

    def append(self, value):
        self.wells.append(value)
        self._refresh()

    def count(self, item):
        return self.wells.count(item)

    def index(self, *args):
        return self.wells.index(*args)

    def __iter__(self):
        return iter(self.wells)

    def __getattr__(self, name):
        name = name.split(".")[0]
        if name in self._attributes:
            return self.df()[name].values.tolist()
        elif name in ["unit_no", "obs_no"]:
            return [getattr(w, name) for w in self]
        else:
            raise AttributeError(
                "Wells object does not have an attribute named '{}'".format(name)
            )

    def _refresh(self):
        if len(self):
            self._attributes = list(self[0].to_scalar_dict().keys())
        else:
            self._attributes = []
        self._map = {w.dh_no: w for w in self}
        self._map.update({w.obs_no.id: w for w in self if w.obs_no.id})
        self._map.update({w.unit_no.hyphen: w for w in self if w.unit_no.hyphen})

    def __dir__(self):
        return sorted(
            list(set([k.split(".")[0] for k in self._attributes])) + super().__dir__()
        )

    def df(self):
        """Return information contained in each Well as a table.

        Returns: pd.DataFrame

        The columns of the returned DataFrame will always contain
        the "dh_no", "id", "title" attributes from the contained
        Well objects.

        Additional columns in the form "unit_no." + key will exist
        for all the keys in :meth:`UnitNo.to_scalar_dict`. Same for
        :meth:`ObsNo.to_scalar_dict`.

        Remaining columns depend on the additional attributes present
        on the contained Well objects.

        """
        df = pd.DataFrame([w.to_scalar_dict() for w in self])
        return df


def parse_well_ids(input_text, **kwargs):
    """Specify well identifiers in free text and have them parsed.

    Args:
        input_text (str): the text to parse

    Other keyword arguments are passed to :func:`parse_well_ids_plaintext`.

    Example of acceptable formats:

        662800125
        6628-125
        G662800125
        6628-00125
        SLE 15
        SLE015
        SLE15

    """
    input_text = input_text.replace("\r", "")
    return parse_well_ids_plaintext(input_text, **kwargs)


def parse_well_ids_plaintext(
    input_text,
    types=("unit_no", "obs_no"),
    unit_no_prefix="",
    obs_no_prefix="",
    dh_re_prefix=r"\A",
):
    """Parse possible well identifiers out of plain text.

    Arguments:
        input_text (str): the text to parse well identifiers from.
            Can include multiple lines.
        types (tuple): types of identifiers to look for. Currently
            supported: "unit_no", "obs_no", "dh_no"
        dh_re_prefix (str): regexp pattern required before a dh_no
            regexp will match

    Returns: a list of tuples e.g.

        >>> from sa_gwdata import parse_well_ids
        >>> parse_well_ids('sle15')
        [('obs_no', 'SLE015')]
        >>> parse_well_ids('6628150')
        []
        >>> parse_well_ids('6628-150')
        [('unit_no', '6628-150')]
        >>> parse_well_ids('662800150')
        [('unit_no', '6628-150')]
        >>> parse_well_ids('259001', types=["dh_no"])
        [('dh_no', '259001')]

    Remember this doesn't actually check whether these identifiers to a well
    in the real world; it just parses a string of text to find possible
    well identifiers. It's pretty robust:

        >>> parse_well_ids("SLE 15, SLE16, and also maybe 5910-1")
        [('unit_no', '5910-1'), ('obs_no', 'SLE015'), ('obs_no', 'SLE016'), ('obs_no', 'YBE591')]

    It has unfortunately matched "ybe 591" from the phrase "maybe 5910-1" as an
    obs_no.

    """
    # WARNING: make sure you update any keyword arguments in WaterConnectSession.find_wells()
    input_text = " " + input_text + " "
    match_counts = {"unit_no": 0, "dh_no": 0, "obs_no": 0}
    well_ids = []
    if "unit_no" in types:
        for pattern in PATTERNS["unit_no"]:
            matches = re.findall(unit_no_prefix + pattern, input_text)
            for match in matches:
                match_counts["unit_no"] += 1
                well_ids.append(
                    ("unit_no", "{}-{:.0f}".format(match[0], int(match[1])))
                )
    if "dh_no" in types:
        for id_type in ("dh_no",):
            for pattern in PATTERNS[id_type]:
                items = input_text.split()
                for item in items:
                    match = re.search(dh_re_prefix + pattern, item)
                    if match:
                        match_counts[id_type] += 1
                        well_ids.append((id_type, match.group()))
    if "obs_no" in types:
        for pattern in PATTERNS["obs_no"]:
            matches = re.findall(obs_no_prefix + pattern, input_text)
            for match in matches:
                match_counts["obs_no"] += 1
                well_ids.append(
                    ("obs_no", "{}{:03.0f}".format(match[0].upper(), int(match[1])))
                )
    return well_ids

