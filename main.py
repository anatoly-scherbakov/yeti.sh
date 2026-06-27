import functools
from pathlib import Path
from typing import Any

from mkdocs_macros.plugin import MacrosPlugin
from rdflib import URIRef

from iolanta.cli.main import decode_datatype
from iolanta.conversions import path_to_iri
from iolanta.iolanta import Iolanta


def as_uri(uri: Any) -> URIRef:
    """Convert a path, string, or URIRef to a URIRef."""
    match uri:
        case Path() as path:
            return path_to_iri(path)
        case URIRef() as uriref:
            return uriref
        case str() as uri_string:
            return URIRef(uri_string)

    uri_type = type(uri)
    raise NotImplementedError(f"{uri} ({uri_type.__name__}) is unknown")


def _as_filter(iolanta_instance: Iolanta, uri: str, datatype: str) -> str:
    """Render a node or document path through Iolanta as the requested datatype."""
    return iolanta_instance.render(
        node=as_uri(uri),
        as_datatype=decode_datatype(datatype),
    )


def define_env(env: MacrosPlugin):
    iolanta = Iolanta(project_root=Path(__file__).parent / "docs")

    env.filters["as"] = functools.partial(_as_filter, iolanta)
    env.filters["uri"] = as_uri
    env.variables["docs"] = Path(__file__).parent / "docs"
    env.variables["URIRef"] = URIRef
