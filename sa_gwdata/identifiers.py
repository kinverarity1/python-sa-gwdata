import re


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
        self.set(*args)

    def set(self, *args):
        """See :class:`UnitNo` constructor for details of arguments."""
        if len(args) == 1:
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
                    "check docs for accepted formats".format(
                        args[0]
                    )
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
        self.set(*args)

    def set(self, *args):
        """See :class:`ObsNo` constructor for details of arguments."""
        if len(args) == 1 and args[0]:
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
                "check docs for accepted formats".format(
                    args[0]
                )
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
        self._well_attributes = []
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
            self.set_well_attribute(key, value)

    def set_well_attribute(self, key, value):
        key = key.lower()
        self._well_attributes.append(key)
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
        return "<sa_gwdata.Well({}) {}>".format(self.dh_no, self.title)

    def path_safe_repr(self, remove_prefix=True):
        """Return title containing only characters which are allowed in
        Windows path names."""
        r = str(self)
        r = r.replace(" /", ";")[1:-1]
        for char in ["\\", "/", "?", ":", "*", '"', "<", ">", "|"]:
            r = r.replace(char, "")
        if remove_prefix:
            parts = r.split(")")
            r = " ".join(parts[1:])[1:]
        return r


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
    dh_re_prefix=r"\A"
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

