r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Accounts
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, Optional, Union
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class SafelistInstance(InstanceResource):
    """
    :ivar sid: The unique string that we created to identify the SafeList resource.
    :ivar phone_number: The phone number in SafeList.
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.phone_number: Optional[str] = payload.get("phone_number")

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Accounts.V1.SafelistInstance>"


class SafelistList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the SafelistList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/SafeList/Numbers"

    def create(self, phone_number: str) -> SafelistInstance:
        """
        Create the SafelistInstance

        :param phone_number: The phone number to be added in SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).

        :returns: The created SafelistInstance
        """

        data = values.of(
            {
                "PhoneNumber": phone_number,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return SafelistInstance(self._version, payload)

    async def create_async(self, phone_number: str) -> SafelistInstance:
        """
        Asynchronously create the SafelistInstance

        :param phone_number: The phone number to be added in SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).

        :returns: The created SafelistInstance
        """

        data = values.of(
            {
                "PhoneNumber": phone_number,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return SafelistInstance(self._version, payload)

    def delete(self, phone_number: Union[str, object] = values.unset) -> bool:
        """
        Asynchronously delete the SafelistInstance

        :param phone_number: The phone number to be removed from SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
        :returns: True if delete succeeds, False otherwise
        """
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        params = values.of(
            {
                "PhoneNumber": phone_number,
            }
        )
        return self._version.delete(
            method="DELETE", uri=self._uri, headers=headers, params=params
        )

    async def delete_async(
        self, phone_number: Union[str, object] = values.unset
    ) -> bool:
        """
        Asynchronously delete the SafelistInstance

        :param phone_number: The phone number to be removed from SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
        :returns: True if delete succeeds, False otherwise
        """
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        params = values.of(
            {
                "PhoneNumber": phone_number,
            }
        )
        return await self._version.delete_async(
            method="DELETE", uri=self._uri, headers=headers, params=params
        )

    def fetch(
        self, phone_number: Union[str, object] = values.unset
    ) -> SafelistInstance:
        """
        Asynchronously fetch the SafelistInstance

        :param phone_number: The phone number to be fetched from SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
        :returns: The fetched SafelistInstance
        """
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        params = values.of(
            {
                "PhoneNumber": phone_number,
            }
        )

        payload = self._version.fetch(
            method="GET", uri=self._uri, headers=headers, params=params
        )

        return SafelistInstance(self._version, payload)

    async def fetch_async(
        self, phone_number: Union[str, object] = values.unset
    ) -> SafelistInstance:
        """
        Asynchronously fetch the SafelistInstance

        :param phone_number: The phone number to be fetched from SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
        :returns: The fetched SafelistInstance
        """
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        params = values.of(
            {
                "PhoneNumber": phone_number,
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, headers=headers, params=params
        )

        return SafelistInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Accounts.V1.SafelistList>"