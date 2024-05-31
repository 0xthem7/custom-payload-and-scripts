import requests 
import threading

endPoint = input('Provide the endoint : ')
def func():
    response = requests.get(f'{endPoint}'))

while True:
    l1.append(threading.Thread(target=func).start())
