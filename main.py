import random
import pandas as pd


class HockeySimulation:
    def __init__(self, iterations):
        self.iterations = iterations
        self.league_average = 3.18
        self.home_team = "New Jersey Devils"
        self.away_team = "New York Rangers"
        self.home_wins = 0
        self.away_wins = 0
        self.home_losses = 0
        self.away_losses = 0
        self.home_OTL = 0
        self.away_OTL = 0
        self.home_score_total = 0
        self.away_score_total = 0
        self.games = []

    def run_simulation(self):
        for _ in range(self.iterations):
            game_result, box_score = self.simulate_game()
            self.games.append(game_result)
            self.print_box_score(box_score)

        self.print_results()

    def simulate_game(self):
        home_score_iteration = 0
        away_score_iteration = 0
        for _ in range(self.iterations):
            print("Game Start: NJ Devils vs. NY Rangers")
            period = 0
            home_score_total_iteration = 0
            away_score_total_iteration = 0
            ot = 0
            game_period = ['Period 1', 'Period 2', 'Period 3']
            NJD = [0, 0, 0]  # Scores for each period
            away_table = [0, 0, 0]

            while period < 3:

                period_count = 0
                total_time = 1200
                period = period + 1
                while period_count <= 1199:
                    period_count += 1
                    total_time -= 1
                    scoring_chance_modifier = random.randint(1, 1000)
                    if (((period_count * 3.18) % scoring_chance_modifier) * 10 < 5.5):
                        chance = random.randint(1, 144)
                        if chance <= 72:
                            if chance < 37:
                                NJD[period - 1] += 1
                                home_score_total_iteration += 1
                                time_string = f"{total_time // 60}:{total_time % 60:02}"
                                print(f"{self.home_team} score! Period: {period}, Time: {time_string}")
                                print(f"Home: {home_score_total_iteration} Away: {away_score_total_iteration}")
                            else:
                                NJD[period - 1] += 0
                        else:
                            if chance > 108:
                                away_table[period - 1] += 1
                                away_score_total_iteration += 1
                                time_string = f"{total_time // 60}:{total_time % 60:02}"
                                print(f"{self.away_team} score! Period: {period}, Time: {time_string}")
                                print(f"Home: {home_score_total_iteration} Away: {away_score_total_iteration}")
                            else:
                                away_table[period - 1] += 0

            if (home_score_total_iteration == away_score_total_iteration):

                period_count = 0

                while (period == 3 and period_count <= 299):
                    print("Overtime Begins!")
                    game_period.append(f"OT{(period + 1) - period}")
                    ot = 1
                    total_time = 300
                    period = period + 1
                    score_column = [0]
                    NJD.extend(score_column)
                    away_table.extend(score_column)
                    while period_count <= 299:
                        if home_score_total_iteration != away_score_total_iteration:
                            print("Overtime Ends!")
                            break
                        period_count += 1
                        total_time -= 1
                        scoring_chance_modifier = random.randint(1, 1000)
                        if period_count % scoring_chance_modifier < 0.005:
                            chance = random.randint(1, 144)
                            if chance <= 72:
                                if chance < 37:
                                    NJD[period - 1] += 1
                                    home_score_total_iteration += 1
                                    time_string = f"{total_time // 60}:{total_time % 60:02}"
                                    print(f"{self.home_team} scores! Period: {period}, Time: {time_string}")
                                    print(f"Home: {home_score_total_iteration} Away: {away_score_total_iteration}")
                                else:
                                    NJD[period - 1] += 0
                            else:
                                if chance >= 108:
                                    away_table[period - 1] += 1
                                    away_score_total_iteration += 1
                                    time_string = f"{total_time // 60}:{total_time % 60:02}"
                                    print(f"{self.away_team} scores! Period: {period}, Time: {time_string}")
                                    print(f"Home: {home_score_total_iteration} Away: {away_score_total_iteration}")
                                else:
                                    away_table[period - 1] += 0
                else:
                    print("A shootout will decide the game!")
                    score_column = [0]
                    NJD.extend(score_column)
                    away_table.extend(score_column)
                    game_period.append("SO")
                    period_count = 0
                    period = period + 1
                    scoring_chance_modifier = random.randint(1, 2)
                    if (scoring_chance_modifier == 1):
                        NJD[period - 1] += 1
                    else:
                        away_table[period - 1] += 1



            self.home_score_total += home_score_total_iteration
            self.away_score_total += away_score_total_iteration

            if (home_score_total_iteration > away_score_total_iteration):
                self.home_wins += 1
                if (ot == 0):
                    self.away_losses += 1
                else:
                    self.away_OTL += 1
            else:
                self.away_wins += 1
                if (ot == 0):
                    self.home_losses += 1
                else:
                    self.home_OTL += 1

            game_result = {
                'home_team': self.home_team,
                'away_team': self.away_team,
                'Team': game_period,
                'NJD': NJD,
                'NYR': away_table,
                'home_score_total': home_score_total_iteration,
                'away_score_total': away_score_total_iteration,
                'overtime': ot,
            }

            box_score = {
                'Team': game_period,
                'NJD': NJD,
                'NYR': away_table,
            }

            return game_result, box_score

        return home_score_iteration, away_score_iteration

    def print_results(self):
        print(self.home_team)
        print(f"W: {self.home_wins} L: {self.home_losses} OTL: {self.home_OTL} GF: {self.home_score_total}")
        print(self.away_team)
        print(f"W: {self.away_wins} L: {self.away_losses} OTL: {self.away_OTL} GF: {self.away_score_total}")

    def print_box_score(self, box_score):
        # Print the box score for the current game
        max_len = max(len(box_score['Team']), len(box_score['NJD']), len(box_score['NYR']))

        # Extend lists to have the same length
        box_score['Team'] += ['Team'] * (max_len - len(box_score['Team']))
        box_score['NJD'] += [0] * (max_len - len(box_score['NJD']))
        box_score['NYR'] += [0] * (max_len - len(box_score['NYR']))

        df = pd.DataFrame.from_dict(box_score, orient='index')
        print(df)


if __name__ == "__main__":
    iterations = 82
    sim = HockeySimulation(iterations)
    sim.run_simulation()
