from data_loader import load_data
from analysis import dropout_rate, proporcion_desercion
if __name__ == "__main__":
  data = load_data()
  rate = dropout_rate(data)

  prop = proporcion_desercion(data)
  print(f"Dropout rate: {rate}%")
  print(f"Dropout proportion: {prop[0]}%")
  if prop[1]:
      print(f"Most common cause of dropout: {prop[1]}")

 
