#!/usr/bin/python


class IronManExceptions(Exception):

    def __init__(self):
        pass

    def __str__(self):
        return ""


class Exceptions:

    def __init__(self):
        pass

    class RequestsLibraryDated(IronManExceptions):

        def __init__(self, version):
            self.version = str(version)

        def __str__(self):
            return "IronMan needs at least requests 2.0, found: " \
                + self.version + "\nPlease upgrade to the latest version."

    class InvalidLibrary(IronManExceptions):
        """
        Raised on trying to change library to through _settings on invalid library argument.
        """

        def __init__(self, library):
            self.library = library

        def __str__(self):
            return "Invalid library string given. Got: " + str(self.library) + ". Valid cases: 'requests' or " + \
                "'urllib2'"


    class NoAPIKey(IronManExceptions):
        """
        Raised on construction of the IronMan object,
        if no API_KEY has been set for the class.
        """

        def __init__(self):
            pass

        def __str__(self):
            return "No API_KEY set. Please initialize a APP_KEY first.\n" \
                + "ie. IronMan.API_Key = \"Really_Application_Key\""

    class MissingJsonResponseParameter(IronManExceptions):
        """
        Raised if construction of namedtuple would fail
        because missing expected response from IronMan API.
        """

        def __init__(self, missing_parameter, raw=None):
            self.missing_parameter = missing_parameter
            self.raw = raw

        def __str__(self):
            exception_string = "Expected parameter from JSON response does not exist." + \
                " Expected: " + self.missing_parameter + " but was not in" + \
                " the dictionary."
            if self.raw:
                exception_string += " Instead, we got: " + str(self.raw)
                return exception_string

    class TokenExpired(IronManExceptions):
        """
        Raised if the request cannot be completed because the access token has expired.
        """

        def __init__(self, time):
            self.time = time

        def __str__(self):
            return "The request cannot be completed because the token has expired. " + \
                "The token expired on: " + self.time


    class UnknownJsonError(IronManExceptions):
        """
        Raised if cannot determine error number from Json
        """

        def __init__(self, result):
            self.result = result

        def __str__(self):
            return str(self.result)

    class APIKeyInvalid(IronManExceptions):
        """
        Raised if you entered your API wrong, or not at all.
        """

        def __init__(self):
            pass

        def __str__(self):
            return "The IronMan API Key is not valid, please double check your account."

    class InvalidRequestToken(IronManExceptions):
        """
        Raised if you your request token is invalid from the POST request.
        """

        def __init__(self):
            pass

        def __str__(self):
            return "The IronMan Request Token is invalid, please verify the authentication response."

    class RequestTokenExpired(IronManExceptions):
        """
        Raised if you your request token has expired from the POST request.
        """

        def __init__(self):
            pass

        def __str__(self):
            return "The IronMan Request Token has expired, please verify the authentication response."

    class InvalidAccessToken(IronManExceptions):
        """
        Raised if you access token is invalid.
        """

        def __init__(self):
            pass

        def __str__(self):
            return "The IronMan Access Token has expired, please get a new token from the IronMan API."

    class ParameterMissing(IronManExceptions):
        """
        Raised if a parameter in the GET or POST request is missing.
        """

        def __init__(self):
            pass

        def __str__(self):
            return "A parameter is missing in the request, please check all parameters in the API call."

    class ParameterNotFormatted(IronManExceptions):
        """
        Raised if a parameter in the GET or POST request is not formatted properly for the provider.
        """

        def __init__(self):
            pass

        def __str__(self):
            return "A parameter is not formatted well in the request, please check all the parameters in the API call."

    class EndPointNotSupported(IronManExceptions):
        """
        Raised if a the endpoint is not supported by the provider which correlates to the token.
        """

        def __init__(self):
            pass

        def __str__(self):
            return "The requested endpoint is not supported by the current ID provider, " + \
                "please check the API support page at http://www.IronMan.com/datapoints"
