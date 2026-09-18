from FileBasedConfigurationManager import FileBasedConfigurationManager


def main():

    # TODO 1:

    config1 = FileBasedConfigurationManager().get_instance()
    
    
    config1.set_configuration("app.name", "myapplication")
    config1.set_configuration("max.connections", "100")
    print(config1.get_configuration("app.name"))
    print(config1.get_configuration("max.connections", int))
    # Get the first Configuration Manager instance.
    
    config2 = FileBasedConfigurationManager().get_instance()
    config2.set_configuration("app.name", "amazon")
    print(config2.get_configuration("app.name"))

   
    # TODO 2:
    # Store configuration values.
    #
    config1.set_configuration("app.name", "MyApplication")
    config1.set_configuration("max.connections", 100)
    config1.set_configuration("timeout", 30.5)

    # TODO 3:
    # Read the configuration values.
    #
    # print("App Name:", ...)
    # print("Max Connections:", ...)
    # print("Timeout:", ...)

    # TODO 4:
    # Get the Singleton instance again.
    

    # TODO 5:
    # Verify that config1 and config2 are the same object.
    #
    # print("Same instance:", ...)

    print(config1 is config2)
    print(id(config1))
    print(id(config2))

    # TODO 6:
    # Remove the timeout configuration.
    #
    # config1.remove_configuration("timeout")
    # print("Timeout after removal:", ...)

    # TODO 7:
    # Clear all configurations.
    #
    # config1.clear()
    # print("App Name after clear:", ...)

    # TODO 8:
    # Reset the Singleton.
    #
    # FileBasedConfigurationManager.reset_instance()

    # TODO 9:
    # Get the Configuration Manager again.
    config3 = None

    # TODO 10:
    # Verify that config1 and config3 are different objects.
    #
    # print("New instance after reset:", ...)


if __name__ == "__main__":
    main()