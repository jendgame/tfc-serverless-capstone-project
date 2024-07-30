r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Ip_messaging
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class UserChannelInstance(InstanceResource):

    class ChannelStatus(object):
        JOINED = "joined"
        INVITED = "invited"
        NOT_PARTICIPATING = "not_participating"

    class NotificationLevel(object):
        DEFAULT = "default"
        MUTED = "muted"

    """
    :ivar account_sid: 
    :ivar service_sid: 
    :ivar channel_sid: 
    :ivar user_sid: 
    :ivar member_sid: 
    :ivar status: 
    :ivar last_consumed_message_index: 
    :ivar unread_messages_count: 
    :ivar links: 
    :ivar url: 
    :ivar notification_level: 
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        user_sid: str,
        channel_sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.channel_sid: Optional[str] = payload.get("channel_sid")
        self.user_sid: Optional[str] = payload.get("user_sid")
        self.member_sid: Optional[str] = payload.get("member_sid")
        self.status: Optional["UserChannelInstance.ChannelStatus"] = payload.get(
            "status"
        )
        self.last_consumed_message_index: Optional[int] = deserialize.integer(
            payload.get("last_consumed_message_index")
        )
        self.unread_messages_count: Optional[int] = deserialize.integer(
            payload.get("unread_messages_count")
        )
        self.links: Optional[Dict[str, object]] = payload.get("links")
        self.url: Optional[str] = payload.get("url")
        self.notification_level: Optional["UserChannelInstance.NotificationLevel"] = (
            payload.get("notification_level")
        )

        self._solution = {
            "service_sid": service_sid,
            "user_sid": user_sid,
            "channel_sid": channel_sid or self.channel_sid,
        }
        self._context: Optional[UserChannelContext] = None

    @property
    def _proxy(self) -> "UserChannelContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: UserChannelContext for this UserChannelInstance
        """
        if self._context is None:
            self._context = UserChannelContext(
                self._version,
                service_sid=self._solution["service_sid"],
                user_sid=self._solution["user_sid"],
                channel_sid=self._solution["channel_sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the UserChannelInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the UserChannelInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "UserChannelInstance":
        """
        Fetch the UserChannelInstance


        :returns: The fetched UserChannelInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "UserChannelInstance":
        """
        Asynchronous coroutine to fetch the UserChannelInstance


        :returns: The fetched UserChannelInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        notification_level: Union[
            "UserChannelInstance.NotificationLevel", object
        ] = values.unset,
        last_consumed_message_index: Union[int, object] = values.unset,
        last_consumption_timestamp: Union[datetime, object] = values.unset,
    ) -> "UserChannelInstance":
        """
        Update the UserChannelInstance

        :param notification_level:
        :param last_consumed_message_index:
        :param last_consumption_timestamp:

        :returns: The updated UserChannelInstance
        """
        return self._proxy.update(
            notification_level=notification_level,
            last_consumed_message_index=last_consumed_message_index,
            last_consumption_timestamp=last_consumption_timestamp,
        )

    async def update_async(
        self,
        notification_level: Union[
            "UserChannelInstance.NotificationLevel", object
        ] = values.unset,
        last_consumed_message_index: Union[int, object] = values.unset,
        last_consumption_timestamp: Union[datetime, object] = values.unset,
    ) -> "UserChannelInstance":
        """
        Asynchronous coroutine to update the UserChannelInstance

        :param notification_level:
        :param last_consumed_message_index:
        :param last_consumption_timestamp:

        :returns: The updated UserChannelInstance
        """
        return await self._proxy.update_async(
            notification_level=notification_level,
            last_consumed_message_index=last_consumed_message_index,
            last_consumption_timestamp=last_consumption_timestamp,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.IpMessaging.V2.UserChannelInstance {}>".format(context)


class UserChannelContext(InstanceContext):

    def __init__(
        self, version: Version, service_sid: str, user_sid: str, channel_sid: str
    ):
        """
        Initialize the UserChannelContext

        :param version: Version that contains the resource
        :param service_sid:
        :param user_sid:
        :param channel_sid:
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "user_sid": user_sid,
            "channel_sid": channel_sid,
        }
        self._uri = (
            "/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}".format(
                **self._solution
            )
        )

    def delete(self) -> bool:
        """
        Deletes the UserChannelInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the UserChannelInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> UserChannelInstance:
        """
        Fetch the UserChannelInstance


        :returns: The fetched UserChannelInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return UserChannelInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            user_sid=self._solution["user_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    async def fetch_async(self) -> UserChannelInstance:
        """
        Asynchronous coroutine to fetch the UserChannelInstance


        :returns: The fetched UserChannelInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return UserChannelInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            user_sid=self._solution["user_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    def update(
        self,
        notification_level: Union[
            "UserChannelInstance.NotificationLevel", object
        ] = values.unset,
        last_consumed_message_index: Union[int, object] = values.unset,
        last_consumption_timestamp: Union[datetime, object] = values.unset,
    ) -> UserChannelInstance:
        """
        Update the UserChannelInstance

        :param notification_level:
        :param last_consumed_message_index:
        :param last_consumption_timestamp:

        :returns: The updated UserChannelInstance
        """
        data = values.of(
            {
                "NotificationLevel": notification_level,
                "LastConsumedMessageIndex": last_consumed_message_index,
                "LastConsumptionTimestamp": serialize.iso8601_datetime(
                    last_consumption_timestamp
                ),
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return UserChannelInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            user_sid=self._solution["user_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    async def update_async(
        self,
        notification_level: Union[
            "UserChannelInstance.NotificationLevel", object
        ] = values.unset,
        last_consumed_message_index: Union[int, object] = values.unset,
        last_consumption_timestamp: Union[datetime, object] = values.unset,
    ) -> UserChannelInstance:
        """
        Asynchronous coroutine to update the UserChannelInstance

        :param notification_level:
        :param last_consumed_message_index:
        :param last_consumption_timestamp:

        :returns: The updated UserChannelInstance
        """
        data = values.of(
            {
                "NotificationLevel": notification_level,
                "LastConsumedMessageIndex": last_consumed_message_index,
                "LastConsumptionTimestamp": serialize.iso8601_datetime(
                    last_consumption_timestamp
                ),
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return UserChannelInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            user_sid=self._solution["user_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.IpMessaging.V2.UserChannelContext {}>".format(context)


class UserChannelPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> UserChannelInstance:
        """
        Build an instance of UserChannelInstance

        :param payload: Payload response from the API
        """
        return UserChannelInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            user_sid=self._solution["user_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.IpMessaging.V2.UserChannelPage>"


class UserChannelList(ListResource):

    def __init__(self, version: Version, service_sid: str, user_sid: str):
        """
        Initialize the UserChannelList

        :param version: Version that contains the resource
        :param service_sid:
        :param user_sid:

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "user_sid": user_sid,
        }
        self._uri = "/Services/{service_sid}/Users/{user_sid}/Channels".format(
            **self._solution
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[UserChannelInstance]:
        """
        Streams UserChannelInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[UserChannelInstance]:
        """
        Asynchronously streams UserChannelInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[UserChannelInstance]:
        """
        Lists UserChannelInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[UserChannelInstance]:
        """
        Asynchronously lists UserChannelInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> UserChannelPage:
        """
        Retrieve a single page of UserChannelInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of UserChannelInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return UserChannelPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> UserChannelPage:
        """
        Asynchronously retrieve a single page of UserChannelInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of UserChannelInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return UserChannelPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> UserChannelPage:
        """
        Retrieve a specific page of UserChannelInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of UserChannelInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return UserChannelPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> UserChannelPage:
        """
        Asynchronously retrieve a specific page of UserChannelInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of UserChannelInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return UserChannelPage(self._version, response, self._solution)

    def get(self, channel_sid: str) -> UserChannelContext:
        """
        Constructs a UserChannelContext

        :param channel_sid:
        """
        return UserChannelContext(
            self._version,
            service_sid=self._solution["service_sid"],
            user_sid=self._solution["user_sid"],
            channel_sid=channel_sid,
        )

    def __call__(self, channel_sid: str) -> UserChannelContext:
        """
        Constructs a UserChannelContext

        :param channel_sid:
        """
        return UserChannelContext(
            self._version,
            service_sid=self._solution["service_sid"],
            user_sid=self._solution["user_sid"],
            channel_sid=channel_sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.IpMessaging.V2.UserChannelList>"
