from .snaptik import snaptik, Snaptik
from .ssstik import ssstik
from .scrapper import VideoInfo
from .tikmate import tikmate, Tikmate
from .mdown import mdown, Mdown
from .Except import InvalidUrl
from .ttdownloader import ttdownloader, TTDownloader
from .tikdown import tikdown, Tikdown
from .tikwm import tikwm, TikWM

__all__ = [
    'snaptik',
    'Snaptik',
    'ssstik',
    'VideoInfo',
    'tikmate',
    'Tikmate',
    'mdown',
    'Mdown',
    'InvalidUrl',
    'ttdownloader',
    'tikdown',
    'Tikdown',
    'TTDownloader',
    'tikwm',
    'TikWM'
]
def robust(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            return tikwm(*args, **kwargs)
    return wrapper


services = {
    'snaptik': robust(snaptik),
    'ssstik': robust(ssstik),
    'tikmate': robust(tikmate),
    'mdown': robust(mdown),
    'ttdownloader': robust(ttdownloader),
    'tikdown': robust(tikdown),
    'tiktok': robust(tikwm),
    'tikwm': tikwm
}
