import re

from click import version_option as click_version_option

from .utils import _colorize


def version_option(
    version=None,
    prog_name=None,
    message="%(prog)s, version %(version)s",
    message_style=None,
    prog_name_style=None,
    version_style=None,
    **kwargs
):
    """
    :param prog_name_style: style of the prog_name.
    :param version_style: style of the version.
    :param message_style: default style of the message.

    for other params see Click's version_option decorator:
    https://click.palletsprojects.com/en/7.x/api/#click.version_option
    """
    msg_parts = []
    for s in re.split(r"(%\(version\)s|%\(prog\)s)", message):
        if s == "%(prog)s":
            msg_parts.append(_colorize(prog_name, prog_name_style or message_style))
        elif s == "%(version)s":
            msg_parts.append(_colorize(version, version_style or message_style))
        else:
            msg_parts.append(_colorize(s, message_style))
    message = "".join(msg_parts)

    return click_version_option(
        version=version, prog_name=prog_name, message=message, **kwargs
    )