class Player:
    def __init__(self, playerName, playerPosition):
        self.playerName = playerName
        self.playerPosition = playerPosition

    def __str__(self):
        return f"{self.playerName} - {self.playerPosition}"


class NFLTeam:
    def __init__(self, teamName, playerList):
        self.teamName = teamName
        self.playerList = playerList

    def display_team(self):
        print(f"Team: {self.teamName}")
        print("Roster:")
        for player in self.playerList:
            print(f" - {player}")


# 1. Create the 4 Player objects
player1 = Player("Joe Montana", "QB")
player2 = Player("Barry Sanders", "RB")
player3 = Player("Jerry Rice", "WR")
player4 = Player("Graham Gano", "K")

# 2. Add players to a list
playerList = [player1, player2, player3, player4]

# 3. Create the NFLTeam object with a team name and the list of players
my_team = NFLTeam("All-Star Legends", playerList)

# 4. Output the team name and all its players to the console
my_team.display_team()
