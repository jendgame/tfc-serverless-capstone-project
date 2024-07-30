r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trunking
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, Optional, Union
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class RecordingInstance(InstanceResource):

    class RecordingMode(object):
        DO_NOT_RECORD = "do-not-record"
        RECORD_FROM_RINGING = "record-from-ringing"
        RECORD_FROM_ANSWER = "record-from-answer"
        RECORD_FROM_RINGING_DUAL = "record-from-ringing-dual"
        RECORD_FROM_ANSWER_DUAL = "record-from-answer-dual"

    class RecordingTrim(object):
        TRIM_SILENCE = "trim-silence"
        DO_NOT_TRIM = "do-not-trim"

    """
    :ivar mode: 
    :ivar trim: 
    """

    def __init__(self, version: Version, payload: Dict[str, Any], trunk_sid: str):
        super().__init__(version)

        self.mode: Optional["RecordingInstance.RecordingMode"] = payload.get("mode")
        self.trim: Optional["RecordingInstance.RecordingTrim"] = payload.get("trim")

        self._solution = {
            "trunk_sid": trunk_sid,
        }
        self._context: Optional[RecordingContext] = None

    @property
    def _proxy(self) -> "RecordingContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: RecordingContext for this RecordingInstance
        """
        if self._context is None:
            self._context = RecordingContext(
                self._version,
                trunk_sid=self._solution["trunk_sid"],
            )
        return self._context

    def fetch(self) -> "RecordingInstance":
        """
        Fetch the RecordingInstance


        :returns: The fetched RecordingInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "RecordingInstance":
        """
        Asynchronous coroutine to fetch the RecordingInstance


        :returns: The fetched RecordingInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        mode: Union["RecordingInstance.RecordingMode", object] = values.unset,
        trim: Union["RecordingInstance.RecordingTrim", object] = values.unset,
    ) -> "RecordingInstance":
        """
        Update the RecordingInstance

        :param mode:
        :param trim:

        :returns: The updated RecordingInstance
        """
        return self._proxy.update(
            mode=mode,
            trim=trim,
        )

    async def update_async(
        self,
        mode: Union["RecordingInstance.RecordingMode", object] = values.unset,
        trim: Union["RecordingInstance.RecordingTrim", object] = values.unset,
    ) -> "RecordingInstance":
        """
        Asynchronous coroutine to update the RecordingInstance

        :param mode:
        :param trim:

        :returns: The updated RecordingInstance
        """
        return await self._proxy.update_async(
            mode=mode,
            trim=trim,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trunking.V1.RecordingInstance {}>".format(context)


class RecordingContext(InstanceContext):

    def __init__(self, version: Version, trunk_sid: str):
        """
        Initialize the RecordingContext

        :param version: Version that contains the resource
        :param trunk_sid: The SID of the Trunk that will have its recording settings updated.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "trunk_sid": trunk_sid,
        }
        self._uri = "/Trunks/{trunk_sid}/Recording".format(**self._solution)

    def fetch(self) -> RecordingInstance:
        """
        Fetch the RecordingInstance


        :returns: The fetched RecordingInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return RecordingInstance(
            self._version,
            payload,
            trunk_sid=self._solution["trunk_sid"],
        )

    async def fetch_async(self) -> RecordingInstance:
        """
        Asynchronous coroutine to fetch the RecordingInstance


        :returns: The fetched RecordingInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return RecordingInstance(
            self._version,
            payload,
            trunk_sid=self._solution["trunk_sid"],
        )

    def update(
        self,
        mode: Union["RecordingInstance.RecordingMode", object] = values.unset,
        trim: Union["RecordingInstance.RecordingTrim", object] = values.unset,
    ) -> RecordingInstance:
        """
        Update the RecordingInstance

        :param mode:
        :param trim:

        :returns: The updated RecordingInstance
        """
        data = values.of(
            {
                "Mode": mode,
                "Trim": trim,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RecordingInstance(
            self._version, payload, trunk_sid=self._solution["trunk_sid"]
        )

    async def update_async(
        self,
        mode: Union["RecordingInstance.RecordingMode", object] = values.unset,
        trim: Union["RecordingInstance.RecordingTrim", object] = values.unset,
    ) -> RecordingInstance:
        """
        Asynchronous coroutine to update the RecordingInstance

        :param mode:
        :param trim:

        :returns: The updated RecordingInstance
        """
        data = values.of(
            {
                "Mode": mode,
                "Trim": trim,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RecordingInstance(
            self._version, payload, trunk_sid=self._solution["trunk_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trunking.V1.RecordingContext {}>".format(context)


class RecordingList(ListResource):

    def __init__(self, version: Version, trunk_sid: str):
        """
        Initialize the RecordingList

        :param version: Version that contains the resource
        :param trunk_sid: The SID of the Trunk from which to fetch the recording settings.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "trunk_sid": trunk_sid,
        }

    def get(self) -> RecordingContext:
        """
        Constructs a RecordingContext

        """
        return RecordingContext(self._version, trunk_sid=self._solution["trunk_sid"])

    def __call__(self) -> RecordingContext:
        """
        Constructs a RecordingContext

        """
        return RecordingContext(self._version, trunk_sid=self._solution["trunk_sid"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Trunking.V1.RecordingList>"