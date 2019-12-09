# -- coding: utf-8 --
# Created by IronMan Development Team
# Copyright 2019 IronMan Inc. All rights reserved.
#


class AuthenticationApi:

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent IronMan object.
        """
        self._lr_object = lr_object


    def resend_email_verification(self, email):
        """This API resends the verification email to the user.
        
        Args:
            email: user's email
            email_template: Email template name
            verification_url: Email verification url
		
        Returns:
            Response containing Definition of Complete Validation data
        17.3
        """

        if(self._lr_object.is_null_or_whitespace(email)):
            raise Exception(self._lr_object.get_validation_message("email"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        body_parameters = {}
        body_parameters["email"] = email

        resource_path = "/v1/email/resendverify"
        return self._lr_object.execute("PUT", resource_path, query_parameters, body_parameters)
