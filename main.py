from data_loader import load_data
from analysis import dropout_rate, proporcion_desercion, dropout_by_career
if __name__ == "__main__":
  data = load_data()
  rate = dropout_rate(data)

  prop = proporcion_desercion(data)
  print(f"Dropout rate: {rate}%")
  print(f"Dropout proportion: {prop[0]}%")
  if prop[1]:
      print(f"Most common cause of dropout: {prop[1]}")

  print("Analysis by career:")
  career_analysis = dropout_by_career(data)
  for career, rate in career_analysis:
      print(f"  {career}: {rate}% dropout rate")

 
