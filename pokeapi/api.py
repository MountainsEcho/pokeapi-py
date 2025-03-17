from __future__ import annotations
from typing import Optional, Union, overload
import logging
from rich import print

import requests

from .models import *


class Api:
    """
    A class to interact with the PokeAPI.
    """

    def __init__(self, *,
                 version: str = "v2"):
        """
        Initializes the Api class.
        """
        self.session = self._ensure_session()
        self.version = version

    def _ensure_session(self) -> requests.Session:
        """
        Ensures that a requests session is created.
        """
        if not hasattr(self, "_session") or self._session is None:
            self._session = requests.Session()
        return self._session

    @property
    def base_url(self):
        """
        Returns the base URL of the API.
        """
        return "https://pokeapi.co/api"

    @property
    def url(self) -> str:
        """
        Returns the full URL of the API.
        The URL is constructed using the base URL and the version.
        """
        return f"{self.base_url}/{self.version}"

    @property
    def version(self) -> str:
        """
        Returns the version of the API.
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """
        Sets the version of the API.
        """
        if not isinstance(version, str):
            raise TypeError("version must be a string")
        if not version:
            raise ValueError("version cannot be empty")
        if version.startswith("/"):
            raise ValueError("version cannot start with '/'")

        self._version = version

    def _make_request(self, url: str, params: dict) -> requests.Response:
        """
        Makes a request to the API.
        """
        try:
            response = self.session.get(url, params=params)
            # Check if the response was successful
            response.raise_for_status()
        except requests.HTTPError as e:
            logging.error(f"Error fetching data from API: {e}")
            raise

        return response

    def get_berry(
        self, *,
        id: Optional[int] = None,
        name: Optional[str] = None,
    ) -> "Berry":
        """
        Returns a Berry object from the API.
        """

        params = {}

        if id is not None:
            if not isinstance(id, int):
                raise TypeError("id must be an integer")
            elif id < 1:
                raise ValueError("id must be greater than 0")

            url = f"{self.url}/berry/{id}/"
        elif name is not None:
            if not isinstance(name, str):
                raise TypeError("name must be a string")
            elif not name:
                raise ValueError("name cannot be empty")

            url = f"{self.url}/berry/{name}/"
        else:
            raise ValueError("Either id or name must be provided")

        # added this in as there is a chance that the get request will fail
        # and if we don't get a response then
        response = None
        try:
            response = self.session.get(url, params=params)
            # Check if the response was successful
            response.raise_for_status()
        except requests.HTTPError as e:
            if response is not None and response.status_code == 404:
                logging.error(f"Berry not found: {e}")
            else:
                logging.error(f"Error fetching data from API: {e}")
            raise

        return Berry.model_validate(response.json())

    def get_all_berries(
        self, *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> list["NamedAPIResource"]:
        """
        Returns a BerryList object from the API.
        """

        params = {}

        if limit is not None:
            if not isinstance(limit, int):
                raise TypeError("limit must be an integer")
            elif limit < 1:
                raise ValueError("limit must be greater than 0")
            params["limit"] = limit

        if offset is not None:
            if not isinstance(offset, int):
                raise TypeError("offset must be an integer")
            elif offset < 0:
                raise ValueError("offset must be greater than or equal to 0")
            params["offset"] = offset

        url = f"{self.url}/berry/"

        try:
            response = self.session.get(url, params=params)
            # Check if the response was successful
            response.raise_for_status()
        except requests.HTTPError as e:
            logging.error(f"Error fetching data from API: {e}")
            raise

        model = NamedAPIResourceList.model_validate(response.json())

        BerryList: list["NamedAPIResource"] = []

        while model.next:
            response = self.session.get(model.next)
            BerryList = NamedAPIResourceList.model_validate(response.json())
            print(BerryList)

        return NamedAPIResourceList.model_validate(response.json())
