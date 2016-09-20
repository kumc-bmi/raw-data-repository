"""The main API definition file.

This defines the APIs and the handlers for the APIs.
"""

import endpoints
import participants_api
import metrics_api


api = endpoints.api_server([participants_api.ParticipantApi,
                            metrics_api.MetricsApi])
