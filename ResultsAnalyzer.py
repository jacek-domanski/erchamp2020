from collections import Counter
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')



class ResultsAnalyzer:
    def __init__(self):
        self.data = list()
        self.ranges_count = Counter()

    def open_file(self):
        with open('full_data.txt', 'r') as file:
            i = 0
            for line in file:
                if i == 0:
                    new_data = dict()
                    new_data['place'] = int(line)

                elif i == 1:
                    new_data['name'] = line.strip()

                elif i == 2:
                    new_data['country'] = line.strip()

                elif i == 4:
                    new_data['minutes'] = self.time_to_minutes(line)
                    self.data.append(new_data)

                i = (i + 1) % 5

    @staticmethod
    def time_to_minutes(t):
        h_m_s = t.strip().split(':')
        m = int(h_m_s[0]) * 60 + int(h_m_s[1])
        return m

    def count_ranges(self):
        for result in self.data:
            range = (result['minutes'] // 10) * 10
            self.ranges_count[range] += 1

    def plot_data(self):
        fig = plt.figure()
        ax = fig.add_axes([0.12, 0.1, 0.84, 0.8])

        ax.bar(self.ranges_count.keys(), self.ranges_count.values())

        ax.set_xlabel('Czas [min]')
        ax.set_ylabel('Liczba grup')
        ax.set_title('Wyniki w grupach po 10 min')
        plt.show()

    def run(self):
        self.open_file()
        self.count_ranges()
        print(list(self.ranges_count.keys())[0])
        self.plot_data()



if __name__ == '__main__':
    results_analyzer = ResultsAnalyzer()
    results_analyzer.run()
