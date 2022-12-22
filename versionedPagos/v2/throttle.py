from rest_framework.throttling import UserRateThrottle

class v2RateThrottle(UserRateThrottle):
    scope = 'api_pagosv2'