class TythonExceptions(Exception):
    
    def __init__(self, meta_info: object):
        """_summary_
        Tython exception object will add on the request ID and Caller type to Tython Exceptions. 

        Args:
            resource (object): Resource that is currently being evaluated by Tython
        """

        try:
            self.request_id = meta_info.request_id
            self.validation_type = meta_info.caller

        except Exception as e:
            
            self.request_id = "Request ID Not Available"
            self.validation_type = "Caller Type Not Available"

    def __str__(self):
        return f'{self.error_code}: {self.message}'


class ViolationException(TythonExceptions):

    def __init__(self, exception: Exception):
        """_summary_
        
        Tython exception object meant to handle generic Exceptions and ConfigIdExceptions that occurs during violation object creation.

        Args:
            exception (Exception): e object generated by an Exception
        """

        try:
            # Build violation object based on configID Exception
            self.error_message = exception.error_message
            self.error_code = exception.error_code
            self.request_id = exception.request_id
            self.exception_type = exception.exception_type
            
        except Exception as e:

            self.error_code = "500"
            self.error_message = f"Could not access property {exception} on resource"
            self.exception_type = exception
            super().__init__(exception)


class ConfigIdException(TythonExceptions):

    def __init__(self, resource: object, config_name: str = ""):
        """_summary_
        Tython Exception object for handling errors related to config id generation. This exception will feed into ViolationException when raised.

        Args:
            resource (object): Resource that is currently being evaluated by Tython
            config_name (str): Name of the config that could not be generated
        """
        self.error_code = "505"
        self.error_message = f"Unable to generate config_id for resource with config name: {config_name}"
        self.exception_type = "Unable to generate config id"
        
        super().__init__(resource)


class GrpcPopulationException(TythonExceptions):

    def __init__(self, meta_info: object, exception: Exception):
        """_summary_
        Tython Exception object for handling errors related to GRPC object creation. Currently it covers all GRPC objects that the runner generates.

        Args:
            resource (object): Resource that is currently being evaluated by Tython
            exception (Exception): e object generated by an Exception
        """
        
        self.error_code = "510"
        self.exception_type = exception
        self.error_message = f"Unable to populate GRPC Violation, Design_Gap, or Exception Object due to {exception} on resource {meta_info.resource_type}"

        super().__init__(meta_info)


class UnpackingException(TythonExceptions):

    def __init__(self, type_url: str = ""):
        """_summary_
        Tython Exception object for handling errors related to the unpacking of a resource based on the type url.
        
        Args:
            type_url (string): Type url string that is attached to the resource that is sent for validation
        """
        self.error_code = "515"
        self.error_message = f"Could Not Unpack Resource Due To No Matching Resource Found For Type Url {type_url}"
        self.exception_type = "Error In Unpacking Resource"
        self.request_id = "Not Available. Unable To Access Resource Info"
        self.validation_type = "Not Available. Unable To Access Resource Info"


class MessageException(TythonExceptions):
    
    def __init__(self):
        """_summary_
        Tython Exception object for handling errors related to the initial grpc message the runner receives.
        """
        self.error_code = "520"
        self.error_message = f"Grpc Message From Validation Broker Was Undefined Or None."
        self.exception_type = "Grpc Message Could Not Be Interpreted"
        self.request_id = "Not Available. Unable To Access Resource Info"
        self.validation_type = "Not Available. Unable To Access Resource Info"


class BlueprintException(TythonExceptions):
    
    def __init__(self, meta: object):
        """_summary_
        Tython Exception object that handles errors related  to blueprint retrieval for validation

        Args:
            resource (object): Resource that is currently being evaluated by Tython
        """
        self.error_code = "525"
        self.error_message = f"Blueprint matching service could not find a validation blueprint for resource {meta.resource_type}"
        self.exception_type = "Validation Blueprint Could Not Be Found"

        super().__init__(meta)
