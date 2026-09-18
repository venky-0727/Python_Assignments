from config_manager_task1 import ConfigManager


class FileBasedConfigurationManager(ConfigManager):

    # TODO:
    # Store the Singleton instance here.
    _instance = None

    def __new__(cls):
        # TODO:
        if (cls._instance is None) :
            cls._instance = super().__new__(cls)
        return cls._instance
    
    

        # Control object creation so that only one
        # FileBasedConfigurationManager object exists.
        
    
    def __init__(self):
        # TODO:

        # Initialize the parent class.
        # Be careful: __init__ can run more than once
        # when using a Singleton with __new__.
        if(hasattr(self, "_initialized")):
            return
        super().__init__()
        self._initialized = True
        

    @classmethod
    def get_instance(cls):
        # TODO:
        # Return the Singleton instance.
        return cls()
        

    @classmethod
    def reset_instance(cls):
        # TODO:
        # Reset the Singleton instance.
        cls._instance = None
        pass

    def get_configuration(self, key, value_type=None):
        # TODO:
        # 1. Get the value using key.
        # 2. If it does not exist, return None.
        # 3. If value_type is None, return the value.
        # 4. Otherwise convert it to the requested type.
        pass    
        val = self.properties.get(key)
        if value_type == None :
            return val
        else :
            val = value_type(val)
            return val



    def set_configuration(self, key, value):
        # TODO:

        self.properties[key] = value
        # Store the configuration.
        

    def remove_configuration(self, key):
        # TODO:
        # Remove the configuration if it exists.
        self.properties.pop(key, None)
        

    def clear(self):
        # TODO:
        # Remove all configurations.
        self.properties.clear()