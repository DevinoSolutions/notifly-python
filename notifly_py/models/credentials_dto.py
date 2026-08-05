from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credentials_dto_tls_options import CredentialsDtoTlsOptions


T = TypeVar("T", bound="CredentialsDto")


@_attrs_define
class CredentialsDto:
    """
    Attributes:
        api_key (str | Unset):
        user (str | Unset):
        secret_key (str | Unset):
        domain (str | Unset):
        password (str | Unset):
        host (str | Unset):
        port (str | Unset):
        secure (bool | Unset):
        region (str | Unset):
        account_sid (str | Unset):
        message_profile_id (str | Unset):
        token (str | Unset):
        from_ (str | Unset):
        sender_name (str | Unset):
        project_name (str | Unset):
        application_id (str | Unset):
        client_id (str | Unset):
        require_tls (bool | Unset):
        ignore_tls (bool | Unset):
        tls_options (CredentialsDtoTlsOptions | Unset):
        base_url (str | Unset):
        webhook_url (str | Unset):
        redirect_url (str | Unset):
        hmac (bool | Unset):
        service_account (str | Unset):
        ip_pool_name (str | Unset):
        api_key_request_header (str | Unset):
        secret_key_request_header (str | Unset):
        id_path (str | Unset):
        date_path (str | Unset):
        api_token (str | Unset):
        authenticate_by_token (bool | Unset):
        authentication_token_key (str | Unset):
        instance_id (str | Unset):
        alert_uid (str | Unset):
        title (str | Unset):
        image_url (str | Unset):
        state (str | Unset):
        external_link (str | Unset):
        channel_id (str | Unset):
        phone_number_identification (str | Unset):
        access_key (str | Unset):
        app_sid (str | Unset):
        sender_id (str | Unset):
        tenant_id (str | Unset):
        app_io_base_url (str | Unset):
        signing_secret (str | Unset):
        outbound_integration_id (str | Unset):
        use_from_address_override (bool | Unset):
        from_address_override (str | Unset):
        email_slug_prefix (str | Unset): Agent default shared inbox slug prefix used in
            `{emailSlugPrefix}-{agentId}@<shared-domain>`. Only meaningful on the NovuAgent email integration.
        external_environment_id (str | Unset): Claude Managed Agents: ID of the Anthropic environment tied to this
            integration. Hydrated by the API at integration provisioning time.
        external_vault_id (str | Unset): Claude Managed Agents: ID of the Anthropic vault (`vlt_…`) tied to this
            integration. Hydrated by the API at integration provisioning time and used to push OAuth-completed MCP
            credentials to the per-vault credentials API.
        external_workspace_id (str | Unset): Claude Managed Agents: id of the Anthropic workspace used in console deep
            links. Defaults to `'default'` (the Default Workspace). Set this when the API key is scoped to a custom
            workspace (e.g. `wrkspc_…`).
    """

    api_key: str | Unset = UNSET
    user: str | Unset = UNSET
    secret_key: str | Unset = UNSET
    domain: str | Unset = UNSET
    password: str | Unset = UNSET
    host: str | Unset = UNSET
    port: str | Unset = UNSET
    secure: bool | Unset = UNSET
    region: str | Unset = UNSET
    account_sid: str | Unset = UNSET
    message_profile_id: str | Unset = UNSET
    token: str | Unset = UNSET
    from_: str | Unset = UNSET
    sender_name: str | Unset = UNSET
    project_name: str | Unset = UNSET
    application_id: str | Unset = UNSET
    client_id: str | Unset = UNSET
    require_tls: bool | Unset = UNSET
    ignore_tls: bool | Unset = UNSET
    tls_options: CredentialsDtoTlsOptions | Unset = UNSET
    base_url: str | Unset = UNSET
    webhook_url: str | Unset = UNSET
    redirect_url: str | Unset = UNSET
    hmac: bool | Unset = UNSET
    service_account: str | Unset = UNSET
    ip_pool_name: str | Unset = UNSET
    api_key_request_header: str | Unset = UNSET
    secret_key_request_header: str | Unset = UNSET
    id_path: str | Unset = UNSET
    date_path: str | Unset = UNSET
    api_token: str | Unset = UNSET
    authenticate_by_token: bool | Unset = UNSET
    authentication_token_key: str | Unset = UNSET
    instance_id: str | Unset = UNSET
    alert_uid: str | Unset = UNSET
    title: str | Unset = UNSET
    image_url: str | Unset = UNSET
    state: str | Unset = UNSET
    external_link: str | Unset = UNSET
    channel_id: str | Unset = UNSET
    phone_number_identification: str | Unset = UNSET
    access_key: str | Unset = UNSET
    app_sid: str | Unset = UNSET
    sender_id: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    app_io_base_url: str | Unset = UNSET
    signing_secret: str | Unset = UNSET
    outbound_integration_id: str | Unset = UNSET
    use_from_address_override: bool | Unset = UNSET
    from_address_override: str | Unset = UNSET
    email_slug_prefix: str | Unset = UNSET
    external_environment_id: str | Unset = UNSET
    external_vault_id: str | Unset = UNSET
    external_workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        user = self.user

        secret_key = self.secret_key

        domain = self.domain

        password = self.password

        host = self.host

        port = self.port

        secure = self.secure

        region = self.region

        account_sid = self.account_sid

        message_profile_id = self.message_profile_id

        token = self.token

        from_ = self.from_

        sender_name = self.sender_name

        project_name = self.project_name

        application_id = self.application_id

        client_id = self.client_id

        require_tls = self.require_tls

        ignore_tls = self.ignore_tls

        tls_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tls_options, Unset):
            tls_options = self.tls_options.to_dict()

        base_url = self.base_url

        webhook_url = self.webhook_url

        redirect_url = self.redirect_url

        hmac = self.hmac

        service_account = self.service_account

        ip_pool_name = self.ip_pool_name

        api_key_request_header = self.api_key_request_header

        secret_key_request_header = self.secret_key_request_header

        id_path = self.id_path

        date_path = self.date_path

        api_token = self.api_token

        authenticate_by_token = self.authenticate_by_token

        authentication_token_key = self.authentication_token_key

        instance_id = self.instance_id

        alert_uid = self.alert_uid

        title = self.title

        image_url = self.image_url

        state = self.state

        external_link = self.external_link

        channel_id = self.channel_id

        phone_number_identification = self.phone_number_identification

        access_key = self.access_key

        app_sid = self.app_sid

        sender_id = self.sender_id

        tenant_id = self.tenant_id

        app_io_base_url = self.app_io_base_url

        signing_secret = self.signing_secret

        outbound_integration_id = self.outbound_integration_id

        use_from_address_override = self.use_from_address_override

        from_address_override = self.from_address_override

        email_slug_prefix = self.email_slug_prefix

        external_environment_id = self.external_environment_id

        external_vault_id = self.external_vault_id

        external_workspace_id = self.external_workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if user is not UNSET:
            field_dict["user"] = user
        if secret_key is not UNSET:
            field_dict["secretKey"] = secret_key
        if domain is not UNSET:
            field_dict["domain"] = domain
        if password is not UNSET:
            field_dict["password"] = password
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if secure is not UNSET:
            field_dict["secure"] = secure
        if region is not UNSET:
            field_dict["region"] = region
        if account_sid is not UNSET:
            field_dict["accountSid"] = account_sid
        if message_profile_id is not UNSET:
            field_dict["messageProfileId"] = message_profile_id
        if token is not UNSET:
            field_dict["token"] = token
        if from_ is not UNSET:
            field_dict["from"] = from_
        if sender_name is not UNSET:
            field_dict["senderName"] = sender_name
        if project_name is not UNSET:
            field_dict["projectName"] = project_name
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if require_tls is not UNSET:
            field_dict["requireTls"] = require_tls
        if ignore_tls is not UNSET:
            field_dict["ignoreTls"] = ignore_tls
        if tls_options is not UNSET:
            field_dict["tlsOptions"] = tls_options
        if base_url is not UNSET:
            field_dict["baseUrl"] = base_url
        if webhook_url is not UNSET:
            field_dict["webhookUrl"] = webhook_url
        if redirect_url is not UNSET:
            field_dict["redirectUrl"] = redirect_url
        if hmac is not UNSET:
            field_dict["hmac"] = hmac
        if service_account is not UNSET:
            field_dict["serviceAccount"] = service_account
        if ip_pool_name is not UNSET:
            field_dict["ipPoolName"] = ip_pool_name
        if api_key_request_header is not UNSET:
            field_dict["apiKeyRequestHeader"] = api_key_request_header
        if secret_key_request_header is not UNSET:
            field_dict["secretKeyRequestHeader"] = secret_key_request_header
        if id_path is not UNSET:
            field_dict["idPath"] = id_path
        if date_path is not UNSET:
            field_dict["datePath"] = date_path
        if api_token is not UNSET:
            field_dict["apiToken"] = api_token
        if authenticate_by_token is not UNSET:
            field_dict["authenticateByToken"] = authenticate_by_token
        if authentication_token_key is not UNSET:
            field_dict["authenticationTokenKey"] = authentication_token_key
        if instance_id is not UNSET:
            field_dict["instanceId"] = instance_id
        if alert_uid is not UNSET:
            field_dict["alertUid"] = alert_uid
        if title is not UNSET:
            field_dict["title"] = title
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if state is not UNSET:
            field_dict["state"] = state
        if external_link is not UNSET:
            field_dict["externalLink"] = external_link
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if phone_number_identification is not UNSET:
            field_dict["phoneNumberIdentification"] = phone_number_identification
        if access_key is not UNSET:
            field_dict["accessKey"] = access_key
        if app_sid is not UNSET:
            field_dict["appSid"] = app_sid
        if sender_id is not UNSET:
            field_dict["senderId"] = sender_id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if app_io_base_url is not UNSET:
            field_dict["AppIOBaseUrl"] = app_io_base_url
        if signing_secret is not UNSET:
            field_dict["signingSecret"] = signing_secret
        if outbound_integration_id is not UNSET:
            field_dict["outboundIntegrationId"] = outbound_integration_id
        if use_from_address_override is not UNSET:
            field_dict["useFromAddressOverride"] = use_from_address_override
        if from_address_override is not UNSET:
            field_dict["fromAddressOverride"] = from_address_override
        if email_slug_prefix is not UNSET:
            field_dict["emailSlugPrefix"] = email_slug_prefix
        if external_environment_id is not UNSET:
            field_dict["externalEnvironmentId"] = external_environment_id
        if external_vault_id is not UNSET:
            field_dict["externalVaultId"] = external_vault_id
        if external_workspace_id is not UNSET:
            field_dict["externalWorkspaceId"] = external_workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credentials_dto_tls_options import CredentialsDtoTlsOptions

        d = dict(src_dict)
        api_key = d.pop("apiKey", UNSET)

        user = d.pop("user", UNSET)

        secret_key = d.pop("secretKey", UNSET)

        domain = d.pop("domain", UNSET)

        password = d.pop("password", UNSET)

        host = d.pop("host", UNSET)

        port = d.pop("port", UNSET)

        secure = d.pop("secure", UNSET)

        region = d.pop("region", UNSET)

        account_sid = d.pop("accountSid", UNSET)

        message_profile_id = d.pop("messageProfileId", UNSET)

        token = d.pop("token", UNSET)

        from_ = d.pop("from", UNSET)

        sender_name = d.pop("senderName", UNSET)

        project_name = d.pop("projectName", UNSET)

        application_id = d.pop("applicationId", UNSET)

        client_id = d.pop("clientId", UNSET)

        require_tls = d.pop("requireTls", UNSET)

        ignore_tls = d.pop("ignoreTls", UNSET)

        _tls_options = d.pop("tlsOptions", UNSET)
        tls_options: CredentialsDtoTlsOptions | Unset
        if isinstance(_tls_options, Unset):
            tls_options = UNSET
        else:
            tls_options = CredentialsDtoTlsOptions.from_dict(_tls_options)

        base_url = d.pop("baseUrl", UNSET)

        webhook_url = d.pop("webhookUrl", UNSET)

        redirect_url = d.pop("redirectUrl", UNSET)

        hmac = d.pop("hmac", UNSET)

        service_account = d.pop("serviceAccount", UNSET)

        ip_pool_name = d.pop("ipPoolName", UNSET)

        api_key_request_header = d.pop("apiKeyRequestHeader", UNSET)

        secret_key_request_header = d.pop("secretKeyRequestHeader", UNSET)

        id_path = d.pop("idPath", UNSET)

        date_path = d.pop("datePath", UNSET)

        api_token = d.pop("apiToken", UNSET)

        authenticate_by_token = d.pop("authenticateByToken", UNSET)

        authentication_token_key = d.pop("authenticationTokenKey", UNSET)

        instance_id = d.pop("instanceId", UNSET)

        alert_uid = d.pop("alertUid", UNSET)

        title = d.pop("title", UNSET)

        image_url = d.pop("imageUrl", UNSET)

        state = d.pop("state", UNSET)

        external_link = d.pop("externalLink", UNSET)

        channel_id = d.pop("channelId", UNSET)

        phone_number_identification = d.pop("phoneNumberIdentification", UNSET)

        access_key = d.pop("accessKey", UNSET)

        app_sid = d.pop("appSid", UNSET)

        sender_id = d.pop("senderId", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        app_io_base_url = d.pop("AppIOBaseUrl", UNSET)

        signing_secret = d.pop("signingSecret", UNSET)

        outbound_integration_id = d.pop("outboundIntegrationId", UNSET)

        use_from_address_override = d.pop("useFromAddressOverride", UNSET)

        from_address_override = d.pop("fromAddressOverride", UNSET)

        email_slug_prefix = d.pop("emailSlugPrefix", UNSET)

        external_environment_id = d.pop("externalEnvironmentId", UNSET)

        external_vault_id = d.pop("externalVaultId", UNSET)

        external_workspace_id = d.pop("externalWorkspaceId", UNSET)

        credentials_dto = cls(
            api_key=api_key,
            user=user,
            secret_key=secret_key,
            domain=domain,
            password=password,
            host=host,
            port=port,
            secure=secure,
            region=region,
            account_sid=account_sid,
            message_profile_id=message_profile_id,
            token=token,
            from_=from_,
            sender_name=sender_name,
            project_name=project_name,
            application_id=application_id,
            client_id=client_id,
            require_tls=require_tls,
            ignore_tls=ignore_tls,
            tls_options=tls_options,
            base_url=base_url,
            webhook_url=webhook_url,
            redirect_url=redirect_url,
            hmac=hmac,
            service_account=service_account,
            ip_pool_name=ip_pool_name,
            api_key_request_header=api_key_request_header,
            secret_key_request_header=secret_key_request_header,
            id_path=id_path,
            date_path=date_path,
            api_token=api_token,
            authenticate_by_token=authenticate_by_token,
            authentication_token_key=authentication_token_key,
            instance_id=instance_id,
            alert_uid=alert_uid,
            title=title,
            image_url=image_url,
            state=state,
            external_link=external_link,
            channel_id=channel_id,
            phone_number_identification=phone_number_identification,
            access_key=access_key,
            app_sid=app_sid,
            sender_id=sender_id,
            tenant_id=tenant_id,
            app_io_base_url=app_io_base_url,
            signing_secret=signing_secret,
            outbound_integration_id=outbound_integration_id,
            use_from_address_override=use_from_address_override,
            from_address_override=from_address_override,
            email_slug_prefix=email_slug_prefix,
            external_environment_id=external_environment_id,
            external_vault_id=external_vault_id,
            external_workspace_id=external_workspace_id,
        )

        credentials_dto.additional_properties = d
        return credentials_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
