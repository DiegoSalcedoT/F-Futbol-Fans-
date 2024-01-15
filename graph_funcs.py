import seaborn as sns
import matplotlib.pyplot as plt

def multi_count_plot(df, columns):
  """
  Creates a single plot with multiple count plots for the given columns in a DataFrame.

  Args:
    df: The DataFrame containing the data.
    columns: A list of column names to create count plots for.

  Returns:
    None
  """
  # Set plot style and figure size
  sns.set(style="whitegrid")
  plt.figure(figsize=(15, 6))

  # Calculate number of subplots needed
  n_plots = len(columns)

  # Create subplots and iterate through columns
  for i, col in enumerate(columns):
    ax = plt.subplot(1, n_plots, i + 1) #create subplot for every column
    sns.countplot(x=col, data=df, ax=ax)

    # Adjust plot titles and labels
    ax.set_title(f'{col} Distribution')
    ax.set_xlabel(col)
    ax.set_ylabel('Count')

    # Add labels on top of the bars
    for bar in ax.patches: # Each individual bar in a bar plot is represented by a patch
      ax.annotate(f'{int(bar.get_height())}',
                  (bar.get_x() + bar.get_width() / 2., bar.get_height() - 10), #graph position
                  ha='center',va='center', # specify horizontal and vertical alignment of the label
                  xytext=(0, 10), # provides an offset from the bar for the label (adjusting vertically to prevent overlap)
                  textcoords='offset points')

  # Adjust spacing between subplots and show the plot
  plt.tight_layout()
  plt.show()


def count_plot(column):
  # Assuming df is your DataFrame
  sns.set(style="whitegrid")
  plt.figure(figsize=(8, 6))

  # Use the value_counts() result directly in the barplot
  ax = sns.countplot(x=column, data=df)

  plt.title(f'{column} Distribution')
  plt.xlabel(column)
  plt.ylabel('Count')

  # Add labels on top of the bars
  for bar in ax.patches: # Each individual bar in a bar plot is represented by a patch
      ax.annotate(f'{int(bar.get_height())}',
                  (bar.get_x() + bar.get_width() / 2., bar.get_height() - 10), #graph position
                  ha='center',va='center', # specify horizontal and vertical alignment of the label
                  xytext=(0, 10), # provides an offset from the bar for the label (adjusting vertically to prevent overlap)
                  textcoords='offset points')

  plt.show()

  