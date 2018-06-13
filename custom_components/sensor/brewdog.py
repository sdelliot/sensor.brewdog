"""
A platform which allows you to get information about a random BreDog beer.
For more details about this component, please refer to the documentation at
https://gitlab.com/custom_components/brewdog
"""
import requests
import voluptuous as vol
from datetime import timedelta
from homeassistant.helpers.entity import Entity


ATTR_COMPONENT = 'component'
ATTR_COMPONENT_VERSION = 'component_version'
ATTR_DESCRIPTION = 'description'
ATTR_FIRSTBREWED = 'first brewed'
ATTR_IMAGE = 'image'

SCAN_INTERVAL = timedelta(seconds=120)

ICON = 'mdi:beer'
COMPONENT_NAME = 'brewdog'
COMPONENT_VERSION = '0.0.1'


BASE_URL = 'https://api.punkapi.com/v2/beers/random'

def setup_platform(hass, config, add_devices, discovery_info=None):
    add_devices([BrewDogSensor()])

class BrewDogSensor(Entity):
    def __init__(self):
        self._state = None
        self._component = COMPONENT_NAME
        self._componentversion = COMPONENT_VERSION
        self.update()

    def update(self):
        rbd = requests.get(BASE_URL, timeout=5).json()[0]
        self._state = rbd['tagline']
        self._firstbrewerd = rbd['first_brewed']
        self._description = rbd['description']
        self._image = rbd['image_url']

    @property
    def name(self):
        return 'Random Brewdog'

    @property
    def state(self):
        return self._state

    @property
    def icon(self):
        return ICON

    @property
    def friendly_name(self):
        return self._fiendlyname

    @property
    def device_state_attributes(self):
        return {
            ATTR_FIRSTBREWED: self._firstbrewerd,
            ATTR_DESCRIPTION: self._description,
            ATTR_IMAGE: self._image
        }