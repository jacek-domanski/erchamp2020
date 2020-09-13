from collections import Counter
from math import floor


class ResultsAnalyzer:
    def __init__(self):
        self.data = list()
        self.ranges_count = Counter()

    def open_file(self):
        with open('short_data.txt', 'r') as file:
            i = 0
            for line in file:
                if i == 0:
                    new_data = dict()
                    new_data['place'] = int(line)

                if i == 1:
                    new_data['name'] = line.strip()

                if i == 2:
                    new_data['country'] = line.strip()

                if i == 3:
                    pass

                if i == 4:
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

    def run(self):
        self.open_file()
        self.count_ranges()

        print(self.ranges_count)


if __name__ == '__main__':
    results_analyzer = ResultsAnalyzer()
    results_analyzer.run()
