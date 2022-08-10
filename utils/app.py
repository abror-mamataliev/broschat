def get_config(type: str) -> str:
    """
    Get the configuration file for the application.

    :param type: The type of the application.
    :return: The configuration file.
    """
    
    return type if type in ["dev", "test"] else "prod"
