class player:
    """
    :param - name
    :param - wins
    :param - loss
    :param - win/loss percentage

    """

    def __init__(self, name):
        self._name = str(name)
        self._wins = 0 # sets default value of wins to 0
        self._loss = 0 # sets default value of loss to 0

    @property
    def name(self):
        return self._name

    @property
    def wins(self):
        return self._wins

    @property
    def loss(self):
        return self._loss

    @name.setter
    def name(self, value):
        if value.isalpha():
            self._name = value
        else:
            print(ValueError)

    @wins.setter
    def wins(self, value):
        if value.isdigit():
            self._wins = value
        else:
            print(ValueError)

    @loss.setter
    def update_loss(self, value):
        if value.isdigit():
            self._loss = value
        else:
            print(ValueError)

    def update_wins(self, value):
        self._wins = value

    def update_loss(self, value):
        self._loss = value

    def display(self):
        return 'Name ' + self._name + ' Wins: ' + str(self._wins) + ' Losses: ' + str(self._loss)

    def __str__(self):
        return 'Player(name= '+self._name+', wins= '+str(self._wins)+', loss= '+str(self._loss)+')'

    def __repr__(self):
        return {'Name':self._name,'wins':self._wins,'loss':self._loss}
