import pandas as pd

class Mission:
    def __init__(self, data):
        self.data = data

    @classmethod
    def from_csv(cls, file_path):
        # Read the CSV file using pandas
        data = pd.read_csv(file_path)
        # Create an instance of Mission with the data
        return cls(data)

# Example usage
if __name__ == "__main__":
    mission = Mission.from_csv('mission.csv')
    print(mission.data)