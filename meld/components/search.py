from flask_meld.component import Component


class Search(Component):
    state = ""
    selected = 1

    ALL_STATES = (
        "Alabama",
        "Alaska",
        "Arizona",
        "Arkansas",
        "California",
        "Colorado",
        "Connecticut",
        "Delaware",
        "Florida",
        "Georgia",
        "Hawaii",
        "Idaho",
        "Illinois",
        "Indiana",
        "Iowa",
        "Kansas",
        "Kentucky",
        "Louisiana",
        "Maine",
        "Maryland",
        "Massachusetts",
        "Michigan",
        "Minnesota",
        "Mississippi",
        "Missouri",
        "Montana",
        "Nebraska",
        "Nevada",
        "New Hampshire",
        "New Jersey",
        "New Mexico",
        "New York",
        "North Carolina",
        "North Dakota",
        "Ohio",
        "Oklahoma",
        "Oregon",
        "Pennsylvania",
        "Rhode Island",
        "South Carolina",
        "South Dakota",
        "Tennessee",
        "Texas",
        "Utah",
        "Vermont",
        "Virginia",
        "Washington",
        "West Virginia",
        "Wisconsin",
        "Wyoming",
    )

    def clear_states(self):
        self.state = ""

    def select(self, value):
        self.state = str(value)

    def select_by_index(self, value):
        self.state = self.states[int(value)-1]

    def select_next(self):
        if self.selected < len(self.states):
            self.selected += 1

    def select_previous(self):
        if self.selected > 1:
            self.selected -= 1

    @property
    def states(self):
        if not self.state:
            return []

        filtered_states = [s for s in self.ALL_STATES if s.lower().startswith(self.state.lower())]
        return filtered_states
