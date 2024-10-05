import matplotlib.pyplot as plt
import pandas as pd

def visualize_distribution(csv_file, gen_column, age_column):
    try:
        # Read the CSV file
        df = pd.read_csv(csv_file)

        # Check if the columns exist
        if gen_column not in df.columns:
            print(f"The column '{gen_column}' does not exist in the CSV file.")
            return
        if age_column not in df.columns:
            print(f"The column '{age_column}' does not exist in the CSV file.")
            return

        # (Gen) bar chart
        plt.figure(figsize=(8, 6))
        df[gen_column].value_counts().plot(kind='bar')
        plt.title('Distribution of Gender')
        plt.xlabel(gen_column)
        plt.ylabel('Count')
        plt.show()

        # (Age) histogram
        plt.figure(figsize=(8, 6))
        df[age_column].plot(kind='hist', bins=4)
        plt.title('Distribution of Age')
        plt.xlabel(age_column)
        plt.ylabel('Frequency')
        plt.show()

    except FileNotFoundError:
        print("The CSV file was not found.")

# Example usage:
visualize_distribution('population_data.csv', 'Gen', 'Age')