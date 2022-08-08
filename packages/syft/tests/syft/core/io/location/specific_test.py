"""In this test suite, we evaluate the SpecificLocation class. For more info
on the SpecificLocation class and its purpose, please see the documentation
in the class itself.

Table of Contents:
    - INITIALIZATION: tests for various ways SpecificLocation can/can't be initialized
    - CLASS METHODS: tests for the use of SpecificLocation's class methods
    - SERDE: test for serialization and deserialization of SpecificLocation.

"""


# stdlib
import uuid

# syft absolute
import syft as sy
from syft.core.common.serde.deserialize import PROTOBUF_START_MAGIC_HEADER_BYTES
from syft.core.common.uid import UID
from syft.core.io.location.specific import SpecificLocation

# --------------------- INITIALIZATION ---------------------

blob_bytes = (
    b"\n\t"
    + PROTOBUF_START_MAGIC_HEADER_BYTES
    + b"\x12/syft.core.io.location.specific.SpecificLocation\x1a\x1a\n\x12\n\x10"
    + b"\xfb\x1b\xb0g[\xb7LI\xbe\xce\xe7\x00\xab\n\x15\x14\x12\x04Test"
)


def test_specific_location_init_without_arguments() -> None:
    """Test that SpecificLocation will self-create an ID object if none is given"""

    # init works without arguments
    loc = SpecificLocation()

    assert isinstance(loc.id, UID)


def test_specific_location_init_with_specific_id() -> None:
    """Test that SpecificLocation will use the ID you pass into the constructor"""

    uid = UID(value=uuid.UUID(int=333779996850170035686993356951732753684))

    loc = SpecificLocation(id=uid)

    assert loc.id == uid


# --------------------- CLASS METHODS ---------------------


def test_compare() -> None:
    """While uses of this feature should be quite rare, we
    should be able to check whether two objects are the same
    based on their IDs being the same by default. Note that
    subclasses will undoubtedly modify this behavior with other
    __eq__ methods."""

    obj = SpecificLocation()
    obj2 = SpecificLocation()

    assert obj != obj2

    obj._id = obj2.id

    assert obj == obj2


def test_to_string() -> None:
    """Tests that SpecificLocation generates an intuitive string."""

    uid = UID(value=uuid.UUID(int=333779996850170035686993356951732753684))
    obj = SpecificLocation(id=uid)
    assert str(obj) == "<SpecificLocation: fb1bb0675bb74c49becee700ab0a1514>"
    assert obj.__repr__() == "<SpecificLocation: fb1bb0675bb74c49becee700ab0a1514>"


def test_pprint() -> None:
    """Tests that SpecificLocation generates a pretty representation."""

    uid = UID(value=uuid.UUID(int=333779996850170035686993356951732753684))
    obj = SpecificLocation(id=uid, name="location")
    assert obj.pprint == "📌 location (SpecificLocation)@<UID:🙍🛖>"
