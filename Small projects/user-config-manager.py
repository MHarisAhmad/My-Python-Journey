test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}

def add_setting(settings_dict,setting_tuple):
    key, value = setting_tuple
    key = key.lower()
    value = value.lower()
    if key in settings_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings_dict[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"
def update_setting(settings_dict,setting_tuple):
    key, value = setting_tuple
    key = key.lower()
    value = value.lower()
    if key in settings_dict:
        settings_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
def delete_setting(settings_dict,key):
    
    key = key.lower()
    if key in settings_dict:
        del settings_dict[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(settings_dict):
    if settings_dict == {}:
        return "No settings available."
    
    output = "Current User Settings:\n"
    
    # 3. Loop through the dictionary items
    for key, value in settings_dict.items():
        # Capitalize the key string, and add a newline (\n) at the end
        output += f"{key.capitalize()}: {value}\n"
        
    # 4. Return the final completed string
    return output

# Add this at the absolute bottom of your file to see output:
print(view_settings(test_settings))

# Try adding a setting
print(add_setting(test_settings, ('audio', 'surround')))

# View them again to see the change
print(view_settings(test_settings))