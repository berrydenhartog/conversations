"""Feature flag objects"""

from enum import StrEnum

from django.utils.text import slugify

from pydantic import BaseModel, ConfigDict


class FeatureToggle(StrEnum):
    """
    Feature toggle states.

    DISABLED: The feature is fully disabled (ie for all users).
    DYNAMIC: The feature can be enabled or disabled based on service like Posthog.
    ENABLED: The feature is fully enabled (ie for all users).
    """

    DISABLED = "disabled"
    DYNAMIC = "dynamic"
    ENABLED = "enabled"

    @property
    def is_always_enabled(self) -> bool:
        """Whether the feature is always enabled"""
        return self.value == self.ENABLED

    @property
    def is_always_disabled(self) -> bool:
        """Whether the feature is always disabled"""
        return self.value == self.DISABLED


class FeatureFlags(BaseModel):
    """Feature flags container."""

    model_config = ConfigDict(
        extra="forbid",
        alias_generator=lambda x: slugify(x).replace("_", "-"),
        populate_by_name=True,
    )

    # features
    web_search: FeatureToggle = FeatureToggle.DISABLED
    document_upload: FeatureToggle = FeatureToggle.DISABLED
