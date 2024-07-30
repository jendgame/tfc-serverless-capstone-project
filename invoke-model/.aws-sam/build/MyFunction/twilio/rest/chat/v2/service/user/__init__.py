r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Chat
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.chat.v2.service.user.user_binding import UserBindingList
from twilio.rest.chat.v2.service.user.user_channel import UserChannelList


class UserInstance(InstanceResource):

    class WebhookEnabledType(object):
        TRUE = "true"
        FALSE = "false"

    """
    :ivar sid: The unique string that we created to identify the User resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the User resource.
    :ivar service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) the User resource is associated with.
    :ivar attributes: The JSON string that stores application-specific data. If attributes have not been set, `{}` is returned.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar role_sid: The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-resource) assigned to the user.
    :ivar identity: The application-defined string that uniquely identifies the resource's User within the [Service](https://www.twilio.com/docs/chat/rest/service-resource). This value is often a username or an email address, and is case-sensitive. See [access tokens](https://www.twilio.com/docs/chat/create-tokens) for more info.
    :ivar is_online: Whether the User is actively connected to the Service instance and online. This value is only returned by Fetch actions that return a single resource and `null` is always returned by a Read action. This value is `null` if the Service's `reachability_enabled` is `false`, if the User has never been online for the Service instance, even if the Service's `reachability_enabled` is `true`.
    :ivar is_notifiable: Whether the User has a potentially valid Push Notification registration (APN or GCM) for the Service instance. If at least one registration exists, `true`; otherwise `false`. This value is only returned by Fetch actions that return a single resource and `null` is always returned by a Read action. This value is `null` if the Service's `reachability_enabled` is `false`, and if the User has never had a notification registration, even if the Service's `reachability_enabled` is `true`.
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar joined_channels_count: The number of Channels the User is a Member of.
    :ivar links: The absolute URLs of the [Channel](https://www.twilio.com/docs/chat/channels) and [Binding](https://www.twilio.com/docs/chat/rest/binding-resource) resources related to the user.
    :ivar url: The absolute URL of the User resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.attributes: Optional[str] = payload.get("attributes")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.role_sid: Optional[str] = payload.get("role_sid")
        self.identity: Optional[str] = payload.get("identity")
        self.is_online: Optional[bool] = payload.get("is_online")
        self.is_notifiable: Optional[bool] = payload.get("is_notifiable")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.joined_channels_count: Optional[int] = deserialize.integer(
            payload.get("joined_channels_count")
        )
        self.links: Optional[Dict[str, object]] = payload.get("links")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "service_sid": service_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[UserContext] = None

    @property
    def _proxy(self) -> "UserContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: UserContext for this UserInstance
        """
        if self._context is None:
            self._context = UserContext(
                self._version,
                service_sid=self._solution["service_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the UserInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the UserInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "UserInstance":
        """
        Fetch the UserInstance


        :returns: The fetched UserInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "UserInstance":
        """
        Asynchronous coroutine to fetch the UserInstance


        :returns: The fetched UserInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        x_twilio_webhook_enabled: Union[
            "UserInstance.WebhookEnabledType", object
        ] = values.unset,
        role_sid: Union[str, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
    ) -> "UserInstance":
        """
        Update the UserInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param role_sid: The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-resource) to assign to the User.
        :param attributes: A valid JSON string that contains application-specific data.
        :param friendly_name: A descriptive string that you create to describe the resource. It is often used for display purposes.

        :returns: The updated UserInstance
        """
        return self._proxy.update(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            role_sid=role_sid,
            attributes=attributes,
            friendly_name=friendly_name,
        )

    async def update_async(
        self,
        x_twilio_webhook_enabled: Union[
            "UserInstance.WebhookEnabledType", object
        ] = values.unset,
        role_sid: Union[str, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
    ) -> "UserInstance":
        """
        Asynchronous coroutine to update the UserInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param role_sid: The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-resource) to assign to the User.
        :param attributes: A valid JSON string that contains application-specific data.
        :param friendly_name: A descriptive string that you create to describe the resource. It is often used for display purposes.

        :returns: The updated UserInstance
        """
        return await self._proxy.update_async(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            role_sid=role_sid,
            attributes=attributes,
            friendly_name=friendly_name,
        )

    @property
    def user_bindings(self) -> UserBindingList:
        """
        Access the user_bindings
        """
        return self._proxy.user_bindings

    @property
    def user_channels(self) -> UserChannelList:
        """
        Access the user_channels
        """
        return self._proxy.user_channels

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Chat.V2.UserInstance {}>".format(context)


class UserContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the UserContext

        :param version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to update the User resource in.
        :param sid: The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/Users/{sid}".format(**self._solution)

        self._user_bindings: Optional[UserBindingList] = None
        self._user_channels: Optional[UserChannelList] = None

    def delete(self) -> bool:
        """
        Deletes the UserInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the UserInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> UserInstance:
        """
        Fetch the UserInstance


        :returns: The fetched UserInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return UserInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> UserInstance:
        """
        Asynchronous coroutine to fetch the UserInstance


        :returns: The fetched UserInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return UserInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        x_twilio_webhook_enabled: Union[
            "UserInstance.WebhookEnabledType", object
        ] = values.unset,
        role_sid: Union[str, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
    ) -> UserInstance:
        """
        Update the UserInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param role_sid: The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-resource) to assign to the User.
        :param attributes: A valid JSON string that contains application-specific data.
        :param friendly_name: A descriptive string that you create to describe the resource. It is often used for display purposes.

        :returns: The updated UserInstance
        """
        data = values.of(
            {
                "RoleSid": role_sid,
                "Attributes": attributes,
                "FriendlyName": friendly_name,
            }
        )
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
            }
        )

        payload = self._version.update(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return UserInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        x_twilio_webhook_enabled: Union[
            "UserInstance.WebhookEnabledType", object
        ] = values.unset,
        role_sid: Union[str, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
    ) -> UserInstance:
        """
        Asynchronous coroutine to update the UserInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param role_sid: The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-resource) to assign to the User.
        :param attributes: A valid JSON string that contains application-specific data.
        :param friendly_name: A descriptive string that you create to describe the resource. It is often used for display purposes.

        :returns: The updated UserInstance
        """
        data = values.of(
            {
                "RoleSid": role_sid,
                "Attributes": attributes,
                "FriendlyName": friendly_name,
            }
        )
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
            }
        )

        payload = await self._version.update_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return UserInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    @property
    def user_bindings(self) -> UserBindingList:
        """
        Access the user_bindings
        """
        if self._user_bindings is None:
            self._user_bindings = UserBindingList(
                self._version,
                self._solution["service_sid"],
                self._solution["sid"],
            )
        return self._user_bindings

    @property
    def user_channels(self) -> UserChannelList:
        """
        Access the user_channels
        """
        if self._user_channels is None:
            self._user_channels = UserChannelList(
                self._version,
                self._solution["service_sid"],
                self._solution["sid"],
            )
        return self._user_channels

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Chat.V2.UserContext {}>".format(context)


class UserPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> UserInstance:
        """
        Build an instance of UserInstance

        :param payload: Payload response from the API
        """
        return UserInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Chat.V2.UserPage>"


class UserList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the UserList

        :param version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the User resources from.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/Users".format(**self._solution)

    def create(
        self,
        identity: str,
        x_twilio_webhook_enabled: Union[
            "UserInstance.WebhookEnabledType", object
        ] = values.unset,
        role_sid: Union[str, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
    ) -> UserInstance:
        """
        Create the UserInstance

        :param identity: The `identity` value that uniquely identifies the new resource's [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/chat/rest/service-resource). This value is often a username or email address. See the Identity documentation for more info.
        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param role_sid: The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-resource) to assign to the new User.
        :param attributes: A valid JSON string that contains application-specific data.
        :param friendly_name: A descriptive string that you create to describe the new resource. This value is often used for display purposes.

        :returns: The created UserInstance
        """

        data = values.of(
            {
                "Identity": identity,
                "RoleSid": role_sid,
                "Attributes": attributes,
                "FriendlyName": friendly_name,
            }
        )
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
                "Content-Type": "application/x-www-form-urlencoded",
            }
        )

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return UserInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    async def create_async(
        self,
        identity: str,
        x_twilio_webhook_enabled: Union[
            "UserInstance.WebhookEnabledType", object
        ] = values.unset,
        role_sid: Union[str, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
    ) -> UserInstance:
        """
        Asynchronously create the UserInstance

        :param identity: The `identity` value that uniquely identifies the new resource's [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/chat/rest/service-resource). This value is often a username or email address. See the Identity documentation for more info.
        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param role_sid: The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-resource) to assign to the new User.
        :param attributes: A valid JSON string that contains application-specific data.
        :param friendly_name: A descriptive string that you create to describe the new resource. This value is often used for display purposes.

        :returns: The created UserInstance
        """

        data = values.of(
            {
                "Identity": identity,
                "RoleSid": role_sid,
                "Attributes": attributes,
                "FriendlyName": friendly_name,
            }
        )
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
                "Content-Type": "application/x-www-form-urlencoded",
            }
        )

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return UserInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[UserInstance]:
        """
        Streams UserInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[UserInstance]:
        """
        Asynchronously streams UserInstance records from the API as a generator stream.
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
    ) -> List[UserInstance]:
        """
        Lists UserInstance records from the API as a list.
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
    ) -> List[UserInstance]:
        """
        Asynchronously lists UserInstance records from the API as a list.
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
    ) -> UserPage:
        """
        Retrieve a single page of UserInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of UserInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return UserPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> UserPage:
        """
        Asynchronously retrieve a single page of UserInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of UserInstance
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
        return UserPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> UserPage:
        """
        Retrieve a specific page of UserInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of UserInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return UserPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> UserPage:
        """
        Asynchronously retrieve a specific page of UserInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of UserInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return UserPage(self._version, response, self._solution)

    def get(self, sid: str) -> UserContext:
        """
        Constructs a UserContext

        :param sid: The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
        """
        return UserContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __call__(self, sid: str) -> UserContext:
        """
        Constructs a UserContext

        :param sid: The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
        """
        return UserContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Chat.V2.UserList>"