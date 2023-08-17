'''
Provide groups configuration
'''
from libqtile.config import Match
from .icons import icons

groups_config = [
    {
        'name': '1',
        'label': icons['chrome'],
        'matches': [Match(wm_class=["Google-chrome"])],
    },
    {
        'name': '2',
        'label': icons['vim'],
        'matches': None,
    },
    {
        'name': '3',
        'label': icons['shell'],
        'matches': None,
    },
    {
        'name': '4',
        'label': icons['fish'],
        'matches': [Match(wm_class=["Org.gnome.Nautilus"])],
    },
    {
        'name': '5',
        'label': icons['linux'],
        'matches': None,
    },
    {
        'name': '6',
        'label': icons['firefox'],
        'matches': [Match(wm_class=["firefox"])],
    },
    {
        'name': '7',
        'label': icons['kitty'],
        'matches': None,
    },
    {
        'name': '8',
        'label': icons['spotify'],
        'matches': [Match(wm_class=["Spotify", "vlc"])],
    },
    {
        'name': '9',
        'label': icons['video_camera'],
        'matches': [Match(wm_class=["obs"])],
    },
    {
        'name': '0',
        'label': icons['ubuntu'],
        'matches': [Match(wm_class=["Bitwarden"])],
    },
    
]
