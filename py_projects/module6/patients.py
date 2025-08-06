class Patient:
    def __init__(self, first_name, middle_name, last_name,
                 address, city, state, zip_code,
                 phone_number, emergency_contact_name, emergency_contact_phone):
        """
        Initializes a new Patient object.
        """
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__phone_number = phone_number
        self.__emergency_contact_name = emergency_contact_name
        self.__emergency_contact_phone = emergency_contact_phone

    # --- Accessor (Getter) Methods ---
    def get_first_name(self):
        return self.__first_name

    def get_middle_name(self):
        return self.__middle_name

    def get_last_name(self):
        return self.__last_name

    def get_full_name(self):
        return f"{self.__first_name} {self.__middle_name} {self.__last_name}".replace("  ", " ").strip()

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip_code(self):
        return self.__zip_code

    def get_full_address(self):
        return f"{self.__address}, {self.__city}, {self.__state} {self.__zip_code}"

    def get_phone_number(self):
        return self.__phone_number

    def get_emergency_contact_name(self):
        return self.__emergency_contact_name

    def get_emergency_contact_phone(self):
        return self.__emergency_contact_phone

    # --- Mutator (Setter) Methods ---
    def set_first_name(self, name):
        self.__first_name = name

    def set_middle_name(self, name):
        self.__middle_name = name

    def set_last_name(self, name):
        self.__last_name = name

    def set_address(self, address):
        self.__address = address

    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
        self.__state = state

    def set_zip_code(self, zip_code):
        self.__zip_code = zip_code

    def set_phone_number(self, phone):
        self.__phone_number = phone

    def set_emergency_contact_name(self, name):
        self.__emergency_contact_name = name

    def set_emergency_contact_phone(self, phone):
        self.__emergency_contact_phone = phone