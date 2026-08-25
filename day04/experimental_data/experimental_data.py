import numpy as np
import matplotlib.pyplot as plt

time = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
temperature = np.array([20.1, 20.8, 21.5, 22.7, 23.9, 25.4, 27.1, 29.3, 31.8, 34.5])


def menu(a,b):
    x = 1
    while x!=0:
        print('Choose what you want:')
        print('1. Average temperature')
        print('2. Maximum temperature')
        print('3. Minimum temperature')
        print('4. Time of maximum temperature')
        print('5. Times when the temperature was above 25')
        print('6. Plot a graph of temperature versus time')
        print('0. Exit')
        x = int(input('Enter a number from 0 to 6: '))
        print()
        
        if x == 1:
            print(f'Average temperature: {np.mean(b)}\n')
        elif x == 2:
            print(f'Maximum temperature: {np.max(b)}\n')
        elif x == 3:
            print(f'Minimum temperature: {np.min(b)}\n')
        elif x == 4:
            print(f'Time of maximum temperature: {a[np.argmax(b)]}\n')
        elif x == 5:
            print(f'Times when the temperature was above 25: { ', '.join(map(str,a[np.where(b>25)]))}\n')
        elif x == 6:
            print('Plot a graph of temperature as a function of time: \n')
            plt.plot(a,b)
            plt.title('temperature as a function of time')
            plt.xlabel('time')
            plt.ylabel('temperature')
            plt.axhline(y = np.mean(b), color='r' )
            plt.text(a[0], np.mean(b), f' Average: {np.mean(b):.2f}', va='bottom', ha='left')
            plt.grid(True)
            plt.show()
        elif x == 0:
            return


menu(time, temperature)
